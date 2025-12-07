import os
from dotenv import load_dotenv
import google.generativeai as genai
import time

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def basic_streaming():
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = "Write a short story about AI in 5 sentences."
    
    print("Streaming response:")
    for chunk in model.generate_content(prompt, stream=True):
        print(chunk.text, end='', flush=True)
    print("\n")

def streaming_with_timing():
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = "Explain machine learning in simple terms."
    
    start = time.time()
    print("Response:")
    for chunk in model.generate_content(prompt, stream=True):
        print(chunk.text, end='', flush=True)
    
    elapsed = time.time() - start
    print(f"\n\nTime taken: {elapsed:.2f}s")

def interactive_streaming_chat():
    model = genai.GenerativeModel('gemini-2.0-flash')
    chat = model.start_chat(history=[])
    
    messages = ["Hi!", "Tell me about Python", "Thanks!"]
    
    for msg in messages:
        print(f"\nUser: {msg}")
        print("AI: ", end='')
        response = chat.send_message(msg, stream=True)
        for chunk in response:
            print(chunk.text, end='', flush=True)
        print()

if __name__ == "__main__":
    print("1. Basic Streaming")
    basic_streaming()
    
    print("\n2. Streaming with Timing")
    streaming_with_timing()
    
    print("\n3. Interactive Streaming Chat")
    interactive_streaming_chat()
