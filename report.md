# Claim Extraction System Report

## Overview
This report details the development of a system to extract specific parts of records discussing particular claims using Large Language Models (LLMs). The system processes records from a CSV file, identifies and extracts relevant claims, and outputs the results in a structured format.

## Approach
The development process followed a structured approach, including data understanding and preprocessing, claim identification, text splitting and annotation, model integration, and library development. The key steps are outlined below:

### Data Understanding and Preprocessing
1. **Data Analysis**: The provided CSV file was analyzed to understand its structure and content. The file contains columns such as ID, Content, URL, Source, Type, CreatedAt, and Reasons.
2. **Preprocessing**: A Python script (`preprocess.py`) was created to clean and normalize the text data. This included handling missing values, normalizing text, and ensuring the 'Content' column was of string type.

### Claim Identification
1. **Local LLM**: The system was designed to use a local LLM for claim identification, avoiding external APIs as per user instructions. The Hugging Face `transformers` library was used with the `facebook/bart-large-mnli` model for zero-shot classification.
2. **Batch Processing**: To improve performance, the claim identification process was implemented using batch processing. The classifier was initialized once and passed to relevant functions to avoid repeated loading.

### Text Splitting and Annotation
1. **Text Splitting**: A script (`text_splitter.py`) was created to split the text into sentences and annotate them with metadata such as speaker, timestamp, and message index.
2. **Annotation**: The annotated text units were saved to a new CSV file for further processing.

### Model Integration
1. **Integration**: The LLM was integrated into the system to process the preprocessed text and identify the units where claims are discussed.
2. **Output**: The system outputs a structured format indicating where the claims are discussed within the records.

### Library Development
1. **Encapsulation**: The developed functionality was encapsulated into a reusable and scalable library.
2. **Documentation**: A README file was created to provide setup instructions, usage guidelines, and details about the output and documentation.

## Challenges
1. **Handling Missing Values**: Ensuring that missing values in the 'Content' and 'Reasons' columns were properly handled to prevent errors during processing.
2. **Performance Optimization**: Implementing batch processing and optimizing model initialization to improve the performance of the claim identification process.
3. **Script Hanging**: Addressing issues with the script hanging during claim identification by adding granular print statements and reducing batch size.

## Results
The system has successfully processed the records and identified claims. The results are saved in the `claims_identified_records.csv` file, which includes columns for ID, Sentence, Sentence_Index, Timestamp, Source, Record_Type, and claim_indices. The `claim_indices` column indicates whether a claim was identified within the text (1.0 for identified claims and 0.0 for non-claims).

### Example Results
Here are some examples of input records and the corresponding extracted claims:

**Input Record:**
```
ID: 69949ac0-6280-5a97-be88-315985fe2cbc
Content: "User adding Daniela Gonzalez, Emma's execops partner, Jack Divita, can you please share some context about the meeting you'd like to set up with me and Emma Auscher and Daniela Gonzalez can help you get it scheduled. Agent: Hi Daniela Gonzalez, nice to be connected with you. Full context: we have the renewal of our contract with Notion coming up at the end of February and we would like to schedule some time with Emma to reflect on what we have achieved together through our partnership so far, share some insights, and make some plans for goals for the coming year. Walk through a proposal for the renewal contract. For each of the points above, we wouldn't need any prep work from Emma. We will come prepared with the data. Please let me know if you have any questions or we can share any additional context on the goal of the meeting. User: Hi Jack Divita, nice to meet you. This is helpful. Could you please confirm your time zone and how much time you will need? Agent: We are in New York. I am sure Emma is busy, so we can make it work with 30 minutes."
Reasons: "Meeting setup, Contract renewal"
```

**Extracted Claims:**
```
ID: 69949ac0-6280-5a97-be88-315985fe2cbc
Claim Indices: [1.0]
```

## Conclusion
The claim extraction system demonstrates the effective use of LLMs and NLP techniques to identify and extract claims from records. The system is designed to be accurate, efficient, and reusable, with comprehensive documentation provided for ease of use.

## Future Work
1. **Performance Improvements**: Further optimization of the claim identification process to reduce processing time.
2. **Detailed Documentation**: Adding more detailed documentation for each script, including examples of input and output.
3. **Testing**: Conducting extensive testing with sample records to validate the system's accuracy and efficiency.

