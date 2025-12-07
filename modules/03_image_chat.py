"""
03 - Image Chat (Multimodal AI)
================================

This module demonstrates multimodal AI capabilities - combining text and images.
Students will learn:
- Image understanding and analysis
- Visual question answering
- Describing images
- Multi-image analysis
- Practical vision applications

Teaching Points:
- Gemini Pro Vision can understand images and answer questions about them
- Images must be properly formatted (PIL Image or file path)
- You can combine multiple images in one prompt
- Multimodal AI opens up exciting new applications
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import io

# Setup
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


# ============================================================================
# SECTION 1: Basic Image Understanding
# ============================================================================

def create_sample_image():
    """
    Create a simple sample image for demonstration
    (In real scenarios, you'd load actual images)
    """
    from PIL import Image, ImageDraw, ImageFont
    
    # Create a colorful image with text
    img = Image.new('RGB', (400, 300), color=(70, 130, 180))
    draw = ImageDraw.Draw(img)
    
    # Add some shapes
    draw.rectangle([50, 50, 150, 150], fill=(255, 255, 0), outline=(0, 0, 0), width=3)
    draw.ellipse([200, 50, 350, 200], fill=(255, 100, 100), outline=(0, 0, 0), width=3)
    
    # Add text
    try:
        draw.text((100, 250), "AI Vision Demo", fill=(255, 255, 255))
    except:
        pass  # Font might not be available
    
    return img


def basic_image_understanding():
    """
    Demonstrate basic image analysis
    """
    print("\n" + "=" * 60)
    print("SECTION 1: Basic Image Understanding")
    print("=" * 60)
    
    # Note: Using gemini-pro-vision for image understanding
    model = genai.GenerativeModel('gemini-pro-vision')
    
    print("\n💡 Creating a sample image...")
    img = create_sample_image()
    
    # Save it so students can see it
    os.makedirs('outputs', exist_ok=True)
    img.save('outputs/sample_image.png')
    print("✅ Sample image created: outputs/sample_image.png")
    
    # Example 1: Simple description
    print("\n1️⃣ Simple Image Description:")
    prompt = "Describe what you see in this image."
    print(f"📝 Prompt: {prompt}")
    
    response = model.generate_content([prompt, img])
    print(f"🤖 Response: {response.text}\n")
    
    # Example 2: Specific question
    print("\n2️⃣ Specific Question:")
    prompt = "What shapes can you identify in this image?"
    print(f"📝 Prompt: {prompt}")
    
    response = model.generate_content([prompt, img])
    print(f"🤖 Response: {response.text}\n")
    
    # Example 3: Color analysis
    print("\n3️⃣ Color Analysis:")
    prompt = "What are the main colors in this image?"
    print(f"📝 Prompt: {prompt}")
    
    response = model.generate_content([prompt, img])
    print(f"🤖 Response: {response.text}\n")


# ============================================================================
# SECTION 2: Loading Images from Files
# ============================================================================

def load_and_analyze_image():
    """
    Show how to load and analyze images from files
    """
    print("\n" + "=" * 60)
    print("SECTION 2: Loading Images from Files")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro-vision')
    
    # Method 1: Using PIL
    print("\n📁 Method 1: Loading with PIL (Python Imaging Library)")
    print("   Code: img = Image.open('path/to/image.jpg')")
    
    # Create sample
    sample_img = create_sample_image()
    
    print("\n   Analyzing the image...")
    prompt = "Is this image more abstract or realistic? Explain briefly."
    response = model.generate_content([prompt, sample_img])
    print(f"   🤖 Response: {response.text}\n")
    
    # Method 2: From bytes
    print("\n💾 Method 2: Loading from bytes")
    print("   Use case: When image comes from API, database, or web")
    
    # Convert to bytes
    byte_arr = io.BytesIO()
    sample_img.save(byte_arr, format='PNG')
    byte_arr = byte_arr.getvalue()
    
    # Load back
    img_from_bytes = Image.open(io.BytesIO(byte_arr))
    print("   ✅ Image loaded from bytes successfully")


# ============================================================================
# SECTION 3: Visual Question Answering
# ============================================================================

def visual_question_answering():
    """
    Advanced Q&A about images
    """
    print("\n" + "=" * 60)
    print("SECTION 3: Visual Question Answering (VQA)")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro-vision')
    
    # Create a more complex sample
    print("\n📸 Creating a detailed sample image...")
    img = Image.new('RGB', (500, 400), color=(240, 240, 240))
    draw = ImageDraw.Draw(img)
    
    # Draw a simple scene
    # Sky
    draw.rectangle([0, 0, 500, 200], fill=(135, 206, 235))
    # Ground
    draw.rectangle([0, 200, 500, 400], fill=(34, 139, 34))
    # Sun
    draw.ellipse([400, 50, 470, 120], fill=(255, 255, 0))
    # House
    draw.rectangle([150, 180, 300, 320], fill=(139, 69, 19))
    draw.polygon([150, 180, 225, 120, 300, 180], fill=(178, 34, 34))
    # Door
    draw.rectangle([200, 250, 250, 320], fill=(101, 67, 33))
    
    img.save('outputs/scene_image.png')
    print("✅ Scene image created: outputs/scene_image.png")
    
    # Ask various questions
    questions = [
        "What objects can you see in this image?",
        "What time of day does this image represent?",
        "Describe the weather conditions in this image.",
        "If this were a real scene, what sounds might you hear?",
        "What season does this image suggest?"
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"\n❓ Question {i}: {question}")
        response = model.generate_content([question, img])
        print(f"🤖 Answer: {response.text}")


# ============================================================================
# SECTION 4: Multiple Images Analysis
# ============================================================================

def multiple_images_analysis():
    """
    Analyze multiple images together
    """
    print("\n" + "=" * 60)
    print("SECTION 4: Multiple Images Analysis")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro-vision')
    
    print("\n📸 Creating two different images...")
    
    # Image 1: Circles
    img1 = Image.new('RGB', (300, 300), color=(255, 255, 255))
    draw1 = ImageDraw.Draw(img1)
    draw1.ellipse([50, 50, 250, 250], fill=(255, 0, 0), outline=(0, 0, 0), width=3)
    img1.save('outputs/image1_circle.png')
    
    # Image 2: Squares
    img2 = Image.new('RGB', (300, 300), color=(255, 255, 255))
    draw2 = ImageDraw.Draw(img2)
    draw2.rectangle([50, 50, 250, 250], fill=(0, 0, 255), outline=(0, 0, 0), width=3)
    img2.save('outputs/image2_square.png')
    
    print("✅ Created: outputs/image1_circle.png")
    print("✅ Created: outputs/image2_square.png")
    
    # Compare the images
    print("\n🔍 Comparing the two images...")
    prompt = "Compare these two images. What are the differences in shapes and colors?"
    
    response = model.generate_content([prompt, img1, img2])
    print(f"\n🤖 Comparison: {response.text}")
    
    # Another comparison
    print("\n🔍 Another comparison...")
    prompt2 = "Which image has a warmer color scheme?"
    
    response2 = model.generate_content([prompt2, img1, img2])
    print(f"🤖 Answer: {response2.text}")


# ============================================================================
# SECTION 5: Practical Applications
# ============================================================================

def practical_image_applications():
    """
    Real-world use cases for image understanding
    """
    print("\n" + "=" * 60)
    print("SECTION 5: Practical Applications")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro-vision')
    
    # Use Case 1: Accessibility (Image descriptions for visually impaired)
    print("\n1️⃣ ACCESSIBILITY: Image Description for Screen Readers")
    print("-" * 60)
    
    img = create_sample_image()
    prompt = """Generate a detailed description of this image for a screen reader.
Include colors, shapes, spatial relationships, and any text.
Format: Start with 'Image description:' """
    
    response = model.generate_content([prompt, img])
    print(response.text)
    
    # Use Case 2: Content Moderation
    print("\n\n2️⃣ CONTENT MODERATION: Safety Check")
    print("-" * 60)
    
    # Create a safe image
    safe_img = Image.new('RGB', (300, 300), color=(200, 200, 255))
    draw = ImageDraw.Draw(safe_img)
    draw.text((100, 140), "Hello World!", fill=(0, 0, 0))
    
    prompt = """Analyze this image for content safety.
Is there any inappropriate, violent, or unsafe content?
Answer: YES or NO, followed by brief reasoning."""
    
    response = model.generate_content([prompt, safe_img])
    print(response.text)
    
    # Use Case 3: Educational Tool
    print("\n\n3️⃣ EDUCATION: Object Identification for Learning")
    print("-" * 60)
    
    edu_img = Image.new('RGB', (400, 300), color=(255, 255, 255))
    draw = ImageDraw.Draw(edu_img)
    # Draw geometric shapes
    draw.polygon([(200, 50), (350, 150), (200, 250), (50, 150)], 
                 fill=(100, 200, 100), outline=(0, 0, 0), width=2)
    
    edu_img.save('outputs/educational_shape.png')
    
    prompt = """This is an educational image for teaching geometry.
What shape is shown? Provide:
1. Name of the shape
2. Number of sides
3. Key properties
4. A fun fact about this shape"""
    
    response = model.generate_content([prompt, edu_img])
    print(response.text)
    
    # Use Case 4: Product Analysis
    print("\n\n4️⃣ E-COMMERCE: Product Description Generator")
    print("-" * 60)
    
    product_img = Image.new('RGB', (300, 300), color=(255, 255, 255))
    draw = ImageDraw.Draw(product_img)
    # Simple "product"
    draw.rectangle([80, 80, 220, 220], fill=(50, 50, 200), outline=(0, 0, 0), width=2)
    draw.text((120, 135), "PRODUCT", fill=(255, 255, 255))
    
    prompt = """Generate a product description for an e-commerce website based on this image.
Include:
- Product type
- Visual features
- Suggested use cases
- Estimated target audience
Keep it under 100 words."""
    
    response = model.generate_content([prompt, product_img])
    print(response.text)


# ============================================================================
# SECTION 6: Image + Text Context
# ============================================================================

def image_with_context():
    """
    Providing additional text context with images
    """
    print("\n" + "=" * 60)
    print("SECTION 6: Combining Image with Text Context")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro-vision')
    
    img = create_sample_image()
    
    # Without context
    print("\n1️⃣ Without additional context:")
    prompt1 = "What is this image about?"
    response1 = model.generate_content([prompt1, img])
    print(f"🤖 Response: {response1.text}\n")
    
    # With context
    print("\n2️⃣ With additional context:")
    prompt2 = """Context: This image is from a computer graphics tutorial about basic shapes.

Question: Based on the context, what concepts is this image teaching?"""
    
    response2 = model.generate_content([prompt2, img])
    print(f"🤖 Response: {response2.text}\n")
    
    print("\n💡 Notice how context helps the AI provide more relevant responses!")


# ============================================================================
# SECTION 7: Best Practices & Tips
# ============================================================================

def best_practices():
    """
    Tips for working with image-based AI
    """
    print("\n" + "=" * 60)
    print("SECTION 7: Best Practices & Tips")
    print("=" * 60)
    
    tips = """
    ✅ IMAGE QUALITY:
       • Use clear, well-lit images
       • Higher resolution is generally better
       • Avoid blurry or heavily compressed images
    
    ✅ PROMPTS:
       • Be specific about what you want to know
       • Ask one clear question at a time
       • Provide context when relevant
    
    ✅ FORMATS:
       • Supported: JPEG, PNG, WebP, HEIC, HEIF
       • Use PIL (Pillow) for image manipulation
       • Images can be from file, URL, or bytes
    
    ✅ LIMITATIONS:
       • May not be accurate with very small text
       • Can struggle with highly abstract images
       • Cultural context may affect interpretation
    
    ✅ ETHICAL CONSIDERATIONS:
       • Respect privacy (faces, license plates)
       • Don't use for surveillance without consent
       • Be aware of bias in image recognition
       • Consider accessibility in your applications
    
    ✅ PERFORMANCE:
       • Large images take longer to process
       • Consider resizing very large images
       • Batch processing can be more efficient
    """
    
    print(tips)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main function with menu
    """
    print("\n")
    print("🎓 " + "=" * 58 + " 🎓")
    print("     GENERATIVE AI SESSION - MODULE 3: IMAGE CHAT")
    print("🎓 " + "=" * 58 + " 🎓")
    
    # Create outputs directory
    os.makedirs('outputs', exist_ok=True)
    
    menu = """
    Choose a section to run:
    
    1. Basic Image Understanding
    2. Loading Images from Files
    3. Visual Question Answering
    4. Multiple Images Analysis
    5. Practical Applications
    6. Image with Text Context
    7. Best Practices & Tips
    
    all - Run all sections
    quit - Exit
    
    """
    
    while True:
        print(menu)
        choice = input("Your choice: ").strip().lower()
        
        if choice in ['quit', 'q', 'exit']:
            print("👋 Goodbye!")
            break
        elif choice == '1':
            basic_image_understanding()
        elif choice == '2':
            load_and_analyze_image()
        elif choice == '3':
            visual_question_answering()
        elif choice == '4':
            multiple_images_analysis()
        elif choice == '5':
            practical_image_applications()
        elif choice == '6':
            image_with_context()
        elif choice == '7':
            best_practices()
        elif choice == 'all':
            basic_image_understanding()
            load_and_analyze_image()
            visual_question_answering()
            multiple_images_analysis()
            practical_image_applications()
            image_with_context()
            best_practices()
            print("\n✅ All sections completed!")
            break
        else:
            print("⚠️  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
    # Teaching Questions:
    # 1. What's the difference between gemini-pro and gemini-pro-vision?
    # 2. How can image understanding benefit accessibility?
    # 3. What are some ethical concerns with AI vision?
