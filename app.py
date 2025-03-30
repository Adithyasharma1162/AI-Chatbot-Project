import streamlit as st
import openai

# Your OpenAI API key
API_KEY = 'your_api_key'
openai.api_key = API_KEY

st.title("AI Chatbot")

user_input = st.text_input("You:")

if st.button('Send'):
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        max_tokens=150
    )
    st.text_area("Bot:", value=response.choices[0].text.strip(), height=200)
