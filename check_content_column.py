import pandas as pd

def check_content_column(file_path):
    # Read the CSV file in chunks
    chunksize = 1000
    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        # Check the data type of the 'Content' column
        non_string_rows = chunk[chunk['Content'].apply(lambda x: not isinstance(x, str))]
        if not non_string_rows.empty:
            print(non_string_rows)

if __name__ == "__main__":
    # Path to the preprocessed CSV file
    file_path = "preprocessed_records.csv"

    # Check the 'Content' column for non-string values
    check_content_column(file_path)
