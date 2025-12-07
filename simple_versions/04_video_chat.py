import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image, ImageDraw

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def create_video_frames():
    frames = []
    for i in range(5):
        img = Image.new('RGB', (300, 200), color=(i*50, 100, 255-i*50))
        draw = ImageDraw.Draw(img)
        draw.text((100, 90), f"Frame {i+1}", fill='white')
        frames.append(img)
    return frames

def analyze_video_frames():
    model = genai.GenerativeModel('gemini-2.0-flash')
    frames = create_video_frames()
    
    prompt = "Describe what happens across these video frames."
    response = model.generate_content([prompt] + frames)
    print(f"Response: {response.text}")

def video_question_answering():
    model = genai.GenerativeModel('gemini-2.0-flash')
    frames = create_video_frames()
    
    prompt = "How many frames are there and what changes?"
    response = model.generate_content([prompt] + frames)
    print(f"Response: {response.text}")

if __name__ == "__main__":
    print("1. Analyze Video Frames")
    analyze_video_frames()
    
    print("\n2. Video Q&A")
    video_question_answering()
