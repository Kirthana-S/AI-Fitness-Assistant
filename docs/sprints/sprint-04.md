# Sprint 04 — Knowledge Base Development & Document Processing

**Project:** AI Fitness Assistant  
**Sprint:** 04  
**Status:** Completed

## Sprint Objective

Develop a fitness knowledge base and implement document processing techniques to prepare information for semantic search and Retrieval-Augmented Generation (RAG).

## User Stories

- As a user, I want the assistant to access fitness-related knowledge so that its responses can be grounded in relevant information.
- As a developer, I want documents to be processed and divided into manageable chunks so that relevant information can be retrieved efficiently.
- As a developer, I want to represent document content as numerical embeddings so that semantic search can identify relevant information.

## Key Deliverables

### Part 1 — Document Processing & Chunking

- Created a dedicated `knowledge_base/` directory.
- Created `fitness_fundamentals.txt`.
- Added fitness knowledge covering progressive overload, strength training, muscle recovery and protein.
- Implemented document loading using Python file handling.
- Implemented topic-based text chunking using regular expressions.
- Successfully generated four document chunks.

### Part 2 — Embeddings & Semantic Search

- Integrated the OpenAI Embeddings API.
- Used `text-embedding-3-small` to generate document embeddings.
- Converted text chunks into numerical vector representations.
- Implemented cosine similarity calculation.
- Generated an embedding for a user query.
- Compared query embeddings against document embeddings.
- Ranked document chunks according to semantic similarity.
- Successfully tested retrieval using a fitness-related question.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Document processing and retrieval logic |
| OpenAI Embeddings API | Text-to-vector conversion |
| text-embedding-3-small | Embedding model |
| Regular Expressions | Topic-based chunking |
| Python Math | Cosine similarity calculation |

## Acceptance Criteria

- [x] Fitness knowledge base created.
- [x] Document loaded successfully.
- [x] Content divided into four topic-based chunks.
- [x] Embeddings generated for document chunks.
- [x] Query embedding generated successfully.
- [x] Cosine similarity implemented.
- [x] Relevant chunks ranked and retrieved.
- [x] Semantic search tested successfully.

## Sprint Outcome

Successfully developed the initial document processing and semantic retrieval pipeline.

The application can now convert fitness knowledge into numerical embeddings and retrieve relevant information based on the meaning of a user's question.

## Next Sprint

**Sprint 05 — Vector Database & Persistent Storage**

Integrate ChromaDB to store document chunks and embeddings persistently, enabling semantic retrieval without regenerating all document embeddings every time the application runs.
