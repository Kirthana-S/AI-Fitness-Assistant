# Sprint 03 — User Profiling & Personalisation

**Project:** AI Fitness Assistant  
**Sprint:** 03  
**Status:** Completed

## Sprint Objective

Enhance the existing AI Fitness Assistant by introducing user profiling and personalisation.

Enable users to provide their fitness goals, training experience, available equipment, workout frequency and preferred workout duration. Use this information to personalise the AI assistant's responses dynamically.

## User Stories

- As a user, I want to specify my fitness goal so that the assistant can tailor its recommendations.
- As a user, I want to provide my training experience so that the assistant can adjust the complexity of its responses.
- As a user, I want to specify my available workout equipment so that suggestions are relevant to my circumstances.
- As a user, I want the assistant to consider my workout frequency and duration when discussing training plans.

## Key Deliverables

- Introduced a fitness profile section in the Streamlit sidebar.
- Added selectable fitness goals.
- Added training experience preferences.
- Added equipment availability options.
- Added a workout frequency slider.
- Added workout duration preferences.
- Implemented dynamic fitness profile construction.
- Incorporated profile information into the system prompt.
- Introduced a conversation reset button.
- Tested personalised responses using different profile configurations.

## User Profile Attributes

| Attribute | Available options |
|---|---|
| Fitness goal | Build muscle, Lose weight, Improve strength, Improve endurance, General fitness |
| Training experience | Beginner, Intermediate, Advanced |
| Equipment | Full gym, Dumbbells/basic equipment, Home/no equipment |
| Workout frequency | 1–7 days per week |
| Workout duration | 30, 45, 60, 90 minutes |

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Profile and application logic |
| Streamlit | Sidebar inputs and interactive controls |
| OpenAI API | Personalised AI response generation |
| Session State | Maintaining application conversation state |

## Acceptance Criteria

- [x] User profile section available in the sidebar.
- [x] Fitness goal selection implemented.
- [x] Training experience selection implemented.
- [x] Equipment selection implemented.
- [x] Workout frequency and duration inputs implemented.
- [x] User profile incorporated into the system prompt.
- [x] Conversation reset functionality implemented.
- [x] Tested responses with different user profile configurations.

## Sprint Outcome

Successfully introduced user profiling and dynamic prompt personalisation, enabling the AI Fitness Assistant to consider individual fitness preferences when generating responses.

## Next Sprint

**Sprint 04 — Knowledge Base Development & Document Processing**

Build a fitness knowledge base, load documents and implement text chunking to prepare information for semantic retrieval.
