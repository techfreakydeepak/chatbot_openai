import streamlit as st
from chatbot import get_openai_response

##Streamlit UI
st.title("Welcome! I'm WeCredit Virtual Assistant")
st.write("Ask me anything about loans, credit scores, or interest rates!")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

##Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

##User input handling
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    ##Get response from OpenAI
    with st.chat_message("assistant"):
        response = get_openai_response(st.session_state.messages, st.session_state["openai_model"])
        response_text = st.write_stream(response)

    st.session_state.messages.append({"role": "assistant", "content": response_text})
