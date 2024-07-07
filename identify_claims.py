import pandas as pd
import requests
import json

def identify_claims(text):
    # Define the Perplexity API endpoint and headers
    api_url = "https://api.perplexity.ai/v1/identify_claims"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"
    }

    # Prepare the payload
    payload = {
        "text": text
    }

    # Make the API request
    response = requests.post(api_url, headers=headers, data=json.dumps(payload))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        result = response.json()
        return result.get("claim_indices", [])
    else:
        print(f"Error: {response.status_code}")
        return []

def process_records(file_path):
    # Load the preprocessed CSV file
    df = pd.read_csv(file_path)

    # Identify claims in each record
    df["claim_indices"] = df["Content"].apply(identify_claims)

    return df

if __name__ == "__main__":
    # Path to the preprocessed CSV file
    file_path = "preprocessed_records.csv"

    # Process the records to identify claims
    df = process_records(file_path)

    # Save the results to a new CSV file
    df.to_csv("claims_identified_records.csv", index=False)
