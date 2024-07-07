import pandas as pd
from claim_extraction_library import process_records, preprocess_data, annotate_text_units
from transformers import pipeline

def load_sample_records(file_path, num_records=5):
    """
    Load the CSV file and return a sample of records.

    Args:
        file_path (str): Path to the CSV file.
        num_records (int): Number of records to sample.

    Returns:
        DataFrame: A sample of records from the CSV file.
    """
    df = pd.read_csv(file_path)
    return df.sample(n=num_records)

def test_claim_extraction(preprocessed_records):
    """
    Process the sample records to extract claims and validate the results.

    Args:
        preprocessed_records (DataFrame): A sample of preprocessed records to process.
    """
    # Annotate the sample records
    annotated_records = annotate_text_units(preprocessed_records)

    # Initialize the classifier
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    # Process the sample records to extract claims
    results = process_records(annotated_records, classifier)

    # Define expected results (placeholder)
    expected_results = {
        # 'record_id': [expected_claim_indices]
        '1': [0, 2],  # Example placeholder values
        '2': [1, 3],  # Example placeholder values
        '3': [0, 1],  # Example placeholder values
        '4': [2, 4],  # Example placeholder values
        '5': [1, 2]   # Example placeholder values
    }

    # Validate the results against expected values
    for result in results:
        record_id = result['record_id']
        claim_indices = result['claim_indices']
        expected_claim_indices = expected_results.get(record_id, [])

        assert claim_indices == expected_claim_indices, f"Test failed for record ID {record_id}. Expected: {expected_claim_indices}, Got: {claim_indices}"
        print(f"Record ID: {record_id}, Claim Indices: {claim_indices} - Test Passed")

if __name__ == "__main__":
    # Path to the preprocessed CSV file
    file_path = "preprocessed_records.csv"

    # Load a sample of records for testing
    try:
        sample_records = load_sample_records(file_path)
        if sample_records.empty:
            raise ValueError("No records found in the CSV file.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        # Preprocess the sample records
        preprocessed_records = preprocess_data(file_path)

        # Test the claim extraction process
        test_claim_extraction(preprocessed_records)
