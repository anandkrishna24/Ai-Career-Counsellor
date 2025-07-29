import streamlit as st
import google.generativeai as genai

# 🔑 Configure Gemini API
genai.configure(api_key="AIzaSyDY9RMEEK2mhY0ren8JkqWI75Q-5P8rEx4")

# Set up model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit app UI
st.set_page_config(page_title="AI Career Counsellor", page_icon="🎓", layout="centered")
st.title("🎓 AI Virtual Career Counsellor")
st.markdown("Ask me anything about careers, skills, or learning paths!")

# Initialize chat history and Gemini convo session
if "messages" not in st.session_state:
    st.session_state.messages = []
if "convo" not in st.session_state:
    st.session_state.convo = model.start_chat(history=[])

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle user input
prompt = st.chat_input("Ask your question...")
if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        with st.spinner("Thinking..."):
            response = st.session_state.convo.send_message(prompt)
            reply = response.text
    except Exception as e:
        reply = f"⚠️ Error connecting to Gemini: {e}"

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
