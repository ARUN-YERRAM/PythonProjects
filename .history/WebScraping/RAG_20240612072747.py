import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datasets import load_dataset, Features, Value
from transformers import RagTokenizer, RagTokenForGeneration, RagRetriever
from flask import Flask, request, jsonify
import torch

# Step 1: Web Scraping
def scrape_news():import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datasets import load_dataset, Features, Value
from transformers import RagTokenizer, RagTokenForGeneration, RagRetriever
from flask import Flask, request, jsonify
import torch

# Step 1: Web Scraping
def scrape_news():
    url = 'https://timesofindia.com'  # Replace with the actual news website URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    headlines = []
    urls = []

    for item in soup.find_all('h2', class_='headline'):  # Adjust the selector to match the website's HTML structure
        headline = item.get_text()
        link = item.find('a')['href']
        headlines.append(headline)
        urls.append(link)

    # Create DataFrame and save to CSV
    df = pd.DataFrame({
        'headline': headlines,
        'url': urls
    })
    df.to_csv('your_data.csv', index=False)

# Run the web scraping function
scrape_news()

# Verify if CSV file was created and contains data
csv_file = 'your_data.csv'
if not os.path.isfile(csv_file):
    raise FileNotFoundError(f"The file {csv_file} was not found.")
if os.stat(csv_file).st_size == 0:
    raise ValueError(f"The file {csv_file} is empty.")

# Load and print the content of the CSV file to verify
df = pd.read_csv(csv_file)
print("CSV file content:")
print(df)

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
question = "What is the latest news?"
response = get_rag_response(question)
print(response)

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

    url = 'https://timesofindia.com' 
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    headlines = []
    urls = []

    for item in soup.find_all('h2', class_='headline'):  # Adjust the selector to match the website's HTML structure
        headline = item.get_text()
        link = item.find('a')['href']
        headlines.append(headline)
        urls.append(link)

    # Create DataFrame and save to CSV
    df = pd.DataFrame({
        'headline': headlines,
        'url': urls
    })
    df.to_csv('your_data.csv', index=False)

scrape_news()

# Step 2: Data Preparation
features = Features({'headline': Value('string'), 'url': Value('string')})
dataset = load_dataset('csv', data_files='your_data.csv', features=features)

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
question = "What is the latest news?"
response = get_rag_response(question)
print(response)

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
