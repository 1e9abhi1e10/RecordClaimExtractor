import pandas as pd

def analyze_nan_rows(file_path):
    # Read the CSV file in chunks
    chunksize = 1000
    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        # Check for NaN values in the 'Content' column
        nan_rows = chunk[chunk['Content'].isna()]
        if not nan_rows.empty:
            # Print the row indices and relevant columns for diagnosis
            print(nan_rows[['ID', 'Content', 'URL', 'Source', 'Type', 'CreatedAt', 'Reasons']])

if __name__ == "__main__":
    # Path to the preprocessed CSV file
    file_path = "preprocessed_records.csv"

    # Analyze the rows with NaN values in the 'Content' column
    analyze_nan_rows(file_path)
