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

## Documentation
- `preprocess.py`: Script for data preprocessing.
- `text_splitter.py`: Script for splitting text into sentences and annotating them.
- `local_claim_identifier.py`: Script for identifying claims using a local LLM.
- `claim_extraction_library.py`: Main script for extracting claims from records.
- `test_claim_extraction.py`: Script for testing the claim extraction process with sample records.

## Report
A brief report detailing the approach, challenges, and results will be provided separately. Please refer to `report.md` for more details.

