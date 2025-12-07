"""
07 - Model Configurations
==========================

This module demonstrates generation parameters and how they affect AI output.
Students will learn:
- Temperature control (creativity vs consistency)
- Top-P (nucleus sampling)
- Top-K sampling
- Max output tokens
- Stop sequences
- How to choose parameters for different use cases

Teaching Points:
- Generation parameters dramatically affect output
- Different tasks need different settings
- Experimentation is key
- Trade-offs between creativity and reliability
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Setup
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


# ============================================================================
# SECTION 1: Understanding Generation Parameters
# ============================================================================

def generation_parameters_overview():
    """
    Explain all generation parameters
    """
    print("\n" + "=" * 60)
    print("SECTION 1: Understanding Generation Parameters")
    print("=" * 60)
    
    overview = """
    🎛️ GENERATION PARAMETERS:
    
    These parameters control HOW the AI generates text.
    Think of them as "knobs" you can tune for different effects.
    
    
    1️⃣ TEMPERATURE (0.0 - 2.0)
    ===========================
    Controls randomness/creativity
    
    Low (0.0 - 0.3): ❄️ Conservative
    • More focused and deterministic
    • Safer, more predictable outputs
    • Good for: Facts, code, structured data
    • Example: "2+2=" → Always "4"
    
    Medium (0.4 - 0.9): 🌡️ Balanced
    • Natural variation
    • Good general-purpose setting
    • Good for: Chat, Q&A, explanations
    • Example: "Hello!" → Various greetings
    
    High (1.0 - 2.0): 🔥 Creative
    • Very diverse outputs
    • Can be unexpected/unusual
    • Good for: Creative writing, brainstorming
    • Example: "Once upon a time" → Wild stories
    
    
    2️⃣ TOP-P / Nucleus Sampling (0.0 - 1.0)
    ========================================
    Controls diversity by probability mass
    
    How it works:
    • Model calculates probabilities for next token
    • Selects from smallest set that adds up to P
    • Higher P = more variety
    
    Low (0.1 - 0.3):
    • Only most likely tokens
    • Very focused output
    
    Medium (0.4 - 0.8):
    • Balanced selection
    • Default: 0.95
    
    High (0.9 - 1.0):
    • Includes less likely options
    • Maximum diversity
    
    
    3️⃣ TOP-K (1 - 100+)
    ====================
    Limits to K most likely next tokens
    
    Low (1 - 10):
    • Very restricted choices
    • Highly focused
    
    Medium (10 - 40):
    • Balanced diversity
    • Default: 40
    
    High (40+):
    • Many options considered
    • More varied output
    
    
    4️⃣ MAX OUTPUT TOKENS
    =====================
    Maximum length of generated response
    
    • 1 token ≈ 0.75 words (English)
    • Controls response length
    • Prevents overly long outputs
    • Default: 2048 for Gemini Pro
    
    Examples:
    • 50 tokens: ~37 words (short answer)
    • 500 tokens: ~375 words (paragraph)
    • 2048 tokens: ~1500 words (article)
    
    
    5️⃣ STOP SEQUENCES
    ==================
    Strings that stop generation
    
    Examples:
    • Stop at "\\n\\n" for paragraphs
    • Stop at "###" for sections
    • Stop at specific phrases
    
    Use cases:
    • Structured output
    • Format control
    • Template filling
    
    
    📊 PARAMETER INTERACTIONS:
    
    Temperature + Top-P:
    • Often used together
    • Both affect diversity
    • Start with one, adjust other
    
    Top-P vs Top-K:
    • Alternative approaches
    • Top-P usually preferred
    • Can use both together
    """
    
    print(overview)


# ============================================================================
# SECTION 2: Temperature Examples
# ============================================================================

def temperature_comparison():
    """
    Compare different temperature settings
    """
    print("\n" + "=" * 60)
    print("SECTION 2: Temperature Comparison")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = "Complete this sentence: The future of artificial intelligence is"
    
    temperatures = [0.0, 0.5, 1.0, 1.5]
    
    print(f"\n📝 Prompt: '{prompt}'\n")
    print("🔬 Testing different temperatures:\n")
    print("=" * 60)
    
    for temp in temperatures:
        print(f"\n🌡️  TEMPERATURE: {temp}")
        print("-" * 60)
        
        # Configure generation settings
        generation_config = genai.types.GenerationConfig(
            temperature=temp,
            max_output_tokens=100
        )
        
        # Generate 3 responses to show variation
        for i in range(3):
            response = model.generate_content(
                prompt,
                generation_config=generation_config
            )
            print(f"\n  Response {i+1}: {response.text}")
        
        print()
        
        if temp == 0.0:
            print("  💡 Notice: Responses are very similar/identical")
        elif temp == 1.5:
            print("  💡 Notice: Responses are quite diverse and creative")


# ============================================================================
# SECTION 3: Top-P (Nucleus Sampling)
# ============================================================================

def top_p_examples():
    """
    Demonstrate top-p sampling
    """
    print("\n" + "=" * 60)
    print("SECTION 3: Top-P (Nucleus Sampling)")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = "Write a creative opening line for a science fiction story."
    
    top_p_values = [0.1, 0.5, 0.95]
    
    print(f"\n📝 Prompt: '{prompt}'\n")
    print("=" * 60)
    
    for top_p in top_p_values:
        print(f"\n🎯 TOP-P: {top_p}")
        print("-" * 60)
        
        generation_config = genai.types.GenerationConfig(
            top_p=top_p,
            temperature=0.9,  # Keep temperature constant
            max_output_tokens=80
        )
        
        # Generate multiple responses
        for i in range(2):
            response = model.generate_content(
                prompt,
                generation_config=generation_config
            )
            print(f"\n  Response {i+1}:\n  {response.text}")
        
        print()


# ============================================================================
# SECTION 4: Top-K Sampling
# ============================================================================

def top_k_examples():
    """
    Demonstrate top-k sampling
    """
    print("\n" + "=" * 60)
    print("SECTION 4: Top-K Sampling")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = "Name a programming language: "
    
    top_k_values = [1, 10, 40]
    
    print(f"\n📝 Prompt: '{prompt}'\n")
    print("=" * 60)
    
    for top_k in top_k_values:
        print(f"\n🔢 TOP-K: {top_k}")
        print("-" * 60)
        
        generation_config = genai.types.GenerationConfig(
            top_k=top_k,
            temperature=1.0,
            max_output_tokens=50
        )
        
        # Generate multiple responses to see variety
        responses = []
        for i in range(5):
            response = model.generate_content(
                prompt,
                generation_config=generation_config
            )
            responses.append(response.text.split()[0])  # Get first word
        
        print(f"  Responses: {responses}")
        print(f"  Unique answers: {len(set(responses))}")


# ============================================================================
# SECTION 5: Max Output Tokens
# ============================================================================

def max_tokens_examples():
    """
    Control response length with max tokens
    """
    print("\n" + "=" * 60)
    print("SECTION 5: Max Output Tokens")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = "Explain what machine learning is."
    
    token_limits = [30, 100, 500]
    
    print(f"\n📝 Prompt: '{prompt}'\n")
    print("=" * 60)
    
    for max_tokens in token_limits:
        print(f"\n📏 MAX TOKENS: {max_tokens} (~{int(max_tokens * 0.75)} words)")
        print("-" * 60)
        
        generation_config = genai.types.GenerationConfig(
            max_output_tokens=max_tokens,
            temperature=0.7
        )
        
        response = model.generate_content(
            prompt,
            generation_config=generation_config
        )
        
        response_text = response.text
        word_count = len(response_text.split())
        
        print(response_text)
        print(f"\n  📊 Actual words: {word_count}")
        print()


# ============================================================================
# SECTION 6: Stop Sequences
# ============================================================================

def stop_sequences_examples():
    """
    Use stop sequences to control output
    """
    print("\n" + "=" * 60)
    print("SECTION 6: Stop Sequences")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    print("\n💡 Stop sequences tell the model when to stop generating")
    print("Useful for structured output and format control\n")
    
    # Example 1: Stop at line break
    print("1️⃣ Stop at double newline (paragraph boundary):")
    print("-" * 60)
    
    prompt1 = "Write about Python programming.\n\n"
    
    generation_config1 = genai.types.GenerationConfig(
        stop_sequences=["\n\n"],
        max_output_tokens=200
    )
    
    response1 = model.generate_content(
        prompt1,
        generation_config=generation_config1
    )
    
    print(response1.text)
    print("\n📌 Generation stopped at paragraph break")
    
    # Example 2: Stop at specific marker
    print("\n\n2️⃣ Stop at specific marker (###):")
    print("-" * 60)
    
    prompt2 = "List three programming languages:\n1."
    
    generation_config2 = genai.types.GenerationConfig(
        stop_sequences=["###", "\n\n"],
        max_output_tokens=200
    )
    
    response2 = model.generate_content(
        prompt2,
        generation_config=generation_config2
    )
    
    print(response2.text)


# ============================================================================
# SECTION 7: Use Case Configurations
# ============================================================================

def use_case_configurations():
    """
    Recommended configurations for different use cases
    """
    print("\n" + "=" * 60)
    print("SECTION 7: Use Case Configurations")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    use_cases = {
        "Factual Q&A": {
            "config": genai.types.GenerationConfig(
                temperature=0.1,
                top_p=0.8,
                max_output_tokens=150
            ),
            "prompt": "What is the capital of France?",
            "rationale": "Low temperature for factual accuracy"
        },
        "Creative Writing": {
            "config": genai.types.GenerationConfig(
                temperature=1.2,
                top_p=0.95,
                max_output_tokens=300
            ),
            "prompt": "Write a creative opening for a mystery novel.",
            "rationale": "High temperature for creativity and variety"
        },
        "Code Generation": {
            "config": genai.types.GenerationConfig(
                temperature=0.2,
                top_p=0.85,
                max_output_tokens=500
            ),
            "prompt": "Write a Python function to calculate factorial.",
            "rationale": "Low temperature for correct, consistent code"
        },
        "Brainstorming": {
            "config": genai.types.GenerationConfig(
                temperature=1.0,
                top_p=0.9,
                max_output_tokens=200
            ),
            "prompt": "Generate 5 unique business ideas for a coffee shop.",
            "rationale": "Balanced for diverse but coherent ideas"
        },
        "Chat/Conversation": {
            "config": genai.types.GenerationConfig(
                temperature=0.7,
                top_p=0.9,
                max_output_tokens=250
            ),
            "prompt": "Hi! How's your day going?",
            "rationale": "Medium temperature for natural conversation"
        }
    }
    
    print("\n📋 Recommended Configurations by Use Case:\n")
    
    for use_case, settings in use_cases.items():
        print("=" * 60)
        print(f"🎯 {use_case.upper()}")
        print("=" * 60)
        
        config = settings['config']
        print(f"\n⚙️  Configuration:")
        print(f"   • Temperature: {config.temperature}")
        print(f"   • Top-P: {config.top_p}")
        print(f"   • Max Tokens: {config.max_output_tokens}")
        print(f"\n💡 Rationale: {settings['rationale']}")
        
        print(f"\n📝 Example Prompt: '{settings['prompt']}'")
        print(f"\n🤖 Response:")
        print("-" * 60)
        
        response = model.generate_content(
            settings['prompt'],
            generation_config=config
        )
        
        print(response.text)
        print()


# ============================================================================
# SECTION 8: Interactive Parameter Testing
# ============================================================================

def interactive_parameter_testing():
    """
    Let users experiment with parameters
    """
    print("\n" + "=" * 60)
    print("SECTION 8: Interactive Parameter Testing")
    print("=" * 60)
    print("\nExperiment with different parameter combinations!")
    print("Type 'quit' to exit\n")
    
    model = genai.GenerativeModel('gemini-pro')
    
    while True:
        print("=" * 60)
        
        # Get prompt
        prompt = input("\nEnter your prompt (or 'quit'): ").strip()
        if prompt.lower() in ['quit', 'exit', 'q']:
            break
        
        if not prompt:
            continue
        
        # Get parameters
        try:
            temp = float(input("Temperature (0.0-2.0, default 0.7): ").strip() or "0.7")
            top_p = float(input("Top-P (0.0-1.0, default 0.95): ").strip() or "0.95")
            max_tokens = int(input("Max tokens (default 200): ").strip() or "200")
            
            # Create configuration
            generation_config = genai.types.GenerationConfig(
                temperature=temp,
                top_p=top_p,
                max_output_tokens=max_tokens
            )
            
            # Generate response
            print("\n⏳ Generating...")
            response = model.generate_content(
                prompt,
                generation_config=generation_config
            )
            
            print("\n🤖 Response:")
            print("-" * 60)
            print(response.text)
            print("-" * 60)
            
            print(f"\n📊 Used: temp={temp}, top_p={top_p}, max_tokens={max_tokens}\n")
            
        except ValueError as e:
            print(f"⚠️  Invalid input: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")


# ============================================================================
# SECTION 9: Parameter Combinations
# ============================================================================

def parameter_combinations():
    """
    Show how parameters work together
    """
    print("\n" + "=" * 60)
    print("SECTION 9: Parameter Combinations")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = "The best thing about learning to code is"
    
    combinations = [
        {
            "name": "Ultra Conservative",
            "config": genai.types.GenerationConfig(
                temperature=0.0,
                top_p=0.5,
                top_k=10
            )
        },
        {
            "name": "Balanced & Reliable",
            "config": genai.types.GenerationConfig(
                temperature=0.7,
                top_p=0.9,
                top_k=40
            )
        },
        {
            "name": "Maximum Creativity",
            "config": genai.types.GenerationConfig(
                temperature=1.5,
                top_p=0.98,
                top_k=100
            )
        }
    ]
    
    print(f"\n📝 Prompt: '{prompt}'\n")
    print("=" * 60)
    
    for combo in combinations:
        print(f"\n⚙️  {combo['name'].upper()}")
        config = combo['config']
        print(f"   Temperature: {config.temperature}, Top-P: {config.top_p}, Top-K: {config.top_k}")
        print("-" * 60)
        
        response = model.generate_content(
            prompt,
            generation_config=config
        )
        
        print(response.text)
        print()


# ============================================================================
# SECTION 10: Best Practices
# ============================================================================

def configuration_best_practices():
    """
    Best practices for using generation parameters
    """
    print("\n" + "=" * 60)
    print("SECTION 10: Best Practices")
    print("=" * 60)
    
    practices = """
    ✅ BEST PRACTICES:
    
    1. START WITH DEFAULTS
       • Temperature: 0.7
       • Top-P: 0.95
       • Top-K: 40
       • Then adjust based on results
    
    2. ADJUST ONE AT A TIME
       • Change temperature first
       • Then fine-tune top-p if needed
       • Easier to understand effects
    
    3. TEST MULTIPLE TIMES
       • Parameters create variation
       • Run same prompt 3-5 times
       • Evaluate consistency
    
    4. MATCH TO USE CASE
       • Facts/Code: Low temperature (0.0-0.3)
       • Chat: Medium temperature (0.5-0.9)
       • Creative: High temperature (1.0-1.5)
    
    5. SET APPROPRIATE LIMITS
       • Max tokens prevents runaway generation
       • Stop sequences for structured output
       • Balance cost vs quality
    
    
    ⚠️ COMMON MISTAKES:
    
    1. Temperature too high for facts
       • Results in hallucinations
       • Inconsistent answers
       • Use < 0.3 for factual content
    
    2. Temperature too low for creativity
       • Repetitive outputs
       • Boring conversations
       • Use > 0.8 for creative tasks
    
    3. Ignoring token limits
       • Unexpected truncation
       • Incomplete responses
       • Set appropriate max_tokens
    
    4. Not testing variations
       • Parameters affect each prompt differently
       • Always test before production
       • Monitor outputs over time
    
    
    🎯 QUICK REFERENCE:
    
    Task                 | Temp  | Top-P | Max Tokens
    ---------------------|-------|-------|------------
    Factual Q&A          | 0.1   | 0.8   | 150
    Code Generation      | 0.2   | 0.85  | 500
    Chat/Conversation    | 0.7   | 0.9   | 250
    Creative Writing     | 1.2   | 0.95  | 500
    Brainstorming        | 1.0   | 0.95  | 200
    Data Extraction      | 0.0   | 0.7   | 100
    Summarization        | 0.3   | 0.85  | 300
    Translation          | 0.3   | 0.9   | Variable
    
    
    💡 PRO TIPS:
    
    • Temperature 0 is deterministic (mostly)
    • Higher temperature ≠ always better
    • Top-p and top-k are alternatives, not required together
    • Monitor costs - longer outputs cost more
    • Save successful configurations
    • Document your parameter choices
    • A/B test different settings
    • User feedback is invaluable
    """
    
    print(practices)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main function with menu
    """
    print("\n")
    print("🎓 " + "=" * 58 + " 🎓")
    print("  GENERATIVE AI SESSION - MODULE 7: MODEL CONFIGURATIONS")
    print("🎓 " + "=" * 58 + " 🎓")
    
    menu = """
    Choose a section to run:
    
    1. Generation Parameters Overview
    2. Temperature Comparison
    3. Top-P (Nucleus Sampling)
    4. Top-K Sampling
    5. Max Output Tokens
    6. Stop Sequences
    7. Use Case Configurations
    8. Interactive Parameter Testing
    9. Parameter Combinations
    10. Best Practices
    
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
            generation_parameters_overview()
        elif choice == '2':
            temperature_comparison()
        elif choice == '3':
            top_p_examples()
        elif choice == '4':
            top_k_examples()
        elif choice == '5':
            max_tokens_examples()
        elif choice == '6':
            stop_sequences_examples()
        elif choice == '7':
            use_case_configurations()
        elif choice == '8':
            interactive_parameter_testing()
        elif choice == '9':
            parameter_combinations()
        elif choice == '10':
            configuration_best_practices()
        elif choice == 'all':
            generation_parameters_overview()
            temperature_comparison()
            top_p_examples()
            top_k_examples()
            max_tokens_examples()
            stop_sequences_examples()
            use_case_configurations()
            parameter_combinations()
            configuration_best_practices()
            print("\n✅ All sections completed!")
            print("💡 Try section 8 separately for interactive testing")
            break
        else:
            print("⚠️  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
    # Teaching Questions:
    # 1. How does temperature affect output?
    # 2. When should you use low vs high temperature?
    # 3. What's the difference between top-p and top-k?
