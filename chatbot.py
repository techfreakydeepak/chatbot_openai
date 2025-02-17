from openai import OpenAI
import streamlit as st

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def get_openai_response(messages, model="gpt-3.5-turbo"):
    """Generates response from OpenAI API based on chat history."""
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True
    )
    return stream
