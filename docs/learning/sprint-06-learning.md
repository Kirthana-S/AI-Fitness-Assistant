# Sprint 06 – Learning Notes: Retrieval-Augmented Generation (RAG)

**Project:** AI Fitness Assistant  
**Sprint:** 06  
**Topic:** Integrating Retrieval-Augmented Generation with an LLM application.

---

## 1. What is Retrieval-Augmented Generation (RAG)?

Retrieval-Augmented Generation (RAG) is an approach that combines information retrieval with Large Language Model (LLM) response generation.

Instead of depending entirely on the information learned during model training, an application can retrieve relevant information from an external knowledge source and provide it to the LLM as additional context.

This helps an AI application generate responses that are more relevant to a specific knowledge base.

### Traditional LLM application

User Question → LLM → Generated Response

### RAG-based application

User Question → Retrieval → Relevant Context → LLM → Generated Response

In this project, ChromaDB acts as the retrieval system, while the OpenAI model generates the final response.

## 2. Why do we need RAG?

A standalone LLM has limitations:

- It may not know the contents of a private or custom knowledge base.
- It may generate answers that are not aligned with specific reference documents.
- It may not have access to newly added external information.
- It can produce hallucinations.

RAG helps address these limitations by supplying relevant external information at response-generation time.

**Example:**

A user asks:

"How can I increase the difficulty of my workouts?"

The application retrieves the Progressive Overload topic from the fitness knowledge base.

The retrieved information explains that progression can involve:

- Increasing resistance or weight.
- Increasing repetitions.
- Increasing sets.
- Improving exercise technique.
- Increasing range of motion where appropriate.

This information is then provided to the LLM to help generate its response.

## 3. Understanding the RAG Architecture

The RAG implementation in this project contains the following stages.

### Stage 1 – User Query

The user submits a question through the Streamlit chat interface.

Example:

"Why is recovery important for muscle growth?"

### Stage 2 – Query Embedding

The user's question is converted into a numerical vector using the OpenAI embedding model:

`text-embedding-3-small`

An embedding represents the semantic meaning of text in numerical form.

### Stage 3 – Semantic Retrieval

The generated query embedding is passed to ChromaDB.

ChromaDB compares the query against the stored document embeddings and retrieves the most relevant documents.

In this implementation, three results are requested.

### Stage 4 – Context Construction

The retrieved documents are extracted and combined into a single text context.

This context becomes additional information for the LLM.

### Stage 5 – Prompt Augmentation

The application combines:

- System instructions.
- User fitness profile.
- Retrieved fitness knowledge.

This is an example of prompt augmentation: dynamically adding relevant information to the instructions supplied to the model.

### Stage 6 – Response Generation

The OpenAI Responses API receives the augmented instructions and conversation history.

The model generates the response, which is displayed through Streamlit.

## 4. Important Concepts Learned

### 4.1 Retrieval vs Generation

These are two different responsibilities.

| Retrieval | Generation |
|---|---|
| Finds relevant information | Produces natural-language responses |
| Uses embeddings and vector search | Uses an LLM |
| Performed by ChromaDB | Performed by OpenAI |
| Returns document chunks | Returns an answer |

### 4.2 Context Injection

Context injection means adding relevant information to the model's input or instructions.

In this project, retrieved fitness documents are injected into the assistant instructions before response generation.

### 4.3 Prompt Augmentation

The original system prompt is enhanced dynamically with retrieved knowledge and the user's fitness profile.

This allows the same assistant to generate responses using different knowledge and user-specific context.

### 4.4 Conversation History

The application continues to pass `st.session_state.messages` to the OpenAI Responses API.

This allows the model to consider previous user and assistant messages when answering follow-up questions.

### 4.5 Top-K Retrieval

Top-K retrieval determines how many relevant documents are returned from the vector database.

In this implementation:

`n_results=3`

This requests the three most relevant document chunks.

The value can be adjusted depending on the size and structure of the knowledge base.

---

## 5. Code Reference

The following snippets represent the main implementation patterns used in Sprint 06.

### 5.1 Importing the Retrieval Function

In `app.py`:

```python
from vector_store import search_documents
```

This makes the semantic retrieval function available to the Streamlit application.

### 5.2 Retrieving Relevant Documents

```python
results = search_documents(user_input, n_results=3)
```

This calls the retrieval function with the user's question and requests three relevant results.

### 5.3 Extracting Retrieved Documents

```python
retrieved_docs = results.get("documents", [[]])[0]
```

ChromaDB returns query results in a structured format.

The code extracts the document chunks from the first query result set.

### 5.4 Constructing the Context

```python
rag_context = "\n\n".join(retrieved_docs)
```

This combines the retrieved document chunks into one context string.

### 5.5 Constructing RAG Instructions

```python
rag_instructions = f"""
{SYSTEM_PROMPT}

{fitness_profile}

RETRIEVED FITNESS KNOWLEDGE:
{rag_context}

Use the retrieved knowledge when relevant.
If the knowledge base does not contain the answer,
be transparent and do not invent information from it.
"""
```

The retrieved knowledge and user profile are dynamically included in the instructions.

### 5.6 Generating the Final Response

```python
response = client.responses.create(
    model="YOUR_EXISTING_MODEL",
    instructions=rag_instructions,
    input=st.session_state.messages,
    max_output_tokens=600
)

ai_response = response.output_text
```

The model receives the augmented instructions and conversation history and generates the response.

**Note:** `YOUR_EXISTING_MODEL` is a placeholder. Retain the actual working model identifier configured in the application.

---

## 6. Technologies and Their Roles

| Technology | Role in the project |
|---|---|
| Python | Core application development |
| Streamlit | Frontend and chat interface |
| OpenAI API | LLM response generation |
| OpenAI Embeddings | Converts text into numerical vectors |
| ChromaDB | Vector storage and semantic retrieval |
| Responses API | Sends instructions and conversation history to the model |

## 7. What I Learned in This Sprint

By completing this sprint, I gained practical understanding of:

1. What Retrieval-Augmented Generation is and why it is useful.
2. How semantic retrieval connects with LLM response generation.
3. How query embeddings are used to retrieve relevant documents.
4. How ChromaDB results can be extracted and converted into context.
5. How retrieved knowledge can be injected into an LLM prompt.
6. How user profiles and retrieved context can work together.
7. How conversation history supports follow-up questions in a RAG application.

## 8. Practical Applications of RAG

RAG is useful in many real-world AI applications:

- Enterprise knowledge assistants.
- Customer support chatbots.
- Document question-answering systems.
- Healthcare information assistants.
- Financial knowledge assistants.
- Internal company policy assistants.
- Technical documentation assistants.

For a Data Analyst transitioning into AI, RAG is particularly useful for building systems that allow users to ask questions about business reports, datasets, documentation and internal knowledge repositories.

## 9. Next Learning Objectives

**Sprint 07 – RAG Testing and Evaluation**

Topics to explore:

- Retrieval relevance and ranking.
- Context quality.
- Hallucination and grounding.
- Empty retrieval handling.
- Evaluation datasets and test questions.
- Improving retrieval reliability.
- Error handling.

---

**Sprint 06 Learning Status: Completed**