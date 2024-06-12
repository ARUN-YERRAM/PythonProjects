import os
import pandas as pd
from datasets import load_dataset, Features, Value
from transformers import RagTokenizer, RagTokenForGeneration, RagRetriever
from flask import Flask, request, jsonify
import torch

# Step 1: Web Scraping (already done separately)
# Ensure your CSV 'technology-of-business.csv' is available.

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
try:
    dataset = load_dataset('csv', data_files=csv_file, features=features)
except Exception as e:
    print("Error loading dataset:", e)
    raise

# Print some debugging information about the dataset
print("Dataset loaded successfully.")
print("Number of examples:", len(dataset))
print("First few examples:")
for example in dataset['train'][:5]:
    print(example)

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
