import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize

# Ensure the necessary NLTK data files are downloaded
nltk.download('punkt')

def split_text_into_sentences(text):
    # Split the text into sentences
    sentences = sent_tokenize(text)
    return sentences

def annotate_text_units(df):
    # Create a list to store the annotated text units
    annotated_rows = []

    for index, row in df.iterrows():
        # Ensure 'Content' column is of string type
        content = str(row['Content'])

        # Split the 'Content' column into sentences
        sentences = split_text_into_sentences(content)

        # Annotate each sentence with metadata
        for i, sentence in enumerate(sentences):
            annotated_rows.append({
                'ID': row['ID'],
                'Sentence': sentence,
                'Sentence_Index': i,
                'Timestamp': row['CreatedAt'],
                'Source': row['Source'],
                'Record_Type': row['Type']
            })

    # Convert the list of annotated rows to a DataFrame
    annotated_df = pd.DataFrame(annotated_rows, columns=['ID', 'Sentence', 'Sentence_Index', 'Timestamp', 'Source', 'Record_Type'])

    return annotated_df

if __name__ == "__main__":
    # Path to the preprocessed CSV file
    file_path = "preprocessed_records.csv"

    # Load the preprocessed CSV file
    df = pd.read_csv(file_path)

    # Annotate the text units
    annotated_df = annotate_text_units(df)

    # Save the annotated text units to a new CSV file
    annotated_df.to_csv("annotated_text_units.csv", index=False)
