import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
from vector_store import search_documents

# Load API key
load_dotenv(
    dotenv_path=os.path.join(os.path.dirname(__file__), ".env")
)

# Page configuration
st.set_page_config(
    page_title="AI Fitness Assistant",
    page_icon="💪",
    layout="centered"
)

st.title("💪 AI Fitness Assistant")
st.write("Your personalised AI-powered fitness companion.")

# Check API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("API key not found. Please check your .env file.")
    st.stop()

client = OpenAI(api_key=api_key)

# Fitness assistant instructions
SYSTEM_PROMPT = """
You are an AI Fitness Assistant.

Help users understand:
- Muscle building and strength training
- Workout routines and exercise selection
- Nutrition and macronutrients
- Recovery and sleep
- Progressive overload
- General exercise science

Personalisation:
Use the user's fitness profile to tailor your answers.
Consider their goals, experience, equipment and availability.

Guidelines:
- Explain concepts in simple language.
- Give practical, evidence-informed suggestions.
- Ask questions when important information is missing.
- Do not diagnose medical conditions.
- Do not prescribe injury treatments.
- Do not claim to measure body fat or health from photographs.
- Recommend qualified professionals for medical concerns.
- Keep conversations focused on fitness and related topics.
"""

# ----------------------------------
# FITNESS PROFILE
# ----------------------------------

st.sidebar.title("🏋️ Fitness Profile")
st.sidebar.write("Tell your assistant about your goals.")

goal = st.sidebar.selectbox(
    "Your fitness goal",
    [
        "Build muscle",
        "Lose weight",
        "Gain Weight",
        "Improve strength",
        "Improve endurance",
        "General fitness"
    ]
)

experience = st.sidebar.selectbox(
    "Training experience",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

equipment = st.sidebar.selectbox(
    "Available equipment",
    [
        "Full gym",
        "Dumbbells and basic equipment",
        "Home workouts without equipment"
    ]
)

workout_days = st.sidebar.slider(
    "Workout days per week",
    min_value=1,
    max_value=7,
    value=4
)

session_duration = st.sidebar.selectbox(
    "Workout duration",
    [
        "30 minutes",
        "45 minutes",
        "60 minutes",
        "90 minutes",
        "120 minutes"
    ]
)

# Create profile context
fitness_profile = f"""
User fitness profile:
Goal: {goal}
Experience: {experience}
Equipment: {equipment}
Workout frequency: {workout_days} days per week
Workout duration: {session_duration}
"""

# ----------------------------------
# CONVERSATION MANAGEMENT
# ----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.sidebar.button("Clear conversation"):
    st.session_state.messages = []
    st.rerun()

# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------------
# CHAT INPUT
# ----------------------------------

user_input = st.chat_input("Ask your fitness question...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = client.responses.create(
                    model="gpt-6-luna",
                    instructions=SYSTEM_PROMPT + "\n" + fitness_profile,
                    input=st.session_state.messages,
                    max_output_tokens=600
                )

                ai_response = response.output_text

                st.markdown(ai_response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": ai_response
                    }
                )

            except OpenAIError as e:
                st.error(f"OpenAI API error: {e}")
                st.session_state.messages.pop()

