
import chromadb
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
client_ai = OpenAI()


# 1. Connect to persistent database
client = chromadb.PersistentClient(
    path="./chroma_db"
)

# 2. Create or retrieve collection
collection = client.get_or_create_collection(
    name="fitness_knowledge"
)


def store_documents(chunks, embeddings):

    # Create unique IDs for each chunk
    ids = [f"fitness_{i}" for i in range(len(chunks))]

    # Add documents and embeddings to ChromaDB
    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=[
            {"source": "fitness_fundamentals.txt"}
            for _ in chunks
        ]
    )

    print("Documents stored successfully!")
    print("Total documents:", collection.count())




EMBEDDING_MODEL = "text-embedding-3-small"


def search_documents(question, n_results=3):

    # Generate embedding for the user's question
    response = client_ai.embeddings.create(
        model=EMBEDDING_MODEL,
        input=question
    )

    question_embedding = response.data[0].embedding

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=n_results
    )

    return results




if __name__ == "__main__":

    print("ChromaDB connected successfully!")
    print("Collection:", collection.name)
    print("Stored documents:", collection.count())

    question = "How can I increase the difficulty of my workouts?"

    print("\nSearching for:", question)

    results = search_documents(question, n_results=3)

    print("\nRelevant knowledge:")

    for i, document in enumerate(results["documents"][0]):
        print(f"\nResult {i + 1}:")
        print(document)
