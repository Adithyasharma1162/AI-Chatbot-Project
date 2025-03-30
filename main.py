import openai
import streamlit as st

# Your OpenAI API key
API_KEY = 'your_api_key'

openai.api_key = API_KEY

# Streamlit UI
st.set_page_config(page_title="AI Chatbot", layout="wide")

st.title("AI Chatbot")

# Create a container for the chatbot
chat_container = st.container()

# Initialize session state to hold the chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:")

if st.button("Send"):
    if user_input:
        # Add user input to chat history
        st.session_state.history.append(("You:", user_input))
        
        # Get response from OpenAI
        response = openai.Completion.create(
            engine="davinci",
            prompt=user_input,
            max_tokens=150
        )
        bot_reply = response.choices[0].text.strip()
        st.session_state.history.append(("Bot:", bot_reply))

# Display the chat history
for speaker, text in st.session_state.history:
    chat_container.markdown(f'**{speaker}**: {text}')