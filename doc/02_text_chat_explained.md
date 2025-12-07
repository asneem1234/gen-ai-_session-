# Module 02 - Text Chat - Detailed Code Explanation

This document explains every line of code in the Text Chat module.

---

## 📊 Visual Overview: Text Chat Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     TEXT CHAT MODULE FLOW                       │
└─────────────────────────────────────────────────────────────────┘

    Setup Phase                Processing Phase              Output Phase
    ───────────               ──────────────────             ────────────
    
┌──────────────┐           ┌──────────────────┐          ┌──────────────┐
│ Import       │           │   User writes    │          │   Display    │
│ Libraries    │    ──→    │   a prompt       │    ──→   │   Response   │
└──────────────┘           └──────────────────┘          └──────────────┘
       │                            │                            │
       ▼                            ▼                            ▼
┌──────────────┐           ┌──────────────────┐          ┌──────────────┐
│ Load .env    │           │  Send to Gemini  │          │  Parse Text  │
│ Configure    │           │  via API call    │          │  Format for  │
│ API Key      │           │                  │          │  Display     │
└──────────────┘           └──────────────────┘          └──────────────┘
       │                            │                            │
       ▼                            ▼                            ▼
┌──────────────┐           ┌──────────────────┐          ┌──────────────┐
│ Create Model │           │ AI processes &   │          │   User sees  │
│ Instance     │           │ generates text   │          │   Result!    │
└──────────────┘           └──────────────────┘          └──────────────┘
```

---

## 🎯 Prompt Engineering: Quality Levels

```
Prompt Quality Impact on Response:

❌ POOR PROMPT:
┌─────────────────────────┐
│ "tell me about dogs"    │  ──→  Vague, generic response
└─────────────────────────┘        (200 words, unfocused)

⚠️ OKAY PROMPT:
┌─────────────────────────────────┐
│ "write about dog breeds"        │  ──→  Better, but still broad
└─────────────────────────────────┘        (better focus)

✅ GREAT PROMPT:
┌───────────────────────────────────────────────────────────────┐
│ "Write a 100-word paragraph about Golden Retrievers          │
│  focusing on their temperament and family compatibility.     │
│  Use friendly tone for pet owners."                          │  ──→  Specific,
└───────────────────────────────────────────────────────────────┘     high-quality
                                                                       response!

┌────────────────────────────────────────────────────────────────────┐
│  KEY ELEMENTS OF GOOD PROMPTS:                                    │
│  ───────────────────────────────                                  │
│  ✓ Specific topic/scope                                           │
│  ✓ Desired length/format                                          │
│  ✓ Tone/style guidance                                            │
│  ✓ Target audience                                                │
│  ✓ Any constraints                                                │
└────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 7 Text Generation Use Cases

```
┌────────────────────────────────────────────────────────────────┐
│  This module demonstrates 7 different ways to use text AI:    │
└────────────────────────────────────────────────────────────────┘

1️⃣ SIMPLE TEXT GENERATION
   ┌──────────────┐      ┌──────────┐      ┌──────────────┐
   │ Basic Prompt │  ──→ │  Gemini  │  ──→ │ Simple Reply │
   └──────────────┘      └──────────┘      └──────────────┘

2️⃣ QUESTION ANSWERING
   ┌──────────────┐      ┌──────────┐      ┌──────────────┐
   │ Ask Question │  ──→ │  Gemini  │  ──→ │ Get Answer   │
   └──────────────┘      └──────────┘      └──────────────┘

3️⃣ CREATIVE WRITING
   ┌──────────────┐      ┌──────────┐      ┌──────────────┐
   │ Story Prompt │  ──→ │  Gemini  │  ──→ │ Creative Text│
   └──────────────┘      └──────────┘      └──────────────┘

4️⃣ SUMMARIZATION
   ┌──────────────┐      ┌──────────┐      ┌──────────────┐
   │ Long Article │  ──→ │  Gemini  │  ──→ │ Short Summary│
   └──────────────┘      └──────────┘      └──────────────┘

5️⃣ TRANSLATION
   ┌──────────────┐      ┌──────────┐      ┌──────────────┐
   │ English Text │  ──→ │  Gemini  │  ──→ │ Spanish Text │
   └──────────────┘      └──────────┘      └──────────────┘

6️⃣ CODE GENERATION
   ┌──────────────┐      ┌──────────┐      ┌──────────────┐
   │ Code Request │  ──→ │  Gemini  │  ──→ │ Python Code  │
   └──────────────┘      └──────────┘      └──────────────┘

7️⃣ INTERACTIVE CHAT
   ┌──────────────┐      ┌──────────┐      ┌──────────────┐
   │ Multi-turn   │  ⇄  │  Gemini  │  ⇄  │ Conversation │
   │ Dialog       │      │          │      │ with Memory  │
   └──────────────┘      └──────────┘      └──────────────┘
```

---

## 🏗️ Code Structure Map

```
02_text_chat.py
│
├── 📦 IMPORTS
│   ├── os
│   ├── dotenv
│   └── google.generativeai
│
├── 🔧 SETUP (runs immediately)
│   ├── load_dotenv()
│   └── genai.configure()
│
├── 🎯 FUNCTION 1: simple_text_generation()
│   └── Basic "Hello" prompt → Response
│
├── 🎯 FUNCTION 2: question_answering()
│   ├── Technical question
│   ├── Historical question
│   └── Comparison question
│
├── 🎯 FUNCTION 3: creative_writing()
│   ├── Story generation
│   ├── Poetry generation
│   └── Professional writing
│
├── 🎯 FUNCTION 4: summarization_examples()
│   ├── Article summary
│   └── Technical summary
│
├── 🎯 FUNCTION 5: translation_examples()
│   ├── English → Spanish
│   └── English → French
│
├── 🎯 FUNCTION 6: code_generation_examples()
│   ├── Function generation
│   └── Class generation
│
├── 🎯 FUNCTION 7: practical_use_cases()
│   ├── Email writing
│   ├── Document formatting
│   └── Data extraction
│
├── 🎯 FUNCTION 8: interactive_chat()
│   └── Multi-turn conversation with memory
│
└── 🚀 MAIN MENU SYSTEM
    ├── Display options
    ├── Get user choice
    └── Call selected function
```

---

## 💬 How Text Generation Works (Step-by-Step)

```
STEP 1: CREATE MODEL
─────────────────────
model = genai.GenerativeModel('gemini-2.0-flash')
           │
           ▼
    ┌──────────────┐
    │ Model Ready  │
    │ to Accept    │
    │ Prompts      │
    └──────────────┘

STEP 2: WRITE PROMPT
────────────────────
prompt = "Explain quantum computing in simple terms"
           │
           ▼
    ┌──────────────┐
    │ Text String  │
    │ Describing   │
    │ Your Request │
    └──────────────┘

STEP 3: GENERATE CONTENT
─────────────────────────
response = model.generate_content(prompt)
              │
              ▼
       ┌────────────────────────────────┐
       │  API Call to Google Servers    │
       │  ─────────────────────────     │
       │  1. Tokenize prompt            │
       │  2. Process through neural net │
       │  3. Generate response tokens   │
       │  4. Decode to text             │
       └────────────┬───────────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │ Response Object Created       │
    │ Contains:                     │
    │ - .text (the generated text)  │
    │ - .candidates (alternatives)  │
    │ - metadata                    │
    └───────────────────────────────┘

STEP 4: USE RESPONSE
────────────────────
print(response.text)
        │
        ▼
┌─────────────────────┐
│ Display on Screen   │
│ OR                  │
│ Save to File        │
│ OR                  │
│ Process Further     │
└─────────────────────┘
```

---

## 🔄 Interactive Chat: Conversation Memory

```
Regular Generation (No Memory):
────────────────────────────────

┌──────────┐     ┌──────────┐     ┌──────────┐
│ Prompt 1 │ ──→ │  Gemini  │ ──→ │ Reply 1  │
└──────────┘     └──────────┘     └──────────┘
                      │
                      ✗ Memory cleared!
                      │
┌──────────┐     ┌──────────┐     ┌──────────┐
│ Prompt 2 │ ──→ │  Gemini  │ ──→ │ Reply 2  │
└──────────┘     └──────────┘     └──────────┘
                      │
                 ⚠️ Cannot reference Prompt 1!


Chat Session (With Memory):
────────────────────────────

┌──────────┐     ┌──────────────────┐     ┌──────────┐
│ Message 1│ ──→ │  Chat Session    │ ──→ │ Reply 1  │
└──────────┘     │  ────────────    │     └──────────┘
                 │  History: []     │
                 └────────┬─────────┘
                          │
                    ✅ History saved:
                    ["User: Msg 1", "AI: Reply 1"]
                          │
┌──────────┐     ┌────────▼─────────┐     ┌──────────┐
│ Message 2│ ──→ │  Chat Session    │ ──→ │ Reply 2  │
└──────────┘     │  ────────────    │     └──────────┘
                 │  History: [...]  │
                 └────────┬─────────┘
                          │
                    ✅ Can reference previous messages!


Implementation:
───────────────

chat = model.start_chat(history=[])
              │
              ▼
┌───────────────────────────────────┐
│  Chat Object with Memory          │
│  ──────────────────────            │
│  - Stores conversation history    │
│  - Maintains context               │
│  - Each message aware of previous │
└───────────────────────────────────┘

response = chat.send_message("Hello")
              │
              ▼
        Automatically:
        1. Appends user message to history
        2. Sends ENTIRE history to API
        3. Gets contextual response
        4. Appends AI response to history
```

---

## 📐 Prompt Structure Examples

```
BASIC STRUCTURE:
════════════════
┌────────────────────────────────┐
│ [Action Verb] + [Topic]       │
│                                │
│ Example:                       │
│ "Explain quantum computing"   │
└────────────────────────────────┘


INTERMEDIATE STRUCTURE:
═══════════════════════
┌────────────────────────────────┐
│ [Action] + [Topic] + [Format] │
│                                │
│ Example:                       │
│ "Explain quantum computing    │
│  in 3 simple paragraphs"      │
└────────────────────────────────┘


ADVANCED STRUCTURE:
═══════════════════
┌─────────────────────────────────────────┐
│ [Context] + [Task] + [Format] +        │
│ [Constraints] + [Style]                 │
│                                         │
│ Example:                                │
│ "You are a teacher for 10-year-olds.   │
│  Explain quantum computing using       │
│  everyday analogies. Write 2 short     │
│  paragraphs. Use simple words.         │
│  Be enthusiastic and encouraging."     │
└─────────────────────────────────────────┘
      │           │          │         │
      ▼           ▼          ▼         ▼
   Context     Task      Format    Style
```

---

## Module Documentation Block

```python
"""
02 - Text Chat
==============
```
**Explanation:** Docstring header for Module 2. The equals signs create a visual underline for the title.

```python
This module demonstrates various text generation and chat capabilities.
Students will learn:
- Simple text generation
- Question-answering
- Different prompting techniques
- Handling long-form content
- Building interactive chat
```
**Explanation:** Lists the learning objectives - what students will be able to do after this module.

```python
Teaching Points:
- Prompt engineering is crucial
- Clear, specific prompts get better results
- Context matters for quality responses
"""
```
**Explanation:** Key concepts instructors should emphasize. The closing `"""` ends the docstring.

---

## Import Statements

```python
import os
```
**Explanation:** Imports the `os` module to interact with operating system features like environment variables.

```python
from dotenv import load_dotenv
```
**Explanation:** Imports the `load_dotenv` function to read `.env` files containing configuration.

```python
import google.generativeai as genai
```
**Explanation:** Imports Google's Generative AI library with the short alias `genai`.

---

## Initial Setup

```python
# Setup
load_dotenv()
```
**Explanation:** Comment describes what follows. Loads environment variables from the `.env` file into memory.

```python
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
```
**Explanation:** Configures the Gemini API by getting the API key from environment variables. This setup happens once at module load, so it's available to all functions.

---

## Section 1: Simple Text Generation Function

```python
# ============================================================================
# SECTION 1: Simple Text Generation
# ============================================================================
```
**Explanation:** Visual separator comment to organize code sections.

```python
def simple_text_generation():
```
**Explanation:** Defines a function with no parameters. This function demonstrates basic text generation.

```python
    """
    Basic text generation - the foundation of all LLM interactions
    """
```
**Explanation:** Function docstring explaining its purpose.

```python
    print("\n" + "=" * 60)
    print("SECTION 1: Simple Text Generation")
    print("=" * 60)
```
**Explanation:** Prints section header with separators. `\n` adds blank line for spacing.

```python
    model = genai.GenerativeModel('gemini-pro')
```
**Explanation:** Creates a new GenerativeModel object for text generation. This is a local variable within this function.

```python
    # Example 1: Direct question
    print("\n1️⃣ Direct Question:")
```
**Explanation:** Comment labels this example. Prints a numbered header with emoji.

```python
    prompt1 = "What is machine learning in one sentence?"
```
**Explanation:** Stores the prompt text in a variable named `prompt1`. This is what we'll send to the AI.

```python
    print(f"📝 Prompt: {prompt1}")
```
**Explanation:** Shows the user what prompt we're sending. The f-string embeds the `prompt1` variable.

```python
    response1 = model.generate_content(prompt1)
```
**Explanation:** Calls the model's `generate_content` method with our prompt. Stores the response object in `response1`.

```python
    print(f"🤖 Response: {response1.text}\n")
```
**Explanation:** Prints the text content from the response. `.text` accesses the text property. `\n` adds a blank line after.

```python
    # Example 2: Creative writing
    print("\n2️⃣ Creative Writing:")
```
**Explanation:** Header for the second example showing a different use case.

```python
    prompt2 = "Write a haiku about artificial intelligence."
```
**Explanation:** A creative writing prompt asking for poetry in haiku format.

```python
    print(f"📝 Prompt: {prompt2}")
```
**Explanation:** Shows the prompt to the user.

```python
    response2 = model.generate_content(prompt2)
```
**Explanation:** Generates content for the creative prompt.

```python
    print(f"🤖 Response:\n{response2.text}\n")
```
**Explanation:** Prints the AI's creative response. The `\n` before `{response2.text}` puts the response on a new line.

```python
    # Example 3: Explanation
    print("\n3️⃣ Technical Explanation:")
```
**Explanation:** Header for the third example demonstrating explanations.

```python
    prompt3 = "Explain neural networks to a 10-year-old."
```
**Explanation:** A prompt requesting simple explanations. The "to a 10-year-old" part guides the AI to use simple language.

```python
    print(f"📝 Prompt: {prompt3}")
```
**Explanation:** Shows what we're asking.

```python
    response3 = model.generate_content(prompt3)
```
**Explanation:** Generates the explanation.

```python
    print(f"🤖 Response: {response3.text}\n")
```
**Explanation:** Prints the AI's simplified explanation.

---

## Section 2: Question Answering Function

```python
# ============================================================================
# SECTION 2: Question Answering
# ============================================================================
```
**Explanation:** Section separator for Q&A demonstrations.

```python
def question_answering():
```
**Explanation:** Defines function to demonstrate different types of questions.

```python
    """
    Different styles of Q&A
    """
```
**Explanation:** Brief docstring.

```python
    print("\n" + "=" * 60)
    print("SECTION 2: Question Answering")
    print("=" * 60)
```
**Explanation:** Prints section header.

```python
    model = genai.GenerativeModel('gemini-pro')
```
**Explanation:** Creates a model instance for this function.

```python
    # Example 1: Factual question
    print("\n1️⃣ Factual Question:")
```
**Explanation:** Labels the first question type - factual questions with verifiable answers.

```python
    prompt = "Who invented the Python programming language and when?"
```
**Explanation:** A factual question about Python's creator. Uses single variable name `prompt` since we're not reusing these.

```python
    print(f"📝 Prompt: {prompt}")
```
**Explanation:** Displays the question.

```python
    response = model.generate_content(prompt)
```
**Explanation:** Gets the answer from the AI.

```python
    print(f"🤖 Response: {response.text}\n")
```
**Explanation:** Prints the factual answer.

```python
    # Example 2: Comparison question
    print("\n2️⃣ Comparison Question:")
```
**Explanation:** Labels the second type - comparison questions that analyze differences.

```python
    prompt = "What are the key differences between supervised and unsupervised learning?"
```
**Explanation:** A question requesting comparison between two concepts.

```python
    print(f"📝 Prompt: {prompt}")
    
    response = model.generate_content(prompt)
    print(f"🤖 Response: {response.text}\n")
```
**Explanation:** Shows prompt, generates response, and prints answer - same pattern as before.

```python
    # Example 3: Opinion question
    print("\n3️⃣ Opinion-Based Question:")
```
**Explanation:** Labels the third type - questions asking for pros/cons or opinions.

```python
    prompt = "What are the pros and cons of using AI in healthcare?"
```
**Explanation:** An opinion question asking for balanced analysis.

```python
    print(f"📝 Prompt: {prompt}")
    
    response = model.generate_content(prompt)
    print(f"🤖 Response: {response.text}\n")
```
**Explanation:** Same pattern: show, generate, print.

---

## Section 3: Prompt Engineering Techniques

```python
# ============================================================================
# SECTION 3: Prompt Engineering Techniques
# ============================================================================
```
**Explanation:** Section separator for prompt engineering demonstrations.

```python
def prompt_engineering_examples():
```
**Explanation:** Defines function showing how prompt quality affects output quality.

```python
    """
    Demonstrate how different prompts affect output quality
    """
```
**Explanation:** Docstring describing the educational purpose.

```python
    print("\n" + "=" * 60)
    print("SECTION 3: Prompt Engineering Techniques")
    print("=" * 60)
```
**Explanation:** Section header.

```python
    model = genai.GenerativeModel('gemini-pro')
```
**Explanation:** Creates model instance.

```python
    # Technique 1: Vague vs Specific
    print("\n1️⃣ VAGUE vs SPECIFIC Prompts:\n")
```
**Explanation:** Labels the first technique comparison. `\n` at end adds spacing.

```python
    print("❌ Vague prompt:")
```
**Explanation:** Red X emoji indicates this is the bad example.

```python
    vague_prompt = "Tell me about AI."
```
**Explanation:** An overly broad, vague prompt that will get generic responses.

```python
    print(f"   '{vague_prompt}'")
```
**Explanation:** Shows the vague prompt. Spaces indent it for visual hierarchy.

```python
    response = model.generate_content(vague_prompt)
```
**Explanation:** Generates content with the vague prompt.

```python
    print(f"   Response length: {len(response.text)} characters")
```
**Explanation:** Shows character count using `len()` function. Helps demonstrate that vague prompts often get longer, less focused responses.

```python
    print(f"   Preview: {response.text[:150]}...\n")
```
**Explanation:** Shows first 150 characters using slice `[:150]`. The `...` indicates truncation. Shows quality without overwhelming output.

```python
    print("✅ Specific prompt:")
```
**Explanation:** Green checkmark emoji indicates this is the good example.

```python
    specific_prompt = "List 3 practical applications of AI in education with one-sentence descriptions."
```
**Explanation:** A specific, detailed prompt that clearly states what format and content is wanted.

```python
    print(f"   '{specific_prompt}'")
```
**Explanation:** Shows the specific prompt.

```python
    response = model.generate_content(specific_prompt)
```
**Explanation:** Generates with the specific prompt.

```python
    print(f"   Response:\n{response.text}\n")
```
**Explanation:** Prints full response since specific prompts usually give concise, useful answers.

```python
    # Technique 2: Role-based prompting
    print("\n2️⃣ ROLE-BASED Prompting:\n")
```
**Explanation:** Header for the second technique.

```python
    role_prompt = """You are an experienced Python tutor. 
Explain what a decorator is to a beginner in simple terms with a short example."""
```
**Explanation:** Multi-line string (triple quotes) containing a role instruction. "You are..." sets the AI's persona, which affects tone and detail level.

```python
    print(f"📝 Prompt: {role_prompt}")
```
**Explanation:** Shows the role-based prompt.

```python
    response = model.generate_content(role_prompt)
    print(f"🤖 Response:\n{response.text}\n")
```
**Explanation:** Generates and prints the response. The role context should produce a tutor-like explanation.

```python
    # Technique 3: Step-by-step instructions
    print("\n3️⃣ STEP-BY-STEP Instructions:\n")
```
**Explanation:** Header for third technique.

```python
    step_prompt = """Break down the following task into steps:
How to create a simple REST API in Python using Flask.
Number each step and keep it concise."""
```
**Explanation:** Multi-line prompt asking for structured, numbered steps. Specifies both content and format.

```python
    print(f"📝 Prompt: {step_prompt}")
    response = model.generate_content(step_prompt)
    print(f"🤖 Response:\n{response.text}\n")
```
**Explanation:** Show, generate, print pattern - requesting step-by-step output.

```python
    # Technique 4: Format specification
    print("\n4️⃣ FORMAT Specification:\n")
```
**Explanation:** Header for fourth technique about specifying output format.

```python
    format_prompt = """List 3 benefits of using version control.
Format your response as:
Benefit 1: [description]
Benefit 2: [description]
Benefit 3: [description]"""
```
**Explanation:** Multi-line prompt that explicitly shows the desired output format. This ensures consistent, parseable responses.

```python
    print(f"📝 Prompt: {format_prompt}")
    response = model.generate_content(format_prompt)
    print(f"🤖 Response:\n{response.text}\n")
```
**Explanation:** Generate and show the formatted response.

---

## Section 4: Interactive Single-Turn Chat

```python
# ============================================================================
# SECTION 4: Interactive Chat (Single Turn)
# ============================================================================
```
**Explanation:** Section separator for interactive chat.

```python
def interactive_single_turn():
```
**Explanation:** Defines function for interactive user input, but without conversation memory.

```python
    """
    Single-turn conversation (no memory)
    """
```
**Explanation:** Docstring emphasizing this doesn't remember previous messages.

```python
    print("\n" + "=" * 60)
    print("SECTION 4: Interactive Single-Turn Chat")
    print("=" * 60)
    print("\nNote: Each question is independent (no conversation memory)")
    print("Type 'quit' to exit\n")
```
**Explanation:** Prints header and important note about no memory. Sets user expectations and shows exit command.

```python
    model = genai.GenerativeModel('gemini-pro')
```
**Explanation:** Creates model instance.

```python
    conversation_count = 0
```
**Explanation:** Initializes a counter variable to track how many messages have been sent. Starts at 0.

```python
    while True:
```
**Explanation:** Starts an infinite loop. Will continue until we explicitly `break` out of it.

```python
        user_input = input("You: ").strip()
```
**Explanation:** Uses `input()` to get text from user. The string "You: " is the prompt shown. `.strip()` removes leading/trailing whitespace.

```python
        if user_input.lower() in ['quit', 'exit', 'q']:
```
**Explanation:** Checks if user wants to exit. `.lower()` converts to lowercase so "QUIT" and "quit" both work. `in [...]` checks if the input matches any item in the list.

```python
            print("👋 Goodbye!")
            break
```
**Explanation:** Prints goodbye message and breaks out of the while loop, ending the function.

```python
        if not user_input:
```
**Explanation:** Checks if input is empty (user just pressed Enter). Empty strings are "falsy" so `not ""` is True.

```python
            print("⚠️  Please enter a message\n")
            continue
```
**Explanation:** Prints warning and uses `continue` to skip the rest of this loop iteration and start over at `while True`.

```python
        try:
```
**Explanation:** Starts try-except block to handle errors gracefully during generation.

```python
            conversation_count += 1
```
**Explanation:** Increments the counter by 1. Shorthand for `conversation_count = conversation_count + 1`.

```python
            print("🤖 AI: ", end="")
```
**Explanation:** Prints the AI label. `end=""` prevents automatic newline, so the response appears on the same line.

```python
            response = model.generate_content(user_input)
```
**Explanation:** Generates response to the user's input.

```python
            print(response.text)
            print()
```
**Explanation:** Prints the response text. Second `print()` adds a blank line for spacing.

```python
            if conversation_count >= 3:
```
**Explanation:** After 3 messages, show an educational note. This helps students understand the limitation.

```python
                print("💡 Notice: Each response is independent. No memory of previous questions.")
                print("   We'll learn how to add memory in Module 06!\n")
```
**Explanation:** Educational messages explaining the limitation and previewing future learning. Lightbulb emoji indicates this is a tip.

```python
        except Exception as e:
```
**Explanation:** Catches any error that occurred in the try block.

```python
            print(f"❌ Error: {e}\n")
```
**Explanation:** Prints the error message so chat can continue even if one request fails.

---

## Section 5: Long-Form Content Generation

```python
# ============================================================================
# SECTION 5: Long-Form Content Generation
# ============================================================================
```
**Explanation:** Section separator.

```python
def long_form_generation():
```
**Explanation:** Function to demonstrate generating longer, structured content.

```python
    """
    Generate longer, structured content
    """
```
**Explanation:** Docstring.

```python
    print("\n" + "=" * 60)
    print("SECTION 5: Long-Form Content Generation")
    print("=" * 60)
```
**Explanation:** Section header.

```python
    model = genai.GenerativeModel('gemini-pro')
```
**Explanation:** Creates model instance.

```python
    # Example: Blog post generation
    print("\n📝 Generating a blog post outline...\n")
```
**Explanation:** Status message showing what's being generated.

```python
    prompt = """Write a detailed outline for a blog post about "Getting Started with AI for Beginners".

Include:
- An engaging introduction
- 5 main sections with subpoints
- A conclusion
- Keep it educational and encouraging"""
```
**Explanation:** Multi-line prompt with detailed instructions. Specifies structure (intro, 5 sections, conclusion) and tone (educational, encouraging). This guides the AI to produce a specific format.

```python
    response = model.generate_content(prompt)
```
**Explanation:** Generates the blog outline.

```python
    print("=" * 60)
    print("📄 Generated Blog Outline:")
    print("=" * 60)
```
**Explanation:** Prints a header to frame the generated content.

```python
    print(response.text)
```
**Explanation:** Prints the full blog outline. No truncation since this is the main deliverable.

```python
    print("=" * 60)
```
**Explanation:** Closing separator line.

---

## Section 6: Code Generation Examples

```python
# ============================================================================
# SECTION 6: Code Generation
# ============================================================================
```
**Explanation:** Section separator for code generation.

```python
def code_generation_examples():
```
**Explanation:** Function demonstrating how to use AI for code generation.

```python
    """
    Using AI to generate code
    """
```
**Explanation:** Docstring.

```python
    print("\n" + "=" * 60)
    print("SECTION 6: Code Generation")
    print("=" * 60)
```
**Explanation:** Section header.

```python
    model = genai.GenerativeModel('gemini-pro')
```
**Explanation:** Creates model.

```python
    # Example 1: Simple function
    print("\n1️⃣ Generate a Simple Function:\n")
```
**Explanation:** Header for first code generation example.

```python
    prompt1 = """Write a Python function that calculates the factorial of a number.
Include:
- Docstring
- Input validation
- Example usage"""
```
**Explanation:** Structured prompt for code generation. Specifies what the function should do and what quality features to include (docstring, validation, example).

```python
    print(f"📝 Request: {prompt1.split('.')[0]}...")
```
**Explanation:** Prints abbreviated version of prompt. `split('.')` splits the string at periods, `[0]` takes first sentence. The `...` indicates truncation.

```python
    response1 = model.generate_content(prompt1)
```
**Explanation:** Generates the code.

```python
    print("\n🤖 Generated Code:")
    print("-" * 60)
```
**Explanation:** Header for the code output. Dashes create a clear boundary.

```python
    print(response1.text)
```
**Explanation:** Prints the generated code.

```python
    print("-" * 60)
```
**Explanation:** Closing boundary line.

```python
    # Example 2: Class generation
    print("\n2️⃣ Generate a Class:\n")
```
**Explanation:** Header for second example.

```python
    prompt2 = """Create a Python class called 'Student' with:
- Attributes: name, age, grades (list)
- Method to add a grade
- Method to calculate average grade
- Include docstrings"""
```
**Explanation:** Detailed prompt for class generation. Lists exact attributes and methods needed. This specificity ensures the AI generates exactly what's needed.

```python
    print(f"📝 Request: Create a Student class...")
```
**Explanation:** Shows abbreviated request.

```python
    response2 = model.generate_content(prompt2)
    print("\n🤖 Generated Code:")
    print("-" * 60)
    print(response2.text)
    print("-" * 60)
```
**Explanation:** Generate, frame, and print the class code.

---

## Section 7: Practical Use Cases

```python
# ============================================================================
# SECTION 7: Practical Use Cases
# ============================================================================
```
**Explanation:** Section separator for real-world applications.

```python
def practical_use_cases():
```
**Explanation:** Function showing practical applications of text generation.

```python
    """
    Real-world applications of text generation
    """
```
**Explanation:** Docstring.

```python
    print("\n" + "=" * 60)
    print("SECTION 7: Practical Use Cases")
    print("=" * 60)
```
**Explanation:** Section header.

```python
    model = genai.GenerativeModel('gemini-pro')
```
**Explanation:** Creates model.

```python
    # Use case 1: Email writing
    print("\n1️⃣ Professional Email Writing:")
```
**Explanation:** First use case header.

```python
    prompt = """Write a professional email to request a meeting with a professor 
to discuss a research opportunity in machine learning. Keep it concise and polite."""
```
**Explanation:** Prompt for professional email. Specifies context (professor meeting), topic (ML research), and tone (concise, polite).

```python
    response = model.generate_content(prompt)
    print(response.text)
    print()
```
**Explanation:** Generates and prints the email.

```python
    # Use case 2: Summarization
    print("\n2️⃣ Text Summarization:")
```
**Explanation:** Second use case header.

```python
    long_text = """Artificial Intelligence (AI) has transformed numerous industries 
over the past decade. From healthcare to finance, education to entertainment, AI 
systems are now integral to modern operations. Machine learning algorithms can 
analyze vast amounts of data to identify patterns and make predictions. Deep 
learning, a subset of machine learning, has been particularly successful in areas 
like computer vision and natural language processing. However, the rapid adoption 
of AI also raises important ethical questions about privacy, bias, and job 
displacement that society must address."""
```
**Explanation:** Multi-line string containing a long paragraph to be summarized. This is the input text.

```python
    prompt = f"Summarize this text in 2 sentences:\n\n{long_text}"
```
**Explanation:** Creates prompt by combining instruction with the text. `\n\n` adds spacing between instruction and text. The f-string embeds the `long_text` variable.

```python
    response = model.generate_content(prompt)
```
**Explanation:** Generates the summary.

```python
    print(f"Original: {len(long_text)} characters")
```
**Explanation:** Shows original text length for comparison.

```python
    print(f"Summary: {response.text}")
    print()
```
**Explanation:** Prints the condensed summary.

```python
    # Use case 3: Translation/Rewriting
    print("\n3️⃣ Text Transformation:")
```
**Explanation:** Third use case header.

```python
    prompt = """Rewrite this technical sentence in simple English:
"The convolutional neural network employs hierarchical feature extraction 
to perform image classification tasks with high accuracy."
"""
```
**Explanation:** Prompt asking to simplify complex technical language. Shows the transformation use case.

```python
    response = model.generate_content(prompt)
    print(f"Simplified: {response.text}")
```
**Explanation:** Generates and prints the simplified version.

---

## Main Execution Function

```python
# ============================================================================
# MAIN EXECUTION
# ============================================================================
```
**Explanation:** Section separator for main function.

```python
def main():
```
**Explanation:** Defines the main orchestration function.

```python
    """
    Main function with menu-driven interface
    """
```
**Explanation:** Docstring describing this as a menu system.

```python
    print("\n")
    print("🎓 " + "=" * 58 + " 🎓")
    print("      GENERATIVE AI SESSION - MODULE 2: TEXT CHAT")
    print("🎓 " + "=" * 58 + " 🎓")
```
**Explanation:** Prints decorative header for the module.

```python
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
```
**Explanation:** Multi-line string stored in `menu` variable. Lists all available options. This makes it easy to reprint the menu.

```python
    while True:
```
**Explanation:** Infinite loop for menu system. Keeps showing menu until user quits.

```python
        print(menu)
```
**Explanation:** Prints the menu options.

```python
        choice = input("Your choice: ").strip().lower()
```
**Explanation:** Gets user input. `.strip()` removes whitespace. `.lower()` converts to lowercase so "QUIT" and "quit" both work.

```python
        if choice == 'quit' or choice == 'q':
```
**Explanation:** Checks if user wants to quit. Accepts both "quit" and "q".

```python
            print("👋 Goodbye!")
            break
```
**Explanation:** Prints goodbye and exits the loop.

```python
        elif choice == '1':
            simple_text_generation()
```
**Explanation:** If user chose '1', call the corresponding function. `elif` means "else if" - only checked if previous conditions were false.

```python
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
```
**Explanation:** Series of elif statements checking for choices 2-7. Each calls the corresponding function.

```python
        elif choice == 'all':
```
**Explanation:** Special option to run all sections at once.

```python
            simple_text_generation()
            question_answering()
            prompt_engineering_examples()
            long_form_generation()
            code_generation_examples()
            practical_use_cases()
```
**Explanation:** Calls most functions in sequence. Note: skips `interactive_single_turn()` since it requires user interaction.

```python
            print("\n✅ All sections completed!")
            print("💡 Try section 4 separately for interactive chat")
```
**Explanation:** Success message after running all sections. Reminds user about the interactive section.

```python
        else:
            print("⚠️  Invalid choice. Please try again.")
```
**Explanation:** If none of the above conditions matched, the input was invalid. Shows warning and loop continues.

---

## Script Entry Point

```python
if __name__ == "__main__":
```
**Explanation:** Checks if this script is being run directly (not imported as a module).

```python
    main()
```
**Explanation:** If run directly, call the main function to start the program.

```python
    # Teaching Questions:
    # 1. What makes a good prompt?
    # 2. How does specificity affect response quality?
    # 3. What are the limitations of single-turn conversations?
```
**Explanation:** Comments for instructors with discussion questions to assess student understanding.

---

## Summary

This module demonstrates:

1. **Multiple text generation patterns**: Questions, creative writing, explanations, code
2. **Prompt engineering techniques**: Vague vs specific, role-based, step-by-step, format specification
3. **Interactive chat**: Using `input()` for user interaction, `while True` loops
4. **String manipulation**: f-strings, slicing `[:150]`, `.split()`, `.strip()`, `.lower()`
5. **Control flow**: if/elif/else chains, try-except blocks, continue/break statements
6. **Menu-driven interface**: User-friendly navigation between sections
7. **Practical applications**: Email writing, summarization, code generation

The code is organized with clear sections, consistent patterns, and educational comments throughout.
