import openai
import streamlit as st
from my_openai import *

# Title
st.title("ChatGPT-like clone")


# Set the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Check if "openai_model" is not stored in session state and set it to "gpt-4"
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4"

# Check if "messages" is not stored in session state and set it to an empty list
if "messages" not in st.session_state:
    st.session_state.messages = []

# Iterate over each message in the session state messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input from chat_input and store it in the prompt variable using the walrus operator ":="
if prompt := st.chat_input("What is up?"):
    # Add user message to session state messages
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # API Call
    response = call_chatcompletion(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
