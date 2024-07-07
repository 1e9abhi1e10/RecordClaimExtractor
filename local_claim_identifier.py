import pandas as pd
from transformers import pipeline
import time

def identify_claims(texts):
    # Load the pre-trained model for text classification within the worker function
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    # Define the candidate labels
    candidate_labels = ["claim", "non-claim"]

    # Classify the text
    print("Classifying text...")
    results = classifier(texts, candidate_labels)
    print("Classification complete.")

    # Determine the indices of sentences that are classified as claims
    claim_indices_list = []
    for result in results:
        claim_indices = [i for i, label in enumerate(result["labels"]) if label == "claim"]
        claim_indices_list.append(claim_indices)

    return claim_indices_list

def process_batch(batch):
    batch_indices, batch_texts = batch
    try:
        print(f"Processing batch {batch_indices}...")
        claim_indices_list = identify_claims(batch_texts)
        print(f"Batch {batch_indices} processed successfully.")
        return list(zip(batch_indices, claim_indices_list))
    except Exception as e:
        print(f"Error processing batch {batch_indices}: {e}")
        return []

def process_records(file_path, batch_size=5):
    # Load the preprocessed CSV file
    df = pd.read_csv(file_path)

    # Ensure 'Content' column is of string type
    df['Content'] = df['Content'].astype(str)

    # Split the data into batches
    batches = [(list(range(i, min(i + batch_size, len(df)))), df['Content'][i:i + batch_size].tolist())
               for i in range(0, len(df), batch_size)]

    start_time = time.time()
    results = []
    for batch in batches:
        batch_result = process_batch(batch)
        results.append(batch_result)

    # Flatten the results and update the DataFrame
    for batch_result in results:
        for idx, claim_indices in batch_result:
            df.at[idx, 'claim_indices'] = claim_indices

    elapsed_time = time.time() - start_time
    print(f"Processed {len(df)} records in {elapsed_time:.2f} seconds")

    return df

if __name__ == "__main__":
    # Path to the preprocessed CSV file
    file_path = "preprocessed_records.csv"

    # Process the records to identify claims
    df = process_records(file_path)

    # Save the results to a new CSV file
    df.to_csv("claims_identified_records.csv", index=False)
