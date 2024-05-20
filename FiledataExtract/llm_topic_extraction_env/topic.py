import openai

def extract_topics_and_subtopics(text):
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=f"Extract topics and subtopics from the following text:\n\n{text}",
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
