from pdf import extract_text_from_pdf
from topic import extract_topics_and_subtopics
import openai


import os
import openai

# Fetch the API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# The rest of your code remains unchanged

def main(pdf_path):
    # Ensure you have set your OpenAI API key
    openai.api_key = 'sk-proj-upjd8QLloQkyPYswHUyiT3BlbkFJfTcoaJ9xK5ArGO7tyX3m'
    
    text = extract_text_from_pdf(pdf_path)
    topics_and_subtopics = extract_topics_and_subtopics(text)
    
    print("Extracted Topics and Subtopics:")
    print(topics_and_subtopics)

if __name__ == "__main__":
    pdf_path = "path_to_your_pdf.pdf"
    main(pdf_path)
