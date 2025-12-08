# 07 Model Configurations - Complete Code Explanation

## 📋 Overview
This code demonstrates how to control AI behavior through configuration parameters. Temperature, max tokens, and top-p sampling allow you to fine-tune responses for different use cases - from deterministic factual answers to creative storytelling. Understanding these settings is essential for building reliable AI applications.

---

## 💻 Complete Code with Line-by-Line Explanation

```python
import os
# WHY: Import operating system module
# WHAT IT DOES: Provides access to environment variables
# WHEN TO USE: Required for reading API keys securely

from dotenv import load_dotenv
# WHY: Import function to load .env file
# WHAT IT DOES: Reads environment variables from .env
# SECURITY: Keeps sensitive information out of code

import google.generativeai as genai
# WHY: Import Google Generative AI library
# WHAT IT DOES: Provides tools for AI operations
# CAPABILITY: Supports extensive configuration options

load_dotenv()
# WHY: Load environment variables at module level
# WHAT IT DOES: Makes GOOGLE_API_KEY accessible
# TIMING: Called immediately before configuration

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
# WHY: Authenticate with Gemini API
# WHAT IT DOES: Sets up API key for all requests
# REQUIRED: Must be done before any AI operations

def temperature_control():
    # WHY: Demonstrate temperature parameter effects
    # WHAT IT DOES: Shows how temperature controls randomness
    # USE CASE: Choosing between consistent vs creative responses
    # RANGE: 0.0 to 2.0 (typically 0.0-1.0 recommended)
    
    prompt = "Complete this sentence: The future of AI is"
    # WHY: Use open-ended prompt for comparison
    # WHAT IT DOES: Creates sentence requiring completion
    # PURPOSE: Same prompt with different temps shows variation
    # OPEN-ENDED: Allows AI to demonstrate creativity vs consistency
    
    print("Low temperature (0.1) - Deterministic:")
    # WHY: Label the low temperature test
    # WHAT IT DOES: Indicates deterministic mode
    # EXPECTATION: Consistent, predictable responses
    
    model = genai.GenerativeModel('gemini-2.0-flash', 
                                   generation_config={'temperature': 0.1})
    # WHY: Create model with low temperature
    # WHAT IT DOES: Initializes model with specific config
    # PARAMETER: generation_config dictionary
    #   - temperature: 0.1 (very low)
    # EFFECT: AI chooses most probable tokens
    # BEHAVIOR: Responses will be similar each time
    # USE CASE: Factual answers, code generation, consistency
    
    response = model.generate_content(prompt)
    # WHY: Generate content with low temperature
    # WHAT IT DOES: Gets deterministic response
    # EXPECTED: Predictable, safe completion
    
    print(f"{response.text}\n")
    # WHY: Display the deterministic response
    # WHAT IT DOES: Shows consistent output
    # TYPICAL: "promising" or "bright" (common words)
    
    print("High temperature (1.5) - Creative:")
    # WHY: Label the high temperature test
    # WHAT IT DOES: Indicates creative mode
    # EXPECTATION: Varied, creative responses
    
    model = genai.GenerativeModel('gemini-2.0-flash',
                                   generation_config={'temperature': 1.5})
    # WHY: Create model with high temperature
    # WHAT IT DOES: Initializes model with creative config
    # PARAMETER: temperature: 1.5 (high)
    # EFFECT: AI explores less probable tokens
    # BEHAVIOR: Responses vary significantly each run
    # USE CASE: Creative writing, brainstorming, variety
    # WARNING: Very high temps (>1.0) can produce nonsense
    
    response = model.generate_content(prompt)
    # WHY: Generate content with high temperature
    # WHAT IT DOES: Gets creative, varied response
    # EXPECTED: Unexpected, imaginative completion
    
    print(f"{response.text}")
    # WHY: Display the creative response
    # WHAT IT DOES: Shows varied output
    # TYPICAL: Unusual or creative word choices

def max_tokens_control():
    # WHY: Demonstrate output length control
    # WHAT IT DOES: Shows how to limit response length
    # USE CASE: Controlling costs, UI constraints, summaries
    # TOKEN: ~4 characters = 1 token (rough estimate)
    
    prompt = "Explain quantum computing"
    # WHY: Use complex topic for length demo
    # WHAT IT DOES: Creates prompt that could generate long response
    # PURPOSE: Shows clear difference between length limits
    # TOPIC: Quantum computing has much to explain
    
    print("Short response (50 tokens):")
    # WHY: Label the short response test
    # WHAT IT DOES: Indicates length limit
    # ~50 tokens ≈ 200 characters ≈ 2-3 sentences
    
    model = genai.GenerativeModel('gemini-2.0-flash',
                                   generation_config={'max_output_tokens': 50})
    # WHY: Create model with token limit
    # WHAT IT DOES: Initializes model with length constraint
    # PARAMETER: max_output_tokens: 50
    # EFFECT: Response stops at ~50 tokens
    # BEHAVIOR: May cut off mid-sentence if limit reached
    # USE CASE: Summaries, short answers, cost control
    # COST: Fewer tokens = lower cost
    
    response = model.generate_content(prompt)
    # WHY: Generate short response
    # WHAT IT DOES: Gets truncated explanation
    # EXPECTED: Brief, possibly incomplete answer
    
    print(f"{response.text}\n")
    # WHY: Display the short response
    # WHAT IT DOES: Shows limited output
    # RESULT: Concise explanation or summary
    
    print("Longer response (200 tokens):")
    # WHY: Label the longer response test
    # WHAT IT DOES: Indicates higher limit
    # ~200 tokens ≈ 800 characters ≈ 8-10 sentences
    
    model = genai.GenerativeModel('gemini-2.0-flash',
                                   generation_config={'max_output_tokens': 200})
    # WHY: Create model with higher token limit
    # WHAT IT DOES: Allows longer, detailed response
    # PARAMETER: max_output_tokens: 200
    # EFFECT: Response can be up to ~200 tokens
    # BEHAVIOR: More comprehensive explanation
    # USE CASE: Detailed answers, articles, explanations
    # TRADEOFF: More tokens = higher cost
    
    response = model.generate_content(prompt)
    # WHY: Generate longer response
    # WHAT IT DOES: Gets detailed explanation
    # EXPECTED: Complete, thorough answer
    
    print(f"{response.text}")
    # WHY: Display the longer response
    # WHAT IT DOES: Shows extended output
    # RESULT: Comprehensive quantum computing explanation

def top_p_sampling():
    # WHY: Demonstrate nucleus sampling (top-p)
    # WHAT IT DOES: Shows probability mass-based token selection
    # USE CASE: Balancing quality and diversity
    # RANGE: 0.0 to 1.0
    
    prompt = "Tell me an interesting fact"
    # WHY: Use fact-based prompt for diversity demo
    # WHAT IT DOES: Creates open-ended request
    # PURPOSE: Shows how top-p affects fact selection
    # VARIETY: Many possible interesting facts exist
    
    print("Top-p = 0.5 (focused):")
    # WHY: Label the focused sampling test
    # WHAT IT DOES: Indicates narrow token selection
    # 0.5 = Consider tokens in top 50% probability mass
    
    model = genai.GenerativeModel('gemini-2.0-flash',
                                   generation_config={'top_p': 0.5})
    # WHY: Create model with nucleus sampling
    # WHAT IT DOES: Initializes model with probability threshold
    # PARAMETER: top_p: 0.5
    # EFFECT: Only considers most probable tokens (50% mass)
    # BEHAVIOR: More focused, safer responses
    # USE CASE: Factual content, professional writing
    # HOW IT WORKS:
    #   1. Sort tokens by probability
    #   2. Sum probabilities until reaching 0.5
    #   3. Only sample from those tokens
    
    response = model.generate_content(prompt)
    # WHY: Generate with focused sampling
    # WHAT IT DOES: Gets response from high-probability tokens
    # EXPECTED: Common, well-known fact
    
    print(f"{response.text}\n")
    # WHY: Display focused response
    # WHAT IT DOES: Shows safer, common output
    # TYPICAL: Well-known scientific facts
    
    print("Top-p = 0.95 (diverse):")
    # WHY: Label the diverse sampling test
    # WHAT IT DOES: Indicates broader token selection
    # 0.95 = Consider tokens in top 95% probability mass
    
    model = genai.GenerativeModel('gemini-2.0-flash',
                                   generation_config={'top_p': 0.95})
    # WHY: Create model with wider sampling
    # WHAT IT DOES: Allows more diverse token choices
    # PARAMETER: top_p: 0.95
    # EFFECT: Considers wider range of tokens (95% mass)
    # BEHAVIOR: More diverse, interesting responses
    # USE CASE: Creative writing, variety, exploration
    # BALANCE: High enough for diversity, not so high for nonsense
    
    response = model.generate_content(prompt)
    # WHY: Generate with diverse sampling
    # WHAT IT DOES: Gets response from broader token set
    # EXPECTED: More unique or unexpected fact
    
    print(f"{response.text}")
    # WHY: Display diverse response
    # WHAT IT DOES: Shows more varied output
    # TYPICAL: Less common but interesting facts

def combined_settings():
    # WHY: Demonstrate using multiple parameters together
    # WHAT IT DOES: Shows balanced configuration
    # USE CASE: Real-world applications need multiple controls
    # GOAL: Achieve specific quality/creativity/length balance
    
    config = {
        'temperature': 0.7,
        'max_output_tokens': 100,
        'top_p': 0.9
    }
    # WHY: Define configuration dictionary
    # WHAT IT DOES: Specifies multiple parameters at once
    # PARAMETERS:
    #   - temperature: 0.7 (moderate creativity)
    #   - max_output_tokens: 100 (medium length)
    #   - top_p: 0.9 (good diversity)
    # BALANCE: Reasonable creativity + quality + length
    # USE CASE: General-purpose content generation
    # EXPLANATION:
    #   - 0.7 temp: Creative but not wild
    #   - 100 tokens: ~400 chars, decent detail
    #   - 0.9 top-p: Diverse but not random
    
    model = genai.GenerativeModel('gemini-2.0-flash', generation_config=config)
    # WHY: Create model with combined configuration
    # WHAT IT DOES: Applies all parameters simultaneously
    # PARAMETER: Pass entire config dictionary
    # EFFECT: All settings work together
    # RESULT: Balanced behavior across all dimensions
    
    response = model.generate_content("Write a creative tagline for an AI company")
    # WHY: Use creative prompt to show balanced config
    # WHAT IT DOES: Requests creative but focused content
    # DEMONSTRATES: Config produces quality creative output
    # TAGLINE: Short, creative, memorable (perfect test)
    
    print(f"Response: {response.text}")
    # WHY: Display the balanced response
    # WHAT IT DOES: Shows result of combined settings
    # EXPECTED: Creative but sensible tagline

if __name__ == "__main__":
    # WHY: Check if script is run directly
    # WHAT IT DOES: Only executes demos when main program
    # BEST PRACTICE: Prevents auto-execution on import
    
    print("1. Temperature Control")
    # WHY: Label the temperature demo
    # WHAT IT DOES: Prints section header
    # UX: Helps user track demo progress
    
    temperature_control()
    # WHY: Execute temperature comparison demo
    # WHAT IT DOES: Shows low vs high temperature effects
    # DEMONSTRATES: Randomness control
    
    print("\n2. Max Tokens Control")
    # WHY: Label the tokens demo
    # WHAT IT DOES: Prints header with spacing
    # UX: Separates demos visually
    
    max_tokens_control()
    # WHY: Execute token limit demo
    # WHAT IT DOES: Shows short vs long responses
    # DEMONSTRATES: Length control
    
    print("\n3. Top-p Sampling")
    # WHY: Label the top-p demo
    # WHAT IT DOES: Prints header
    # INDICATES: Nucleus sampling test
    
    top_p_sampling()
    # WHY: Execute top-p comparison demo
    # WHAT IT DOES: Shows focused vs diverse sampling
    # DEMONSTRATES: Diversity control
    
    print("\n4. Combined Settings")
    # WHY: Label the combined demo
    # WHAT IT DOES: Prints header
    # INDICATES: Multiple parameters together
    
    combined_settings()
    # WHY: Execute combined configuration demo
    # WHAT IT DOES: Shows balanced parameter usage
    # DEMONSTRATES: Real-world configuration
```

---

## 🔄 Code Workflow Diagram

```
┌────────────────────────────────────────────────────────────────────┐
│                        START PROGRAM                                │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  1. IMPORT & CONFIGURE                                              │
│     ├─ Import: os, dotenv, genai                                   │
│     ├─ Load .env file                                              │
│     └─ Configure API key                                           │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  2. DEFINE CONFIGURATION FUNCTIONS                                  │
│     ├─ temperature_control()                                       │
│     ├─ max_tokens_control()                                        │
│     ├─ top_p_sampling()                                            │
│     └─ combined_settings()                                         │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  3. DEMO 1: Temperature Control                                     │
│     │                                                               │
│     ├─ Prompt: "Complete: The future of AI is..."                  │
│     │                                                               │
│     ├─ LOW TEMPERATURE (0.1):                                      │
│     │   │                                                           │
│     │   ├─ Create model with temp=0.1                              │
│     │   │                                                           │
│     │   ├─ Token Selection Process:                                │
│     │   │   ┌─────────────────────────────────────┐                │
│     │   │   │ Possible next tokens:               │                │
│     │   │   │ "promising" → 80% probability ✓     │                │
│     │   │   │ "bright"    → 15% probability       │                │
│     │   │   │ "uncertain" → 3% probability        │                │
│     │   │   │ "purple"    → 2% probability        │                │
│     │   │   │                                     │                │
│     │   │   │ Low temp: Always picks "promising"  │                │
│     │   │   │ (highest probability)               │                │
│     │   │   └─────────────────────────────────────┘                │
│     │   │                                                           │
│     │   └─ Output: "promising, with continued advances..."         │
│     │       └─ CONSISTENT (run again = same result)                │
│     │                                                               │
│     ├─ HIGH TEMPERATURE (1.5):                                     │
│     │   │                                                           │
│     │   ├─ Create model with temp=1.5                              │
│     │   │                                                           │
│     │   ├─ Token Selection Process:                                │
│     │   │   ┌─────────────────────────────────────┐                │
│     │   │   │ Same token probabilities:           │                │
│     │   │   │ "promising" → 80%  ← Maybe         │                │
│     │   │   │ "bright"    → 15%  ← Maybe         │                │
│     │   │   │ "uncertain" → 3%   ← Possible!     │                │
│     │   │   │ "purple"    → 2%   ← Even this!    │                │
│     │   │   │                                     │                │
│     │   │   │ High temp: Explores lower probs     │                │
│     │   │   │ (more randomness)                   │                │
│     │   │   └─────────────────────────────────────┘                │
│     │   │                                                           │
│     │   └─ Output: "uncertain yet fascinating, unfolding..."       │
│     │       └─ VARIABLE (run again = different result)             │
│     │                                                               │
│     └─ Temperature Scale:                                          │
│         ┌─────────────────────────────────────────────┐            │
│         │ 0.0 ════════════════════════════════ 2.0   │            │
│         │  ↑                    ↑              ↑     │            │
│         │  │                    │              │     │            │
│         │ Deterministic    Balanced      Chaotic     │            │
│         │ (facts, code)    (general)   (creative)    │            │
│         │                                            │            │
│         │ 0.1: Almost no randomness                  │            │
│         │ 0.7: Good balance (recommended)            │            │
│         │ 1.5: High creativity (can be nonsensical) │            │
│         └─────────────────────────────────────────────┘            │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  4. DEMO 2: Max Tokens Control                                      │
│     │                                                               │
│     ├─ Prompt: "Explain quantum computing"                         │
│     │                                                               │
│     ├─ SHORT (50 tokens):                                          │
│     │   │                                                           │
│     │   ├─ Model config: max_output_tokens=50                      │
│     │   │                                                           │
│     │   ├─ Generation Process:                                     │
│     │   │   Token 1: "Quantum"                                     │
│     │   │   Token 2: "computing"                                   │
│     │   │   Token 3: "uses"                                        │
│     │   │   ...                                                    │
│     │   │   Token 48: "information"                                │
│     │   │   Token 49: "processing"                                 │
│     │   │   Token 50: "." → STOP! ✋ (limit reached)               │
│     │   │                                                           │
│     │   └─ Output: "Quantum computing uses quantum mechanics       │
│     │       principles like superposition and entanglement..."     │
│     │       └─ ~200 characters, brief explanation                  │
│     │                                                               │
│     ├─ LONG (200 tokens):                                          │
│     │   │                                                           │
│     │   ├─ Model config: max_output_tokens=200                     │
│     │   │                                                           │
│     │   ├─ Generation continues to 200 tokens                      │
│     │   │                                                           │
│     │   └─ Output: "Quantum computing uses quantum mechanics...    │
│     │       Unlike classical computers that use bits... Qubits     │
│     │       can exist in superposition... This enables parallel    │
│     │       processing... Applications include cryptography..."    │
│     │       └─ ~800 characters, detailed explanation               │
│     │                                                               │
│     └─ Token Length Comparison:                                    │
│         ┌──────────────────────────────────────────┐               │
│         │ 50 tokens  ████ (~2-3 sentences)        │               │
│         │ 100 tokens ████████ (~5-6 sentences)    │               │
│         │ 200 tokens ████████████████ (~10-12)    │               │
│         │ 500 tokens ████████████████████████████ │               │
│         │                                         │               │
│         │ Rule of thumb: 1 token ≈ 4 characters   │               │
│         └──────────────────────────────────────────┘               │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  5. DEMO 3: Top-p Sampling (Nucleus Sampling)                       │
│     │                                                               │
│     ├─ Prompt: "Tell me an interesting fact"                       │
│     │                                                               │
│     ├─ FOCUSED (top_p=0.5):                                        │
│     │   │                                                           │
│     │   ├─ Model config: top_p=0.5                                 │
│     │   │                                                           │
│     │   ├─ Token Selection Process:                                │
│     │   │   ┌─────────────────────────────────────────┐            │
│     │   │   │ All possible tokens (sorted by prob):  │            │
│     │   │   │                                         │            │
│     │   │   │ Token A: 30% ✓ ┐                       │            │
│     │   │   │ Token B: 15% ✓ │ Sum = 50%             │            │
│     │   │   │ Token C: 5%  ✓ ┘ (top-p threshold)     │            │
│     │   │   │ Token D: 3%  ✗ (below threshold)       │            │
│     │   │   │ Token E: 2%  ✗                          │            │
│     │   │   │ ...more...                              │            │
│     │   │   │                                         │            │
│     │   │   │ Only A, B, C considered for selection   │            │
│     │   │   └─────────────────────────────────────────┘            │
│     │   │                                                           │
│     │   └─ Output: "The human brain contains approximately         │
│     │       86 billion neurons." (common fact)                     │
│     │                                                               │
│     ├─ DIVERSE (top_p=0.95):                                       │
│     │   │                                                           │
│     │   ├─ Model config: top_p=0.95                                │
│     │   │                                                           │
│     │   ├─ Token Selection Process:                                │
│     │   │   ┌─────────────────────────────────────────┐            │
│     │   │   │ All possible tokens:                    │            │
│     │   │   │                                         │            │
│     │   │   │ Token A: 30% ✓ ┐                       │            │
│     │   │   │ Token B: 15% ✓ │                       │            │
│     │   │   │ Token C: 5%  ✓ │                       │            │
│     │   │   │ Token D: 3%  ✓ │ Sum = 95%             │            │
│     │   │   │ Token E: 2%  ✓ │ (top-p threshold)     │            │
│     │   │   │ ...many more ✓ ┘                       │            │
│     │   │   │ Token Z: 0.1% ✗ (below threshold)      │            │
│     │   │   │                                         │            │
│     │   │   │ Many tokens considered for selection    │            │
│     │   │   └─────────────────────────────────────────┘            │
│     │   │                                                           │
│     │   └─ Output: "Octopuses have three hearts and blue           │
│     │       blood." (less common, more interesting)                │
│     │                                                               │
│     └─ Top-p Scale:                                                │
│         ┌──────────────────────────────────────────┐               │
│         │ 0.0 ════════════════════════════════ 1.0 │               │
│         │  ↑            ↑            ↑         ↑   │               │
│         │ Impossible  Very       Balanced   Almost │               │
│         │           Focused                   All  │               │
│         │                                          │               │
│         │ 0.5: Only top 50% prob mass (safe)      │               │
│         │ 0.9: Top 90% prob mass (recommended)    │               │
│         │ 0.95: Top 95% prob mass (diverse)       │               │
│         └──────────────────────────────────────────┘               │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  6. DEMO 4: Combined Settings                                       │
│     │                                                               │
│     ├─ Configuration Dictionary:                                   │
│     │   {                                                           │
│     │     'temperature': 0.7,      ← Moderate creativity           │
│     │     'max_output_tokens': 100, ← Medium length                │
│     │     'top_p': 0.9              ← Good diversity               │
│     │   }                                                           │
│     │                                                               │
│     ├─ Prompt: "Write a creative tagline for an AI company"        │
│     │                                                               │
│     ├─ How Parameters Work Together:                               │
│     │   │                                                           │
│     │   ├─ Step 1: Top-p filters tokens (top 90% mass)             │
│     │   │   └─ Removes very unlikely words                         │
│     │   │                                                           │
│     │   ├─ Step 2: Temperature adjusts probabilities               │
│     │   │   └─ Moderate randomness within filtered set             │
│     │   │                                                           │
│     │   ├─ Step 3: Generate tokens one by one                      │
│     │   │   └─ "Empowering" "tomorrow," "today."                   │
│     │   │                                                           │
│     │   └─ Step 4: Stop at max_output_tokens (100)                 │
│     │       └─ Or natural completion, whichever first              │
│     │                                                               │
│     └─ Output: "Empowering tomorrow, today: Where human            │
│         imagination meets artificial intelligence to create         │
│         infinite possibilities."                                    │
│         └─ Creative ✓, Concise ✓, Quality ✓                        │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│                     PROGRAM COMPLETE ✅                             │
│  All configuration demonstrations complete!                         │
│  - Temperature: Controls randomness/creativity                      │
│  - Max tokens: Controls response length                             │
│  - Top-p: Controls diversity via probability filtering              │
│  - Combined: Balanced configuration for real use                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Sample Output

### ✅ Complete Successful Execution

```
1. Temperature Control
Low temperature (0.1) - Deterministic:
promising, with continued advances in machine learning, natural language processing, and responsible AI development transforming industries and society.

High temperature (1.5) - Creative:
uncertain yet endlessly fascinating, a kaleidoscope of potential where silicon dreams dance with quantum whispers, perhaps transcending our wildest imaginings or maybe just making really good pizza recommendations.

2. Max Tokens Control
Short response (50 tokens):
Quantum computing uses quantum mechanics principles like superposition and entanglement to process information. Unlike classical computers using bits (0 or 1), quantum computers use qubits that can be both simultaneously, enabling parallel processing for complex problems.

Longer response (200 tokens):
Quantum computing uses quantum mechanics principles to process information in fundamentally different ways than classical computers. While traditional computers use bits representing either 0 or 1, quantum computers use quantum bits (qubits) that can exist in superposition—simultaneously representing 0 and 1. This property, along with quantum entanglement (where qubits become correlated), allows quantum computers to perform many calculations in parallel. Quantum computing shows promise for solving complex problems in cryptography, drug discovery, financial modeling, and optimization tasks that would take classical computers impractically long times. However, qubits are fragile and require extreme conditions like near-absolute zero temperatures. Current quantum computers are still limited in size and error-prone, but ongoing research continues advancing this revolutionary technology.

3. Top-p Sampling
Top-p = 0.5 (focused):
The human brain contains approximately 86 billion neurons, each capable of forming thousands of connections with other neurons, creating an incredibly complex network that enables thought, memory, and consciousness.

Top-p = 0.95 (diverse):
Octopuses have three hearts: two pump blood to the gills, while the third pumps it to the rest of the body. Even more fascinating, when an octopus swims, the heart that delivers blood to the body actually stops beating!

4. Combined Settings
Response: Empowering tomorrow, today: Where human imagination meets artificial intelligence to create infinite possibilities for a smarter, more connected world.
```

---

## 🎯 Key Concepts Explained

### 1. **Temperature: Randomness Control**

```python
# Temperature affects token probability distribution

# Low temperature (0.1)
# Probabilities: [80%, 15%, 3%, 2%]
# After temp: [95%, 4%, 0.5%, 0.5%] ← More peaked
# Effect: Almost always picks highest probability

# High temperature (1.5)
# Probabilities: [80%, 15%, 3%, 2%]
# After temp: [40%, 25%, 20%, 15%] ← More flattened
# Effect: More likely to pick lower probability options
```

**Use Cases:**
- **0.0-0.3:** Code generation, factual answers, consistency needed
- **0.4-0.7:** General purpose, balanced creativity
- **0.8-1.0:** Creative writing, brainstorming
- **1.0+:** Experimental, very creative (can be nonsensical)

### 2. **Max Output Tokens: Length Control**

```python
# Token counting examples
"Hello" = 1 token
"Hello, world!" = 4 tokens
"The quick brown fox" = 4 tokens

# Rough conversion: 1 token ≈ 4 characters (English)

# Setting limits
max_output_tokens=50   # ~200 chars, 2-3 sentences
max_output_tokens=100  # ~400 chars, 5-6 sentences
max_output_tokens=500  # ~2000 chars, paragraph
max_output_tokens=2000 # ~8000 chars, article
```

**Use Cases:**
- **50-100:** Short answers, UI constraints, cost control
- **100-300:** Standard responses, chatbot replies
- **500-1000:** Detailed explanations, articles
- **1000+:** Long-form content, documentation

### 3. **Top-p (Nucleus Sampling): Diversity Control**

```python
# How top-p works:
# 1. Sort all possible tokens by probability
# 2. Sum probabilities until reaching top_p threshold
# 3. Only sample from those tokens

# Example with top_p=0.8:
tokens = [
    ("the", 0.5),    # Cumulative: 0.5 ✓
    ("a", 0.2),      # Cumulative: 0.7 ✓
    ("this", 0.15),  # Cumulative: 0.85 ✗ (exceeds 0.8)
    ("that", 0.1),   # Not considered
    # ... rest ignored
]
# Only "the" and "a" considered for selection
```

**Use Cases:**
- **0.5-0.7:** Focused, consistent output
- **0.8-0.9:** Balanced quality and diversity (recommended)
- **0.9-0.95:** More creative, diverse responses
- **0.95-1.0:** Maximum diversity (can be unpredictable)

### 4. **Temperature vs Top-p**

```python
# Often used together!

# Temperature: Adjusts probability distribution
# Top-p: Filters which tokens can be selected

# Recommended combinations:
config_creative = {'temperature': 0.9, 'top_p': 0.95}
config_balanced = {'temperature': 0.7, 'top_p': 0.9}
config_focused = {'temperature': 0.3, 'top_p': 0.8}
config_deterministic = {'temperature': 0.1, 'top_p': 0.5}
```

---

## 🚀 What Happens Behind the Scenes

### Token Generation Process with Configuration:

```
1. MODEL RECEIVES PROMPT
   "Complete: The future of AI is"

2. PREDICT NEXT TOKEN PROBABILITIES
   All possible tokens:
   "promising" → 0.35
   "bright"    → 0.20
   "uncertain" → 0.10
   "exciting"  → 0.08
   ... (thousands more)

3. APPLY TOP-P FILTER (if set)
   top_p=0.8
   ├─ "promising" 0.35 (cumulative: 0.35) ✓
   ├─ "bright"    0.20 (cumulative: 0.55) ✓
   ├─ "uncertain" 0.10 (cumulative: 0.65) ✓
   ├─ "exciting"  0.08 (cumulative: 0.73) ✓
   └─ Next token 0.07 (cumulative: 0.80) → STOP
   
   Remaining tokens considered: 5

4. APPLY TEMPERATURE
   temperature=0.7
   ├─ Adjusts probabilities
   └─ "promising": 0.35 → 0.40 (slightly increased)

5. SAMPLE TOKEN
   Select one token based on adjusted probabilities
   Selected: "promising"

6. CHECK MAX_TOKENS
   Current tokens: 8
   max_output_tokens: 100
   ├─ Continue? YES (8 < 100)
   └─ Add "promising" to output

7. REPEAT STEPS 2-6
   Until:
   - Reach max_output_tokens, OR
   - Generate stop token (natural end), OR
   - Hit context limit
```

---

## 📝 Common Use Cases

### Use Case 1: Code Generation (Deterministic)
```python
def generate_code():
    config = {
        'temperature': 0.1,     # Very consistent
        'max_output_tokens': 500,
        'top_p': 0.5            # Safe choices only
    }
    model = genai.GenerativeModel('gemini-2.0-flash', generation_config=config)
    response = model.generate_content("Write a Python function to sort a list")
    return response.text
```

### Use Case 2: Creative Writing (High Creativity)
```python
def creative_story():
    config = {
        'temperature': 0.9,     # Very creative
        'max_output_tokens': 1000,
        'top_p': 0.95           # Maximum diversity
    }
    model = genai.GenerativeModel('gemini-2.0-flash', generation_config=config)
    response = model.generate_content("Write a sci-fi short story about AI")
    return response.text
```

### Use Case 3: Chatbot (Balanced)
```python
def chatbot_response(message):
    config = {
        'temperature': 0.7,     # Friendly variety
        'max_output_tokens': 150,  # Concise replies
        'top_p': 0.9            # Good quality
    }
    model = genai.GenerativeModel('gemini-2.0-flash', generation_config=config)
    response = model.generate_content(message)
    return response.text
```

### Use Case 4: Summaries (Short & Focused)
```python
def summarize_text(text):
    config = {
        'temperature': 0.3,     # Consistent summaries
        'max_output_tokens': 100,  # Brief output
        'top_p': 0.8            # Focused
    }
    model = genai.GenerativeModel('gemini-2.0-flash', generation_config=config)
    response = model.generate_content(f"Summarize: {text}")
    return response.text
```

---

## 💡 Best Practices

### 1. **Start with Defaults, Then Tune**
```python
# Start simple
model = genai.GenerativeModel('gemini-2.0-flash')

# Test output quality
# Then adjust if needed

# If too random → lower temperature
# If too repetitive → raise temperature
# If too long → add max_output_tokens
# If too generic → raise top_p
```

### 2. **Don't Set Extreme Values**
```python
# BAD: Too extreme
config = {'temperature': 2.0, 'top_p': 1.0}  # Nonsense
config = {'temperature': 0.0, 'top_p': 0.1}  # Too rigid

# GOOD: Reasonable ranges
config = {'temperature': 0.7, 'top_p': 0.9}  # Balanced
```

### 3. **Consider Use Case**
```python
# Different tasks need different configs
configs = {
    'factual': {'temperature': 0.2, 'top_p': 0.7},
    'creative': {'temperature': 0.9, 'top_p': 0.95},
    'code': {'temperature': 0.1, 'top_p': 0.5},
    'chat': {'temperature': 0.7, 'top_p': 0.9}
}
```

### 4. **Monitor Token Usage**
```python
# Check token count for cost control
response = model.generate_content(prompt)
# Note: Actual token count available in response metadata
print(f"Tokens used: {response.usage_metadata.total_token_count}")
```

---

## ⚠️ Important Notes

1. **Default Values:** If not specified, Gemini uses sensible defaults
2. **Temperature Range:** 0.0-2.0 (stick to 0.0-1.0 for quality)
3. **Top-p Range:** 0.0-1.0 (0.9 is common default)
4. **Max Tokens:** Response can be shorter than limit (natural ending)
5. **Token Counting:** Approximate (4 chars ≈ 1 token for English)
6. **Configuration Scope:** Settings apply per model instance
7. **Cost Impact:** More tokens = higher cost
8. **Quality vs Creativity:** Always a tradeoff

---

## 🔧 Advanced: Configuration Comparison Table

| Use Case | Temperature | Max Tokens | Top-p | Why |
|----------|-------------|------------|-------|-----|
| **Code Generation** | 0.1-0.2 | 500-1000 | 0.5-0.7 | Need consistency, correctness |
| **Factual Q&A** | 0.2-0.4 | 100-300 | 0.7-0.8 | Accurate, focused answers |
| **Chatbot** | 0.6-0.8 | 100-200 | 0.9 | Natural, varied responses |
| **Creative Writing** | 0.8-1.0 | 1000+ | 0.95 | Maximum creativity, diversity |
| **Summaries** | 0.3-0.5 | 50-150 | 0.8 | Consistent, concise output |
| **Brainstorming** | 0.9-1.2 | 200-500 | 0.95 | Diverse ideas, unexpected |
| **Translation** | 0.3 | 500+ | 0.8 | Accurate, consistent |
| **Classification** | 0.1 | 10-50 | 0.5 | Deterministic labels |

---

## 🔗 Prerequisites

1. ✅ Completed previous lessons (01-06)
2. ✅ Understanding of probability concepts (helpful)
3. ✅ Basic understanding of token-based language models

---

## 🎓 Learning Outcomes

After understanding this code, you should know:

- ✅ How temperature controls randomness and creativity
- ✅ How max_output_tokens limits response length
- ✅ How top-p sampling filters token selection
- ✅ When to use different configuration settings
- ✅ How to combine parameters for specific use cases
- ✅ The tradeoffs between quality, creativity, and cost
- ✅ How to tune configurations for your application
- ✅ Best practices for different content types

---

## 🔜 Next Steps

1. Move to `08_system_instructions.py` to learn about system prompts
2. Experiment with different temperature values for your use case
3. Build a configuration selector based on task type
4. Create A/B tests comparing different settings
5. Monitor token usage to optimize costs

---

**⚙️ Excellent!** You now understand how to fine-tune AI behavior through configuration parameters!
