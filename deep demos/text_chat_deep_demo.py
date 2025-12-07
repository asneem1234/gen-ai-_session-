"""
Deep Demo: Text Chat - Behind The Scenes
=========================================

This demo shows EXACTLY what happens when you call Gemini:
- Token conversion
- Prompt structure
- Processing steps
- Response generation
- Token usage

Perfect for showing students "what's under the hood"
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai
import time

# Setup
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


def print_section(title):
    """Print a fancy section header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")


def simulate_tokenization(text):
    """
    Simulate tokenization (show approximate tokens)
    Real tokenization is more complex, this is for educational purposes
    """
    # Rough approximation: ~4 characters = 1 token
    words = text.split()
    tokens = []
    token_count = 0
    
    for word in words:
        # Simulate word being split into tokens
        if len(word) <= 4:
            tokens.append(f"[{word}]")
            token_count += 1
        else:
            # Longer words might be multiple tokens
            chunks = [word[i:i+4] for i in range(0, len(word), 4)]
            for chunk in chunks:
                tokens.append(f"[{chunk}]")
                token_count += 1
    
    return tokens, token_count


def deep_text_chat_demo():
    """
    Comprehensive demo showing each step of AI text generation
    """
    
    print("\n" + "🎓" * 35)
    print("      DEEP DIVE: WHAT HAPPENS WHEN YOU CALL GEMINI AI")
    print("🎓" * 35)
    
    # User input
    print_section("STEP 1: USER INPUT")
    
    user_prompt = "Explain what happens when you make a cup of tea in 3 steps"
    
    print(f"📝 User's Question:")
    print(f"   '{user_prompt}'")
    print(f"\n📊 Length: {len(user_prompt)} characters")
    
    # Tokenization
    print_section("STEP 2: TOKENIZATION (Text → Tokens)")
    
    print("💡 What is Tokenization?")
    print("   AI models don't read text like humans. They convert words")
    print("   into numbers (tokens) that they can process.")
    print()
    
    tokens, token_count = simulate_tokenization(user_prompt)
    
    print(f"📦 Your text broken into tokens (approximate):")
    print("   " + " ".join(tokens[:15]))
    if len(tokens) > 15:
        print("   " + " ".join(tokens[15:]))
    print(f"\n📊 Approximate Token Count: {token_count} tokens")
    print(f"   (Actual may vary - this is a simplified simulation)")
    
    # Prompt structure
    print_section("STEP 3: PROMPT STRUCTURE")
    
    print("🏗️  Your prompt is structured for the AI:")
    print()
    print("┌─────────────────────────────────────────────────────────────┐")
    print("│ [SYSTEM CONTEXT]                                            │")
    print("│ • Model: gemini-2.0-flash                                         │")
    print("│ • Temperature: 0.7 (default)                                │")
    print("│ • Max tokens: 8192 (default)                                │")
    print("├─────────────────────────────────────────────────────────────┤")
    print("│ [USER INPUT]                                                │")
    print(f"│ {user_prompt[:60]:<59} │")
    if len(user_prompt) > 60:
        print(f"│ {user_prompt[60:]:<59} │")
    print("└─────────────────────────────────────────────────────────────┘")
    
    # API Call
    print_section("STEP 4: SENDING TO GEMINI")
    
    print("🌐 Making API call to Google's servers...")
    print("   ↓ Your prompt travels over HTTPS")
    print("   ↓ Reaches Google's AI infrastructure")
    print("   ↓ Routed to a Gemini Pro model instance")
    print()
    
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    print("⏳ Waiting for response...\n")
    
    start_time = time.time()
    
    # Make the actual API call
    response = model.generate_content(user_prompt)
    
    end_time = time.time()
    response_time = end_time - start_time
    
    # Processing simulation
    print_section("STEP 5: AI PROCESSING (What Happens Inside)")
    
    print("🧠 Inside Gemini's Neural Network:")
    print()
    print("   1️⃣  Token Embedding")
    print("      Each token → high-dimensional vector (numbers)")
    print("      Example: 'tea' → [0.234, -0.891, 0.445, ... 2048 dimensions]")
    print()
    print("   2️⃣  Attention Mechanism")
    print("      AI analyzes relationships between words")
    print("      'cup' + 'tea' → strong connection")
    print("      'make' + 'steps' → procedural context")
    print()
    print("   3️⃣  Transformer Layers (Billions of Parameters)")
    print("      40+ layers processing your input")
    print("      Pattern matching against training data")
    print("      Understanding context and intent")
    print()
    print("   4️⃣  Response Generation")
    print("      Predicting next token, one at a time")
    print("      Each token chosen based on probability")
    print("      Temperature controls randomness")
    print()
    
    # Response received
    print_section("STEP 6: RESPONSE RECEIVED")
    
    print(f"✅ Response generated in {response_time:.2f} seconds")
    print()
    print("📨 Raw Response Object:")
    print(f"   Type: {type(response)}")
    print(f"   Has text: {hasattr(response, 'text')}")
    print()
    
    # Token usage (if available)
    print("📊 Token Usage:")
    if hasattr(response, 'usage_metadata') and response.usage_metadata:
        print(f"   • Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"   • Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"   • Total tokens: {response.usage_metadata.total_token_count}")
    else:
        print("   • Prompt tokens: ~" + str(token_count))
        print("   • Response tokens: ~" + str(len(response.text.split()) // 4 * 5))
        print("   (Exact counts require API response metadata)")
    
    # Generated text
    print_section("STEP 7: GENERATED TEXT")
    
    print("🤖 AI's Response:")
    print()
    print("─" * 70)
    print(response.text)
    print("─" * 70)
    
    # Response analysis
    print_section("STEP 8: RESPONSE ANALYSIS")
    
    response_words = response.text.split()
    response_chars = len(response.text)
    response_lines = response.text.count('\n') + 1
    
    print("📈 Response Statistics:")
    print(f"   • Word count: {len(response_words)}")
    print(f"   • Character count: {response_chars}")
    print(f"   • Lines: {response_lines}")
    print(f"   • Average word length: {response_chars / len(response_words):.1f} chars")
    print()
    print(f"⚡ Generation Speed:")
    print(f"   • {len(response_words) / response_time:.1f} words per second")
    print(f"   • {response_chars / response_time:.1f} characters per second")
    
    # Behind the scenes
    print_section("STEP 9: BEHIND THE SCENES")
    
    print("🔍 What You Don't See:")
    print()
    print("   💰 Cost (for you, with free tier):")
    print("      • This request: ~$0.000 (free tier)")
    print("      • In production: ~$0.0005 per 1K tokens")
    print()
    print("   🌍 Infrastructure:")
    print("      • Datacenter: Google's global network")
    print("      • Hardware: TPU/GPU clusters")
    print("      • Model size: Billions of parameters")
    print("      • Training data: Trillions of tokens")
    print()
    print("   🔐 Security:")
    print("      • HTTPS encryption")
    print("      • API key authentication")
    print("      • Rate limiting")
    print("      • Content filtering")
    print()
    print("   ⚙️  Optimization:")
    print("      • Caching layers")
    print("      • Load balancing")
    print("      • Model quantization")
    print("      • Batch processing")
    
    # Complete flow diagram
    print_section("COMPLETE FLOW DIAGRAM")
    
    print("""
    Your Code                    Google's Infrastructure
    ═════════                    ═══════════════════════
    
         │
         ├─► generate_content("question")
         │
         ├─► Tokenization
         │      │
         │      ↓
         ├─► HTTPS Request ──────────► API Gateway
         │                                  │
         │                                  ↓
         │                             Load Balancer
         │                                  │
         │                                  ↓
         │                             Auth Check
         │                                  │
         │                                  ↓
         │                             Rate Limit
         │                                  │
         │                                  ↓
         │                             Model Server
         │                                  │
         │                                  ├─► Embedding
         │                                  ├─► Attention
         │                                  ├─► Transform
         │                                  ├─► Generate
         │                                  │
         │                                  ↓
         ◄─── Response ◄──────────────  Response
         │
         ├─► response.text
         │
         ↓
    Display to User
    """)
    
    # Interactive comparison
    print_section("BONUS: INTERACTIVE COMPARISON")
    
    print("🎮 Let's try different prompts and see the difference!\n")
    
    test_prompts = [
        ("Short", "What is AI?"),
        ("Detailed", "Explain artificial intelligence, its history, types, and applications in detail"),
        ("Creative", "Write a haiku about programming")
    ]
    
    for label, prompt in test_prompts:
        print(f"\n{'─'*70}")
        print(f"📝 {label} Prompt: '{prompt}'")
        tokens_approx, count = simulate_tokenization(prompt)
        print(f"📊 Tokens: ~{count}")
        
        start = time.time()
        resp = model.generate_content(prompt)
        elapsed = time.time() - start
        
        print(f"⏱️  Response time: {elapsed:.2f}s")
        print(f"📝 Response length: {len(resp.text)} chars, {len(resp.text.split())} words")
        print(f"\n🤖 Response preview:")
        print(f"   {resp.text[:100]}..." if len(resp.text) > 100 else f"   {resp.text}")
    
    # Summary
    print_section("🎓 KEY TAKEAWAYS")
    
    print("""
    ✅ What You Learned:
    
    1. Text → Tokens → Numbers (that's how AI reads)
    2. Your prompt + config = structured input
    3. Billions of parameters process your request
    4. Response generated token by token
    5. All this happens in < 1 second!
    
    💡 Why This Matters:
    
    • Understanding tokens helps optimize costs
    • Knowing response time helps UX design
    • Seeing the flow helps debugging
    • Token limits explain why context matters
    
    🚀 Now You Know:
    
    When you call model.generate_content(), you're:
    • Tokenizing text
    • Sending structured prompts
    • Triggering billions of calculations
    • Getting back intelligently generated text
    
    That "simple" one-liner does A LOT! 🤯
    """)
    
    print("\n" + "="*70)
    print("  END OF DEEP DIVE")
    print("="*70 + "\n")


def main():
    """Run the deep demo"""
    try:
        deep_text_chat_demo()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure you have:")
        print("  1. Set up GOOGLE_API_KEY in .env file")
        print("  2. Installed: pip install google-generativeai python-dotenv")


if __name__ == "__main__":
    main()
