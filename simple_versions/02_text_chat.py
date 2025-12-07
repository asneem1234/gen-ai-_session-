import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def simple_generation():
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = "What is machine learning in one sentence?"
    response = model.generate_content(prompt)
    print(f"Response: {response.text}")

def question_answering():
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = "Who invented Python programming language?"
    response = model.generate_content(prompt)
    print(f"Response: {response.text}")

def creative_writing():
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = "Write a short story about AI in 3 sentences."
    response = model.generate_content(prompt)
    print(f"Response: {response.text}")

def summarization():
    model = genai.GenerativeModel('gemini-2.0-flash')
    text = "Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed."
    prompt = f"Summarize this in 10 words: {text}"
    response = model.generate_content(prompt)
    print(f"Response: {response.text}")

def interactive_chat():
    model = genai.GenerativeModel('gemini-2.0-flash')
    chat = model.start_chat(history=[])
    
    messages = [
        "Hi, what's your name?",
        "What can you help me with?",
        "Tell me a joke"
    ]
    
    

if __name__ == "__main__":
    print("1. Simple Generation")
    simple_generation()
    
    print("\n2. Question Answering")
    question_answering()
    
    print("\n3. Creative Writing")
    creative_writing()
    
    print("\n4. Summarization")
    summarization()
    
    print("\n5. Interactive Chat")
    interactive_chat()
