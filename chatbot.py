import os
import streamlit as st
from openai import OpenAI
from sentiment import get_sentiment

# Load OpenAI API key (from .env or Streamlit secrets)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"] if st.secrets else os.getenv("OPENAI_API_KEY"))

def generate_response(user_input):
    sentiment = get_sentiment(user_input)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # ✅ Use gpt-3.5-turbo here
        messages=[
            {"role": "system", "content": "You are a compassionate mental health support assistant."},
            {"role": "user", "content": f"The user message is {sentiment}. Respond with care:\n\n{user_input}"}
        ],
        temperature=0.7,
        max_tokens=150
    )

    reply = response.choices[0].message.content.strip()
    return reply, sentiment
