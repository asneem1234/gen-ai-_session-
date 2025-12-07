"""
02 - Text Chat
==============

This module demonstrates various text generation and chat capabilities.
Students will learn:
- Simple text generation
- Question-answering
- Different prompting techniques
- Handling long-form content
- Building interactive chat

Teaching Points:
- Prompt engineering is crucial
- Clear, specific prompts get better results
- Context matters for quality responses
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Setup
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


# ============================================================================
# SECTION 1: Simple Text Generation
# ============================================================================

def simple_text_generation():
    """
    Basic text generation - the foundation of all LLM interactions
    """
    print("\n" + "=" * 60)
    print("SECTION 1: Simple Text Generation")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    # Example 1: Direct question
    print("\n1️⃣ Direct Question:")
    prompt1 = "What is machine learning in one sentence?"
    print(f"📝 Prompt: {prompt1}")
    
    response1 = model.generate_content(prompt1)
    print(f"🤖 Response: {response1.text}\n")
    
    # Example 2: Creative writing
    print("\n2️⃣ Creative Writing:")
    prompt2 = "Write a haiku about artificial intelligence."
    print(f"📝 Prompt: {prompt2}")
    
    response2 = model.generate_content(prompt2)
    print(f"🤖 Response:\n{response2.text}\n")
    
    # Example 3: Explanation
    print("\n3️⃣ Technical Explanation:")
    prompt3 = "Explain neural networks to a 10-year-old."
    print(f"📝 Prompt: {prompt3}")
    
    response3 = model.generate_content(prompt3)
    print(f"🤖 Response: {response3.text}\n")


# ============================================================================
# SECTION 2: Question Answering
# ============================================================================

def question_answering():
    """
    Different styles of Q&A
    """
    print("\n" + "=" * 60)
    print("SECTION 2: Question Answering")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    # Example 1: Factual question
    print("\n1️⃣ Factual Question:")
    prompt = "Who invented the Python programming language and when?"
    print(f"📝 Prompt: {prompt}")
    
    response = model.generate_content(prompt)
    print(f"🤖 Response: {response.text}\n")
    
    # Example 2: Comparison question
    print("\n2️⃣ Comparison Question:")
    prompt = "What are the key differences between supervised and unsupervised learning?"
    print(f"📝 Prompt: {prompt}")
    
    response = model.generate_content(prompt)
    print(f"🤖 Response: {response.text}\n")
    
    # Example 3: Opinion question
    print("\n3️⃣ Opinion-Based Question:")
    prompt = "What are the pros and cons of using AI in healthcare?"
    print(f"📝 Prompt: {prompt}")
    
    response = model.generate_content(prompt)
    print(f"🤖 Response: {response.text}\n")


# ============================================================================
# SECTION 3: Prompt Engineering Techniques
# ============================================================================

def prompt_engineering_examples():
    """
    Demonstrate how different prompts affect output quality
    """
    print("\n" + "=" * 60)
    print("SECTION 3: Prompt Engineering Techniques")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    # Technique 1: Vague vs Specific
    print("\n1️⃣ VAGUE vs SPECIFIC Prompts:\n")
    
    print("❌ Vague prompt:")
    vague_prompt = "Tell me about AI."
    print(f"   '{vague_prompt}'")
    response = model.generate_content(vague_prompt)
    print(f"   Response length: {len(response.text)} characters")
    print(f"   Preview: {response.text[:150]}...\n")
    
    print("✅ Specific prompt:")
    specific_prompt = "List 3 practical applications of AI in education with one-sentence descriptions."
    print(f"   '{specific_prompt}'")
    response = model.generate_content(specific_prompt)
    print(f"   Response:\n{response.text}\n")
    
    # Technique 2: Role-based prompting
    print("\n2️⃣ ROLE-BASED Prompting:\n")
    role_prompt = """You are an experienced Python tutor. 
Explain what a decorator is to a beginner in simple terms with a short example."""
    
    print(f"📝 Prompt: {role_prompt}")
    response = model.generate_content(role_prompt)
    print(f"🤖 Response:\n{response.text}\n")
    
    # Technique 3: Step-by-step instructions
    print("\n3️⃣ STEP-BY-STEP Instructions:\n")
    step_prompt = """Break down the following task into steps:
How to create a simple REST API in Python using Flask.
Number each step and keep it concise."""
    
    print(f"📝 Prompt: {step_prompt}")
    response = model.generate_content(step_prompt)
    print(f"🤖 Response:\n{response.text}\n")
    
    # Technique 4: Format specification
    print("\n4️⃣ FORMAT Specification:\n")
    format_prompt = """List 3 benefits of using version control.
Format your response as:
Benefit 1: [description]
Benefit 2: [description]
Benefit 3: [description]"""
    
    print(f"📝 Prompt: {format_prompt}")
    response = model.generate_content(format_prompt)
    print(f"🤖 Response:\n{response.text}\n")


# ============================================================================
# SECTION 4: Interactive Chat (Single Turn)
# ============================================================================

def interactive_single_turn():
    """
    Single-turn conversation (no memory)
    """
    print("\n" + "=" * 60)
    print("SECTION 4: Interactive Single-Turn Chat")
    print("=" * 60)
    print("\nNote: Each question is independent (no conversation memory)")
    print("Type 'quit' to exit\n")
    
    model = genai.GenerativeModel('gemini-pro')
    
    conversation_count = 0
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
            
        if not user_input:
            print("⚠️  Please enter a message\n")
            continue
        
        try:
            conversation_count += 1
            print("🤖 AI: ", end="")
            
            response = model.generate_content(user_input)
            print(response.text)
            print()
            
            if conversation_count >= 3:
                print("💡 Notice: Each response is independent. No memory of previous questions.")
                print("   We'll learn how to add memory in Module 06!\n")
                
        except Exception as e:
            print(f"❌ Error: {e}\n")


# ============================================================================
# SECTION 5: Long-Form Content Generation
# ============================================================================

def long_form_generation():
    """
    Generate longer, structured content
    """
    print("\n" + "=" * 60)
    print("SECTION 5: Long-Form Content Generation")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    # Example: Blog post generation
    print("\n📝 Generating a blog post outline...\n")
    
    prompt = """Write a detailed outline for a blog post about "Getting Started with AI for Beginners".

Include:
- An engaging introduction
- 5 main sections with subpoints
- A conclusion
- Keep it educational and encouraging"""
    
    response = model.generate_content(prompt)
    
    print("=" * 60)
    print("📄 Generated Blog Outline:")
    print("=" * 60)
    print(response.text)
    print("=" * 60)


# ============================================================================
# SECTION 6: Code Generation
# ============================================================================

def code_generation_examples():
    """
    Using AI to generate code
    """
    print("\n" + "=" * 60)
    print("SECTION 6: Code Generation")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    # Example 1: Simple function
    print("\n1️⃣ Generate a Simple Function:\n")
    prompt1 = """Write a Python function that calculates the factorial of a number.
Include:
- Docstring
- Input validation
- Example usage"""
    
    print(f"📝 Request: {prompt1.split('.')[0]}...")
    response1 = model.generate_content(prompt1)
    print("\n🤖 Generated Code:")
    print("-" * 60)
    print(response1.text)
    print("-" * 60)
    
    # Example 2: Class generation
    print("\n2️⃣ Generate a Class:\n")
    prompt2 = """Create a Python class called 'Student' with:
- Attributes: name, age, grades (list)
- Method to add a grade
- Method to calculate average grade
- Include docstrings"""
    
    print(f"📝 Request: Create a Student class...")
    response2 = model.generate_content(prompt2)
    print("\n🤖 Generated Code:")
    print("-" * 60)
    print(response2.text)
    print("-" * 60)


# ============================================================================
# SECTION 7: Practical Use Cases
# ============================================================================

def practical_use_cases():
    """
    Real-world applications of text generation
    """
    print("\n" + "=" * 60)
    print("SECTION 7: Practical Use Cases")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    # Use case 1: Email writing
    print("\n1️⃣ Professional Email Writing:")
    prompt = """Write a professional email to request a meeting with a professor 
to discuss a research opportunity in machine learning. Keep it concise and polite."""
    
    response = model.generate_content(prompt)
    print(response.text)
    print()
    
    # Use case 2: Summarization
    print("\n2️⃣ Text Summarization:")
    long_text = """Artificial Intelligence (AI) has transformed numerous industries 
over the past decade. From healthcare to finance, education to entertainment, AI 
systems are now integral to modern operations. Machine learning algorithms can 
analyze vast amounts of data to identify patterns and make predictions. Deep 
learning, a subset of machine learning, has been particularly successful in areas 
like computer vision and natural language processing. However, the rapid adoption 
of AI also raises important ethical questions about privacy, bias, and job 
displacement that society must address."""
    
    prompt = f"Summarize this text in 2 sentences:\n\n{long_text}"
    response = model.generate_content(prompt)
    print(f"Original: {len(long_text)} characters")
    print(f"Summary: {response.text}")
    print()
    
    # Use case 3: Translation/Rewriting
    print("\n3️⃣ Text Transformation:")
    prompt = """Rewrite this technical sentence in simple English:
"The convolutional neural network employs hierarchical feature extraction 
to perform image classification tasks with high accuracy."
"""
    response = model.generate_content(prompt)
    print(f"Simplified: {response.text}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main function with menu-driven interface
    """
    print("\n")
    print("🎓 " + "=" * 58 + " 🎓")
    print("      GENERATIVE AI SESSION - MODULE 2: TEXT CHAT")
    print("🎓 " + "=" * 58 + " 🎓")
    
    menu = """
    Choose a section to run (or 'all' to run everything):
    
    1. Simple Text Generation
    2. Question Answering
    3. Prompt Engineering Techniques
    4. Interactive Single-Turn Chat
    5. Long-Form Content Generation
    6. Code Generation Examples
    7. Practical Use Cases
    
    all - Run all sections
    quit - Exit
    
    """
    
    while True:
        print(menu)
        choice = input("Your choice: ").strip().lower()
        
        if choice == 'quit' or choice == 'q':
            print("👋 Goodbye!")
            break
        elif choice == '1':
            simple_text_generation()
        elif choice == '2':
            question_answering()
        elif choice == '3':
            prompt_engineering_examples()
        elif choice == '4':
            interactive_single_turn()
        elif choice == '5':
            long_form_generation()
        elif choice == '6':
            code_generation_examples()
        elif choice == '7':
            practical_use_cases()
        elif choice == 'all':
            simple_text_generation()
            question_answering()
            prompt_engineering_examples()
            long_form_generation()
            code_generation_examples()
            practical_use_cases()
            print("\n✅ All sections completed!")
            print("💡 Try section 4 separately for interactive chat")
            break
        else:
            print("⚠️  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
    # Teaching Questions:
    # 1. What makes a good prompt?
    # 2. How does specificity affect response quality?
    # 3. What are the limitations of single-turn conversations?
