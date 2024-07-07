# Claim Extraction Library

## Overview
This library provides functionality to extract specific parts of records discussing particular claims using Large Language Models (LLMs). The system processes records from a CSV file, identifies and extracts relevant claims, and outputs the results in a structured format.

## Requirements
- Python 3.6 or higher
- pip (Python package installer)

## Setup

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/1e9abhi1e10/RecordClaimExtractor.git
   cd RecordClaimExtractor
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Extracting Claims
1. Place the input CSV file in the repository directory.
2. Run the main script to extract claims from the records and output the results to a CSV file:
   ```bash
   python claim_extraction_library.py
   ```

### Testing
1. Define the expected results for the sample records in the `test_claim_extraction.py` script.
2. Run the test script to verify the claim extraction process with sample records:
   ```bash
   python test_claim_extraction.py
   ```

## Output
The system outputs a structured format indicating where the claims are discussed within the records. The output is saved to a CSV file named `extracted_claims.csv` in the repository directory with the following structure:
```json
[
  {
    "record_id": "a879cf1-120c-5a69-b059-5820f08abae3",
    "claim_indices": [2, 5, 7]
  },
  ...
]
```

## Documentation
- `preprocess.py`: Script for data preprocessing.
- `text_splitter.py`: Script for splitting text into sentences and annotating them.
- `local_claim_identifier.py`: Script for identifying claims using a local LLM.
- `claim_extraction_library.py`: Main script for extracting claims from records.
- `test_claim_extraction.py`: Script for testing the claim extraction process with sample records.

## Report
A brief report detailing the approach, challenges, and results will be provided separately. Please refer to `report.md` for more details.

