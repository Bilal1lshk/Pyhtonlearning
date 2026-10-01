import ast
import json
import os
import re
import sys
import glob
import time
import tokenize

from dotenv import load_dotenv
from google import genai

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "comments_embeddings.json")

EMBED_MODELS = ["gemini-embedding-001", "text-embedding-004"]

load_dotenv(os.path.join(BASE_DIR, ".env"))


def source_files():
    files = []
    for base in (BASE_DIR, os.path.dirname(BASE_DIR)):
        for path in glob.glob(os.path.join(base, "*.py")):
            if os.path.basename(path) in ("embed_comments.py", "query_comments.py", "rag.py"):
                continue
            files.append(path)
    return sorted(set(os.path.normpath(f) for f in files))


def extract_comment_blocks(path):
    comments = []
    block = []
    prev_line = None
    try:
        with tokenize.open(path) as f:
            for tok in tokenize.generate_tokens(f.readline):
                if tok.type == tokenize.COMMENT:
                    if block and tok.start[0] > prev_line + 1:
                        comments.append(" ".join(block))
                        block = []
                    block.append(tok.string.lstrip("#").strip())
                    prev_line = tok.end[0]
                elif block:
                    comments.append(" ".join(block))
                    block = []
                    prev_line = None
        if block:
            comments.append(" ".join(block))
    except Exception as e:
        print(f"  ! error reading comments in {path}: {e}")
    return [c for c in comments if c and any(ch.isalnum() for ch in c)]


def extract_docstrings(path):
    docs = []
    try:
        with open(path, encoding="utf-8") as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                doc = ast.get_docstring(node)
                if doc:
                    docs.append(doc.strip())
    except Exception as e:
        print(f"  ! error reading docstrings in {path}: {e}")
    return docs


def collect_chunks():
    chunks = []
    for path in source_files():
        rel = os.path.relpath(path, os.path.dirname(BASE_DIR))
        for text in extract_comment_blocks(path):
            chunks.append({"file": rel, "type": "comment", "text": text})
        for text in extract_docstrings(path):
            chunks.append({"file": rel, "type": "docstring", "text": text})
    return chunks


def _retry_delay(exc):
    match = re.search(r"retry in (\d+(?:\.\d+)?)s", str(exc))
    return float(match.group(1)) + 1.0 if match else 8.0


def embed_batch(client, model, contents, batch_size=50):
    vectors = []
    for i in range(0, len(contents), batch_size):
        batch = contents[i:i + batch_size]
        attempts = 0
        while True:
            try:
                result = client.models.embed_content(
                    model=model,
                    contents=batch,
                    config={"task_type": "RETRIEVAL_DOCUMENT"},
                )
                vectors.extend(e.values for e in result.embeddings)
                break
            except Exception as e:
                if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                    attempts += 1
                    if attempts > 5:
                        raise
                    delay = _retry_delay(e)
                    print(f"  ! rate limited, retrying in {delay:.0f}s ...")
                    time.sleep(delay)
                else:
                    raise
    return vectors


def load_embedding_model():
    client = genai.Client(api_key=os.getenv("gemini_api_key"))
    for candidate in EMBED_MODELS:
        try:
            print(f"Checking model {candidate} ...")
            test = client.models.embed_content(model=candidate, contents=["ping"])
            print(f" -> {candidate} ready.")
            return client, candidate
        except Exception as e:
            print(f"  ! {candidate} failed: {str(e)[:120]}")
    sys.exit("No embedding model available.")


def main():
    chunks = collect_chunks()
    if not chunks:
        print("No comments/docstrings found.")
        return

    print(f"Extracted {len(chunks)} comment/step blocks.")
    print("Extracting docs: " + ", ".join(sorted({c['file'] for c in chunks})))

    client, model = load_embedding_model()
    vectors = embed_batch(client, model, [c["text"] for c in chunks])

    os.makedirs(DATA_DIR, exist_ok=True)
    payload = {
        "model": model,
        "dimensions": len(vectors[0]),
        "count": len(chunks),
        "items": [
            {"id": i, **chunks[i], "vector": vectors[i]}
            for i in range(len(chunks))
        ],
    }
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    print(f"Saved {len(chunks)} embeddings -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()