import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def simple_chat_with_memory():
    model = genai.GenerativeModel('gemini-2.0-flash')
    chat = model.start_chat(history=[])
    
    print("Chat with memory:")
    messages = [
        "My name is Alice",
        "What's my name?",
        "I like Python programming",
        "What do I like?"
    ]
    
    for msg in messages:
        print(f"\nUser: {msg}")
        response = chat.send_message(msg)
        print(f"AI: {response.text}")

def chat_with_history():
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    history = [
        {"role": "user", "parts": ["Hi, I'm learning AI"]},
        {"role": "model", "parts": ["Hello! That's great! I'm here to help you learn about AI."]}
    ]
    
    chat = model.start_chat(history=history)
    
    print("Continuing previous conversation:")
    response = chat.send_message("Can you remind me what we're discussing?")
    print(f"AI: {response.text}")

def multi_turn_conversation():
    model = genai.GenerativeModel('gemini-2.0-flash')
    chat = model.start_chat(history=[])
    
    print("Interactive conversation:")
    
    response = chat.send_message("I want to learn about neural networks")
    print(f"User: I want to learn about neural networks")
    print(f"AI: {response.text}\n")
    
    response = chat.send_message("Can you explain it in simpler terms?")
    print(f"User: Can you explain it in simpler terms?")
    print(f"AI: {response.text}\n")
    
    response = chat.send_message("Give me an example")
    print(f"User: Give me an example")
    print(f"AI: {response.text}")

if __name__ == "__main__":
    print("1. Simple Chat with Memory")
    simple_chat_with_memory()
    
    print("\n\n2. Chat with History")
    chat_with_history()
    
    print("\n\n3. Multi-turn Conversation")
    multi_turn_conversation()
