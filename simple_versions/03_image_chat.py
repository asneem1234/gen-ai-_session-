import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image, ImageDraw

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def create_sample_image():
    img = Image.new('RGB', (400, 300), color='lightblue')
    draw = ImageDraw.Draw(img)
    draw.rectangle([50, 50, 350, 250], fill='white', outline='black', width=3)
    draw.text((150, 140), "Hello AI!", fill='black')
    return img

def basic_image_understanding():
    model = genai.GenerativeModel('gemini-2.0-flash')
    img = create_sample_image()
    
    prompt = "Describe what you see in this image."
    response = model.generate_content([prompt, img])
    print(f"Response: {response.text}")

def visual_question_answering():
    model = genai.GenerativeModel('gemini-2.0-flash')
    img = create_sample_image()
    
    questions = [
        "What color is the background?",
        "What text is visible?",
        "Describe the shapes in the image"
    ]
    
    for q in questions:
        print(f"\nQ: {q}")
        response = model.generate_content([q, img])
        print(f"A: {response.text}")

def compare_images():
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    img1 = Image.new('RGB', (200, 200), color='red')
    img2 = Image.new('RGB', (200, 200), color='blue')
    
    prompt = "What's different between these two images?"
    response = model.generate_content([prompt, img1, img2])
    print(f"Response: {response.text}")

if __name__ == "__main__":
    print("1. Basic Image Understanding")
    basic_image_understanding()
    
    print("\n2. Visual Q&A")
    visual_question_answering()
    
    print("\n3. Compare Images")
    compare_images()
