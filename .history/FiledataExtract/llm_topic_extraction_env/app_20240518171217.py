from pdfminer.high_level import extract_text
import openai
import os

# Fetch the API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define functions to extract text from PDF and extract topics and subtopics
def extract_text_from_pdf(pdf_path):
    text = extract_text(pdf_path)
    return text

def extract_topics_and_subtopics(text):
    # This function should be implemented separately
    # It's unclear from your code how you're extracting topics and subtopics using OpenAI
    pass

def main(pdf_path):
    # Ensure you have set your OpenAI API key
    openai.api_key = 'your-openai-api-key-here'
    
    text = extract_text_from_pdf(pdf_path)
    topics_and_subtopics = extract_topics_and_subtopics(text)
    
    print("Extracted Topics and Subtopics:")
    print(topics_and_subtopics)

if __name__ == "__main__":
    pdf_path = r"C:\Users\Yerram Abhilash\OneDrive\Documents\ArDocs\Unit-2 IML-1.pdf"
    main(pdf_path)
