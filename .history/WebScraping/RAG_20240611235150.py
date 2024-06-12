from datasets import load_dataset, Features, Value

features = Features({'headline': Value('string'), 'url': Value('string')})
dataset = load_dataset('csv', data_files='your_data.csv', features=features)

from transformers import RagTokenizer, RagTokenForGeneration, RagRetriever

tokenizer = RagTokenizer.from_pretrained('facebook/rag-token-nq')
model = RagTokenForGeneration.from_pretrained('facebook/rag-token-nq')

retriever = RagRetriever.from_pretrained('facebook/rag-token-nq', dataset=dataset)
model.set_retriever(retriever)
