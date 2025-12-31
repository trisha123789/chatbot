import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "models/gemini-flash-latest"

st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("🤖 Gemini AI Chatbot")
st.write("Ask me anything!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")

if user_input:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=user_input
    )

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Gemini", response.text))

for role, text in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**🧑 You:** {text}")
    else:
        st.markdown(f"**🤖 Gemini:** {text}")
