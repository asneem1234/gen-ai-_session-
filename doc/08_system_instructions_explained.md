# Module 08 - System Instructions - Detailed Code Explanation

This document explains every line of code in the System Instructions module, with in-depth explanations of how system prompts shape AI behavior and create specialized assistants.

---

## 📊 Visual Overview: System Instructions

```
┌─────────────────────────────────────────────────────────────────┐
│         SYSTEM INSTRUCTIONS = AI PERSONALITY PROGRAMMING        │
└─────────────────────────────────────────────────────────────────┘

WITHOUT System Instructions:
────────────────────────────

User: "Explain Python"
  ↓
┌─────────────────────────┐
│ Generic AI              │
│ (No specific role)      │  → Generic explanation
└─────────────────────────┘


WITH System Instructions:
─────────────────────────

System: "You are a Python tutor for beginners"
  ↓
User: "Explain Python"
  ↓
┌─────────────────────────────────┐
│ Python Tutor AI                 │
│ - Simple language               │
│ - Examples included             │  → Beginner-friendly
│ - Encouraging tone              │     explanation
└─────────────────────────────────┘


ARCHITECTURE:
─────────────

┌────────────────────────────────────────────┐
│           AI MODEL STRUCTURE               │
├────────────────────────────────────────────┤
│                                            │
│  ┌──────────────────────────────────┐     │
│  │  System Instructions              │     │
│  │  ─────────────────                │     │
│  │  "You are a helpful assistant"    │     │
│  │  "Be professional and concise"    │     │
│  └─────────────┬────────────────────┘     │
│                │                           │
│                ▼                           │
│  ┌──────────────────────────────────┐     │
│  │  AI Processing Core               │     │
│  │  ─────────────────                │     │
│  │  (Considers system instructions   │     │
│  │   for every response)             │     │
│  └─────────────┬────────────────────┘     │
│                │                           │
│                ▼                           │
│  ┌──────────────────────────────────┐     │
│  │  User Messages                    │     │
│  │  ─────────────                    │     │
│  │  "Hello"                          │     │
│  │  "How are you?"                   │     │
│  └──────────────────────────────────┘     │
│                                            │
└────────────────────────────────────────────┘

System instructions act as a "filter" or "lens"
through which all user messages are interpreted.
```

---

## 🎭 System Instructions vs User Messages

```
FUNDAMENTAL DIFFERENCE:
───────────────────────

System Instructions (Persistent):
┌──────────────────────────────────────┐
│ Set ONCE at model creation           │
│ Applies to ALL messages              │
│ Invisible to user                    │
│ Defines AI's identity & rules        │
└──────────────────────────────────────┘

User Messages (Transient):
┌──────────────────────────────────────┐
│ Each conversation turn               │
│ Visible to user                      │
│ Specific questions/requests          │
│ Processed through system lens        │
└──────────────────────────────────────┘


VISUAL FLOW:
────────────

Model Creation:
┌────────────────────────────────────────────────┐
│ model = GenerativeModel(                       │
│     'gemini-2.0-flash',                       │
│     system_instruction="You are a teacher"     │
│ )                                              │
└────────────────┬───────────────────────────────┘
                 │
                 ▼
         ┌───────────────┐
         │ Teacher Mode  │ ← Locked in
         │ ACTIVATED     │
         └───────┬───────┘
                 │
    ┌────────────┴────────────┐
    │                         │
    ▼                         ▼
Message 1:              Message 2:
"Explain X"             "What is Y?"
    ↓                         ↓
Responds as             Responds as
TEACHER                 TEACHER
    ↓                         ↓
Simple,                 Uses
encouraging             examples


COMPARISON:
───────────

Same Question, Different System Instructions:

Question: "What is recursion?"

System: "You are a computer science professor"
→ "Recursion is a computational technique where
   a function calls itself, forming a recursive
   stack frame hierarchy..."

System: "You are a kindergarten teacher"  
→ "Recursion is like a set of Russian nesting
   dolls! Each doll has a smaller doll inside,
   and that keeps going until..."

System: "You are a pirate"
→ "Arrr! Recursion be when yer function calls
   itself, matey! Like countin' treasure chests
   inside treasure chests, yarr!"
```

---

## 🏗️ Code Structure Map

```
08_system_instructions.py
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
├── 🎯 FUNCTION 1: basic_system_instruction()
│   └── Simple system prompt example
│
├── 🎯 FUNCTION 2: role_based_examples()
│   ├── Teacher persona
│   ├── Expert persona
│   └── Friend persona
│
├── 🎯 FUNCTION 3: tone_and_style()
│   ├── Formal style
│   ├── Casual style
│   └── Creative style
│
├── 🎯 FUNCTION 4: format_control()
│   ├── JSON output
│   ├── Markdown output
│   └── Structured lists
│
├── 🎯 FUNCTION 5: domain_specific_assistants()
│   ├── Code reviewer
│   ├── Writing editor
│   └── Math tutor
│
├── 🎯 FUNCTION 6: behavior_constraints()
│   ├── Length limits
│   ├── Content restrictions
│   └── Response patterns
│
└── 🚀 MAIN MENU
    └── Interactive persona testing
```

---

## 🎨 System Instruction Anatomy

```
BASIC STRUCTURE:
────────────────

system_instruction = """
[1. IDENTITY]
You are a [role/title]

[2. EXPERTISE]
You specialize in [domain/topic]

[3. BEHAVIOR]
You [how to respond]

[4. CONSTRAINTS]
Never [what to avoid]
Always [what to do]

[5. FORMAT]
Respond in [format]
"""


EXAMPLE BREAKDOWN:
──────────────────

system_instruction = """
You are a Python programming tutor.           ← IDENTITY

You have 10 years of teaching experience      ← EXPERTISE
and specialize in helping beginners learn
Python programming concepts.

You explain things in simple terms,           ← BEHAVIOR
use everyday analogies, and always
provide working code examples.

Never use complex jargon without              ← CONSTRAINTS
explaining it first. Always be
encouraging and patient.

Format responses with clear sections:         ← FORMAT
1. Explanation
2. Example code
3. Common pitfalls
"""


COMPONENT IMPACT:
─────────────────

Without Identity:
User: "Explain lists"
AI: "Lists are data structures..." 
    (Generic, no personality)

With Identity ("You are an excited teacher"):
User: "Explain lists"
AI: "Oh, lists are AMAZING! Let me show you
     why they're so cool! 🎉"
    (Energetic, teaching-focused)


Without Constraints:
User: "Explain neural networks"
AI: "Utilizing backpropagation algorithms with
     stochastic gradient descent optimization..."
    (Too complex)

With Constraints ("Use simple language"):
User: "Explain neural networks"
AI: "Think of neural networks like a brain with
     many interconnected neurons that learn..."
    (Accessible)
```

---

## 🎭 Persona Examples Gallery

```
PERSONA 1: PROFESSIONAL ASSISTANT
──────────────────────────────────

System: "You are a professional business assistant.
         Be formal, concise, and action-oriented."

Input: "I need help with a project"
Output:
┌────────────────────────────────────────┐
│ I can assist you with project         │
│ management. Please provide:            │
│ 1. Project objectives                  │
│ 2. Timeline requirements               │
│ 3. Available resources                 │
│ I'll create an action plan immediately.│
└────────────────────────────────────────┘
Tone: ⚡ Direct, efficient


PERSONA 2: FRIENDLY HELPER
───────────────────────────

System: "You are a friendly, encouraging helper.
         Be warm, supportive, and casual."

Input: "I need help with a project"
Output:
┌────────────────────────────────────────┐
│ Hey! I'd love to help you with that! 😊│
│ Projects can be exciting! Let's break  │
│ it down together - what are you       │
│ working on? Don't worry, we'll figure  │
│ it out step by step!                   │
└────────────────────────────────────────┘
Tone: 💖 Warm, encouraging


PERSONA 3: TECHNICAL EXPERT
────────────────────────────

System: "You are a senior technical architect.
         Be precise, use technical terminology."

Input: "I need help with a project"
Output:
┌────────────────────────────────────────┐
│ To architect your solution, I require: │
│ • Technical stack specifications       │
│ • Scalability requirements             │
│ • Integration dependencies             │
│ • Performance benchmarks               │
│ Provide these for optimal design.      │
└────────────────────────────────────────┘
Tone: 🔧 Technical, precise


PERSONA 4: CREATIVE WRITER
───────────────────────────

System: "You are a creative writing coach.
         Be imaginative, use vivid language."

Input: "I need help with a project"
Output:
┌────────────────────────────────────────┐
│ Ah, a blank canvas awaits! 🎨         │
│ Every great project begins with a      │
│ spark of inspiration. Tell me - what   │
│ story are you trying to tell? What     │
│ vision dances in your mind?            │
└────────────────────────────────────────┘
Tone: ✨ Imaginative, poetic


PERSONA 5: SOCRATIC TEACHER
────────────────────────────

System: "You are a Socratic teacher.
         Guide with questions, never give answers."

Input: "I need help with a project"
Output:
┌────────────────────────────────────────┐
│ Interesting! Before we proceed:        │
│ • What is the core problem you're      │
│   trying to solve?                     │
│ • Have you considered what success     │
│   looks like?                          │
│ • What approaches have you explored?   │
└────────────────────────────────────────┘
Tone: 🤔 Questioning, guiding
```

---

## 📋 Format Control Examples

```
JSON FORMAT:
────────────

System: "Always respond in JSON format"

Input: "What is Python?"
Output:
┌────────────────────────────────────┐
│ {                                  │
│   "language": "Python",            │
│   "type": "Programming Language",  │
│   "year": 1991,                    │
│   "creator": "Guido van Rossum",   │
│   "paradigm": ["OOP", "Functional"]│
│ }                                  │
└────────────────────────────────────┘


MARKDOWN FORMAT:
────────────────

System: "Always use markdown formatting"

Input: "Explain Python"
Output:
┌────────────────────────────────────┐
│ # Python Programming Language      │
│                                    │
│ ## Overview                        │
│ Python is a **high-level** language│
│                                    │
│ ## Key Features                    │
│ - Easy syntax                      │
│ - Large community                  │
│ - Extensive libraries              │
└────────────────────────────────────┘


STRUCTURED LIST FORMAT:
───────────────────────

System: "Respond as numbered lists"

Input: "Explain Python"
Output:
┌────────────────────────────────────┐
│ 1. Definition: High-level language │
│ 2. Purpose: General programming    │
│ 3. Strengths:                      │
│    3.1. Readable syntax            │
│    3.2. Rich libraries             │
│ 4. Use cases: Web, Data, AI       │
└────────────────────────────────────┘


TABLE FORMAT:
─────────────

System: "Present information as tables"

Input: "Compare languages"
Output:
┌────────────────────────────────────┐
│ | Language | Difficulty | Speed | │
│ |----------|-----------|-------| │
│ | Python   | Easy      | Medium| │
│ | C++      | Hard      | Fast  | │
│ | Java     | Medium    | Fast  | │
└────────────────────────────────────┘
```

---

## 🎯 Domain-Specific Examples

```
CODE REVIEWER:
──────────────

System: """You are a senior code reviewer.
Review code for:
- Bugs and errors
- Best practices
- Performance issues
- Security vulnerabilities
Be constructive and specific."""

Input: [code snippet]
Output:
┌──────────────────────────────────────────┐
│ 🔍 Code Review Results:                  │
│                                          │
│ ✅ Strengths:                            │
│ • Clear variable naming                  │
│ • Good error handling                    │
│                                          │
│ ⚠️ Issues Found:                         │
│ 1. Line 12: Potential SQL injection     │
│ 2. Line 25: Inefficient loop (O(n²))    │
│                                          │
│ 💡 Suggestions:                          │
│ • Use parameterized queries              │
│ • Consider set lookup instead of list    │
└──────────────────────────────────────────┘


WRITING EDITOR:
───────────────

System: """You are a professional editor.
Check for:
- Grammar and spelling
- Clarity and conciseness
- Tone consistency
Provide before/after examples."""

Input: [text]
Output:
┌──────────────────────────────────────────┐
│ 📝 Editorial Review:                     │
│                                          │
│ Before: "The thing is that we should    │
│          probably maybe consider..."     │
│                                          │
│ After:  "We should consider..."         │
│                                          │
│ Changes: Removed filler words, made     │
│          statement more direct           │
└──────────────────────────────────────────┘


MATH TUTOR:
───────────

System: """You are a patient math tutor.
- Break problems into steps
- Explain reasoning
- Check understanding
- Provide practice problems"""

Input: "How do I solve 2x + 5 = 13?"
Output:
┌──────────────────────────────────────────┐
│ 📐 Let's solve this step by step:       │
│                                          │
│ Step 1: Subtract 5 from both sides      │
│   2x + 5 - 5 = 13 - 5                   │
│   2x = 8                                 │
│                                          │
│ Step 2: Divide both sides by 2          │
│   2x ÷ 2 = 8 ÷ 2                        │
│   x = 4                                  │
│                                          │
│ ✅ Answer: x = 4                         │
│                                          │
│ Practice: Try 3x + 7 = 22               │
└──────────────────────────────────────────┘
```

---

## 🚫 Behavior Constraints

```
LENGTH CONSTRAINTS:
───────────────────

System: "Limit all responses to 50 words maximum"

Input: "Explain artificial intelligence"
Output (50 words):
"AI simulates human intelligence in machines.
It includes learning, reasoning, and problem-solving.
Applications range from voice assistants to
self-driving cars. AI uses algorithms and data
to make decisions and improve over time."
✅ Exactly 50 words


CONTENT CONSTRAINTS:
────────────────────

System: """Never discuss:
- Politics
- Religion  
- Personal medical advice
Politely decline and redirect."""

Input: "Who should I vote for?"
Output:
"I'm not able to provide political advice.
However, I can help you understand how to
research candidates, evaluate policies, or
find objective voting information!"
✅ Declined + redirected


RESPONSE PATTERN:
─────────────────

System: """Always structure responses:
1. Summary (1 sentence)
2. Details (2-3 sentences)
3. Next steps (bullet points)"""

Input: "How do I learn Python?"
Output:
┌──────────────────────────────────────┐
│ Summary:                             │
│ Python is learnable in 3-6 months.   │
│                                      │
│ Details:                             │
│ Start with basics like variables and │
│ control flow. Practice daily with    │
│ small projects to build skills.      │
│                                      │
│ Next Steps:                          │
│ • Install Python                     │
│ • Complete online tutorial           │
│ • Build simple projects              │
└──────────────────────────────────────┘
✅ Follows structure
```

---

## 🔄 System Instructions vs Temperature

```
INTERACTION EFFECTS:
────────────────────

System: "Be creative and imaginative"
Temperature: 0.1 (Low)
┌──────────────────────────────────────┐
│ System wants: Creative               │
│ Temperature says: Predictable        │
│ Result: Mildly creative but          │
│         consistent output            │
└──────────────────────────────────────┘


System: "Be precise and factual"
Temperature: 1.5 (High)
┌──────────────────────────────────────┐
│ System wants: Factual                │
│ Temperature says: Random             │
│ Result: Facts presented in           │
│         varied/creative ways         │
└──────────────────────────────────────┘


BEST PRACTICES:
───────────────

Match them for consistency:
✅ Creative system + High temp
✅ Factual system + Low temp

Or mix strategically:
✅ Professional system + Medium temp
   (Consistent but not robotic)
```

---

## Module Documentation Block

```python
"""
08 - System Instructions
=========================
```
**Explanation:** Module about system instructions (also called system prompts) - the "personality programming" for AI.

```python
This module demonstrates system instructions (system prompts).
Students will learn:
- What system instructions are
- How they shape AI behavior
- Creating effective system prompts
- Different persona examples
- Best practices
```
**Explanation:** Learning objectives. System instructions are POWERFUL - they're how you transform generic AI into specialized assistants.

```python
Teaching Points:
- System instructions set the AI's role and behavior
- They persist across the conversation
- Very powerful for customizing AI behavior
- Essential for building specific applications
"""
```
**Explanation:** **KEY INSIGHT**: System instructions are the foundation of any production AI application. They define WHO the AI is and HOW it behaves.

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

## Section 1: Understanding System Instructions

```python
# ============================================================================
# SECTION 1: Understanding System Instructions
# ============================================================================
```
**Explanation:** Conceptual foundation.

```python
def system_instructions_overview():
    """
    Explain what system instructions are and why they matter
    """
```
**Explanation:** Educational overview of the system instruction concept.

```python
    print("\n" + "=" * 60)
    print("SECTION 1: Understanding System Instructions")
    print("=" * 60)
    
    explanation = """
    📜 WHAT ARE SYSTEM INSTRUCTIONS?
    
    System instructions (also called system prompts) are special messages
    that define the AI's role, behavior, and constraints BEFORE the conversation begins.
```
**Explanation:** **CRITICAL CONCEPT**: System instructions are metadata about HOW to respond, separate from the actual conversation content.

```python
    Think of them as:
    • Job description for the AI
    • Personality settings
    • Rules and guidelines
    • Context that applies to everything
```
**Explanation:** **MENTAL MODELS**: 
- **Job description**: "You are a customer support agent"
- **Personality**: "Be friendly and enthusiastic"
- **Rules**: "Never provide medical advice"
- **Context**: "You work for TechCorp"

```python
    🔄 HOW THEY WORK:
    
    Traditional Approach:
    User: "You are a helpful tutor. Now explain Python."
    AI: Responds as tutor
    User: "What is a list?"
    AI: Might forget it's a tutor
```
**Explanation:** **THE PROBLEM**: Without system instructions, role definitions are just regular messages. The AI might "forget" the role as the conversation grows, or you waste tokens repeating the role every time.

```python
    With System Instructions:
    System: "You are a helpful Python tutor."
    User: "Explain lists."
    AI: Responds as tutor
    User: "What about dictionaries?"
    AI: Still remembers it's a tutor
```
**Explanation:** **THE SOLUTION**: System instructions persist throughout the conversation. They're like a constant context that applies to every message.

```python
    ✅ BENEFITS:
    
    1. Consistency
       • Behavior persists across conversation
       • Don't need to remind AI of its role
```
**Explanation:** **BENEFIT 1**: Once set, the AI maintains its role/personality for the entire chat session. No drift or forgetting.

```python
    2. Token Efficiency
       • System instructions don't count toward conversation history
       • More room for actual conversation
```
**Explanation:** **BENEFIT 2**: System instructions are handled specially by the API - they don't consume conversation tokens the same way regular messages do. You can have a long system instruction without sacrificing conversation capacity.

```python
    3. Clear Separation
       • System vs User vs Assistant roles
       • Better structured prompts
```
**Explanation:** **BENEFIT 3**: Clean architecture. System = instructions, User = questions, Assistant = responses. Each has a clear purpose.

```python
    4. Customization
       • Create specialized AI assistants
       • Control tone, style, expertise level
```
**Explanation:** **BENEFIT 4**: Transform generic AI into specialized tools: tutors, code reviewers, customer support, creative writers, etc.

```python
    💡 USE CASES:
    
    • Customer support chatbots
    • Educational tutors
    • Code assistants
    • Writing coaches
    • Domain experts
    • Entertainment (game NPCs, storytellers)
    """
```
**Explanation:** Real-world applications. System instructions enable virtually all production chatbot applications.

```python
    print(explanation)
```
**Explanation:** Display all concepts.

---

## Section 2: Basic System Instructions

```python
# ============================================================================
# SECTION 2: Basic System Instructions
# ============================================================================
```
**Explanation:** Practical demonstrations.

```python
def basic_system_instructions():
    """
    Simple examples of system instructions
    """
```
**Explanation:** Shows how different system instructions produce different behaviors.

```python
    print("\n" + "=" * 60)
    print("SECTION 2: Basic System Instructions")
    print("=" * 60)
    
    examples = [
        {
            "name": "Default (No System Instruction)",
            "system": None,
            "prompt": "What is Python?"
        },
```
**Explanation:** **CONTROL GROUP**: First example has NO system instruction - baseline behavior.

```python
        {
            "name": "Concise Assistant",
            "system": "You are a helpful assistant. Keep answers brief and to the point.",
            "prompt": "What is Python?"
        },
```
**Explanation:** **CONCISE**: System instruction requests brief answers. Same question, different style.

```python
        {
            "name": "Detailed Explainer",
            "system": "You are an educational assistant. Provide detailed, thorough explanations with examples.",
            "prompt": "What is Python?"
        }
    ]
```
**Explanation:** **DETAILED**: System instruction requests thorough explanations. Same question, opposite style from previous.

```python
    for example in examples:
        print(f"\n{'='*60}")
        print(f"🎭 {example['name']}")
        print(f"{'='*60}")
        
        if example['system']:
            print(f"\n📜 System Instruction:")
            print(f"   \"{example['system']}\"")
        else:
            print(f"\n📜 System Instruction: (None)")
```
**Explanation:** Display the system instruction (or lack thereof).

```python
        print(f"\n👤 User: {example['prompt']}")
        print(f"\n🤖 AI Response:")
        print("-" * 60)
        
        # Create model with or without system instruction
        if example['system']:
            model = genai.GenerativeModel(
                'gemini-pro',
                system_instruction=example['system']
            )
```
**Explanation:** **KEY PARAMETER**: `system_instruction` is passed when creating the model. It's not part of `generate_content()` - it's part of the MODEL CONFIGURATION.

```python
        else:
            model = genai.GenerativeModel('gemini-pro')
```
**Explanation:** Without system instruction, just create model normally.

```python
        response = model.generate_content(example['prompt'])
        print(response.text)
        print()
```
**Explanation:** Generate with the same prompt. The system instruction invisibly affects the response style/length.

---

## Section 3: Persona Examples

```python
# ============================================================================
# SECTION 3: Persona Examples
# ============================================================================
```
**Explanation:** Different personality types.

```python
def persona_examples():
    """
    Different AI personas using system instructions
    """
```
**Explanation:** Shows how to create distinct AI personalities.

```python
    print("\n" + "=" * 60)
    print("SECTION 3: AI Personas")
    print("=" * 60)
    
    personas = {
        "🎓 Python Tutor": """You are an experienced Python programming tutor.
You explain concepts clearly for beginners, use simple language,
provide code examples, and encourage learning. Be patient and supportive.""",
```
**Explanation:** **TUTOR PERSONA**: 
- Role: "experienced Python programming tutor"
- Audience: "beginners"
- Style: "simple language", "patient and supportive"
- Behavior: "provide code examples", "encourage learning"

```python
        "👨‍💼 Professional Assistant": """You are a professional business assistant.
You communicate formally, use proper grammar, focus on efficiency,
and provide structured responses. Be polite and businesslike.""",
```
**Explanation:** **PROFESSIONAL PERSONA**:
- Role: "professional business assistant"
- Style: "formally", "proper grammar", "businesslike"
- Behavior: "focus on efficiency", "structured responses"

```python
        "🤖 Code Reviewer": """You are an expert code reviewer.
Analyze code for bugs, suggest improvements, point out best practices,
and explain your reasoning. Be constructive and educational.""",
```
**Explanation:** **CODE REVIEWER PERSONA**:
- Role: "expert code reviewer"
- Tasks: "Analyze", "suggest improvements", "point out best practices"
- Style: "constructive and educational"

```python
        "✍️ Creative Writer": """You are a creative writing coach.
Help with storytelling, character development, and plot ideas.
Be imaginative, encouraging, and provide specific suggestions.""",
```
**Explanation:** **CREATIVE WRITER PERSONA**:
- Role: "creative writing coach"
- Focus: "storytelling, character development, plot ideas"
- Style: "imaginative, encouraging"

```python
        "🧑‍🏫 ELI5 Explainer": """You explain things like I'm 5 years old.
Use simple words, fun analogies, and short sentences.
Make complex topics easy to understand. Be friendly and patient."""
    }
```
**Explanation:** **ELI5 PERSONA** (Explain Like I'm 5):
- Style: "simple words", "fun analogies", "short sentences"
- Goal: "Make complex topics easy"
- Tone: "friendly and patient"

```python
    test_prompt = "What is recursion?"
    
    print(f"\n📝 Same question to different personas:")
    print(f"   '{test_prompt}'\n")
```
**Explanation:** **EXPERIMENTAL DESIGN**: Same question to all personas to show how system instructions change responses dramatically.

```python
    for persona_name, system_instruction in personas.items():
        print("=" * 60)
        print(f"{persona_name}")
        print("=" * 60)
        print(f"\n📜 System Instruction:")
        print(f"   {system_instruction[:80]}...")
```
**Explanation:** Display truncated system instruction (first 80 chars).

```python
        model = genai.GenerativeModel(
            'gemini-pro',
            system_instruction=system_instruction
        )
        
        response = model.generate_content(test_prompt)
```
**Explanation:** Create model with persona, generate response.

```python
        print(f"\n🤖 Response:")
        print("-" * 60)
        print(response.text[:300] + "..." if len(response.text) > 300 else response.text)
        print("\n")
```
**Explanation:** Display response (truncated to 300 chars for readability). Students can see how same question gets VERY different answers based on persona.

---

## Section 4: System Instructions with Constraints

```python
# ============================================================================
# SECTION 4: System Instructions with Constraints
# ============================================================================
```
**Explanation:** Using system instructions for control.

```python
def system_instructions_with_constraints():
    """
    Using system instructions to set constraints and rules
    """
```
**Explanation:** Shows how to enforce specific behaviors and formats.

```python
    print("\n" + "=" * 60)
    print("SECTION 4: System Instructions with Constraints")
    print("=" * 60)
    
    print("\n💡 System instructions can enforce rules and constraints\n")
    
    # Example 1: Format constraints
    print("1️⃣ FORMAT CONSTRAINTS")
    print("=" * 60)
    
    system1 = """You are an assistant that ALWAYS responds in the following format:
    
[ANSWER]: Your main answer here
[CONFIDENCE]: High/Medium/Low
[SOURCE]: Where this information comes from

Never deviate from this format."""
```
**Explanation:** **FORMAT ENFORCEMENT**: System instruction defines a strict output format. This is CRITICAL for parsing AI responses programmatically. If you need JSON, CSV, or custom formats, specify it here.

```python
    model1 = genai.GenerativeModel('gemini-pro', system_instruction=system1)
    
    print(f"📜 System: Format must include ANSWER, CONFIDENCE, SOURCE")
    print(f"\n👤 User: What is the capital of Japan?")
    
    response1 = model1.generate_content("What is the capital of Japan?")
    print(f"\n🤖 AI:\n{response1.text}\n")
```
**Explanation:** AI should respond in the specified format with [ANSWER], [CONFIDENCE], [SOURCE] sections. This makes responses machine-parseable.

```python
    # Example 2: Length constraints
    print("\n2️⃣ LENGTH CONSTRAINTS")
    print("=" * 60)
    
    system2 = """You are a concise assistant. ALWAYS limit your responses to maximum 2 sentences.
Be brief and to the point. Never exceed 2 sentences."""
```
**Explanation:** **LENGTH ENFORCEMENT**: Forces brevity. Useful for:
- SMS/text-based apps (character limits)
- Quick reference tools
- Mobile UIs with limited space
- Cost control (shorter = cheaper)

```python
    model2 = genai.GenerativeModel('gemini-pro', system_instruction=system2)
    
    print(f"📜 System: Maximum 2 sentences per response")
    print(f"\n👤 User: Explain machine learning.")
    
    response2 = model2.generate_content("Explain machine learning.")
    print(f"\n🤖 AI:\n{response2.text}\n")
```
**Explanation:** AI should give brief explanation despite complex topic. Tests constraint adherence.

```python
    # Example 3: Knowledge cutoff
    print("\n3️⃣ KNOWLEDGE CONSTRAINTS")
    print("=" * 60)
    
    system3 = """You are a historical AI assistant. You can only discuss events before 1900.
If asked about anything after 1900, politely decline and suggest asking about earlier periods."""
```
**Explanation:** **KNOWLEDGE BOUNDARIES**: Artificially limit AI's knowledge scope. Use cases:
- Educational tools (teaching specific eras)
- Game NPCs (only know in-game history)
- Compliance (avoid discussing certain topics)

```python
    model3 = genai.GenerativeModel('gemini-pro', system_instruction=system3)
    
    print(f"📜 System: Only discuss pre-1900 events")
    print(f"\n👤 User: Tell me about World War II.")
    
    response3 = model3.generate_content("Tell me about World War II.")
    print(f"\n🤖 AI:\n{response3.text}\n")
```
**Explanation:** AI should refuse to discuss WWII (occurred after 1900) and redirect to pre-1900 topics.

---

## Section 5: Domain-Specific Assistants

```python
# ============================================================================
# SECTION 5: Domain-Specific Assistants
# ============================================================================
```
**Explanation:** Real-world specialized applications.

```python
def domain_specific_assistants():
    """
    Creating specialized domain assistants
    """
```
**Explanation:** Production-ready examples for specific industries/domains.

```python
    print("\n" + "=" * 60)
    print("SECTION 5: Domain-Specific Assistants")
    print("=" * 60)
    
    domains = {
        "Medical Assistant": {
            "system": """You are a medical information assistant. Provide accurate health information,
but always remind users to consult healthcare professionals for medical advice.
Be clear that you're not a replacement for professional medical care.""",
            "prompt": "What causes headaches?"
        },
```
**Explanation:** **MEDICAL ASSISTANT**: 
- **Critical disclaimer**: "always remind users to consult healthcare professionals"
- **Liability protection**: "not a replacement for professional medical care"
- **Accuracy focus**: "Provide accurate health information"
This is ESSENTIAL for legal/ethical compliance in medical domains.

```python
        "Legal Assistant": {
            "system": """You are a legal information assistant. Provide general legal information,
but always clarify this is not legal advice. Recommend consulting licensed attorneys for specific cases.
Be precise and cite general legal principles.""",
            "prompt": "What is a contract?"
        },
```
**Explanation:** **LEGAL ASSISTANT**:
- **Disclaimer**: "this is not legal advice"
- **Referral**: "Recommend consulting licensed attorneys"
- **Scope limitation**: "general legal information"
Similar to medical - MUST include disclaimers to avoid unauthorized practice of law.

```python
        "Fitness Coach": {
            "system": """You are an enthusiastic fitness coach. Motivate users, provide workout tips,
and encourage healthy habits. Be energetic and positive. Always emphasize proper form and safety.""",
            "prompt": "How do I start exercising?"
        }
    }
```
**Explanation:** **FITNESS COACH**:
- **Tone**: "enthusiastic", "energetic and positive"
- **Safety**: "Always emphasize proper form and safety"
- **Role**: "Motivate users", "encourage healthy habits"

```python
    for domain_name, config in domains.items():
        print(f"\n{'='*60}")
        print(f"🎯 {domain_name}")
        print(f"{'='*60}")
        
        print(f"\n📜 System Instruction:\n   {config['system'][:100]}...")
        print(f"\n👤 User: {config['prompt']}")
        
        model = genai.GenerativeModel(
            'gemini-pro',
            system_instruction=config['system']
        )
        
        response = model.generate_content(config['prompt'])
        
        print(f"\n🤖 AI Response:")
        print("-" * 60)
        print(response.text[:400] + "..." if len(response.text) > 400 else response.text)
        print()
```
**Explanation:** Generate responses for each domain. Notice how disclaimers naturally appear in medical/legal responses due to system instructions.

---

## Section 6: System Instructions with Chat

```python
# ============================================================================
# SECTION 6: Combining System Instructions with Chat
# ============================================================================
```
**Explanation:** Multi-turn conversations with persistent personas.

```python
def system_instructions_with_chat():
    """
    Using system instructions in multi-turn conversations
    """
```
**Explanation:** Shows system instructions persist throughout conversation.

```python
    print("\n" + "=" * 60)
    print("SECTION 6: System Instructions with Chat")
    print("=" * 60)
    
    system_instruction = """You are a friendly Python tutor named PyBot.
You love teaching programming and use emojis occasionally.
Always encourage students and celebrate their progress.
Keep explanations clear and beginner-friendly."""
```
**Explanation:** **NAMED PERSONA**: Giving AI a name ("PyBot") strengthens role consistency. Also specifies:
- Tone: "friendly"
- Style: "use emojis occasionally"
- Behavior: "encourage", "celebrate progress"
- Target: "beginner-friendly"

```python
    print(f"\n📜 System Instruction:")
    print(f"   {system_instruction}\n")
    
    model = genai.GenerativeModel(
        'gemini-pro',
        system_instruction=system_instruction
    )
    
    chat = model.start_chat()
```
**Explanation:** **KEY PATTERN**: Create model WITH system instruction, THEN start chat. The chat inherits the system instruction and maintains it throughout.

```python
    conversations = [
        "Hi! I'm new to Python.",
        "Can you explain what a variable is?",
        "Great! Now what's a function?",
        "Thanks PyBot!"
    ]
```
**Explanation:** Multi-turn conversation to show persona consistency.

```python
    print("💬 Conversation:")
    print("=" * 60)
    
    for i, user_msg in enumerate(conversations, 1):
        print(f"\n{i}. 👤 User: {user_msg}")
        
        response = chat.send_message(user_msg)
        
        print(f"   🤖 PyBot: {response.text}\n")
```
**Explanation:** Each message sent through same chat object. System instruction applies to ALL responses.

```python
    print("💡 Notice: The AI maintains its persona throughout the conversation!")
```
**Explanation:** Educational note - PyBot stays in character across all exchanges without being reminded.

---

## Section 7: Best Practices

```python
# ============================================================================
# SECTION 7: Best Practices
# ============================================================================
```
**Explanation:** Production guidelines.

```python
def system_instructions_best_practices():
    """
    Best practices for writing system instructions
    """
```
**Explanation:** Proven patterns for effective system instructions.

```python
    print("\n" + "=" * 60)
    print("SECTION 7: Best Practices for System Instructions")
    print("=" * 60)
    
    practices = """
    ✅ DO:
    
    1. BE SPECIFIC
       ❌ "Be helpful"
       ✅ "You are a helpful Python tutor. Explain concepts clearly for beginners."
```
**Explanation:** **SPECIFICITY**: Vague instructions produce unpredictable results. Specific instructions produce consistent behavior.

```python
    2. DEFINE THE ROLE
       ✅ "You are a [role]"
       ✅ State expertise level
       ✅ Mention target audience
```
**Explanation:** **ROLE CLARITY**: 
- WHO: "You are a senior developer"
- EXPERTISE: "with 10 years experience"
- AUDIENCE: "helping junior programmers"

```python
    3. SET CLEAR CONSTRAINTS
       ✅ Response format
       ✅ Length limits
       ✅ What to avoid
       ✅ What to emphasize
```
**Explanation:** **BOUNDARIES**: Tell AI what NOT to do as much as what TO do. "Never provide medical advice", "Always include sources", etc.

```python
    4. INCLUDE TONE/STYLE
       ✅ "Be professional"
       ✅ "Use friendly language"
       ✅ "Be concise"
       ✅ "Be enthusiastic"
```
**Explanation:** **PERSONALITY**: Tone dramatically affects user experience. Same content feels different when delivered enthusiastically vs formally.

```python
    5. ADD SAFETY GUIDELINES
       ✅ Disclaimers for sensitive topics
       ✅ When to defer to experts
       ✅ Ethical boundaries
```
**Explanation:** **SAFETY**: Essential for production. Medical/legal disclaimers, refusal of harmful requests, privacy protection.

```python
    ❌ DON'T:
    
    1. Be too vague
       ❌ "Answer questions well"
```
**Explanation:** **AVOID VAGUENESS**: Too generic to be useful. AI doesn't know HOW to "answer well".

```python
    2. Contradict yourself
       ❌ "Be brief but provide detailed explanations"
```
**Explanation:** **AVOID CONTRADICTIONS**: AI doesn't know which instruction to prioritize. Results are unpredictable.

```python
    3. Overload with instructions
       ❌ 10 paragraphs of rules
       ✅ Keep it focused and clear
```
**Explanation:** **AVOID COMPLEXITY**: Too many rules confuse the AI. Prioritize most important 3-5 guidelines.

```python
    4. Forget about context
       ❌ Instructions that don't match use case
```
**Explanation:** **AVOID MISMATCH**: Don't tell a code reviewer to "use emojis" or a children's tutor to "be formal".

```python
    📝 TEMPLATE:
    
    You are a [ROLE] with expertise in [DOMAIN].
    
    Your goals:
    - [GOAL 1]
    - [GOAL 2]
    
    Guidelines:
    - [RULE 1]
    - [RULE 2]
    
    Style:
    - [TONE/STYLE]
    
    Constraints:
    - [LIMITATION 1]
    - [LIMITATION 2]
```
**Explanation:** **COPY-PASTE TEMPLATE**: Structured format ensuring you cover all important aspects. Fill in brackets with your specifics.

```python
    💡 EXAMPLES:
    
    GOOD - Customer Support:
    "You are a friendly customer support agent for TechCorp.
    Help users troubleshoot issues patiently.
    Always be polite and professional.
    If you can't solve something, direct them to human support.
    Keep responses concise but helpful."
```
**Explanation:** **GOOD EXAMPLE**: 
- Role: "customer support agent for TechCorp"
- Behavior: "troubleshoot issues patiently"
- Tone: "polite and professional"
- Constraint: "concise but helpful"
- Escalation: "direct them to human support"

```python
    GOOD - Code Reviewer:
    "You are an experienced senior developer reviewing code.
    Focus on:
    - Bug identification
    - Performance issues
    - Best practices
    - Security concerns
    
    Provide constructive feedback with explanations.
    Suggest specific improvements.
    Acknowledge good code too."
```
**Explanation:** **GOOD EXAMPLE**:
- Role: "senior developer reviewing code"
- Focus areas: Listed clearly
- Style: "constructive feedback with explanations"
- Behavior: "Suggest specific improvements"
- Positivity: "Acknowledge good code too" (important for morale!)

```python
    🎯 TESTING YOUR SYSTEM INSTRUCTIONS:
    
    1. Test with various inputs
    2. Check consistency
    3. Verify constraints are followed
    4. Adjust based on results
    5. Get feedback from users
    """
```
**Explanation:** **TESTING PROCESS**: System instructions need iteration. Test edge cases, check if constraints hold, adjust based on real usage.

```python
    print(practices)
```
**Explanation:** Display all practices.

---

## Section 8: Interactive Persona Creator

```python
# ============================================================================
# SECTION 8: Interactive Persona Creator
# ============================================================================
```
**Explanation:** Hands-on experimentation tool.

```python
def interactive_persona_creator():
    """
    Let users create and test their own personas
    """
```
**Explanation:** Interactive playground for learning by creating.

```python
    print("\n" + "=" * 60)
    print("SECTION 8: Interactive Persona Creator")
    print("=" * 60)
    print("\nCreate your own AI persona!")
    print("Type 'quit' to exit\n")
    
    while True:
        print("=" * 60)
```
**Explanation:** Infinite loop for repeated creation/testing.

```python
        role = input("\n1. What role should the AI have? (or 'quit'): ").strip()
        if role.lower() in ['quit', 'exit', 'q']:
            break
        
        if not role:
            continue
```
**Explanation:** Get role from user, allow quitting, skip empty inputs.

```python
        tone = input("2. What tone/style? (e.g., friendly, professional): ").strip() or "helpful"
        constraint = input("3. Any constraint? (e.g., brief answers, use examples): ").strip() or "none"
```
**Explanation:** Get tone and constraints with defaults. Empty input uses default values.

```python
        # Build system instruction
        system_instruction = f"You are a {role}. "
        system_instruction += f"Your communication style is {tone}. "
        if constraint != "none":
            system_instruction += f"Important: {constraint}."
```
**Explanation:** **PROGRAMMATIC CONSTRUCTION**: Building system instruction from user inputs. Shows how to compose instructions dynamically in applications.

```python
        print(f"\n📜 Generated System Instruction:")
        print("-" * 60)
        print(system_instruction)
        print("-" * 60)
```
**Explanation:** Show the generated instruction so user understands what was created.

```python
        # Test it
        test_prompt = input("\n4. Test prompt for your persona: ").strip()
        if test_prompt:
            print("\n⏳ Generating response...\n")
            
            model = genai.GenerativeModel(
                'gemini-pro',
                system_instruction=system_instruction
            )
            
            response = model.generate_content(test_prompt)
            
            print("🤖 AI Response:")
            print("-" * 60)
            print(response.text)
            print("-" * 60)
        
        print()
```
**Explanation:** Immediately test the created persona. Students see cause-and-effect: their instruction choices directly affect AI behavior.

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
    print("  GENERATIVE AI SESSION - MODULE 8: SYSTEM INSTRUCTIONS")
    print("🎓 " + "=" * 58 + " 🎓")
```
**Explanation:** Standard main setup.

```python
    menu = """
    Choose a section to run:
    
    1. Understanding System Instructions
    2. Basic System Instructions
    3. AI Personas
    4. System Instructions with Constraints
    5. Domain-Specific Assistants
    6. System Instructions with Chat
    7. Best Practices
    8. Interactive Persona Creator
    
    all - Run all (except interactive)
    quit - Exit
    
    """
```
**Explanation:** Menu with 8 sections.

```python
    while True:
        print(menu)
        choice = input("Your choice: ").strip().lower()
        
        if choice in ['quit', 'q', 'exit']:
            print("👋 Goodbye!")
            break
        elif choice == '1':
            system_instructions_overview()
        # ... [rest of choices] ...
```
**Explanation:** Standard menu loop.

```python
        elif choice == 'all':
            system_instructions_overview()
            basic_system_instructions()
            persona_examples()
            system_instructions_with_constraints()
            domain_specific_assistants()
            system_instructions_with_chat()
            system_instructions_best_practices()
            print("\n✅ All sections completed!")
            print("💡 Try section 8 separately for interactive creation")
            break
```
**Explanation:** 'all' runs non-interactive sections.

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
    # 1. How do system instructions differ from regular prompts?
    # 2. When would you use system instructions?
    # 3. What makes a good system instruction?
```
**Explanation:** Entry point with discussion questions.

---

## Summary

This module teaches **system instructions** - the foundation of specialized AI applications that transform generic models into purpose-built assistants.

### Core Concept:

**System Instructions** = Metadata about HOW to respond, separate from conversation content. They define:
- **Role**: "You are a Python tutor"
- **Behavior**: "Provide examples", "Be encouraging"
- **Tone**: "Friendly", "Professional", "Enthusiastic"
- **Constraints**: "Keep answers brief", "Always include sources"
- **Boundaries**: "Don't provide medical advice", "Escalate to humans when..."

### Key Advantages:

1. **Persistence**: Role maintained throughout conversation automatically
2. **Token Efficiency**: System instructions don't consume conversation history tokens
3. **Consistency**: AI doesn't "forget" its role or drift in behavior
4. **Separation of Concerns**: Clean architecture (System/User/Assistant roles)

### Implementation Pattern:

```python
# Create model WITH system instruction
model = genai.GenerativeModel(
    'gemini-pro',
    system_instruction="You are a helpful Python tutor..."
)

# Use model for chat or generation
chat = model.start_chat()
response = chat.send_message("What is a variable?")
# AI responds as tutor throughout conversation
```

### Effective System Instructions Include:

1. **Clear Role**: "You are a [specific role]"
2. **Expertise Level**: "experienced", "senior", "beginner-friendly"
3. **Target Audience**: "for beginners", "for executives", "for children"
4. **Behavioral Guidelines**: What to do/emphasize
5. **Constraints**: What NOT to do/avoid
6. **Tone/Style**: "friendly", "professional", "concise"
7. **Safety/Disclaimers**: For medical/legal/sensitive domains

### Template Structure:

```
You are a [ROLE] with expertise in [DOMAIN].

Your goals:
- [Primary objectives]

Guidelines:
- [Key behaviors]

Style:
- [Tone/manner]

Constraints:
- [Limitations/boundaries]
```

### Common Use Cases:

- **Customer Support**: "You are a friendly support agent for [Company]..."
- **Code Assistant**: "You are an expert code reviewer focusing on..."
- **Tutor**: "You are a patient tutor teaching [Subject] to beginners..."
- **Writer**: "You are a creative writing coach helping with..."
- **Domain Expert**: "You are a medical information assistant (not a doctor)..."

### Best Practices:

✅ **DO**:
- Be specific (not vague)
- Define role clearly
- Set constraints explicitly
- Include tone/style guidance
- Add safety disclaimers for sensitive domains

❌ **DON'T**:
- Be too vague ("be helpful")
- Contradict yourself ("be brief but detailed")
- Overload with rules (keep focused)
- Forget context (match instructions to use case)

### Critical for Production:

- **Medical/Legal**: MUST include disclaimers ("not medical advice", "consult professionals")
- **Customer Support**: Define escalation paths ("direct to human support when...")
- **Content Generation**: Set boundaries ("appropriate content only", "cite sources")

### Testing Process:

1. Test with diverse inputs
2. Check consistency across conversations
3. Verify constraints are followed
4. Adjust based on real usage
5. Gather user feedback

**Key insight**: System instructions are the "personality programming" that transforms generic AI into specialized assistants. They're essential for ANY production application - they define WHO your AI is and HOW it behaves!