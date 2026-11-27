# Sprint 06 – Retrieval-Augmented Generation (RAG) Integration

**Project:** AI Fitness Assistant  
**Sprint:** 06  
**Status:** Completed  
**Focus:** Integrating ChromaDB semantic retrieval with the OpenAI-powered Streamlit chatbot.

---

## 1. Sprint Objective

The objective of this sprint was to integrate the existing ChromaDB vector database with the AI Fitness Assistant to implement a Retrieval-Augmented Generation (RAG) pipeline.

The chatbot was enhanced to retrieve relevant fitness knowledge from the knowledge base before generating responses using the OpenAI API.

## 2. Implementation Overview

### 2.1 Connected ChromaDB to the Streamlit Application

Imported the existing `search_documents()` function from `vector_store.py` into `app.py`.

This enabled the Streamlit application to access the persistent fitness knowledge collection.

### 2.2 Implemented Knowledge Retrieval

Whenever a user submits a fitness question:

- The question is converted into an embedding using `text-embedding-3-small`.
- ChromaDB searches the existing fitness knowledge collection.
- The three most relevant document chunks are retrieved.

### 2.3 Constructed Retrieved Context

The retrieved documents are extracted from the ChromaDB query results and combined into a single context string.

This context is then included in the instructions sent to the OpenAI model.

### 2.4 Integrated Retrieval with Response Generation

The retrieved fitness knowledge is combined with:

- The existing fitness assistant system prompt.
- The user's fitness profile.
- The conversation history.
- The current user question.

The OpenAI model uses this information to generate relevant and personalised responses.

### 2.5 Preserved Existing Chatbot Functionality

The existing application functionality was retained:

- Streamlit chat interface.
- Fitness profile configuration.
- Conversation history.
- Follow-up question support.
- Conversation reset functionality.
- OpenAI API error handling.

## 3. Technical Components

| Component | Technology | Purpose |
|---|---|---|
| User interface | Streamlit | Chat interface |
| Programming language | Python | Application logic |
| Language model | OpenAI API | Response generation |
| Embedding model | text-embedding-3-small | Question embeddings |
| Vector database | ChromaDB | Semantic retrieval |
| Configuration | python-dotenv | API key management |

## 4. RAG Workflow

1. User submits a fitness question.
2. The question is converted into an embedding.
3. ChromaDB retrieves the three most relevant fitness knowledge chunks.
4. Retrieved documents are combined into context.
5. The context is added to the assistant instructions along with the fitness profile.
6. The OpenAI model generates a response using the retrieved context and conversation history.
7. The response is displayed in the Streamlit application and saved to conversation history.

## 5. Testing and Validation

The integrated application was launched successfully using Streamlit.

**Test scenarios:**

| Test | Expected behaviour | Result |
|---|---|---|
| Ask about progressive overload | Relevant fitness explanation | Passed |
| Ask how to increase workout difficulty | Relevant knowledge-based response | Passed |
| Ask about muscle recovery | Relevant recovery explanation | Passed |
| Ask a follow-up question | Maintains conversational context | Passed |
| Run the Streamlit application | Application launches successfully | Passed |

## 6. Sprint Outcome

Successfully implemented the first working RAG pipeline in the AI Fitness Assistant.

The application can now retrieve relevant information from its fitness knowledge base and provide contextual responses through the OpenAI API.

This sprint established the foundation for building more advanced AI applications using retrieval, embeddings, vector databases and LLM integration.

## 7. Deliverables

- Integrated ChromaDB retrieval into `app.py`.
- Connected `search_documents()` from `vector_store.py`.
- Implemented retrieved context construction.
- Integrated retrieved knowledge with OpenAI response generation.
- Successfully tested chatbot responses and follow-up conversations.

## 8. Next Sprint

**Sprint 07 – RAG Testing and Evaluation**

Planned activities:

- Validate retrieval relevance.
- Test questions outside the knowledge base.
- Improve handling of empty retrieval results.
- Evaluate response grounding.
- Improve error handling and retrieval reliability.

---

**Sprint Status: Completed**