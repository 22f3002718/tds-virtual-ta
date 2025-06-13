import json
from openai import OpenAI
import os

# Use environment variable for API key (recommended)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "your-openai-api-key"))

def load_data():
    with open("data/discourse/discourse_posts.json") as f:
        return json.load(f)

def generate_answer(question):
    posts = load_data()
    context = "\n".join([p["title"] for p in posts[:10]])  # Keep it short for speed

    prompt = f"Question: {question}\n\nContext from Discourse:\n{context}\n\nAnswer:"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content, posts[:2]  # Return 2 links for now
