from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
if not token:
    raise ValueError("GITHUB_TOKEN not set")
endpoint = "https://models.github.ai/inference"
model_name = "openai/text-embedding-3-small"


client = OpenAI(
    base_url=endpoint,
    api_key=token,
)


text = "Eiffel Tower is in Paris and is a famous landmark, it is 324 meters tall"

response = client.embeddings.create(
    input=text,
    model = model_name
)

print("Embedding vector:", response.data[0].embedding)
