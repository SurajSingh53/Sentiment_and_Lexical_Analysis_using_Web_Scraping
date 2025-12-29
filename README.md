# Sentiment and Lexical Analysis using Web Scraping

## Overview

This project performs **sentiment analysis and lexical analysis** on textual data collected from web sources. It automates the process of scraping content, cleaning and preprocessing text, and generating sentiment-based insights using natural language processing techniques.

The system is designed for real-world unstructured text and can be extended for research, analytics, or NLP-based applications.

---

## Objectives

- Extract textual content from web pages  
- Clean and normalize raw text  
- Perform sentiment and lexical analysis  
- Generate structured outputs for analysis and modeling  

---

## System Workflow

1. **Web Scraping**  
   Extracts textual content from web pages using HTTP requests and HTML parsing.

2. **Text Preprocessing**  
   Removes punctuation, stopwords, and irrelevant characters to normalize text.

3. **Sentiment Analysis**  
   Applies lexicon-based techniques to compute sentiment polarity.

4. **Lexical Analysis**  
   Computes word frequency and lexical statistics.

5. **Output Generation**  
   Stores processed results in structured files for further use.

---

## Project Structure

```
Sentiment_and_Lexical_Analysis_using_Web_Scraping/
│
├── Code.py                  # Main script for scraping and analysis
├── Input.xlsx               # Input URLs or raw text
├── Output.xlsx              # Output with sentiment and lexical metrics
├── positive.txt             # Positive sentiment lexicon
├── negative.txt             # Negative sentiment lexicon
├── Stop_word.txt            # Stopword list
└── README.md                # Project documentation
```

---

## Requirements

Install dependencies using:

```bash
pip install pandas requests beautifulsoup4 nltk openpyxl
```

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/SurajSingh53/Sentiment_and_Lexical_Analysis_using_Web_Scraping.git
```

2. Navigate to the project directory:
```bash
cd Sentiment_and_Lexical_Analysis_using_Web_Scraping
```

3. Run the script:
```bash
python Code.py
```

4. View the results in:
```
Output.xlsx
```

---

## Output Description

The generated output includes:
- Cleaned textual content  
- Sentiment polarity scores  
- Word frequency and lexical metrics  

This data can be used for sentiment trend analysis, NLP research, or dataset preparation.

---

## Use Cases

- Customer feedback analysis  
- Opinion mining and sentiment research  
- NLP experimentation and prototyping  

---

## Notes

- Ensure compliance with website scraping policies.
- Accuracy depends on data quality and preprocessing logic.
- Intended for educational and research use.

---

## License
Nothing really tbh...:)

This project is intended for educational and research purposes.
