# Sprint 02 — Learning Documentation

## 1. Sprint Objective

Understand how to integrate a Large Language Model (LLM) into a Python application using the OpenAI API and build a conversational AI experience.

## 2. Understanding Large Language Models

A Large Language Model (LLM) is an AI model trained on large amounts of text to understand and generate human-like language.

In this project, the LLM acts as the intelligence layer behind the chatbot.

Instead of generating predefined responses, the application sends the user's message to the model and receives a generated response.

## 3. OpenAI API Integration

### What is an API?

An Application Programming Interface (API) allows two software systems to communicate with each other.

In our project:

- Streamlit handles the user interface.
- Python manages the application logic.
- The OpenAI API provides access to the language model.
- The model generates the response.

### OpenAI Python SDK

Installed and configured the OpenAI Python SDK to communicate with the API.

The application uses an OpenAI client to send requests and receive model responses.

## 4. Environment Variables and API Key Security

Created a `.env` file to store the API key.

Example:

```env
OPENAI_API_KEY=your_api_key_here
```

Used `python-dotenv` to load environment variables.

```python
from dotenv import load_dotenv

load_dotenv()
```

**Concept learned:** Sensitive credentials should not be hardcoded into application source files or committed to public repositories.

The `.env` file is excluded through `.gitignore`.

## 5. System Prompt and Prompt Engineering

Introduced a system prompt to define the chatbot's role and behaviour.

The system prompt establishes:

- The assistant's identity as a fitness-focused assistant.
- Its primary area of expertise.
- The expected response behaviour.
- Boundaries for handling unrelated questions.

**Concept learned: Prompt Engineering**

Prompt engineering involves designing instructions and context to influence how an LLM responds.

In this project, the system prompt helps keep the assistant focused on fitness-related interactions.

## 6. Generating AI Responses

Integrated the OpenAI Responses API into the application.

Conceptual workflow:

1. User submits a question.
2. Python prepares the request.
3. The application sends the system instructions and conversation context to the model.
4. The model processes the request.
5. The generated response is displayed in Streamlit.

The application uses:

```python
client.responses.create(...)
```

The model identifier is configured in the application.

## 7. Conversation History and Context

Introduced conversation history into the API request.

Instead of sending only the latest question, the application includes previous messages so the model can understand follow-up questions.

Example:

**User:** What is progressive overload?

**Assistant:** Explains progressive overload.

**User:** Can you give me an example?

The previous conversation provides the context needed to understand what "it" refers to.

**Concept learned:** Context management is essential for conversational AI applications.

## 8. Application Architecture

```text
User
 |
 v
Streamlit Chat Interface
 |
 v
Python Application Logic
 |
 v
System Prompt + Conversation History
 |
 v
OpenAI API
 |
 v
LLM Response
 |
 v
Streamlit Chat Interface
```

## 9. Technical Concepts Learned

| Concept | Explanation | Application |
|---|---|---|
| LLM | Model that understands and generates language | AI response generation |
| API | Interface for software communication | Connecting Python to OpenAI |
| SDK | Library simplifying API integration | OpenAI Python SDK |
| System prompt | Instructions defining model behaviour | Fitness-focused assistant |
| Prompt engineering | Designing effective instructions | Controlling response behaviour |
| Context management | Supplying relevant conversation history | Follow-up questions |
| Environment variables | External configuration values | API key security |

## 10. Testing and Validation

Performed the following tests:

- Verified that the API connection worked.
- Submitted fitness-related questions.
- Checked whether the model generated meaningful answers.
- Tested follow-up questions to verify conversational context.
- Tested unrelated questions to examine the fitness-focused system prompt.

**Result:** The application successfully generated AI responses and maintained conversational context.

## 11. Challenges and Learnings

### API configuration

Configured the API key through `.env` rather than embedding it in Python code.

### Separating interface and intelligence

Learned the difference between a chatbot interface and the language model responsible for generating responses.

### Context handling

Learned why sending conversation history matters for follow-up interactions.

## 12. Sprint Outcome

Successfully transformed the basic chatbot into an AI-powered conversational application using the OpenAI API.

The application now has:

- A conversational AI engine.
- Fitness-specific system instructions.
- Context-aware interactions.
- Secure API credential configuration.

## 13. Next Sprint

**Sprint 03 — User Profiling & Personalisation**

Introduce user-specific fitness profiles and dynamically incorporate their preferences into the system prompt.

---

# 14. Code Reference — Sprint 02

This section contains the key implementation patterns used during this sprint for future reference.

**Note:** These are reference snippets based on our documented implementation. Compare them with your actual `app.py` before treating them as an exact copy of the original source code.

### 14.1 Load environment variables

```python
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from .env
load_dotenv()

# Initialise OpenAI client
client = OpenAI()
```

### 14.2 API configuration

`.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

The OpenAI SDK reads the API key from the environment.

### 14.3 System prompt

```python
SYSTEM_PROMPT = """
You are an AI Fitness Assistant.

Your role is to help users understand:
- Fitness fundamentals
- Strength training
- Muscle building
- Workout planning
- Recovery and nutrition

Keep your responses focused on fitness-related topics.
Provide clear, practical and understandable explanations.
"""
```

### 14.4 Generate an AI response

```python
response = client.responses.create(
    model=MODEL_NAME,
    instructions=SYSTEM_PROMPT,
    input=conversation_history
)

assistant_response = response.output_text
```

`MODEL_NAME` should be the model identifier already configured in the working application.

### 14.5 Maintain conversation history

Conceptual example using Streamlit session state:

```python
import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []

# Add the user's message
st.session_state.messages.append({
    "role": "user",
    "content": user_input
})

# Send conversation history to the model
response = client.responses.create(
    model=MODEL_NAME,
    instructions=SYSTEM_PROMPT,
    input=st.session_state.messages
)

assistant_response = response.output_text

# Store assistant response
st.session_state.messages.append({
    "role": "assistant",
    "content": assistant_response
})
```

**Important:** This is an illustrative conversation-history pattern, not a guaranteed line-for-line copy of the original `app.py`. Adapt it to your actual message-handling structure.

### 14.6 Display chat messages in Streamlit

```python
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
```

### 14.7 Accept user input

```python
user_input = st.chat_input("Ask me a fitness question...")
```

### 14.8 Dependencies used

Relevant packages:

```text
streamlit
openai
python-dotenv
```

Install dependencies using:

```bash
./venv/bin/python -m pip install streamlit openai python-dotenv
```

---

**End of Sprint 02 Learning Documentation**