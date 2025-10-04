from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_embedding(text: str):
    return client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    ).embeddings[0].values
