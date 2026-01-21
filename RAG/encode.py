# Encode function to encode documents into embeddings space

import re
import os
from google import genai
from dotenv import load_dotenv

# load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def preprocess(document: str) -> str:
    document = document.lower().replace('\n', ' ').replace('\t', ' ')
    document = re.sub(r"[^a-z0-9\s\.,!?'-]", '', document)
    document = re.sub(r'\s+', ' ', document).strip()
    return document

def encode(document):
    result = client.models.embed_content(
        model="text-embedding-004",
        contents=document
    )
    return result.embeddings[0].values

def normalize(embedding):
    norm = sum([x**2 for x in embedding]) ** 0.5
    normalized_embedding = [x / norm for x in embedding]
    return normalized_embedding

if __name__ == "__main__":
    dummy_text = "The Canon EOS 70D DSLR camera features a 20.2-megapixel APS-C CMOS sensor."

    preprocessed_text = preprocess(dummy_text)
    processed_text = encode(preprocessed_text)
    processed_text = normalize(processed_text)
    print(f"Embedding dimension: {len(processed_text)}")
    print(f"First 5 values: {processed_text[:5]}")