import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datasets import load_dataset, Features, Value
from transformers import RagTokenizer, RagTokenForGeneration, RagRetriever
from flask import Flask, request, jsonify
import torch

# Step 1: Web Scraping
def scrape_news():
    url = 'https://www.bbc.com/news/technology'
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve webpage. Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')

    headlines = []
    urls = []

    for item in soup.find_all('a', class_='gs-c-promo-heading'):
        headline = item.get_text().strip()
        link = item['href']
        if not link.startswith('http'):
            link = 'https://www.bbc.com' + link
        headlines.append(headline)
        urls.append(link)

    # Create DataFrame and save to CSV
    df = pd.DataFrame({
        'headline': headlines,
        'url': urls
    })
    df.to_csv('technology-of-business.csv', index=False)
    print("Scraping completed. Data saved to 'technology-of-business.csv'.")

# Run the web scraping function
scrape_news()

# Verify if CSV file was created and contains data
csv_file = 'technology-of-business.csv'
if not os.path.isfile(csv_file):
    raise FileNotFoundError(f"The file {csv_file} was not found.")
if os.stat(csv_file).st_size == 0:
    raise ValueError(f"The file {csv_file} is empty.")

# Load and print the content of the CSV file to verify
df = pd.read_csv(csv_file)
print("CSV file content:")
print(df.head())

# Step 2: Data Preparation
features = Features({'headline': Value('string'), 'url': Value('string')})
dataset = load_dataset('csv', data_files=csv_file, features=features)

# Step 3: Initialize RAG Model
tokenizer = RagTokenizer.from_pretrained('facebook/rag-token-nq')
model = RagTokenForGeneration.from_pretrained('facebook/rag-token-nq')
retriever = RagRetriever.from_pretrained('facebook/rag-token-nq', dataset=dataset)
model.set_retriever(retriever)

# Step 4: Query and Response Generation
def get_rag_response(question):
    try:
        input_ids = tokenizer(question, return_tensors='pt').input_ids
        output_ids = model.generate(input_ids, num_beams=5, max_length=50, early_stopping=True)
        return tokenizer.decode(output_ids[0], skip_special_tokens=True)
    except Exception as e:
        return f"An error occurred: {e}"

# Test the function with a sample query
question = "What is the latest technology news?"
response = get_rag_response(question)
print("Sample Response: ", response)

# Flask web interface
app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    question = data['question']
    response = get_rag_response(question)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
