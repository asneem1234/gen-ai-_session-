# Module 07 - Model Configurations - Detailed Code Explanation

This document explains every line of code in the Model Configurations module, with in-depth explanations of generation parameters and how they control AI output.

---

## 📊 Visual Overview: Generation Parameters

```
┌─────────────────────────────────────────────────────────────────┐
│           GENERATION PARAMETERS = AI OUTPUT CONTROLS            │
└─────────────────────────────────────────────────────────────────┘

Think of it like adjusting controls on a machine:

Default Settings:             Custom Settings:
┌──────────────┐             ┌──────────────┐
│ Temperature  │             │ Temperature  │
│     1.0      │             │     0.2      │ ← More predictable
├──────────────┤             ├──────────────┤
│   Top-P      │             │   Top-P      │
│     0.95     │             │     0.8      │ ← More focused
├──────────────┤             ├──────────────┤
│  Max Tokens  │             │  Max Tokens  │
│    2048      │             │     100      │ ← Shorter output
└──────────────┘             └──────────────┘
       ↓                            ↓
Creative, varied             Consistent, precise
responses                    responses


HOW IT AFFECTS OUTPUT:
──────────────────────

Same Prompt: "Complete: The future of AI is..."

High Temperature (1.5):           Low Temperature (0.1):
┌────────────────────────┐       ┌────────────────────────┐
│ "The future of AI is   │       │ "The future of AI is   │
│  absolutely mind-      │       │  expected to continue  │
│  blowing! Imagine      │       │  advancing in areas    │
│  sentient robots,      │       │  such as natural       │
│  flying cars, and      │       │  language processing   │
│  telepathic devices!"  │       │  and computer vision." │
└────────────────────────┘       └────────────────────────┘
      Creative ✨                      Predictable 📊
      Varied                           Consistent
      Risky                            Safe
```

---

## 🌡️ Temperature Parameter Deep Dive

```
WHAT IS TEMPERATURE?
────────────────────

Temperature controls randomness in token selection.

How AI Chooses Next Word:
┌─────────────────────────────────────────────┐
│ Prompt: "The cat is very"                   │
│                                             │
│ AI's internal probabilities:                │
│ ┌──────────┬─────────┐                     │
│ │ Word     │ Prob %  │                     │
│ ├──────────┼─────────┤                     │
│ │ cute     │  45%    │ ████████           │
│ │ playful  │  25%    │ █████              │
│ │ fluffy   │  15%    │ ███                │
│ │ hungry   │  10%    │ ██                 │
│ │ loud     │   5%    │ █                  │
│ └──────────┴─────────┘                     │
└─────────────────────────────────────────────┘


TEMPERATURE = 0.0 (Deterministic):
──────────────────────────────────

Always picks highest probability:
┌──────────┬─────────┬────────┐
│ Word     │ Prob %  │ Pick?  │
├──────────┼─────────┼────────┤
│ cute     │  99%    │   ✅   │ ← Always this one
│ playful  │   1%    │   ❌   │
│ fluffy   │   0%    │   ❌   │
└──────────┴─────────┴────────┘

Output (every time): "The cat is very cute"
Use case: Factual answers, consistency


TEMPERATURE = 0.7 (Balanced):
──────────────────────────────

Weighted random selection:
┌──────────┬─────────┬────────┐
│ Word     │ Prob %  │ Pick?  │
├──────────┼─────────┼────────┤
│ cute     │  45%    │ Maybe  │ ← Often
│ playful  │  25%    │ Maybe  │ ← Sometimes
│ fluffy   │  15%    │ Maybe  │ ← Rarely
│ hungry   │  10%    │ Maybe  │ ← Very rarely
│ loud     │   5%    │ Maybe  │ ← Almost never
└──────────┴─────────┴────────┘

Output (varies):
- "The cat is very cute"
- "The cat is very playful"
- "The cat is very fluffy"
Use case: Natural conversation


TEMPERATURE = 2.0 (Creative/Random):
────────────────────────────────────

Nearly equal probabilities:
┌──────────┬─────────┬────────┐
│ Word     │ Prob %  │ Pick?  │
├──────────┼─────────┼────────┤
│ cute     │  25%    │ Equal  │ ← All have
│ playful  │  22%    │ chance │   similar
│ fluffy   │  20%    │        │   chance
│ hungry   │  18%    │        │
│ loud     │  15%    │        │
└──────────┴─────────┴────────┘

Output (unpredictable):
- "The cat is very philosophical"
- "The cat is very algebraic" 
- "The cat is very quantum"
Use case: Creative writing, brainstorming


VISUAL SCALE:
─────────────

Temperature:
0.0    0.5    1.0    1.5    2.0
│──────│──────│──────│──────│
│      │      │      │      │
Boring         Normal         Chaos
Repetitive     Balanced       Nonsense
Predictable    Creative       Random
Factual        Engaging       Wild
```

---

## 🎯 Top-P (Nucleus Sampling)

```
WHAT IS TOP-P?
──────────────

Top-P limits word choices to smallest set that adds up to P probability.

Example: Top-P = 0.9 (90%)

Word Probabilities:
┌──────────┬─────────┬───────────┐
│ Word     │ Prob %  │ Cumulative│
├──────────┼─────────┼───────────┤
│ happy    │  40%    │  40%      │ ✅ Include
│ joyful   │  30%    │  70%      │ ✅ Include
│ excited  │  20%    │  90%      │ ✅ Include (hits 90%)
│ thrilled │   5%    │  95%      │ ❌ Exclude
│ ecstatic │   3%    │  98%      │ ❌ Exclude
│ delighted│   2%    │ 100%      │ ❌ Exclude
└──────────┴─────────┴───────────┘
            ↑ Only choose from top 3 words


VISUALIZATION:
──────────────

Top-P = 0.5 (50%):
┌────────────────────────────┐
│ ████████████████ happy 45% │ ✅ 
│ ██████ sad 10%             │ ❌ Cutoff here (55% total)
│ ███ angry 5%               │ ❌
│ ██ confused 3%             │ ❌
└────────────────────────────┘
Only "happy" is considered!
Result: Very focused


Top-P = 0.95 (95%):
┌────────────────────────────┐
│ ████████████████ happy 45% │ ✅
│ ██████████ sad 20%         │ ✅
│ ██████ angry 15%           │ ✅
│ ████ confused 10%          │ ✅
│ ██ surprised 5%            │ ✅ (Total: 95%)
│ █ other 5%                 │ ❌
└────────────────────────────┘
Many options considered!
Result: More diverse


TOP-P vs TOP-K:
───────────────

Top-P (Dynamic):
  Adapts to probability distribution
  "Include words until 90% probability"
  
  High confidence: few words
  Low confidence: many words

Top-K (Fixed):
  Always considers K words
  "Always include top 40 words"
  
  Simple but inflexible
```

---

## 🏗️ Code Structure Map

```
07_model_configurations.py
│
├── 📦 IMPORTS
│   ├── os
│   ├── dotenv
│   └── google.generativeai
│
├── 🔧 SETUP
│   ├── load_dotenv()
│   └── genai.configure()
│
├── 🎯 FUNCTION 1: temperature_examples()
│   ├── Low (0.1) - Deterministic
│   ├── Medium (0.7) - Balanced
│   └── High (1.5) - Creative
│
├── 🎯 FUNCTION 2: top_p_examples()
│   ├── Low (0.5) - Focused
│   ├── Medium (0.8) - Moderate
│   └── High (0.95) - Diverse
│
├── 🎯 FUNCTION 3: top_k_examples()
│   ├── Low (10) - Limited choices
│   ├── Medium (40) - Balanced
│   └── High (100) - Many options
│
├── 🎯 FUNCTION 4: max_tokens_examples()
│   ├── Short (50 tokens)
│   ├── Medium (200 tokens)
│   └── Long (1000 tokens)
│
├── 🎯 FUNCTION 5: stop_sequences_examples()
│   ├── Stop at punctuation
│   ├── Stop at keyword
│   └── Multiple stop conditions
│
├── 🎯 FUNCTION 6: combined_configurations()
│   └── Mix multiple parameters
│
└── 🚀 MAIN MENU
    └── Interactive parameter testing
```

---

## 📏 Max Output Tokens

```
WHAT ARE TOKENS?
────────────────

Tokens ≈ Words (rough approximation)
- 1 token ≈ 0.75 words (English)
- "Hello world" = 2 tokens
- "The quick brown fox" = 4 tokens

Token counting:
┌────────────────────────────────────┐
│ Text: "AI is amazing!"             │
│ Tokens: ["AI", " is", " amazing", "!"]│
│ Count: 4 tokens                    │
└────────────────────────────────────┘


MAX_OUTPUT_TOKENS EXAMPLES:
───────────────────────────

Prompt: "Write about dogs"

max_output_tokens = 20:
┌──────────────────────────────┐
│ "Dogs are loyal companions   │
│  that bring joy to families  │
│  around the world."          │ ← Stops here (20 tokens)
└──────────────────────────────┘
Use: Short answers, summaries


max_output_tokens = 100:
┌──────────────────────────────┐
│ "Dogs are loyal companions   │
│  that bring joy to families  │
│  around the world. They come │
│  in many breeds, from tiny   │
│  Chihuahuas to large Great   │
│  Danes. Dogs require daily   │
│  exercise, proper nutrition, │
│  and regular vet visits..."  │ ← Stops here (100 tokens)
└──────────────────────────────┘
Use: Paragraphs, explanations


max_output_tokens = 1000:
┌──────────────────────────────┐
│ [Full essay about dogs       │
│  with introduction, body     │
│  paragraphs, examples,       │
│  and conclusion]             │
│                              │
│ (Multiple paragraphs)        │
└──────────────────────────────┘
Use: Articles, detailed content


COST IMPLICATIONS:
──────────────────

Higher tokens = Higher cost!

┌──────────┬────────┬─────────┐
│ Tokens   │ Cost   │ Use Case│
├──────────┼────────┼─────────┤
│ 50       │ $0.001 │ Quick Q&A│
│ 200      │ $0.004 │ Paragraph│
│ 1000     │ $0.020 │ Article │
│ 4000     │ $0.080 │ Essay   │
└──────────┴────────┴─────────┘

⚠️ Set appropriate limits!
```

---

## 🎨 Parameter Combinations for Different Use Cases

```
USE CASE MATRIX:
────────────────

1. FACTUAL Q&A (e.g., "What is Python?")
┌─────────────────────────────────────┐
│ temperature: 0.1   (Consistent)     │
│ top_p: 0.8         (Focused)        │
│ max_tokens: 200    (Concise)        │
└─────────────────────────────────────┘
Goal: Accurate, reliable answers


2. CREATIVE WRITING (e.g., "Write a story")
┌─────────────────────────────────────┐
│ temperature: 1.2   (Creative)       │
│ top_p: 0.95        (Diverse)        │
│ max_tokens: 1000   (Detailed)       │
└─────────────────────────────────────┘
Goal: Original, engaging content


3. CODE GENERATION (e.g., "Write Python function")
┌─────────────────────────────────────┐
│ temperature: 0.2   (Predictable)    │
│ top_p: 0.85        (Focused)        │
│ max_tokens: 500    (Complete code)  │
└─────────────────────────────────────┘
Goal: Working, correct code


4. CASUAL CHAT (e.g., "How are you?")
┌─────────────────────────────────────┐
│ temperature: 0.7   (Natural)        │
│ top_p: 0.9         (Varied)         │
│ max_tokens: 150    (Brief)          │
└─────────────────────────────────────┘
Goal: Engaging conversation


5. BRAINSTORMING (e.g., "Give me ideas")
┌─────────────────────────────────────┐
│ temperature: 1.5   (Very creative)  │
│ top_p: 0.98        (Wide range)     │
│ max_tokens: 300    (Multiple ideas) │
└─────────────────────────────────────┘
Goal: Diverse, unexpected ideas


6. SUMMARIZATION (e.g., "Summarize this")
┌─────────────────────────────────────┐
│ temperature: 0.3   (Focused)        │
│ top_p: 0.85        (Key points)     │
│ max_tokens: 100    (Brief)          │
└─────────────────────────────────────┘
Goal: Concise, accurate summary
```

---

## ⚙️ Configuration Object Structure

```
PYTHON CONFIGURATION:
─────────────────────

Method 1: Dictionary
config = {
    'temperature': 0.7,
    'top_p': 0.9,
    'top_k': 40,
    'max_output_tokens': 200
}

model = genai.GenerativeModel(
    'gemini-2.0-flash',
    generation_config=config
)


Method 2: Direct Parameters
model = genai.GenerativeModel(
    'gemini-2.0-flash',
    generation_config={
        'temperature': 0.7,
        'top_p': 0.9
    }
)


VISUAL STRUCTURE:
─────────────────

┌─────────────────────────────────────┐
│ GenerativeModel                     │
│ ├── model_name: 'gemini-2.0-flash' │
│ └── generation_config:              │
│     ├── temperature: 0.7            │
│     ├── top_p: 0.9                  │
│     ├── top_k: 40                   │
│     ├── max_output_tokens: 200      │
│     ├── stop_sequences: [...]       │
│     └── candidate_count: 1          │
└─────────────────────────────────────┘


AVAILABLE PARAMETERS:
─────────────────────

┌────────────────────┬──────────┬─────────────┐
│ Parameter          │ Range    │ Default     │
├────────────────────┼──────────┼─────────────┤
│ temperature        │ 0.0-2.0  │ 1.0         │
│ top_p              │ 0.0-1.0  │ 0.95        │
│ top_k              │ 1-100+   │ 40          │
│ max_output_tokens  │ 1-8192   │ 2048        │
│ stop_sequences     │ list     │ []          │
│ candidate_count    │ 1-8      │ 1           │
└────────────────────┴──────────┴─────────────┘
```

---

## 🔄 Parameter Interaction Effects

```
TEMPERATURE + TOP-P INTERACTION:
────────────────────────────────

Both Low (temp=0.1, top_p=0.5):
┌────────────────────────────────┐
│ Effect: VERY CONSISTENT        │
│ - Same output every time       │
│ - Predictable                  │
│ - Safe for production          │
└────────────────────────────────┘

Both High (temp=1.5, top_p=0.98):
┌────────────────────────────────┐
│ Effect: VERY CREATIVE          │
│ - Highly varied output         │
│ - Unpredictable                │
│ - Risk of nonsense             │
└────────────────────────────────┘

Mixed (temp=0.2, top_p=0.95):
┌────────────────────────────────┐
│ Effect: CONTROLLED VARIETY     │
│ - Mostly consistent            │
│ - Some variation               │
│ - Balanced approach            │
└────────────────────────────────┘


TOKENS + TEMPERATURE:
─────────────────────

Short + High Temp:
"Write a story (max 20 tokens, temp=1.5)"
→ "Alien robots danced quantum..." 
   (Creative but incomplete)

Long + Low Temp:
"Write a story (max 500 tokens, temp=0.2)"
→ Detailed, coherent, complete story
   (Predictable but thorough)


RECOMMENDATION MATRIX:
──────────────────────

         │ Short Output │ Long Output │
─────────┼──────────────┼─────────────┤
Low Temp │ Quick facts  │ Documentation│
         │ (Good)       │ (Good)      │
─────────┼──────────────┼─────────────┤
High Temp│ Random ideas │ Creative    │
         │ (Risky)      │ stories     │
         │              │ (Good)      │
```

---

## Module Documentation Block

```python
"""
07 - Model Configurations
==========================
```
**Explanation:** Module about generation parameters - the "knobs" that control HOW AI generates text.

```python
This module demonstrates generation parameters and how they affect AI output.
Students will learn:
- Temperature control (creativity vs consistency)
- Top-P (nucleus sampling)
- Top-K sampling
- Max output tokens
- Stop sequences
- How to choose parameters for different use cases
```
**Explanation:** Learning objectives. These parameters are CRITICAL - same prompt with different parameters produces wildly different outputs.

```python
Teaching Points:
- Generation parameters dramatically affect output
- Different tasks need different settings
- Experimentation is key
- Trade-offs between creativity and reliability
"""
```
**Explanation:** **KEY INSIGHT**: There's no "best" settings - it's about matching parameters to your use case. Factual Q&A needs different settings than creative writing.

---

## Import Statements

```python
import os
```
**Explanation:** File/directory operations.

```python
from dotenv import load_dotenv
```
**Explanation:** Environment variables for API keys.

```python
import google.generativeai as genai
```
**Explanation:** Google's Generative AI SDK.

```python
# Setup
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
```
**Explanation:** Standard initialization.

---

## Section 1: Generation Parameters Overview

```python
# ============================================================================
# SECTION 1: Understanding Generation Parameters
# ============================================================================
```
**Explanation:** Educational overview of all parameters.

```python
def generation_parameters_overview():
    """
    Explain all generation parameters
    """
```
**Explanation:** Conceptual foundation - explains what each parameter does.

```python
    print("\n" + "=" * 60)
    print("SECTION 1: Understanding Generation Parameters")
    print("=" * 60)
    
    overview = """
    🎛️ GENERATION PARAMETERS:
    
    These parameters control HOW the AI generates text.
    Think of them as "knobs" you can tune for different effects.
```
**Explanation:** **FUNDAMENTAL CONCEPT**: These parameters don't change WHAT the AI knows, but HOW it selects words from its knowledge.

```python
    1️⃣ TEMPERATURE (0.0 - 2.0)
    ===========================
    Controls randomness/creativity
```
**Explanation:** **MOST IMPORTANT PARAMETER**: Temperature controls the randomness of word selection.

```python
    Low (0.0 - 0.3): ❄️ Conservative
    • More focused and deterministic
    • Safer, more predictable outputs
    • Good for: Facts, code, structured data
    • Example: "2+2=" → Always "4"
```
**Explanation:** **LOW TEMPERATURE**: AI picks the most probable next word almost always. At 0.0, it's nearly deterministic (same input = same output). Perfect for facts where you want consistency.

```python
    Medium (0.4 - 0.9): 🌡️ Balanced
    • Natural variation
    • Good general-purpose setting
    • Good for: Chat, Q&A, explanations
    • Example: "Hello!" → Various greetings
```
**Explanation:** **MEDIUM TEMPERATURE**: Natural conversation range. Responses are consistent but not robotic. Default territory for most applications.

```python
    High (1.0 - 2.0): 🔥 Creative
    • Very diverse outputs
    • Can be unexpected/unusual
    • Good for: Creative writing, brainstorming
    • Example: "Once upon a time" → Wild stories
```
**Explanation:** **HIGH TEMPERATURE**: AI considers less probable words. Can produce surprising, creative, sometimes weird results. At 2.0, outputs can be nonsensical.

```python
    2️⃣ TOP-P / Nucleus Sampling (0.0 - 1.0)
    ========================================
    Controls diversity by probability mass
    
    How it works:
    • Model calculates probabilities for next token
    • Selects from smallest set that adds up to P
    • Higher P = more variety
```
**Explanation:** **TOP-P MECHANISM**: 
- AI calculates probability for each possible next word
- Sorts by probability (e.g., "the" 30%, "a" 20%, "an" 15%, etc.)
- Adds probabilities until reaching P (e.g., 0.9 = 90%)
- Samples only from that subset
- Example: If "the" (30%) + "a" (20%) + "an" (15%) + "this" (10%) + "that" (15%) = 90%, only consider those 5 words, ignore rest

```python
    Low (0.1 - 0.3):
    • Only most likely tokens
    • Very focused output
    
    Medium (0.4 - 0.8):
    • Balanced selection
    • Default: 0.95
    
    High (0.9 - 1.0):
    • Includes less likely options
    • Maximum diversity
```
**Explanation:** **TOP-P RANGES**: At 0.1, only considering top ~10% probability mass (very few words). At 0.95, considering words until they account for 95% of probability (many words).

```python
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
```
**Explanation:** **TOP-K VS TOP-P**: 
- **Top-K**: Fixed number of words (e.g., top 40 most probable)
- **Top-P**: Dynamic number based on cumulative probability
- Example: For "The cat ___", top-40 considers top 40 words. Top-p 0.9 might consider 20 words if top 20 account for 90% probability, or 60 words if they're more evenly distributed.

```python
    4️⃣ MAX OUTPUT TOKENS
    =====================
    Maximum length of generated response
    
    • 1 token ≈ 0.75 words (English)
    • Controls response length
    • Prevents overly long outputs
    • Default: 2048 for Gemini Pro
```
**Explanation:** **TOKENS VS WORDS**: Tokens are sub-word units. "tokenization" might be 3 tokens: ["token", "ization"]. Rough rule: 1 token ≈ 0.75 words for English.

```python
    Examples:
    • 50 tokens: ~37 words (short answer)
    • 500 tokens: ~375 words (paragraph)
    • 2048 tokens: ~1500 words (article)
```
**Explanation:** Practical examples for sizing. 50 tokens = a sentence or two. 2048 = a full article.

```python
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
```
**Explanation:** **STOP SEQUENCES**: Tell AI "stop generating when you hit this text". Useful for:
- Preventing overgeneration
- Structured formats (JSON, Markdown sections)
- Template completion (fill blanks, don't continue beyond)

```python
    📊 PARAMETER INTERACTIONS:
    
    Temperature + Top-P:
    • Often used together
    • Both affect diversity
    • Start with one, adjust other
```
**Explanation:** **INTERACTION**: Temperature and top-p both control randomness, but differently. Temperature adjusts the probability distribution (flattens peaks), top-p limits the selection pool. They work together - high temp with low top-p creates focused creativity.

```python
    Top-P vs Top-K:
    • Alternative approaches
    • Top-P usually preferred
    • Can use both together
    """
```
**Explanation:** **TOP-P VS TOP-K**: Modern systems prefer top-p (more adaptive). Can use both: "Consider top-40 words (top-k), then sample from top 90% of those (top-p)".

```python
    print(overview)
```
**Explanation:** Display all concepts.

---

## Section 2: Temperature Comparison

```python
# ============================================================================
# SECTION 2: Temperature Examples
# ============================================================================
```
**Explanation:** Practical demonstration of temperature effects.

```python
def temperature_comparison():
    """
    Compare different temperature settings
    """
```
**Explanation:** Shows how temperature changes output dramatically.

```python
    print("\n" + "=" * 60)
    print("SECTION 2: Temperature Comparison")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = "Complete this sentence: The future of artificial intelligence is"
```
**Explanation:** Open-ended prompt where creativity matters - perfect for showing temperature effects.

```python
    temperatures = [0.0, 0.5, 1.0, 1.5]
```
**Explanation:** Range from ultra-conservative (0.0) to highly creative (1.5).

```python
    print(f"\n📝 Prompt: '{prompt}'\n")
    print("🔬 Testing different temperatures:\n")
    print("=" * 60)
    
    for temp in temperatures:
        print(f"\n🌡️  TEMPERATURE: {temp}")
        print("-" * 60)
```
**Explanation:** Loop through temperatures to compare.

```python
        # Configure generation settings
        generation_config = genai.types.GenerationConfig(
            temperature=temp,
            max_output_tokens=100
        )
```
**Explanation:** **KEY OBJECT**: `GenerationConfig` is how we pass parameters. It's a configuration object with all available settings.

```python
        # Generate 3 responses to show variation
        for i in range(3):
            response = model.generate_content(
                prompt,
                generation_config=generation_config
            )
            print(f"\n  Response {i+1}: {response.text}")
```
**Explanation:** **CRITICAL**: Generate 3 times with SAME settings to show variation. At temp 0.0, all 3 should be similar/identical. At temp 1.5, all 3 should be quite different.

```python
        print()
        
        if temp == 0.0:
            print("  💡 Notice: Responses are very similar/identical")
        elif temp == 1.5:
            print("  💡 Notice: Responses are quite diverse and creative")
```
**Explanation:** Educational hints to help students see the pattern.

---

## Section 3: Top-P Examples

```python
# ============================================================================
# SECTION 3: Top-P (Nucleus Sampling)
# ============================================================================
```
**Explanation:** Demonstrating nucleus sampling.

```python
def top_p_examples():
    """
    Demonstrate top-p sampling
    """
```
**Explanation:** Shows how top-p affects word selection pool.

```python
    print("\n" + "=" * 60)
    print("SECTION 3: Top-P (Nucleus Sampling)")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = "Write a creative opening line for a science fiction story."
```
**Explanation:** Creative task where top-p effects are visible.

```python
    top_p_values = [0.1, 0.5, 0.95]
```
**Explanation:** Range from very restricted (0.1) to very diverse (0.95).

```python
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
```
**Explanation:** **IMPORTANT**: Keep temperature constant (0.9) to isolate top-p's effect. Scientific approach - change one variable at a time.

```python
        # Generate multiple responses
        for i in range(2):
            response = model.generate_content(
                prompt,
                generation_config=generation_config
            )
            print(f"\n  Response {i+1}:\n  {response.text}")
        
        print()
```
**Explanation:** Generate twice to show variation at each top-p level.

---

## Section 4: Top-K Examples

```python
# ============================================================================
# SECTION 4: Top-K Sampling
# ============================================================================
```
**Explanation:** Demonstrating fixed-number sampling.

```python
def top_k_examples():
    """
    Demonstrate top-k sampling
    """
```
**Explanation:** Shows how limiting to K words affects diversity.

```python
    print("\n" + "=" * 60)
    print("SECTION 4: Top-K Sampling")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = "Name a programming language: "
```
**Explanation:** Simple prompt where the variety of answers shows top-k's effect.

```python
    top_k_values = [1, 10, 40]
```
**Explanation:** 
- **top_k=1**: Only most probable word (always same answer)
- **top_k=10**: Choose from 10 most probable words
- **top_k=40**: Choose from 40 most probable words

```python
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
```
**Explanation:** Temperature 1.0 ensures randomness; top-k controls the pool size.

```python
        # Generate multiple responses to see variety
        responses = []
        for i in range(5):
            response = model.generate_content(
                prompt,
                generation_config=generation_config
            )
            responses.append(response.text.split()[0])  # Get first word
```
**Explanation:** Generate 5 times, extract first word (the programming language name). `.split()[0]` splits text by whitespace and gets first element.

```python
        print(f"  Responses: {responses}")
        print(f"  Unique answers: {len(set(responses))}")
```
**Explanation:** **CLEVER ANALYSIS**: Show all responses AND count unique ones. `set()` removes duplicates, so `len(set(...))` shows variety. Top-k=1 should give 1 unique answer (always same). Top-k=40 should give more variety.

---

## Section 5: Max Output Tokens

```python
# ============================================================================
# SECTION 5: Max Output Tokens
# ============================================================================
```
**Explanation:** Controlling response length.

```python
def max_tokens_examples():
    """
    Control response length with max tokens
    """
```
**Explanation:** Shows how token limits affect response length.

```python
    print("\n" + "=" * 60)
    print("SECTION 5: Max Output Tokens")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = "Explain what machine learning is."
```
**Explanation:** Topic that can be explained briefly or extensively - perfect for showing length control.

```python
    token_limits = [30, 100, 500]
```
**Explanation:** Range from very short (30 ≈ 22 words) to long (500 ≈ 375 words).

```python
    print(f"\n📝 Prompt: '{prompt}'\n")
    print("=" * 60)
    
    for max_tokens in token_limits:
        print(f"\n📏 MAX TOKENS: {max_tokens} (~{int(max_tokens * 0.75)} words)")
        print("-" * 60)
```
**Explanation:** Show estimated word count using 0.75 conversion ratio.

```python
        generation_config = genai.types.GenerationConfig(
            max_output_tokens=max_tokens,
            temperature=0.7
        )
        
        response = model.generate_content(
            prompt,
            generation_config=generation_config
        )
```
**Explanation:** Generate with different length limits.

```python
        response_text = response.text
        word_count = len(response_text.split())
```
**Explanation:** Count actual words. `.split()` splits on whitespace, `len()` counts elements.

```python
        print(response_text)
        print(f"\n  📊 Actual words: {word_count}")
        print()
```
**Explanation:** Show response and actual word count to verify token→word conversion.

---

## Section 6: Stop Sequences

```python
# ============================================================================
# SECTION 6: Stop Sequences
# ============================================================================
```
**Explanation:** Using stop sequences for control.

```python
def stop_sequences_examples():
    """
    Use stop sequences to control output
    """
```
**Explanation:** Shows how to make AI stop at specific points.

```python
    print("\n" + "=" * 60)
    print("SECTION 6: Stop Sequences")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    print("\n💡 Stop sequences tell the model when to stop generating")
    print("Useful for structured output and format control\n")
```
**Explanation:** **USE CASES**: 
- Stop at paragraph breaks
- Stop at section markers
- Stop when completing templates

```python
    # Example 1: Stop at line break
    print("1️⃣ Stop at double newline (paragraph boundary):")
    print("-" * 60)
    
    prompt1 = "Write about Python programming.\n\n"
```
**Explanation:** Prompt ends with `\n\n` to establish pattern, but we'll stop generation at first double newline.

```python
    generation_config1 = genai.types.GenerationConfig(
        stop_sequences=["\n\n"],
        max_output_tokens=200
    )
```
**Explanation:** **STOP_SEQUENCES**: List of strings that trigger stopping. When AI generates any of these strings, it stops immediately.

```python
    response1 = model.generate_content(
        prompt1,
        generation_config=generation_config1
    )
    
    print(response1.text)
    print("\n📌 Generation stopped at paragraph break")
```
**Explanation:** AI stops after first paragraph (when it would naturally write `\n\n`).

```python
    # Example 2: Stop at specific marker
    print("\n\n2️⃣ Stop at specific marker (###):")
    print("-" * 60)
    
    prompt2 = "List three programming languages:\n1."
```
**Explanation:** Started a list, AI will continue numbering.

```python
    generation_config2 = genai.types.GenerationConfig(
        stop_sequences=["###", "\n\n"],
        max_output_tokens=200
    )
```
**Explanation:** Multiple stop sequences: stop at "###" OR double newline. Whichever comes first.

```python
    response2 = model.generate_content(
        prompt2,
        generation_config=generation_config2
    )
    
    print(response2.text)
```
**Explanation:** AI completes the list and stops at natural paragraph break or if it generates "###".

---

## Section 7: Use Case Configurations

```python
# ============================================================================
# SECTION 7: Use Case Configurations
# ============================================================================
```
**Explanation:** Recommended settings for real applications.

```python
def use_case_configurations():
    """
    Recommended configurations for different use cases
    """
```
**Explanation:** **MOST PRACTICAL SECTION**: Shows proven configurations for common scenarios.

```python
    print("\n" + "=" * 60)
    print("SECTION 7: Use Case Configurations")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    use_cases = {
```
**Explanation:** Dictionary of use cases with their ideal configurations.

```python
        "Factual Q&A": {
            "config": genai.types.GenerationConfig(
                temperature=0.1,
                top_p=0.8,
                max_output_tokens=150
            ),
            "prompt": "What is the capital of France?",
            "rationale": "Low temperature for factual accuracy"
        },
```
**Explanation:** **FACTUAL Q&A**: 
- **Temp 0.1**: Very low for consistency (facts shouldn't vary)
- **Top_p 0.8**: Moderate pool (not too restrictive)
- **Max 150**: Short, direct answers
- Use when: User asks questions with definitive answers

```python
        "Creative Writing": {
            "config": genai.types.GenerationConfig(
                temperature=1.2,
                top_p=0.95,
                max_output_tokens=300
            ),
            "prompt": "Write a creative opening for a mystery novel.",
            "rationale": "High temperature for creativity and variety"
        },
```
**Explanation:** **CREATIVE WRITING**:
- **Temp 1.2**: High for unique, surprising outputs
- **Top_p 0.95**: Large pool for diverse word choices
- **Max 300**: Longer for story development
- Use when: Content should be unique and imaginative

```python
        "Code Generation": {
            "config": genai.types.GenerationConfig(
                temperature=0.2,
                top_p=0.85,
                max_output_tokens=500
            ),
            "prompt": "Write a Python function to calculate factorial.",
            "rationale": "Low temperature for correct, consistent code"
        },
```
**Explanation:** **CODE GENERATION**:
- **Temp 0.2**: Low for correct syntax (code must work)
- **Top_p 0.85**: Balanced (some variety in style, but reliable)
- **Max 500**: Enough for complete functions
- Use when: Generating code that must be functional

```python
        "Brainstorming": {
            "config": genai.types.GenerationConfig(
                temperature=1.0,
                top_p=0.9,
                max_output_tokens=200
            ),
            "prompt": "Generate 5 unique business ideas for a coffee shop.",
            "rationale": "Balanced for diverse but coherent ideas"
        },
```
**Explanation:** **BRAINSTORMING**:
- **Temp 1.0**: High-medium for variety
- **Top_p 0.9**: Good diversity
- **Max 200**: Multiple ideas, not too long
- Use when: Need multiple creative but sensible options

```python
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
```
**Explanation:** **CHAT/CONVERSATION**:
- **Temp 0.7**: Sweet spot for natural but not repetitive
- **Top_p 0.9**: Natural language variety
- **Max 250**: Conversational length
- Use when: Building chatbots

```python
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
```
**Explanation:** Display configuration details and reasoning.

```python
        print(f"\n📝 Example Prompt: '{settings['prompt']}'")
        print(f"\n🤖 Response:")
        print("-" * 60)
        
        response = model.generate_content(
            settings['prompt'],
            generation_config=config
        )
        
        print(response.text)
        print()
```
**Explanation:** **DEMONSTRATE**: Actually run each configuration to show real results. Students see theory in action.

---

## Section 8: Interactive Testing

```python
# ============================================================================
# SECTION 8: Interactive Parameter Testing
# ============================================================================
```
**Explanation:** Hands-on experimentation.

```python
def interactive_parameter_testing():
    """
    Let users experiment with parameters
    """
```
**Explanation:** Interactive playground for learning by doing.

```python
    print("\n" + "=" * 60)
    print("SECTION 8: Interactive Parameter Testing")
    print("=" * 60)
    print("\nExperiment with different parameter combinations!")
    print("Type 'quit' to exit\n")
    
    model = genai.GenerativeModel('gemini-pro')
    
    while True:
        print("=" * 60)
```
**Explanation:** Infinite loop for repeated experimentation.

```python
        # Get prompt
        prompt = input("\nEnter your prompt (or 'quit'): ").strip()
        if prompt.lower() in ['quit', 'exit', 'q']:
            break
        
        if not prompt:
            continue
```
**Explanation:** Get user prompt, allow quitting, skip empty inputs.

```python
        # Get parameters
        try:
            temp = float(input("Temperature (0.0-2.0, default 0.7): ").strip() or "0.7")
            top_p = float(input("Top-P (0.0-1.0, default 0.95): ").strip() or "0.95")
            max_tokens = int(input("Max tokens (default 200): ").strip() or "200")
```
**Explanation:** **INPUT WITH DEFAULTS**: `input(...).strip() or "0.7"` means if user hits Enter (empty string), use default. `.strip()` removes whitespace, empty string is falsy in Python, so `or` returns the default.

```python
            # Create configuration
            generation_config = genai.types.GenerationConfig(
                temperature=temp,
                top_p=top_p,
                max_output_tokens=max_tokens
            )
```
**Explanation:** Build config from user inputs.

```python
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
```
**Explanation:** Generate and display result with parameters used. Helps users learn what works.

```python
        except ValueError as e:
            print(f"⚠️  Invalid input: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
```
**Explanation:** Error handling for invalid inputs (non-numeric) or API failures.

---

## Section 9: Parameter Combinations

```python
# ============================================================================
# SECTION 9: Parameter Combinations
# ============================================================================
```
**Explanation:** Showing how parameters work together.

```python
def parameter_combinations():
    """
    Show how parameters work together
    """
```
**Explanation:** Demonstrates synergistic effects of multiple parameters.

```python
    print("\n" + "=" * 60)
    print("SECTION 9: Parameter Combinations")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = "The best thing about learning to code is"
```
**Explanation:** Open-ended prompt where different combinations show distinct effects.

```python
    combinations = [
        {
            "name": "Ultra Conservative",
            "config": genai.types.GenerationConfig(
                temperature=0.0,
                top_p=0.5,
                top_k=10
            )
        },
```
**Explanation:** **ULTRA CONSERVATIVE**: All parameters set for maximum focus. Temp 0.0 (deterministic) + low top_p (small pool) + low top_k (few options) = extremely predictable.

```python
        {
            "name": "Balanced & Reliable",
            "config": genai.types.GenerationConfig(
                temperature=0.7,
                top_p=0.9,
                top_k=40
            )
        },
```
**Explanation:** **BALANCED**: Default-like settings. Works well for most applications.

```python
        {
            "name": "Maximum Creativity",
            "config": genai.types.GenerationConfig(
                temperature=1.5,
                top_p=0.98,
                top_k=100
            )
        }
    ]
```
**Explanation:** **MAXIMUM CREATIVITY**: All parameters set for maximum diversity. High temp (random) + high top_p (large pool) + high top_k (many options) = very creative/unpredictable.

```python
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
```
**Explanation:** Generate with each combination to show how they interact.

---

## Section 10: Best Practices

```python
# ============================================================================
# SECTION 10: Best Practices
# ============================================================================
```
**Explanation:** Production guidelines.

```python
def configuration_best_practices():
    """
    Best practices for using generation parameters
    """
```
**Explanation:** Accumulated wisdom for real-world usage.

```python
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
```
**Explanation:** **START SIMPLE**: Don't over-optimize prematurely. Begin with defaults, measure results, then tune.

```python
    2. ADJUST ONE AT A TIME
       • Change temperature first
       • Then fine-tune top-p if needed
       • Easier to understand effects
```
**Explanation:** **SCIENTIFIC METHOD**: Change one variable at a time so you know what causes what. Temperature has biggest impact, start there.

```python
    3. TEST MULTIPLE TIMES
       • Parameters create variation
       • Run same prompt 3-5 times
       • Evaluate consistency
```
**Explanation:** **STATISTICAL VALIDITY**: Single run isn't enough. Parameters introduce randomness - need multiple samples to judge quality.

```python
    4. MATCH TO USE CASE
       • Facts/Code: Low temperature (0.0-0.3)
       • Chat: Medium temperature (0.5-0.9)
       • Creative: High temperature (1.0-1.5)
```
**Explanation:** **CONTEXT MATTERS**: No universal "best" settings. Match to your specific need.

```python
    5. SET APPROPRIATE LIMITS
       • Max tokens prevents runaway generation
       • Stop sequences for structured output
       • Balance cost vs quality
```
**Explanation:** **COST CONTROL**: Longer outputs cost more. Set limits to prevent unexpected bills.

```python
    ⚠️ COMMON MISTAKES:
    
    1. Temperature too high for facts
       • Results in hallucinations
       • Inconsistent answers
       • Use < 0.3 for factual content
```
**Explanation:** **CRITICAL ERROR**: High temperature on facts = AI makes up wrong answers confidently. "What's 2+2?" with temp 1.5 might say "5" because it's considering unlikely options.

```python
    2. Temperature too low for creativity
       • Repetitive outputs
       • Boring conversations
       • Use > 0.8 for creative tasks
```
**Explanation:** **BORING OUTPUTS**: Temp 0.0 for creative writing = all stories sound the same.

```python
    3. Ignoring token limits
       • Unexpected truncation
       • Incomplete responses
       • Set appropriate max_tokens
```
**Explanation:** **TRUNCATION ISSUES**: If response cuts off mid-sentence, you hit token limit. Always set max_tokens appropriately.

```python
    4. Not testing variations
       • Parameters affect each prompt differently
       • Always test before production
       • Monitor outputs over time
```
**Explanation:** **TEST IN PRODUCTION-LIKE CONDITIONS**: What works on test prompts might not work on real user inputs.

```python
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
```
**Explanation:** **CHEAT SHEET**: Copy-paste ready configurations for common tasks. Starting point for your tuning.

```python
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
```
**Explanation:** Advanced tips from production experience.

```python
    print(practices)
```
**Explanation:** Display all best practices.

---

## Main Function

```python
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
```
**Explanation:** Standard main setup.

```python
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
```
**Explanation:** Menu with 10 sections.

```python
    while True:
        print(menu)
        choice = input("Your choice: ").strip().lower()
        
        if choice in ['quit', 'q', 'exit']:
            print("👋 Goodbye!")
            break
        elif choice == '1':
            generation_parameters_overview()
        # ... [rest of choices] ...
```
**Explanation:** Standard menu loop.

```python
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
```
**Explanation:** 'all' runs all except interactive (section 8).

```python
        else:
            print("⚠️  Invalid choice. Please try again.")
```
**Explanation:** Invalid input handling.

---

## Script Entry Point

```python
if __name__ == "__main__":
    main()
    
    # Teaching Questions:
    # 1. How does temperature affect output?
    # 2. When should you use low vs high temperature?
    # 3. What's the difference between top-p and top-k?
```
**Explanation:** Entry point with discussion questions.

---

## Summary

This module teaches **generation parameters** - the controls that determine HOW AI selects words when generating text.

### The Five Key Parameters:

1. **Temperature (0.0-2.0)**: Controls randomness
   - **How it works**: Adjusts probability distribution (flattens peaks at higher temps)
   - **Low (0.0-0.3)**: Deterministic, consistent, safe
   - **Medium (0.4-0.9)**: Natural, balanced
   - **High (1.0-2.0)**: Creative, diverse, unpredictable

2. **Top-P / Nucleus Sampling (0.0-1.0)**: Controls diversity by probability mass
   - **How it works**: Samples from smallest set of words that sum to P probability
   - **Example**: At 0.9, consider words until their probabilities add to 90%
   - **Adaptive**: Considers more words when probabilities are flat, fewer when peaked

3. **Top-K (1-100+)**: Limits to K most likely words
   - **How it works**: Fixed number of candidate words
   - **Example**: Top-40 always considers exactly 40 words
   - **Fixed**: Same count regardless of probability distribution

4. **Max Output Tokens**: Controls response length
   - **Conversion**: 1 token ≈ 0.75 words (English)
   - **Examples**: 50 tokens = short answer, 2048 = article

5. **Stop Sequences**: Strings that halt generation
   - **Use cases**: Paragraph breaks (`\n\n`), section markers (`###`), template boundaries

### Critical Concepts:

- **Parameters interact**: Temperature + top-p both affect diversity differently
- **Context-dependent**: Different tasks need different settings
- **No universal best**: Must match to use case
- **Trade-offs**: Creativity vs consistency, length vs cost

### Quick Reference:

| Task | Temp | Top-P | Max Tokens | Why |
|------|------|-------|------------|-----|
| **Factual Q&A** | 0.1 | 0.8 | 150 | Accuracy matters |
| **Code** | 0.2 | 0.85 | 500 | Must be correct |
| **Chat** | 0.7 | 0.9 | 250 | Natural variation |
| **Creative** | 1.2 | 0.95 | 500 | Unique outputs |
| **Brainstorm** | 1.0 | 0.95 | 200 | Diverse ideas |

### Best Practices:

1. **Start with defaults** (temp 0.7, top-p 0.95)
2. **Adjust one parameter at a time**
3. **Test multiple times** (randomness requires statistical sampling)
4. **Match to use case** (facts = low temp, creativity = high temp)
5. **Monitor costs** (longer = more expensive)

### Common Mistakes:

- ❌ High temp for facts → Hallucinations
- ❌ Low temp for creativity → Boring, repetitive
- ❌ Not setting token limits → Unexpected truncation
- ❌ Not testing variations → Production surprises

### The Mental Model:

Think of text generation as:
1. **AI calculates probability for every possible next word**
2. **Top-k/top-p filter the candidate pool**
3. **Temperature adjusts the probability distribution**
4. **AI randomly samples from the adjusted pool**
5. **Repeats until reaching max tokens or stop sequence**

**Key insight**: Parameters don't change what the AI "knows" - they change how it selects from what it knows. Same knowledge, different selection process = dramatically different outputs!