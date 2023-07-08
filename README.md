# 🚀 ChatGPT-like Clone Application

This application is a simple ChatGPT-like clone built with OpenAI's GPT-4 model and Streamlit.

Link: [here](https://wyn-chat.streamlit.app/)

## 📚 Dependencies

To run this application, you need to have the following libraries installed:

- openai
- streamlit

You can install these libraries using pip:

```bash
pip install openai streamlit
```

## 🔑 API Key

To use this application, you need to have an OpenAI API key. After acquiring the key, you should store it in Streamlit's secret management system. The application uses this key to access OpenAI's services:

```python
openai.api_key = st.secrets["OPENAI_API_KEY"]
```

## 🤖 Chat Functionality

This application has a simple chat functionality built with Streamlit's session state. The application initializes a new chat session:

```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

## 📨 Sending and Receiving Messages

Users can send messages using the chat input field. The application appends user messages to the session state and sends them to the GPT-4 model for processing. The model then generates a response:

```python
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
```

## 🚦 Running the Application

To run this application, navigate to the directory containing the script and run:

```bash
streamlit run app.py
```

Replace `app.py` with the name of your script.

That's it! You should be able to interact with the GPT-4 model in a chat-like interface. Enjoy your conversation with AI! 🤖💬🎉

# 🔒 Safety Considerations

When running the application, bear in mind that the GPT-4 model, like any AI model, has potential risks and limitations. It is designed to generate creative text based on the prompts it receives. But this could include sensitive content if the prompts include such information. Always use caution when engaging with the model and make sure not to input any personally identifiable information. 🚫👥

# 🛠️ Customization

The application can be customized as needed. For example, you can modify the script to include other OpenAI models or change the chat user interface to your liking. The power is in your hands! 💪👨‍💻🔧

# 🙌 Contribution

Feel free to contribute to this project. Whether it's improving the code, adding features, or reporting issues, all contributions are welcome! Collaboration is the key to making this application better! 🤲🤝💡

# 📝 License

The project is open-source and free for all to use, modify, and distribute. Just remember to respect OpenAI's usage policies and guidelines when using their API and models. ⚖️📜🔐

# 🎉 Enjoy!

We hope you enjoy using this ChatGPT-like clone application. It's a simple way to experiment with AI chat models and get a taste of what's possible with current AI technologies. Enjoy your conversation with the AI and have fun! 🎈🥳🚀