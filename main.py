import openai

# Your OpenAI API key
API_KEY = 'your_api_key'

openai.api_key = API_KEY

def chatbot_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    user_input = input("You: ")
    print("Bot:", chatbot_response(user_input))
