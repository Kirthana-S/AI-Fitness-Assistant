# Sprint 04 — Learning Documentation

# Part 1: Document Processing & Chunking

## 1. Sprint Objective

Understand how to create a knowledge base, load documents programmatically and split large text into smaller chunks.

This is an important foundation for building Retrieval-Augmented Generation (RAG) applications.

## 2. Understanding a Knowledge Base

A knowledge base is a collection of information that an application can access to answer relevant questions.

In our AI Fitness Assistant, the knowledge base contains fitness-related information.

Created the following structure:

```text
AI-Fitness-Assistant/
│
└── knowledge_base/
    └── fitness_fundamentals.txt
```

The text file contains information covering:

- Progressive overload
- Strength training
- Muscle recovery
- Protein and muscle

## 3. Document Loading

Implemented a Python function to read the contents of the fitness knowledge document.

**Concept learned: File Handling**

Python file handling allows applications to read, write and process information stored in files.

The application reads the document and loads its contents into a Python string for further processing.

## 4. Understanding Text Chunking

Text chunking is the process of dividing a larger document into smaller, manageable pieces of text.

### Why is chunking important?

When building retrieval-based AI applications, sending an entire document for every question may be inefficient.

Instead, smaller chunks allow the system to retrieve only the information relevant to the user's question.

### Chunking approach used

Implemented topic-based chunking using Python regular expressions.

The document uses topic headings in the following format:

```text
TOPIC: Progressive Overload

TOPIC: Strength Training

TOPIC: Muscle Recovery

TOPIC: Protein and Muscle
```

The application splits the document whenever it encounters a new `TOPIC:` heading.

### Result

Successfully generated four separate chunks from the fitness document.

## 5. Understanding Regular Expressions

Regular expressions (RegEx) are patterns used to identify and manipulate text.

In this project, the following expression was used:

```python
r"(?=TOPIC: )"
```

This is a positive lookahead.

It identifies positions immediately before `TOPIC: ` without consuming the heading itself.

This allows the text to be split while preserving each topic heading in its corresponding chunk.

## 6. Technical Concepts Learned — Part 1

| Concept | Explanation | Application |
|---|---|---|
| Knowledge base | Collection of information | Fitness reference document |
| File handling | Reading and processing files | Loading `.txt` document |
| Text preprocessing | Preparing text for further processing | Cleaning and splitting content |
| Chunking | Dividing text into smaller pieces | Four fitness topic chunks |
| Regular expressions | Pattern-based text processing | Detecting topic headings |

---

# Part 2: Embeddings & Semantic Search

## 7. Sprint Objective

Understand how text can be converted into numerical vectors and how semantic search can retrieve relevant information based on meaning rather than exact keyword matches.

## 8. Understanding Embeddings

An embedding is a numerical representation of text in a vector space.

An embedding model converts text into a list of numbers that captures semantic information about the text.

In our project, we used the OpenAI embedding model:

`text-embedding-3-small`

Each fitness document chunk was converted into a numerical vector.

The model produces 1536-dimensional embeddings by default.

### Example

Original text:

"Progressive overload involves gradually increasing the demands placed on the body during training."

The embedding model converts this text into a numerical vector.

The actual vector contains many numerical values and is not directly readable as ordinary text.

## 9. Generating Document Embeddings

Integrated the OpenAI Embeddings API into `retriever.py`.

The process:

1. Load the four document chunks.
2. Send the chunks to the embeddings endpoint.
3. Receive the numerical vectors.
4. Store the vectors temporarily in Python memory.

**Concept learned:** Embedding generation.

The original text remains available separately from its numerical representation.

## 10. Understanding Semantic Search

Traditional keyword search looks for matching words or phrases.

Semantic search attempts to identify information that is similar in meaning.

Example:

**User question:** How can I make my workouts more challenging?

The knowledge base may contain:

"Progressive overload involves gradually increasing training demands."

Even though the wording is different, the concepts are related.

Semantic search helps identify this relevant information.

## 11. Understanding Cosine Similarity

Cosine similarity measures the similarity between two vectors by calculating the cosine of the angle between them.

It is commonly used to compare text embeddings.

The formula is:

\[
\text{Cosine Similarity}(A,B)=
\frac{A \cdot B}{\|A\|\|B\|}
\]

Where:

- A = Query embedding
- B = Document embedding
- A · B = Dot product
- ||A|| and ||B|| = Vector magnitudes

For non-zero vectors, a higher cosine similarity generally indicates greater directional similarity.

## 12. Implementing Semantic Search

Implemented the following process:

1. Generate an embedding for the user's question.
2. Compare it against the stored document embeddings.
3. Calculate cosine similarity scores.
4. Sort the results in descending similarity order.
5. Return the most relevant document chunks.

### Example test question

"How can I increase the difficulty of my workouts?"

The system successfully retrieved relevant fitness information, including the progressive overload topic.

## 13. Document Retrieval Workflow

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
    Four Text Chunks
          |
          v
    OpenAI Embeddings
          |
          v
   Numerical Vectors
          |
          v
      User Question
          |
          v
   Query Embedding
          |
          v
   Cosine Similarity
          |
          v
     Rank Results
          |
          v
  Relevant Text Chunks
```

## 14. Technical Concepts Learned — Part 2

| Concept | Explanation | Application |
|---|---|---|
| Embeddings | Numerical representations of text | Fitness document vectors |
| Vector | Ordered collection of numerical values | Embedding representation |
| Embedding model | Model that converts text into vectors | text-embedding-3-small |
| Semantic search | Search based on meaning | Fitness information retrieval |
| Cosine similarity | Measures directional similarity | Query-document comparison |
| Ranking | Ordering results by relevance | Top relevant chunks |

## 15. Testing and Validation

### Document Processing Tests

- Verified successful document loading.
- Verified that the document was divided into four chunks.
- Checked that each topic heading was preserved.

### Embedding Tests

- Verified successful API connection.
- Generated embeddings for all four chunks.
- Verified embedding dimensions.

### Semantic Search Tests

- Generated an embedding for a test question.
- Compared it against document embeddings.
- Verified that relevant fitness chunks were returned.
- Confirmed that progressive overload appeared among the relevant results.

**Result:** Document processing, embedding generation and semantic search were successfully tested.

## 16. Challenges and Learnings

### API credits exhausted

During embedding generation, the API returned a 429 error indicating that no credits remained.

**Resolution:** Added $5 in API credit and reran the embedding test successfully.

### Understanding the difference between keyword search and semantic search

Learned that semantic search can retrieve related information even when the wording of a question differs from the source document.

### Embeddings versus original text

Learned that embeddings are numerical representations, not replacements for the original text. Both are needed for our retrieval workflow.

## 17. Sprint Outcome

Successfully developed the initial knowledge retrieval pipeline.

The application can now:

- Load fitness documents.
- Split content into topic-based chunks.
- Generate numerical embeddings.
- Convert user questions into embeddings.
- Compare vectors using cosine similarity.
- Rank and retrieve relevant knowledge.

## 18. Next Sprint

**Sprint 05 — Vector Database & Persistent Storage**

Integrate ChromaDB to store document chunks, embeddings and metadata persistently, and implement database-based semantic search.

---

# 19. Code Reference — Sprint 04

The following snippets represent the important implementation patterns used during this sprint. They are reconstructed reference examples; check your actual `retriever.py` before treating them as exact copies.

## Part 1 — Document Processing

### 19.1 Import required libraries

```python
import re
```

### 19.2 Load the document

```python
def load_document(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return content
```

### 19.3 Split document into chunks

```python
def split_into_chunks(content):

    chunks = re.split(r"(?=TOPIC: )", content)

    chunks = [
        chunk.strip()
        for chunk in chunks
        if chunk.strip()
    ]

    return chunks
```

### 19.4 Test document chunking

```python
if __name__ == "__main__":

    content = load_document(
        "knowledge_base/fitness_fundamentals.txt"
    )

    chunks = split_into_chunks(content)

    print("Total chunks:", len(chunks))

    for i, chunk in enumerate(chunks):
        print(f"\nChunk {i + 1}:")
        print(chunk)
```

## Part 2 — Embeddings & Semantic Search

### 19.5 Initialise OpenAI client

```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

EMBEDDING_MODEL = "text-embedding-3-small"
```

### 19.6 Generate embeddings

```python
def generate_embeddings(text_list):

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text_list
    )

    embeddings = [
        item.embedding
        for item in response.data
    ]

    return embeddings
```

### 19.7 Calculate cosine similarity

```python
import math

def cosine_similarity(vec_a, vec_b):

    dot_product = sum(
        a * b
        for a, b in zip(vec_a, vec_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vec_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vec_b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (
        magnitude_a * magnitude_b
    )
```

### 19.8 Implement semantic search

```python
def search_knowledge(question, chunks, chunk_embeddings):

    question_embedding = generate_embeddings(
        [question]
    )[0]

    similarities = []

    for i, embedding in enumerate(chunk_embeddings):

        score = cosine_similarity(
            question_embedding,
            embedding
        )

        similarities.append((score, chunks[i]))

    similarities.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return similarities
```

### 19.9 Test semantic search

```python
question = "How can I increase the difficulty of my workouts?"

results = search_knowledge(
    question,
    chunks,
    chunk_embeddings
)

for score, chunk in results[:3]:

    print("\nSimilarity Score:", score)
    print("Relevant Chunk:")
    print(chunk)
```

### 19.10 Dependencies used

Relevant packages:

```text
openai
python-dotenv
```

Install them using:

```bash
./venv/bin/python -m pip install openai python-dotenv
```

---

**End of Sprint 04 Learning Documentation**
