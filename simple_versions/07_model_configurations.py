import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def temperature_control():
    prompt = "Complete this sentence: The future of AI is"
    
    print("Low temperature (0.1) - Deterministic:")
    model = genai.GenerativeModel('gemini-2.0-flash', 
                                   generation_config={'temperature': 0.1})
    response = model.generate_content(prompt)
    print(f"{response.text}\n")
    
    print("High temperature (1.5) - Creative:")
    model = genai.GenerativeModel('gemini-2.0-flash',
                                   generation_config={'temperature': 1.5})
    response = model.generate_content(prompt)
    print(f"{response.text}")

def max_tokens_control():
    prompt = "Explain quantum computing"
    
    print("Short response (50 tokens):")
    model = genai.GenerativeModel('gemini-2.0-flash',
                                   generation_config={'max_output_tokens': 50})
    response = model.generate_content(prompt)
    print(f"{response.text}\n")
    
    print("Longer response (200 tokens):")
    model = genai.GenerativeModel('gemini-2.0-flash',
                                   generation_config={'max_output_tokens': 200})
    response = model.generate_content(prompt)
    print(f"{response.text}")

def top_p_sampling():
    prompt = "Tell me an interesting fact"
    
    print("Top-p = 0.5 (focused):")
    model = genai.GenerativeModel('gemini-2.0-flash',
                                   generation_config={'top_p': 0.5})
    response = model.generate_content(prompt)
    print(f"{response.text}\n")
    
    print("Top-p = 0.95 (diverse):")
    model = genai.GenerativeModel('gemini-2.0-flash',
                                   generation_config={'top_p': 0.95})
    response = model.generate_content(prompt)
    print(f"{response.text}")

def combined_settings():
    config = {
        'temperature': 0.7,
        'max_output_tokens': 100,
        'top_p': 0.9
    }
    
    model = genai.GenerativeModel('gemini-2.0-flash', generation_config=config)
    response = model.generate_content("Write a creative tagline for an AI company")
    print(f"Response: {response.text}")

if __name__ == "__main__":
    print("1. Temperature Control")
    temperature_control()
    
    print("\n2. Max Tokens Control")
    max_tokens_control()
    
    print("\n3. Top-p Sampling")
    top_p_sampling()
    
    print("\n4. Combined Settings")
    combined_settings()
