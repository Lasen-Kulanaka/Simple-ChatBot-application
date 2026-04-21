from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

client = genai.Client()

config = types.GenerateContentConfig(
    system_instruction="Answer within 200 characters",
    temperature=0.9
)

chat = client.chats.create(model="gemini-2.5-flash", config=config)

print("\n________AI chatbot started. Type \"end\" to end the chat_________\n")

userinput = input("User : ")

while userinput.lower() != "end":
    response = chat.send_message(userinput)
    print("Bot : "+response.text)
    userinput = input("User : ")

print("\n_________Chatbot has shutdown_________\n")