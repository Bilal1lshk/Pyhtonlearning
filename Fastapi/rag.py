import chromadb

client = chromadb.Client()
collection = client.create_collection(name="pdf_embeddings")

collection.add(
    documents=[
        "In 1950, Alan Turing published 'Computing Machinery and Intelligence', "
        "asking whether machines can think and proposing the imitation game, "
        "now known as the Turing Test.",
        "The 1956 Dartmouth workshop is widely seen as the birth of AI as a field. "
        "John McCarthy coined the term 'artificial intelligence' for it.",
        "In the 1980s, expert systems used hand-written if-then rules to capture "
        "human expertise. They worked in narrow domains but were costly to maintain.",
        "AI winters were periods in the 1970s and late 1980s when funding and "
        "interest dropped because progress did not match the early promises.",
        "In 1997, IBM's Deep Blue defeated world chess champion Garry Kasparov, "
        "showing that search and computing power could beat top human players.",
        "In 2012, the AlexNet neural network won the ImageNet competition by a wide "
        "margin, starting the deep learning boom powered by GPUs and large datasets.",
        "In 2017, the paper 'Attention Is All You Need' introduced the Transformer "
        "architecture, which became the foundation of modern language models.",
        "Large language models trained on huge text corpora, such as GPT and Claude, "
        "can write, summarize, translate, and reason across many tasks.",
        "Retrieval-Augmented Generation (RAG) lets a model look up relevant documents "
        "at question time, giving more accurate and up-to-date answers with sources.",
        "AI agents combine language models with tools, memory, and planning so they "
        "can complete multi-step tasks such as research, coding, and automation.",
    ],
    metadatas=[
        {"source": "ai_history.pdf", "page": 1, "era": "foundations", "year": 1950},
        {"source": "ai_history.pdf", "page": 2, "era": "foundations", "year": 1956},
        {"source": "ai_history.pdf", "page": 4, "era": "symbolic", "year": 1980},
        {"source": "ai_history.pdf", "page": 5, "era": "symbolic", "year": 1974},
        {"source": "ai_history.pdf", "page": 6, "era": "milestones", "year": 1997},
        {"source": "deep_learning.pdf", "page": 1, "era": "deep-learning", "year": 2012},
        {"source": "deep_learning.pdf", "page": 3, "era": "deep-learning", "year": 2017},
        {"source": "modern_ai.pdf", "page": 1, "era": "generative", "year": 2022},
        {"source": "modern_ai.pdf", "page": 4, "era": "generative", "year": 2020},
        {"source": "modern_ai.pdf", "page": 7, "era": "agents", "year": 2024},
    ],
    ids=[f"doc{i}" for i in range(1, 11)],
)

# Search 1: plain search
results = collection.query(
    query_texts=["What made modern language models possible?"],
    n_results=3,
)
print(results["documents"][0])

# Search 2: search with a metadata filter
filtered = collection.query(
    query_texts=["How did AI improve?"],
    n_results=2,
    where={"era": "deep-learning"},
)
print(filtered["documents"][0])