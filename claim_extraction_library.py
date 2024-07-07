import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
from transformers import pipeline

# Ensure the necessary NLTK data files are downloaded
nltk.download('punkt')

# Data Preprocessing Module
def preprocess_data(file_path):
    """
    Preprocess the data by reading the CSV file, filling missing values, and ensuring correct data types.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        DataFrame: Preprocessed data.
    """
    df = pd.read_csv(file_path)
    df['Content'] = df['Content'].fillna('').astype(str)
    df['Reasons'] = df['Reasons'].fillna('')
    return df

# Text Splitting Module
def split_text_into_sentences(text):
    """
    Split the given text into sentences.

    Args:
        text (str): The text to split.

    Returns:
        list: A list of sentences.
    """
    sentences = sent_tokenize(text)
    return sentences

def annotate_text_units(df):
    """
    Annotate the text units by splitting the content into sentences and adding metadata.

    Args:
        df (DataFrame): The DataFrame containing the records.

    Returns:
        DataFrame: Annotated text units with metadata.
    """
    annotated_rows = []
    for index, row in df.iterrows():
        content = str(row['Content'])
        sentences = split_text_into_sentences(content)
        for i, sentence in enumerate(sentences):
            annotated_rows.append({
                'ID': row['ID'],
                'Sentence': sentence,
                'Sentence_Index': i,
                'Timestamp': row['CreatedAt'],
                'Source': row['Source'],
                'Record_Type': row['Type']
            })
    annotated_df = pd.DataFrame(annotated_rows, columns=['ID', 'Sentence', 'Sentence_Index', 'Timestamp', 'Source', 'Record_Type'])
    return annotated_df

# Claim Identification Module
def identify_claims(texts, classifier):
    """
    Identify claims in the given texts using a zero-shot classification model.

    Args:
        texts (list): A list of texts to classify.
        classifier (pipeline): The zero-shot classification model.

    Returns:
        list: A list of claim indices for each text.
    """
    candidate_labels = ["claim", "non-claim"]
    results = classifier(texts, candidate_labels)
    claim_indices_list = []
    for result in results:
        claim_indices = [i for i, label in enumerate(result["labels"]) if label == "claim"]
        claim_indices_list.append(claim_indices)
    return claim_indices_list

def process_batch(batch, classifier):
    """
    Process a batch of texts to identify claims.

    Args:
        batch (tuple): A tuple containing batch indices and batch texts.
        classifier (pipeline): The zero-shot classification model.

    Returns:
        list: A list of tuples containing batch indices and claim indices.
    """
    batch_indices, batch_texts = batch
    try:
        claim_indices_list = identify_claims(batch_texts, classifier)
        return list(zip(batch_indices, claim_indices_list))
    except Exception as e:
        print(f"Error processing batch {batch_indices}: {e}")
        return []

def process_records(df, classifier, batch_size=5):
    """
    Process the records to identify claims in batches.

    Args:
        df (DataFrame): The DataFrame containing the annotated text units.
        classifier (pipeline): The zero-shot classification model.
        batch_size (int): The size of each batch for processing.

    Returns:
        DataFrame: The DataFrame with identified claim indices.
    """
    df['Sentence'] = df['Sentence'].astype(str)
    batches = [(list(range(i, min(i + batch_size, len(df)))), df['Sentence'][i:i + batch_size].tolist())
               for i in range(0, len(df), batch_size)]
    results = []
    for batch in batches:
        print(f"Processing batch {batch[0]}...")
        batch_result = process_batch(batch, classifier)
        results.append(batch_result)
    for batch_result in results:
        for idx, claim_indices in batch_result:
            df.at[idx, 'claim_indices'] = claim_indices
    return df

# Integration and Output Module
def extract_claims(file_path, output_path):
    """
    Extract claims from the records and save the results to a CSV file.

    Args:
        file_path (str): Path to the input CSV file.
        output_path (str): Path to the output CSV file.
    """
    df = preprocess_data(file_path)
    annotated_df = annotate_text_units(df)
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    claims_df = process_records(annotated_df, classifier)
    claims_df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_file = "preprocessed_records.csv"
    output_file = "claims_identified_records.csv"
    extract_claims(input_file, output_file)
