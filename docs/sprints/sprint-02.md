# Sprint 02 — OpenAI API Integration & Conversational AI

**Project:** AI Fitness Assistant  
**Sprint:** 02  
**Status:** Completed

## Sprint Objective

Integrate an OpenAI language model into the existing Streamlit chatbot to generate intelligent, context-aware responses and establish the foundation for a domain-specific AI assistant.

## User Stories

- As a user, I want the chatbot to generate meaningful responses to my questions so that I can interact with an AI assistant.
- As a user, I want the assistant to remember the conversation context so that I can ask follow-up questions.
- As a developer, I want API credentials to be securely managed so that sensitive information is not exposed in source code.

## Key Deliverables

- Integrated the OpenAI Python SDK.
- Configured API credentials using environment variables.
- Used a `.env` file and `python-dotenv` for configuration.
- Implemented an OpenAI system prompt to establish the assistant's fitness-specific role.
- Integrated API response generation into the Streamlit chat workflow.
- Passed conversation history to the model to support contextual interactions.
- Tested fitness-related and unrelated questions to validate the assistant's domain focus.

## Technology Stack

| Technology | Purpose |
|---|---|
| OpenAI API | Language model access |
| OpenAI Python SDK | API communication |
| python-dotenv | Environment variable management |
| Python | Application logic |
| Streamlit | Chat interface |

## Acceptance Criteria

- [x] OpenAI API connection established.
- [x] API credentials loaded from environment variables.
- [x] Model generates responses to user questions.
- [x] System prompt establishes a fitness-focused assistant.
- [x] Conversation history is passed to support follow-up questions.
- [x] Application tested with different questions.

## Sprint Outcome

Successfully integrated an OpenAI language model into the chatbot, establishing the conversational intelligence layer and enabling context-aware fitness-related interactions.

## Next Sprint

Introduce user profiling and personalisation to tailor responses according to individual fitness goals, training experience and available equipment.
