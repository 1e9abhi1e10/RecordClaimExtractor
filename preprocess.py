import pandas as pd
import re

def preprocess_text(text):
    # Normalize text by converting to lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_data(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Handle missing values
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column] = df[column].fillna('')
        else:
            df[column] = df[column].fillna(0)

    # Ensure 'Content' and 'Reasons' columns have no NaN values
    if 'Content' in df.columns:
        print(f"NaN values in 'Content' before fillna: {df['Content'].isna().sum()}")
        df['Content'] = df['Content'].astype(str).fillna('')
        print(f"NaN values in 'Content' after fillna: {df['Content'].isna().sum()}")
    else:
        print("Error: 'Content' column not found in the CSV file.")

    if 'Reasons' in df.columns:
        print(f"NaN values in 'Reasons' before fillna: {df['Reasons'].isna().sum()}")
        df['Reasons'] = df['Reasons'].astype(str).fillna('')
        print(f"NaN values in 'Reasons' after fillna: {df['Reasons'].isna().sum()}")
    else:
        print("Error: 'Reasons' column not found in the CSV file.")

    # Normalize text in the 'Content' and 'Reasons' columns
    if 'Content' in df.columns:
        df['Content'] = df['Content'].apply(preprocess_text)
    if 'Reasons' in df.columns:
        df['Reasons'] = df['Reasons'].apply(preprocess_text)

    return df

if __name__ == "__main__":
    # Path to the CSV file
    file_path = 'records.csv'

    # Preprocess the data
    df = preprocess_data(file_path)

    # Save the preprocessed data to a new CSV file
    df.to_csv('preprocessed_records.csv', index=False)
