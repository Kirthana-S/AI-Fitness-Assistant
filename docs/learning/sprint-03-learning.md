# Sprint 03 — Learning Documentation

## 1. Sprint Objective

Understand how to introduce user profiling and personalisation into an AI application using Streamlit inputs, Python variables and dynamic prompt construction.

The objective was to move from a generic AI chatbot towards an assistant that can adapt its responses based on user-provided information.

## 2. Understanding User Profiling

User profiling is the process of collecting relevant information about a user to personalise an application's behaviour.

In our AI Fitness Assistant, users provide information about their fitness preferences and training circumstances.

The profile includes:

- Fitness goal
- Training experience
- Available equipment
- Workout frequency
- Preferred workout duration

### Why is user profiling important in AI applications?

A generic AI assistant generates responses based primarily on the user's question and general instructions.

A personalised AI assistant can additionally consider relevant user-provided context.

For example:

**User A:**
- Goal: Build muscle
- Experience: Beginner
- Equipment: Full gym

**User B:**
- Goal: Improve endurance
- Experience: Advanced
- Equipment: Home/no equipment

Even if both users ask the same question, the assistant can tailor its response according to their different profiles.

## 3. Building the User Profile Interface

Used Streamlit sidebar components to collect profile information.

The implemented controls include:

| Streamlit component | Purpose |
|---|---|
| `st.selectbox()` | Select fitness goals, experience and equipment |
| `st.slider()` | Select workout frequency |
| `st.selectbox()` | Select workout duration |
| `st.sidebar` | Organise profile controls in the sidebar |
| `st.button()` | Provide conversation reset functionality |

The sidebar allows users to configure their preferences without cluttering the main chat interface.

## 4. Dynamic Fitness Profile Construction

After collecting user inputs, Python combines the selected values into a fitness profile.

Example:

```python
fitness_profile = f"""
User Fitness Profile:

Fitness Goal: {fitness_goal}
Training Experience: {experience}
Available Equipment: {equipment}
Workout Days Per Week: {workout_days}
Workout Duration: {workout_duration}
"""
```

**Concept learned: Dynamic string construction**

Python f-strings allow variable values to be inserted into text dynamically.

This enables the application to construct different profile descriptions based on user selections.

## 5. Understanding Context Injection

Context injection means adding relevant information to the instructions or context supplied to an AI model.

In this project, the fitness profile is incorporated into the system prompt.

Conceptual example:

```python
personalised_prompt = SYSTEM_PROMPT + fitness_profile
```

The application can then pass the personalised instructions to the OpenAI API.

### How does this help?

The model receives additional information about the user's goals and preferences before generating its response.

For example, a beginner interested in muscle building may receive a different explanation from an advanced user focused on endurance.

## 6. Prompt Personalisation

Previously, the assistant relied on a fixed system prompt.

After this sprint, the prompt incorporates dynamic user profile information.

### Previous approach

```text
System instructions
       |
       v
AI model
       |
       v
Response
```

### Personalised approach

```text
System instructions
       +
User fitness profile
       |
       v
AI model
       |
       v
Personalised response
```

**Concept learned: Personalised Prompt Engineering**

Prompt engineering can incorporate dynamic context instead of relying only on static instructions.

## 7. Streamlit Session State

Session state was also used in managing the chatbot conversation.

Streamlit reruns the application when users interact with widgets.

Session state allows information such as conversation messages to persist across these reruns.

Example:

```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

### Conversation Reset

Introduced a reset button to clear the conversation history.

Conceptual example:

```python
if st.button("Reset Conversation"):
    st.session_state.messages = []
```

The application can then start a fresh conversation.

## 8. Application Workflow

```text
User
 |
 v
Fitness Profile Sidebar
 |
 v
Collect User Preferences
 |
 v
Construct Fitness Profile
 |
 v
Combine Profile with System Prompt
 |
 v
OpenAI API
 |
 v
Generate Personalised Response
 |
 v
Streamlit Chat Interface
```

## 9. Technical Concepts Learned

| Concept | Explanation | Application |
|---|---|---|
| User profiling | Collecting relevant user information | Fitness profile |
| Dynamic inputs | Collecting variable user selections | Streamlit controls |
| Python f-strings | Constructing dynamic strings | Fitness profile creation |
| Context injection | Adding relevant context to model instructions | Profile integration |
| Prompt personalisation | Adapting instructions based on user information | Personalised responses |
| Session state | Maintaining information across reruns | Conversation history |
| State reset | Clearing stored session information | Reset button |

## 10. Testing and Validation

Tested the application using different fitness profile configurations.

Validation included:

- Changing fitness goals.
- Changing training experience.
- Selecting different equipment options.
- Changing workout frequency.
- Changing preferred workout duration.
- Asking the same question with different profile configurations.
- Testing conversation reset functionality.

**Result:** The application successfully accepted different user profiles and incorporated profile information into its AI instructions.

## 11. Challenges and Learnings

### Dynamic prompt construction

Learned how to combine static system instructions with dynamically generated profile information.

### Managing application state

Understood why Streamlit session state is important for maintaining conversation history across application reruns.

### Personalisation versus generic responses

Learned how additional context can influence the relevance and style of AI-generated responses.

## 12. Sprint Outcome

Successfully implemented user profiling and personalised prompt construction.

The AI Fitness Assistant can now incorporate user-provided fitness preferences when generating responses.

## 13. Next Sprint

**Sprint 04 — Knowledge Base Development & Document Processing**

Build a fitness knowledge base and understand document loading, preprocessing and text chunking as the foundation for Retrieval-Augmented Generation (RAG).

---

# 14. Code Reference — Sprint 03

The following snippets represent the key implementation patterns used during this sprint. They are reference examples based on our documented implementation, not necessarily exact copies of every section in the original `app.py`.

### 14.1 Fitness goal selection

```python
fitness_goal = st.sidebar.selectbox(
    "Fitness Goal",
    [
        "Build muscle",
        "Lose weight",
        "Improve strength",
        "Improve endurance",
        "General fitness"
    ]
)
```

### 14.2 Training experience selection

```python
experience = st.sidebar.selectbox(
    "Training Experience",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)
```

### 14.3 Equipment selection

```python
equipment = st.sidebar.selectbox(
    "Available Equipment",
    [
        "Full gym",
        "Dumbbells/basic equipment",
        "Home/no equipment"
    ]
)
```

### 14.4 Workout frequency

```python
workout_days = st.sidebar.slider(
    "Workout Days Per Week",
    min_value=1,
    max_value=7,
    value=3
)
```

### 14.5 Workout duration

```python
workout_duration = st.sidebar.selectbox(
    "Workout Duration",
    ["30 minutes", "45 minutes", "60 minutes", "90 minutes"]
)
```

### 14.6 Constructing the fitness profile

```python
fitness_profile = f"""
User Fitness Profile:

Fitness Goal: {fitness_goal}
Training Experience: {experience}
Available Equipment: {equipment}
Workout Days Per Week: {workout_days}
Workout Duration: {workout_duration}
"""
```

### 14.7 Combining the profile with the system prompt

```python
personalised_prompt = SYSTEM_PROMPT + "\n" + fitness_profile
```

### 14.8 Passing personalised instructions to the OpenAI API

```python
response = client.responses.create(
    model=MODEL_NAME,
    instructions=personalised_prompt,
    input=conversation_history
)

assistant_response = response.output_text
```

### 14.9 Conversation history initialisation

```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

### 14.10 Reset conversation

```python
if st.sidebar.button("Reset Conversation"):
    st.session_state.messages = []
```

### 14.11 Dependencies used

Relevant packages:

```text
streamlit
openai
python-dotenv
```

These were already installed during the previous development sprints.

---

**End of Sprint 03 Learning Documentation**