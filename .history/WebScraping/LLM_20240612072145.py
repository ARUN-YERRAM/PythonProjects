import tensorflow_hub as hub
import numpy as np
from scipy.spatial.distance import cosine

# Load pre-trained USE model
model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")


def calculate_use_similarity(text1, text2):
    embeddings = model([text1, text2])
    similarity = 1 - cosine(embeddings[0].numpy(), embeddings[1].numpy())
    return similarity

# Example usage
text1 = "Artificial intelligence is transforming many industries.Companies are investing heavily in AI research and development.AI technologies are improving efficiency and productivity.Some jobs are being replaced by AI, while others are being created.The impact of AI is being felt across various sectors, from healthcare to finance."
text2 = "Many sectors are being changed by AI technology.Businesses are putting a lot of money into AI innovations.AI systems are boosting both efficiency and productivity.While some roles are being automated, new job opportunities are emerging.The influence of AI spans multiple industries, including healthcare and finance."
similarity = calculate_use_similarity(text1, text2)
print(f"Similarity: {similarity}")