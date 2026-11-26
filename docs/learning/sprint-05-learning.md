# Sprint 05 — Learning Documentation

# ChromaDB & Vector Database Integration

## 1. Sprint Objective

Understand how vector databases work and integrate ChromaDB into the AI Fitness Assistant to store and retrieve document embeddings persistently.

Previously, document embeddings were generated and maintained in Python memory.

In this sprint, we introduced persistent vector storage.

## 2. Understanding Vector Databases

A vector database is designed to store and search numerical vector representations of information.

In AI applications, embeddings represent the semantic characteristics of text, images or other supported data.

Vector databases allow applications to retrieve information based on vector similarity.

### Why do we need a vector database?

Our previous implementation had two limitations:

- Embeddings were maintained temporarily in Python memory.
- The application needed to regenerate document embeddings when the script was executed again.

A persistent vector database addresses these limitations by storing embeddings and their associated documents.

## 3. Understanding ChromaDB

ChromaDB is an open-source vector database used to store and retrieve embeddings.

For our project, ChromaDB provides:

- Persistent local storage.
- Collection management.
- Document storage.
- Embedding storage.
- Metadata storage.
- Similarity-based retrieval.

Installed ChromaDB version 1.5.9 in the project's virtual environment.

Installation command:

```bash
./venv/bin/python -m pip install chromadb
```

Version verification:

```bash
./venv/bin/python -c "import chromadb; print(chromadb.__version__)"
```

## 4. Understanding Persistent Storage

ChromaDB provides a `PersistentClient` that stores database information locally.

Unlike temporary Python variables, the database remains available after the Python process ends.

Our database directory:

```text
AI-Fitness-Assistant/
│
└── chroma_db/
```

The directory is excluded from Git using `.gitignore`.

### Concept learned: Persistence

Persistence means storing information so that it remains available beyond the lifetime of the running program.

This is important for AI applications because generating embeddings repeatedly can consume unnecessary API usage and time.

## 5. Understanding Collections

A collection is a logical group of related records in ChromaDB.

Created the collection:

`fitness_knowledge`

It stores the fitness document chunks, their embeddings and metadata.

### Collection structure

| Field | Purpose | Project example |
|---|---|---|
| ID | Unique record identifier | fitness_0 |
| Document | Original text | Progressive overload content |
| Embedding | Numerical vector | OpenAI embedding |
| Metadata | Additional information | Source filename |

## 6. Understanding Document Storage

Created `vector_store.py` to separate vector database operations from the document-processing logic.

The application stores four records using the ChromaDB `upsert()` method.

### What is upsert?

Upsert combines two operations:

- Insert a new record if its ID does not exist.
- Update an existing record if the same ID already exists.

This helps prevent duplicate records when the same ingestion process is executed again with the same IDs.

## 7. Understanding Metadata

Metadata is additional information associated with a stored document.

In our project, the source filename is stored alongside each fitness knowledge chunk.

Example:

```python
{"source": "fitness_fundamentals.txt"}
```

Metadata can help identify where information originated and can support filtering during retrieval.

## 8. Understanding Semantic Retrieval in ChromaDB

ChromaDB provides a `query()` method to search for relevant records.

Our retrieval approach uses OpenAI embeddings.

The process:

1. Accept a user question.
2. Generate an embedding using `text-embedding-3-small`.
3. Pass the question embedding to ChromaDB.
4. ChromaDB compares it with stored document embeddings.
5. Retrieve the requested number of relevant results.

### Why use query_embeddings?

We generate embeddings ourselves using OpenAI.

Therefore, we use `query_embeddings` to pass the numerical representation directly to ChromaDB.

This also ensures that document and query embeddings use the same embedding model.

## 9. Application Architecture

```text
Fitness Knowledge Document
          |
          v
     Document Loading
          |
          v
      Text Chunking
          |
          v
    Generate Embeddings
          |
          v
       ChromaDB
          |
          v
  Persistent Vector Storage
          |
          |
User Question
          |
          v
  Generate Query Embedding
          |
          v
   ChromaDB Similarity Search
          |
          v
    Relevant Documents
```

## 10. Technical Concepts Learned

| Concept | Explanation | Application |
|---|---|---|
| Vector database | Database designed for vector storage and retrieval | ChromaDB |
| Persistence | Information remains available after program termination | Local database |
| Collection | Logical grouping of records | fitness_knowledge |
| Upsert | Insert or update records | Document storage |
| Metadata | Additional information associated with records | Source filename |
| Vector similarity | Comparing numerical representations | Semantic retrieval |
| Query embedding | Vector representation of a search question | User question embedding |

## 11. Testing and Validation

### ChromaDB Installation

- Verified ChromaDB installation.
- Confirmed installed version 1.5.9.

### Database Creation

- Successfully created a persistent database.
- Created the `fitness_knowledge` collection.
- Verified database connectivity.

### Document Storage

- Stored four fitness knowledge chunks.
- Stored their embeddings.
- Stored source metadata.
- Confirmed that the collection contained four records.

### Persistence Test

Closed the database process and executed `vector_store.py` again.

**Result:** The database reopened successfully and still contained four stored records.

### Semantic Retrieval

The ChromaDB retrieval function was implemented using `collection.query()` and OpenAI query embeddings.

**Status:** Final execution and retrieval relevance testing pending.

## 12. Challenges and Learnings

### Python command not found

The macOS terminal did not recognise the `python` command.

**Resolution:** Used the project's virtual environment executable:

```bash
./venv/bin/python
```

### Temporary versus persistent storage

Learned the difference between maintaining vectors in Python memory and storing them in a persistent database.

### Avoiding unnecessary embedding generation

Learned that document embeddings can be stored once and reused during subsequent searches, provided the source documents and embedding configuration have not changed.

## 13. Sprint Outcome

Successfully installed ChromaDB and created a persistent vector database.

Stored four fitness knowledge chunks along with their embeddings and metadata.

Verified that the stored records remained available after reopening the database.

## 14. Next Sprint

**Sprint 06 — Retrieval-Augmented Generation (RAG) Integration**

Integrate the retrieved fitness knowledge with the OpenAI language model to generate context-aware responses grounded in the knowledge base.

---

# 15. Code Reference — Sprint 05

The following code snippets represent the implementation patterns used during this sprint.

## 15.1 Import ChromaDB

```python
import chromadb
```

## 15.2 Create a persistent database client

```python
client = chromadb.PersistentClient(
    path="./chroma_db"
)
```

## 15.3 Create or retrieve a collection

```python
collection = client.get_or_create_collection(
    name="fitness_knowledge"
)
```

## 15.4 Store document chunks and embeddings

```python
def store_documents(chunks, embeddings):

    ids = [
        f"fitness_{i}"
        for i in range(len(chunks))
    ]

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
```

## 15.5 Initialise OpenAI embedding client

```python
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client_ai = OpenAI()

EMBEDDING_MODEL = "text-embedding-3-small"
```

## 15.6 Generate a query embedding

```python
def search_documents(question, n_results=3):

    response = client_ai.embeddings.create(
        model=EMBEDDING_MODEL,
        input=question
    )

    question_embedding = response.data[0].embedding

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=n_results
    )

    return results
```

## 15.7 Inspect retrieved documents

```python
results = search_documents(
    "How can I increase the difficulty of my workouts?",
    n_results=3
)

for i, document in enumerate(results["documents"][0]):

    print(f"\nResult {i + 1}:")
    print(document)
```

## 15.8 Check collection count

```python
print("Collection:", collection.name)
print("Stored documents:", collection.count())
```

## 15.9 Dependencies

Relevant packages:

```text
chromadb
openai
python-dotenv
```

Install using:

```bash
./venv/bin/python -m pip install chromadb openai python-dotenv
```

---

**End of Sprint 05 Learning Documentation**
