import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def basic_system_instruction():
    instruction = "You are a helpful Python tutor. Always explain concepts clearly and provide code examples."
    
    model = genai.GenerativeModel('gemini-2.0-flash', system_instruction=instruction)
    response = model.generate_content("What is a list comprehension?")
    print(f"Response: {response.text}")

def role_based_assistant():
    instruction = "You are a professional email writer. Write formal, concise emails."
    
    model = genai.GenerativeModel('gemini-2.0-flash', system_instruction=instruction)
    response = model.generate_content("Write an email requesting a meeting with the team")
    print(f"Response: {response.text}")

def style_control():
    instruction = "You are a creative storyteller. Write in a mysterious, engaging style."
    
    model = genai.GenerativeModel('gemini-2.0-flash', system_instruction=instruction)
    response = model.generate_content("Write a short paragraph about a locked door")
    print(f"Response: {response.text}")

def format_control():
    instruction = "Always respond in JSON format with keys: 'answer', 'confidence', 'explanation'"
    
    model = genai.GenerativeModel('gemini-2.0-flash', system_instruction=instruction)
    response = model.generate_content("What is machine learning?")
    print(f"Response: {response.text}")

def multiple_personas():
    personas = {
        "Teacher": "You are a patient teacher. Explain things step by step.",
        "Expert": "You are a technical expert. Use precise terminology.",
        "Friend": "You are a friendly peer. Use casual, simple language."
    }
    
    prompt = "Explain what an API is"
    
    for name, instruction in personas.items():
        print(f"\n{name} persona:")
        model = genai.GenerativeModel('gemini-2.0-flash', system_instruction=instruction)
        response = model.generate_content(prompt)
        print(f"{response.text}")

if __name__ == "__main__":
    print("1. Basic System Instruction")
    basic_system_instruction()
    
    print("\n2. Role-based Assistant")
    role_based_assistant()
    
    print("\n3. Style Control")
    style_control()
    
    print("\n4. Format Control")
    format_control()
    
    print("\n5. Multiple Personas")
    multiple_personas()
