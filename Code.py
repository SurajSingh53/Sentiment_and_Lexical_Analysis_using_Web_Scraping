#1. Importing all the requireds libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import re
import os

#2. Creating functions
#a. Read the file containg positive word and return the text. 
def extract_positive_words(positive_file):     
    with open(positive_file, "r") as pf:
        positive_words = set(pf.read().splitlines())
    return positive_words

#b. Read the file containg negetive word and return the text.
def extract_negative_words(negative_file):
    with open(negative_file, "r") as nf:
        negative_words = set(nf.read().splitlines())
    return negative_words

#c. Read the file containg Stopwords and return the text. (I have merged all the stop word text files beforehand in a single text file )
def extract_stop_words(stop_words_file):
    with open(stop_words_file, "r") as sw:
        stop_words = set(sw.read().splitlines())
    return stop_words

#d. This function only return the text file in which there are words not present in the file stopword created earlier.
def remove_stop_words(words, stop_words):
    return [word for word in words if word.lower() not in stop_words]

#e. This function returns avg sentence length.
def extract_avg_sentence_length(text):
    sentences = nltk.sent_tokenize(text)
    total_sentence_length = sum(len(sent) for sent in sentences)
    return total_sentence_length / len(sentences)

#f. This funtion returns Complex word count(words with more than 2 syllables).
def extract_num_complex_words(words):
    cmu_dict = nltk.corpus.cmudict.dict()
    complex_word_count = sum(1 for word in words if syllable_count(word, cmu_dict) > 2)
    return complex_word_count

#f. This funtion returns total syllable count in a text.
def syllable_count(word, cmu_dict):
    if word.lower() in cmu_dict:
        return max([len(list(y for y in x if y[-1].isdigit())) for x in cmu_dict[word.lower()]])
    else:
        return 0
#g. This is the main funtion which both analyse and load the output result. 
def extract_and_analyze_data(input_file, output_file, positive_file, negative_file, stop_words_file):
    df = pd.read_excel(input_file)  
    sia = SentimentIntensityAnalyzer()
    
    positive_words = extract_positive_words(positive_file)
    negative_words = extract_negative_words(negative_file)
    stop_words = extract_stop_words(stop_words_file)
    
    for index, row in df.iterrows():
        url_id = row['URL_ID']
        url = row['URL']
        
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            article_title = soup.title.text.strip()
            paragraphs = soup.find_all('p')
            article_text = "\n".join([p.get_text() for p in paragraphs])
            
            with open(f"{url_id}.txt", "w", encoding="utf-8") as f:
                f.write(f"{article_title}\n\n{article_text}")
            
            words = nltk.word_tokenize(article_text)
            filtered_words = remove_stop_words(words, stop_words)
            tagged_words = nltk.pos_tag(words)
            
            num_positive_words = sum(1 for word in filtered_words if word.lower() in positive_words)
            num_negative_words = sum(1 for word in filtered_words if word.lower() in negative_words)
            cmu_dict = nltk.corpus.cmudict.dict()
            complex_word_count = extract_num_complex_words(words)
            
            positive_score = num_positive_words
            negative_score = num_negative_words
            polarity_score = ((positive_score - negative_score) / (positive_score + negative_score + 1e-6)) * 1e-6
            word_count = len(filtered_words)
            subjectivity_score = ((positive_score + negative_score) / word_count) * 1e-6
            total_sentence_length = sum(len(sent) for sent in paragraphs)
            avg_sentence_length = total_sentence_length / len(paragraphs)
            complex_word_percentage = complex_word_count / len(words)

        # Writing the output over the output.xlsx file.            
            df.at[index, 'POSITIVE SCORE'] = positive_score
            df.at[index, 'NEGATIVE SCORE'] = negative_score
            df.at[index, 'POLARITY SCORE'] = polarity_score
            df.at[index, 'SUBJECTIVITY SCORE'] = subjectivity_score
            df.at[index, 'AVG SENTENCE LENGTH'] = avg_sentence_length
            df.at[index, 'PERCENTAGE OF COMPLEX WORDS'] = complex_word_percentage*100
            df.at[index, 'FOG INDEX'] = 0.4 * (avg_sentence_length + complex_word_percentage)
            df.at[index, 'AVG NUMBER OF WORDS PER SENTENCE'] = len(words) / len(paragraphs)
            df.at[index, 'COMPLEX WORD COUNT'] = complex_word_count
            df.at[index, 'WORD COUNT'] = word_count
            df.at[index, 'SYLLABLE PER WORD'] = sum(syllable_count(word, cmu_dict) for word in words) / len(words)
            df.at[index, 'PERSONAL PRONOUNS'] = sum(1 for word, tag in tagged_words if tag in ['PRP', 'PRP$', 'WP', 'WP$'])
            df.at[index, 'AVG WORD LENGTH'] = sum(len(word) for word in words) / len(words)
            
        except Exception as e:
            print(f"Error processing URL_ID {url_id}: {e}")
    df.to_excel(output_file, index=False)

input_file = "Input.xlsx"
output_file = "Output.xlsx"
positive_file = "positive.txt"
negative_file = "negative.txt"
stop_words_file = "Stop_word.txt"

extract_and_analyze_data(input_file, output_file, positive_file, negative_file, stop_words_file)
