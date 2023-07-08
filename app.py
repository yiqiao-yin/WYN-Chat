import openai
import streamlit as st

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

    with st.chat_message("assistant"):
        # Create an empty placeholder to hold the assistant's response
        message_placeholder = st.empty()
        full_response = ""

        # Iterate over the responses received from OpenAI ChatCompletion API
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):

            # Append the assistant's response to the full_response string
            full_response += response.choices[0].delta.get("content", "")

            # Update the message_placeholder with the current full_response
            message_placeholder.markdown(full_response + "▌")

        # Update the message_placeholder with the final full_response
        message_placeholder.markdown(full_response)

    # Add assistant message to session state messages
    st.session_state.messages.append({"role": "assistant", "content": full_response})
