import json
import os
import sys

from dotenv import load_dotenv
from google import genai

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv(os.path.join(BASE_DIR, ".env"))


def load_items(filename):
    path = os.path.join(BASE_DIR, "data", filename)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0


def main():
    if len(sys.argv) < 2:
        print('Usage: python query_comments.py "your question" [top_k] [comments|pdf]')
        return
    store = sys.argv[3] if len(sys.argv) > 3 else "comments"
    filename = "pdf_embeddings.json" if store == "pdf" else "comments_embeddings.json"
    top_k = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    data = load_items(filename)
    model = data["model"]

    client = genai.Client(api_key=os.getenv("gemini_api_key"))
    result = client.models.embed_content(model=model, contents=[sys.argv[1]])
    query_vector = result.embeddings[0].values

    scored = sorted(
        ((cosine(query_vector, item["vector"]), item) for item in data["items"]),
        key=lambda x: x[0],
        reverse=True,
    )

    print(f"Top {top_k} matches ({filename}, model: {model})\n")
    for rank, (score, item) in enumerate(scored[:top_k], 1):
        source = item.get("file", "?")
        if item.get("type") == "pdf":
            source = f"pdf page {item.get('page')} chunk {item.get('chunk')}: {source}"
        print(f"{rank}. [{item['type']}] {source}  (similarity: {score:.3f})")
        print(f"   {item['text'][:180]}\n")


if __name__ == "__main__":
    main()