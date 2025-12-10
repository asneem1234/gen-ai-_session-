import os
from dotenv import load_dotenv
import google.generativeai as genai

def setup_environment():
    load_dotenv()
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file")
    genai.configure(api_key=api_key)
    print("✅ API configured successfully")
    return api_key

def test_model():
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    response = model.generate_content("Say hello!")
    print(f"Response: {response.text}")

if __name__ == "__main__":
    setup_environment()
    test_model()
