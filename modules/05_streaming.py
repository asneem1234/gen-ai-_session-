"""
05 - Streaming Concepts
=======================

This module demonstrates streaming responses from the AI model.
Students will learn:
- What is streaming and why it matters
- Implementing streaming responses
- Real-time token generation
- User experience improvements
- Handling streaming errors

Teaching Points:
- Streaming provides immediate feedback to users
- Better UX for long responses
- Token-by-token generation
- Essential for chat applications
- Reduces perceived latency
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai
import time
import sys

# Setup
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


# ============================================================================
# SECTION 1: Understanding Streaming
# ============================================================================

def streaming_concepts():
    """
    Explain what streaming is and why it's important
    """
    print("\n" + "=" * 60)
    print("SECTION 1: Understanding Streaming")
    print("=" * 60)
    
    explanation = """
    🌊 WHAT IS STREAMING?
    
    NON-STREAMING (Traditional):
    ----------------------------
    1. User sends prompt
    2. AI processes entire response
    3. User waits...
    4. Complete response appears all at once
    
    ⏱️ Problem: Long wait time before seeing anything
    
    STREAMING:
    ----------
    1. User sends prompt
    2. AI starts generating
    3. Tokens appear in real-time as generated
    4. User sees response building up
    
    ✅ Benefit: Immediate feedback, better UX
    
    
    📊 COMPARISON:
    
    Prompt: "Write a 500-word essay about AI"
    
    Non-Streaming:
    • User waits 15 seconds
    • Entire essay appears at once
    • Perception: "Is it working?"
    
    Streaming:
    • Text starts appearing after 0.5 seconds
    • Words flow continuously
    • Perception: "It's working! I can start reading!"
    
    
    💡 WHEN TO USE STREAMING:
    
    ✅ Use streaming for:
       • Interactive chat applications
       • Long-form content generation
       • Real-time user interfaces
       • Progressive web apps
    
    ❌ Don't need streaming for:
       • Batch processing
       • Background jobs
       • Very short responses
       • Data processing pipelines
    
    
    ⚙️ HOW IT WORKS:
    
    1. Instead of: response = model.generate_content(prompt)
    2. Use: response = model.generate_content(prompt, stream=True)
    3. Iterate: for chunk in response: print(chunk.text)
    """
    
    print(explanation)


# ============================================================================
# SECTION 2: Basic Streaming Example
# ============================================================================

def basic_streaming_example():
    """
    Simple streaming demonstration
    """
    print("\n" + "=" * 60)
    print("SECTION 2: Basic Streaming Example")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = "Write a short paragraph about the benefits of renewable energy."
    
    print(f"\n📝 Prompt: {prompt}\n")
    print("🤖 AI Response (streaming):")
    print("-" * 60)
    
    # Enable streaming with stream=True
    response = model.generate_content(prompt, stream=True)
    
    # Iterate through chunks as they arrive
    for chunk in response:
        print(chunk.text, end='', flush=True)
    
    print("\n" + "-" * 60)
    print("✅ Streaming complete!")


# ============================================================================
# SECTION 3: Streaming vs Non-Streaming Comparison
# ============================================================================

def compare_streaming_vs_non_streaming():
    """
    Side-by-side comparison of both approaches
    """
    print("\n" + "=" * 60)
    print("SECTION 3: Streaming vs Non-Streaming Comparison")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = "Explain quantum computing in simple terms. Keep it brief."
    
    # Non-Streaming
    print("\n1️⃣ NON-STREAMING Approach:")
    print("-" * 60)
    print("⏳ Waiting for complete response...\n")
    
    start_time = time.time()
    response = model.generate_content(prompt, stream=False)
    end_time = time.time()
    
    print("🤖 Response:")
    print(response.text)
    print(f"\n⏱️  Time to first output: {end_time - start_time:.2f} seconds")
    print("📊 User experience: Wait → Complete text appears")
    
    # Streaming
    print("\n\n2️⃣ STREAMING Approach:")
    print("-" * 60)
    print("🤖 Response:\n")
    
    start_time = time.time()
    first_chunk_time = None
    
    response_stream = model.generate_content(prompt, stream=True)
    
    for i, chunk in enumerate(response_stream):
        if i == 0:
            first_chunk_time = time.time() - start_time
        print(chunk.text, end='', flush=True)
        time.sleep(0.05)  # Simulate reading time for demo
    
    end_time = time.time()
    
    print(f"\n\n⏱️  Time to first output: {first_chunk_time:.2f} seconds")
    print(f"⏱️  Total time: {end_time - start_time:.2f} seconds")
    print("📊 User experience: Immediate start → Progressive display")


# ============================================================================
# SECTION 4: Token-by-Token Streaming
# ============================================================================

def token_by_token_streaming():
    """
    Demonstrate granular token streaming
    """
    print("\n" + "=" * 60)
    print("SECTION 4: Token-by-Token Streaming")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = "List 5 programming languages and one-word descriptions."
    
    print(f"\n📝 Prompt: {prompt}\n")
    print("🤖 Streaming Response:")
    print("-" * 60)
    
    # Track chunks
    chunk_count = 0
    total_text = ""
    
    response = model.generate_content(prompt, stream=True)
    
    for chunk in response:
        chunk_count += 1
        chunk_text = chunk.text
        total_text += chunk_text
        
        # Display with visual indicator
        print(chunk_text, end='', flush=True)
        
        # Small delay to visualize streaming
        time.sleep(0.02)
    
    print("\n" + "-" * 60)
    print(f"📊 Statistics:")
    print(f"   • Total chunks: {chunk_count}")
    print(f"   • Total characters: {len(total_text)}")
    print(f"   • Average chunk size: {len(total_text)/chunk_count:.1f} chars")


# ============================================================================
# SECTION 5: Interactive Streaming Chat
# ============================================================================

def interactive_streaming_chat():
    """
    Interactive chat with streaming responses
    """
    print("\n" + "=" * 60)
    print("SECTION 5: Interactive Streaming Chat")
    print("=" * 60)
    print("\nType your messages and see streaming responses!")
    print("Type 'quit' to exit\n")
    
    model = genai.GenerativeModel('gemini-pro')
    
    conversation_count = 0
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
            
        if not user_input:
            continue
        
        conversation_count += 1
        
        print("🤖 AI: ", end='', flush=True)
        
        try:
            # Stream the response
            response = model.generate_content(user_input, stream=True)
            
            for chunk in response:
                print(chunk.text, end='', flush=True)
            
            print("\n")
            
            if conversation_count == 1:
                print("💡 Notice how the response appears word-by-word!\n")
                
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


# ============================================================================
# SECTION 6: Progress Indicators with Streaming
# ============================================================================

def streaming_with_progress():
    """
    Streaming with visual progress indicators
    """
    print("\n" + "=" * 60)
    print("SECTION 6: Streaming with Progress Indicators")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = "Write a three-paragraph story about a robot learning to paint."
    
    print(f"\n📝 Prompt: {prompt}\n")
    print("🤖 Generating story with progress indicator:")
    print("=" * 60)
    
    # Method 1: Character counter
    print("\n[Method 1: Character Counter]\n")
    
    char_count = 0
    response = model.generate_content(prompt, stream=True)
    
    for chunk in response:
        chunk_text = chunk.text
        print(chunk_text, end='', flush=True)
        char_count += len(chunk_text)
        
        # Update counter in status line (would use different approach in GUI)
        if char_count % 50 == 0:
            sys.stdout.write(f' [{char_count} chars]')
            sys.stdout.flush()
    
    print(f"\n\n✅ Complete! Total: {char_count} characters")
    
    # Method 2: Typing effect
    print("\n" + "=" * 60)
    print("[Method 2: Typing Effect]\n")
    
    prompt2 = "Describe a sunset in 2 sentences."
    response2 = model.generate_content(prompt2, stream=True)
    
    for chunk in response2:
        for char in chunk.text:
            print(char, end='', flush=True)
            time.sleep(0.03)  # Typing effect
    
    print("\n")


# ============================================================================
# SECTION 7: Error Handling in Streaming
# ============================================================================

def streaming_error_handling():
    """
    Properly handle errors in streaming responses
    """
    print("\n" + "=" * 60)
    print("SECTION 7: Error Handling in Streaming")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    print("\n✅ BEST PRACTICE: Always use try-except with streaming\n")
    
    code_example = """
def safe_streaming_response(model, prompt):
    try:
        response = model.generate_content(prompt, stream=True)
        
        accumulated_text = ""
        
        for chunk in response:
            try:
                text = chunk.text
                accumulated_text += text
                print(text, end='', flush=True)
                
            except ValueError as e:
                # Handle blocked content or safety filters
                print(f"\\n⚠️  Content blocked: {e}")
                break
                
            except Exception as e:
                # Handle other chunk-level errors
                print(f"\\n❌ Chunk error: {e}")
                continue
        
        return accumulated_text
        
    except Exception as e:
        print(f"❌ Stream error: {e}")
        return None
"""
    
    print("CODE EXAMPLE:")
    print("-" * 60)
    print(code_example)
    
    # Demonstrate safe implementation
    print("\n\nDEMONSTRATION:")
    print("-" * 60)
    
    def safe_streaming_response(model, prompt):
        try:
            response = model.generate_content(prompt, stream=True)
            
            accumulated_text = ""
            
            for chunk in response:
                try:
                    text = chunk.text
                    accumulated_text += text
                    print(text, end='', flush=True)
                    
                except ValueError as e:
                    print(f"\n⚠️  Content blocked: {e}")
                    break
                    
                except Exception as e:
                    print(f"\n❌ Chunk error: {e}")
                    continue
            
            return accumulated_text
            
        except Exception as e:
            print(f"❌ Stream error: {e}")
            return None
    
    test_prompt = "Explain why error handling is important in production code."
    print(f"\nPrompt: {test_prompt}\n")
    safe_streaming_response(model, test_prompt)
    print("\n")


# ============================================================================
# SECTION 8: Practical Streaming Applications
# ============================================================================

def practical_streaming_applications():
    """
    Real-world uses of streaming
    """
    print("\n" + "=" * 60)
    print("SECTION 8: Practical Streaming Applications")
    print("=" * 60)
    
    applications = """
    🚀 REAL-WORLD USE CASES:
    
    1. 💬 CHAT APPLICATIONS
       • Instant messaging feel
       • Better than "typing..." indicators
       • User can start reading while AI generates
       
       Implementation:
       - WebSocket for real-time communication
       - Send chunks as they arrive
       - Update UI incrementally
    
    2. 📝 CONTENT GENERATION TOOLS
       • Blog post writers
       • Code generators
       • Email composers
       
       Benefit:
       - Users can edit early parts while rest generates
       - Faster perceived performance
       - Can interrupt if going wrong direction
    
    3. 🎓 EDUCATIONAL PLATFORMS
       • Tutoring chatbots
       • Interactive learning
       • Real-time explanations
       
       Benefit:
       - More engaging for students
       - Natural conversation flow
       - Immediate feedback
    
    4. 🛠️ CODE ASSISTANTS
       • IDE integrations
       • Code completion
       • Debugging help
       
       Benefit:
       - See code as it's generated
       - Can accept/reject parts
       - Faster development workflow
    
    5. 📞 CUSTOMER SUPPORT
       • Chatbots
       • FAQ assistants
       • Ticket resolution
       
       Benefit:
       - Natural conversation
       - Reduces waiting anxiety
       - Professional appearance
    
    
    💻 IMPLEMENTATION PATTERNS:
    
    Pattern 1: Web Application
    --------------------------
    Backend (Python):
        for chunk in response:
            yield f"data: {chunk.text}\\n\\n"
    
    Frontend (JavaScript):
        const eventSource = new EventSource('/stream');
        eventSource.onmessage = (event) => {
            displayText += event.data;
            updateUI(displayText);
        };
    
    Pattern 2: Desktop App
    ----------------------
    Use threading:
        def stream_response(prompt, callback):
            response = model.generate_content(prompt, stream=True)
            for chunk in response:
                callback(chunk.text)
    
    Pattern 3: Mobile App
    ---------------------
    Use async/await:
        async def stream_to_ui(prompt):
            response = model.generate_content(prompt, stream=True)
            for chunk in response:
                await update_ui(chunk.text)
    """
    
    print(applications)


# ============================================================================
# SECTION 9: Performance Considerations
# ============================================================================

def streaming_performance():
    """
    Performance tips for streaming
    """
    print("\n" + "=" * 60)
    print("SECTION 9: Performance Considerations")
    print("=" * 60)
    
    tips = """
    ⚡ OPTIMIZATION TIPS:
    
    1. BUFFER MANAGEMENT
       ❌ Don't: Update UI for every single character
       ✅ Do: Buffer small chunks, update in reasonable intervals
       
       Example:
       buffer = ""
       for chunk in response:
           buffer += chunk.text
           if len(buffer) > 50:  # Update every 50 chars
               update_ui(buffer)
               buffer = ""
    
    2. NETWORK EFFICIENCY
       • Use HTTP/2 for multiplexing
       • Enable compression
       • Keep connections alive
       • Use CDN for static assets
    
    3. UI RESPONSIVENESS
       • Use virtual scrolling for long outputs
       • Debounce updates if needed
       • Don't block main thread
       • Show loading states
    
    4. ERROR RECOVERY
       • Implement retry logic
       • Save partial responses
       • Graceful degradation
       • User-friendly error messages
    
    5. RESOURCE MANAGEMENT
       • Close streams properly
       • Clean up event listeners
       • Monitor memory usage
       • Implement timeouts
    
    
    📊 MEASURING PERFORMANCE:
    
    Key Metrics:
    • Time to first byte (TTFB)
    • Tokens per second
    • Total generation time
    • Network latency
    • UI responsiveness
    
    
    🔍 DEBUGGING:
    
    Common Issues:
    1. Choppy streaming → Network buffering
    2. Delayed start → Cold start/model loading
    3. Missing chunks → Error handling needed
    4. Memory leaks → Clean up properly
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
    print("    GENERATIVE AI SESSION - MODULE 5: STREAMING CONCEPTS")
    print("🎓 " + "=" * 58 + " 🎓")
    
    menu = """
    Choose a section to run:
    
    1. Understanding Streaming
    2. Basic Streaming Example
    3. Streaming vs Non-Streaming Comparison
    4. Token-by-Token Streaming
    5. Interactive Streaming Chat
    6. Streaming with Progress Indicators
    7. Error Handling in Streaming
    8. Practical Applications
    9. Performance Considerations
    
    all - Run all (except interactive)
    quit - Exit
    
    """
    
    while True:
        print(menu)
        choice = input("Your choice: ").strip().lower()
        
        if choice in ['quit', 'q', 'exit']:
            print("👋 Goodbye!")
            break
        elif choice == '1':
            streaming_concepts()
        elif choice == '2':
            basic_streaming_example()
        elif choice == '3':
            compare_streaming_vs_non_streaming()
        elif choice == '4':
            token_by_token_streaming()
        elif choice == '5':
            interactive_streaming_chat()
        elif choice == '6':
            streaming_with_progress()
        elif choice == '7':
            streaming_error_handling()
        elif choice == '8':
            practical_streaming_applications()
        elif choice == '9':
            streaming_performance()
        elif choice == 'all':
            streaming_concepts()
            basic_streaming_example()
            compare_streaming_vs_non_streaming()
            token_by_token_streaming()
            streaming_with_progress()
            streaming_error_handling()
            practical_streaming_applications()
            streaming_performance()
            print("\n✅ All sections completed!")
            print("💡 Try section 5 separately for interactive chat")
            break
        else:
            print("⚠️  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
    # Teaching Questions:
    # 1. Why is streaming important for user experience?
    # 2. When would you NOT use streaming?
    # 3. How would you implement streaming in a web app?
