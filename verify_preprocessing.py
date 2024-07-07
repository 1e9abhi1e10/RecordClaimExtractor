import pandas as pd

def verify_preprocessing(file_path, num_lines=5):
    # Load the preprocessed CSV file
    df = pd.read_csv(file_path)

    # Check for NaN values in 'Content' and 'Reasons' columns
    nan_content = df[df['Content'].isna()]
    nan_reasons = df[df['Reasons'].isna()]

    # Print rows with NaN values in 'Content' and 'Reasons' columns
    if not nan_content.empty:
        print("Rows with NaN values in 'Content' column:")
        print(nan_content)
    if not nan_reasons.empty:
        print("Rows with NaN values in 'Reasons' column:")
        print(nan_reasons)

    # Print the first few lines of the 'Content' and 'Reasons' columns
    print(df[['Content', 'Reasons']].head(num_lines))

if __name__ == "__main__":
    # Path to the preprocessed CSV file
    file_path = "preprocessed_records.csv"

    # Verify the preprocessing by printing the first few lines
    verify_preprocessing(file_path)
