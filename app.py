from dotenv import load_dotenv
import os

load_dotenv()  # This loads the variables from .env file into environment

print(os.getenv("OPENAI_API_KEY"))  # Should print your key now


import streamlit as st
from chatbot import generate_response

st.set_page_config(page_title="Mental Health Chatbot", page_icon="🧠", layout="centered")

st.title("🧠 Mental Health Support Chatbot")
st.caption("Talk about how you're feeling. I'm here to listen. 💙")

# Store conversation history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("How are you feeling today?", "")
    submitted = st.form_submit_button("Send")

# If user sends a message
if submitted and user_input:
    response, sentiment = generate_response(user_input)
    st.session_state.chat_history.append(("🧍 You", user_input))
    st.session_state.chat_history.append(("🤖 Bot", f"{response}  \n _(Sentiment: {sentiment})_"))

# Display conversation
for sender, message in reversed(st.session_state.chat_history):
    st.markdown(f"**{sender}:** {message}")

# Add emergency help resources
st.markdown("---")
st.subheader("🚨 Emergency Mental Health Resources")
st.markdown("""
- 📞 **[iCall](https://icallhelpline.org/)** – Free, confidential mental health helpline in India.
- 📞 **[Samaritans India](http://samaritansmumbai.com/)** – Helpline: +91 84229 84528
- 🌐 **[Mental Health Foundation](https://www.mentalhealth.org.uk/your-mental-health/getting-help)**
- 🌐 **[Find a Therapist](https://www.psychologytoday.com/)**
""")
