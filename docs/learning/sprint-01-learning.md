# Sprint 01 — Learning Documentation

## 1. Objective

Understand the fundamentals of setting up a Python application and developing a basic chatbot interface using Streamlit.

## 2. Project Environment Setup

### Python Virtual Environment

Created an isolated Python environment using:

```bash
python3 -m venv venv
```

Activated the environment on macOS:

```bash
source venv/bin/activate
```

Used the environment-specific Python executable to install and run packages:

```bash
./venv/bin/python -m pip install streamlit
```

**Concept learned:** Virtual environments isolate project dependencies and reduce conflicts between Python projects.

## 3. Streamlit Application

Created `app.py` to build the chatbot interface.

Key Streamlit components explored:

- `st.title()` — Displays the application heading.
- `st.chat_message()` — Displays individual chat messages.
- `st.chat_input()` — Accepts user input.
- `st.session_state` — Maintains application state across Streamlit reruns.

## 4. Conversation Management

Implemented conversation history using Streamlit session state.

**Why is this important?**

Streamlit reruns the application when users interact with its widgets. Session state allows us to preserve conversation messages across these reruns.

## 5. Application Workflow

1. User opens the Streamlit application.
2. Chat interface is displayed.
3. User enters a message.
4. The application processes the input.
5. Conversation history is updated.
6. Previous messages remain visible during the session.

## 6. Technical Concepts Learned

| Concept | Explanation |
|---|---|
| Python environment | Isolated environment for project dependencies |
| Streamlit | Python framework for interactive web applications |
| Session state | Stores information across application reruns |
| Chat interface | User-facing conversational interface |
| Git | Tracks source code changes |

## 7. Testing and Validation

- Verified that the Streamlit application launches.
- Verified that the chat interface renders correctly.
- Tested user message input.
- Verified that conversation history is retained during the session.

## 8. Challenges and Learnings

### Python command not found

The macOS terminal did not recognise the `python` command.

**Resolution:** Used the virtual environment's direct Python executable:

```bash
./venv/bin/python
```

### Streamlit module not found

The global Python installation did not contain Streamlit.

**Resolution:** Installed and executed Streamlit within the project virtual environment.

## 9. Sprint Outcome

Successfully created the initial interactive chatbot application and established the Python development environment.

## 10. Next Sprint

Integrate the OpenAI API and understand how Large Language Models generate responses.
