from vector_store import store_documents
import os
import re
import math

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv(os.path.join(BASE_DIR, ".env"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

KNOWLEDGE_FILE = os.path.join(
    BASE_DIR,
    "knowledge_base",
    "fitness_fundamentals.txt"
)

# Embedding model
EMBEDDING_MODEL = "text-embedding-3-small"


def load_document():
    """Read the fitness knowledge document."""

    with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as file:
        return file.read()


def split_into_chunks(content):
    """Split document into topic-based chunks."""

    chunks = re.split(r"(?=TOPIC: )", content)

    return [
        chunk.strip()
        for chunk in chunks
        if chunk.strip()
    ]


def generate_embeddings(text_list):
    """Convert text into numerical vectors."""

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text_list
    )

    return [item.embedding for item in response.data]


def cosine_similarity(vector_a, vector_b):
    """Calculate similarity between two vectors."""

    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def search_knowledge(question, chunks, chunk_embeddings):
    """Find the most relevant document chunk."""

    question_embedding = generate_embeddings([question])[0]

    results = []

    for chunk, embedding in zip(chunks, chunk_embeddings):

        score = cosine_similarity(
            question_embedding,
            embedding
        )

        results.append((score, chunk))

    results.sort(key=lambda item: item[0], reverse=True)

    return results


if __name__ == "__main__":

    # Load and split document
    document = load_document()
    chunks = split_into_chunks(document)

    print(f"Total chunks: {len(chunks)}")

    # Generate document embeddings
    print("\nGenerating document embeddings...")

    chunk_embeddings = generate_embeddings(chunks)
    store_documents(chunks, chunk_embeddings)
    print("Embeddings generated successfully!")

    # Test semantic search
    question = "How can I increase the difficulty of my workouts?"

    print(f"\nUser question: {question}")

    results = search_knowledge(
        question,
        chunks,
        chunk_embeddings
    )

    print("\nMost relevant results:")

    for score, chunk in results[:3]:

        print(f"\nSimilarity score: {score:.4f}")
        print(chunk)
