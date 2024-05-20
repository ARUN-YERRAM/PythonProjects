from pdf_extractor import extract_text_from_pdf
from topic_extractor import extract_topics_and_subtopics
import openai

def main(pdf_path):
    # Ensure you have set your OpenAI API key
    openai.api_key = 'your_openai_api_key'
    
    text = extract_text_from_pdf(pdf_path)
    topics_and_subtopics = extract_topics_and_subtopics(text)
    
    print("Extracted Topics and Subtopics:")
    print(topics_and_subtopics)

if __name__ == "__main__":
    pdf_path = "path_to_your_pdf.pdf"
    main(pdf_path)
