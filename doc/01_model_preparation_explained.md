# Module 01 - Model Preparation - Detailed Code Explanation

This document explains every line of code in the Model Preparation module.

---

## 📊 Visual Overview: How AI API Setup Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    YOUR PYTHON APPLICATION                      │
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    │
│  │   Load API   │ → │  Configure   │ → │   Create     │    │
│  │   Key from   │    │   Gemini     │    │   Model      │    │
│  │   .env file  │    │   Library    │    │   Instance   │    │
│  └──────────────┘    └──────────────┘    └──────────────┘    │
│         │                    │                    │            │
└─────────┼────────────────────┼────────────────────┼────────────┘
          │                    │                    │
          ▼                    ▼                    ▼
    ┌──────────┐         ┌──────────┐        ┌──────────┐
    │  .env    │         │  genai   │        │  Model   │
    │  File    │         │  Setup   │        │  Ready!  │
    └──────────┘         └──────────┘        └──────────┘
          │                    │                    │
          └────────────────────┴────────────────────┘
                               │
                               ▼
                    ┌────────────────────┐
                    │  Send Request to   │
                    │  Google's Gemini   │
                    │  API via HTTPS     │
                    └──────────┬─────────┘
                               │
                               ▼
                    ┌────────────────────┐
                    │  Gemini Servers    │
                    │  Process Request   │
                    └──────────┬─────────┘
                               │
                               ▼
                    ┌────────────────────┐
                    │  Response Returns  │
                    │  to Your Code      │
                    └────────────────────┘
```

---

## 🔐 API Key Security Flow

```
❌ WRONG WAY (Hardcoded):
┌─────────────────────────────────┐
│  code.py                        │
│  ───────                        │
│  api_key = "AIza123secret456"  │  ← Visible in code!
│                                 │  ← Gets committed to Git!
│                                 │  ← Anyone can steal it!
└─────────────────────────────────┘

✅ RIGHT WAY (Environment Variables):
┌─────────────────┐      ┌──────────────────┐      ┌─────────────┐
│   .env file     │ ──→  │   Your Code      │ ──→  │   Gemini    │
│   (ignored by   │      │   ────────       │      │   API       │
│    Git!)        │      │   load_dotenv()  │      │             │
│                 │      │   api_key =      │      │             │
│ GOOGLE_API_KEY= │      │   os.getenv()    │      │             │
│ AIza123...      │      │                  │      │             │
└─────────────────┘      └──────────────────┘      └─────────────┘
     ↑                            │
     │                            ▼
     │                   ┌────────────────┐
     │                   │ Key is secure! │
     │                   │ Not in code!   │
     │                   │ Not in Git!    │
     └───────────────────┴────────────────┘
```

---

## 🏗️ Code Structure Diagram

```
┌────────────────────────────────────────────────────────────────┐
│  01_model_preparation.py                                       │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  📦 IMPORTS                                                    │
│  ├─ os                  (system operations)                   │
│  ├─ dotenv              (load .env files)                     │
│  └─ google.generativeai (Gemini API)                          │
│                                                                │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  🔧 FUNCTIONS                                                  │
│                                                                │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ 1. setup_environment()                                  │ │
│  │    ├─ Load .env file                                    │ │
│  │    ├─ Check if API key exists                           │ │
│  │    └─ Configure Gemini with API key                     │ │
│  └─────────────────────────────────────────────────────────┘ │
│                          ↓                                     │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ 2. test_text_model()                                    │ │
│  │    ├─ Create text model (gemini-2.0-flash)             │ │
│  │    ├─ Send test prompt                                  │ │
│  │    └─ Display response                                  │ │
│  └─────────────────────────────────────────────────────────┘ │
│                          ↓                                     │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ 3. test_vision_model()                                  │ │
│  │    ├─ Create vision model (gemini-1.5-flash)           │ │
│  │    ├─ Explain capabilities                              │ │
│  │    └─ Show example use cases                            │ │
│  └─────────────────────────────────────────────────────────┘ │
│                          ↓                                     │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ 4. main()                                               │ │
│  │    ├─ Call setup_environment()                          │ │
│  │    ├─ Call test_text_model()                            │ │
│  │    └─ Call test_vision_model()                          │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Execution Flow

```
START
  │
  ▼
┌─────────────────────┐
│ if __name__ ==      │  ← Check if script is run directly
│    "__main__":      │
└──────────┬──────────┘
           │ YES
           ▼
┌─────────────────────┐
│  main()             │  ← Entry point function
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ setup_environment() │
│ ─────────────────── │
│ 1. Load .env        │
│ 2. Get API key      │
│ 3. Configure genai  │
└──────────┬──────────┘
           │
           ├─── Success? ───┐
           │                │
        YES│             NO │
           ▼                ▼
┌─────────────────┐   ┌──────────────┐
│ test_text_model │   │ Print error  │
│ ─────────────── │   │ Exit         │
│ Create model    │   └──────────────┘
│ Send "Hello"    │
│ Print response  │
└────────┬────────┘
         │
         ▼
┌──────────────────┐
│ test_vision_model│
│ ──────────────── │
│ Explain vision   │
│ Show examples    │
└────────┬─────────┘
         │
         ▼
┌─────────────────┐
│  Success! ✅    │
│  Ready to code  │
└─────────────────┘
         │
         ▼
       END
```

---

## 🌐 API Communication Flow

```
Your Computer                    Internet                    Google Servers
─────────────                    ────────                    ──────────────

┌──────────────┐                                          ┌────────────────┐
│ Python Code  │                                          │ Gemini API     │
│              │                                          │ Servers        │
│ model.       │                                          │                │
│ generate_    │  ──1. HTTPS Request──────────────────>  │                │
│ content()    │     (with API key + prompt)              │                │
│              │                                          │                │
│              │                                          │ ┌────────────┐ │
│              │                                          │ │ Validate   │ │
│              │                                          │ │ API Key    │ │
│              │                                          │ └─────┬──────┘ │
│              │                                          │       │        │
│              │                                          │       ▼        │
│              │                                          │ ┌────────────┐ │
│              │                                          │ │ Process    │ │
│              │                                          │ │ Prompt     │ │
│              │                                          │ └─────┬──────┘ │
│              │                                          │       │        │
│              │                                          │       ▼        │
│              │                                          │ ┌────────────┐ │
│              │                                          │ │ Generate   │ │
│              │                                          │ │ Response   │ │
│              │                                          │ └─────┬──────┘ │
│              │                                          │       │        │
│              │  <──2. HTTPS Response─────────────────  │       │        │
│              │     (JSON with generated text)           │       │        │
│              │                                          └───────┴────────┘
│ Print        │
│ response     │
│              │
└──────────────┘

Time: ~1-3 seconds total
Data: Encrypted via HTTPS (secure)
Cost: Free tier or pay-per-token
```

---

## 💾 File Structure in Your Project

```
your-project/
│
├── .env                          ← Your secrets (API keys)
│   GOOGLE_API_KEY=AIza...        ← Never commit to Git!
│
├── .gitignore                    ← Tells Git to ignore .env
│   .env
│
├── 01_model_preparation.py       ← This script
│   │
│   ├─ import os                  ← Read environment
│   ├─ import dotenv              ← Load .env file
│   ├─ import genai               ← Gemini API
│   │
│   └─ Functions:
│       ├─ setup_environment()    ← Load API key
│       ├─ test_text_model()      ← Test text generation
│       └─ test_vision_model()    ← Test vision capabilities
│
└── requirements.txt              ← Dependencies
    google-generativeai
    python-dotenv
```

---

## Module Documentation Block

```python
"""
01 - AI Model Preparation
=========================
```
**Explanation:** This is a docstring (multi-line comment) that documents what this module does. The triple quotes allow multi-line text.

```python
This module demonstrates the fundamental setup for working with Google's Gemini API.
Students will learn:
- How to configure API keys securely
- Initialize the Gemini model
- Test basic connectivity
- Understand model selection
- Handle common errors
```
**Explanation:** Describes the learning objectives of this module - what students will be able to do after completing it.

```python
Teaching Points:
- Always use environment variables for API keys (never hardcode!)
- Different models for different tasks (gemini-pro vs gemini-pro-vision)
- Importance of error handling in production
"""
```
**Explanation:** Key concepts to emphasize when teaching. The closing `"""` ends the docstring.

---

## Import Statements

```python
import os
```
**Explanation:** Imports the `os` module, which provides functions to interact with the operating system (like reading environment variables).

```python
from dotenv import load_dotenv
```
**Explanation:** Imports the `load_dotenv` function from the `dotenv` package. This function reads `.env` files and loads variables into the environment.

```python
import google.generativeai as genai
```
**Explanation:** Imports Google's Generative AI library and gives it a shorter alias `genai` for convenience. This is the main SDK for working with Gemini.

---

## Section 1: Environment Setup Function

```python
# ============================================================================
# SECTION 1: Environment Setup
# ============================================================================
```
**Explanation:** Visual separator comment to organize code into logical sections. Makes code easier to read and navigate.

```python
def setup_environment():
```
**Explanation:** Defines a function named `setup_environment`. Functions are reusable blocks of code that perform specific tasks.

```python
    """
    Load environment variables from .env file
    This is the secure way to handle API keys
    """
```
**Explanation:** Function docstring explaining what this function does. Good practice for documentation.

```python
    print("=" * 60)
```
**Explanation:** Prints 60 equal signs to create a visual separator line. The `*` operator repeats the string.

```python
    print("SECTION 1: Environment Setup")
```
**Explanation:** Prints a header to show which section is running.

```python
    print("=" * 60)
```
**Explanation:** Prints another separator line to frame the header.

```python
    # Load environment variables
    load_dotenv()
```
**Explanation:** Calls `load_dotenv()` which reads the `.env` file and loads all variables into the system environment. The comment explains what this line does.

```python
    # Get API key
    api_key = os.getenv('GOOGLE_API_KEY')
```
**Explanation:** Uses `os.getenv()` to retrieve the value of the `GOOGLE_API_KEY` environment variable and stores it in the `api_key` variable.

```python
    if not api_key:
```
**Explanation:** Checks if `api_key` is None or empty. The `not` operator converts truthy/falsy values to boolean.

```python
        raise ValueError(
```
**Explanation:** If no API key was found, raise (throw) a `ValueError` exception to stop execution.

```python
            "❌ GOOGLE_API_KEY not found!\n"
```
**Explanation:** First line of the error message. `\n` creates a new line. The emoji makes it visually clear this is an error.

```python
            "Please create a .env file and add your API key:\n"
            "GOOGLE_API_KEY=your_key_here"
        )
```
**Explanation:** Continuation of the error message with instructions on how to fix the problem. The closing parenthesis ends the `raise` statement.

```python
    print("✅ Environment variables loaded successfully")
```
**Explanation:** If we reach this line, the API key exists. Print a success message with a checkmark emoji.

```python
    print(f"✅ API Key found: {api_key[:10]}..." + "*" * 20)
```
**Explanation:** Prints the first 10 characters of the API key followed by asterisks. This confirms the key is loaded without showing the full key (security). `f""` is an f-string that allows embedding variables with `{}`. `[:10]` is a slice that takes the first 10 characters.

```python
    return api_key
```
**Explanation:** Returns the API key so other functions can use it. This is the output of the function.

---

## Section 2: API Configuration Function

```python
# ============================================================================
# SECTION 2: API Configuration
# ============================================================================
```
**Explanation:** Another visual separator for the next section.

```python
def configure_api(api_key):
```
**Explanation:** Defines a function that takes `api_key` as a parameter (input). This function will configure the Gemini API.

```python
    """
    Configure the Google Generative AI API with your key
    """
```
**Explanation:** Function docstring describing its purpose.

```python
    print("\n" + "=" * 60)
```
**Explanation:** `\n` adds a blank line before printing 60 equal signs. This creates spacing between sections.

```python
    print("SECTION 2: API Configuration")
    print("=" * 60)
```
**Explanation:** Prints the section header with separators.

```python
    try:
```
**Explanation:** Starts a try-except block. Code inside `try` will be executed, and if an error occurs, the `except` block will handle it.

```python
        genai.configure(api_key=api_key)
```
**Explanation:** Calls the `configure` method from the `genai` library, passing our API key. This sets up authentication for all future API calls.

```python
        print("✅ Gemini API configured successfully")
```
**Explanation:** If configuration succeeds, print a success message.

```python
    except Exception as e:
```
**Explanation:** If any exception (error) occurs in the `try` block, catch it and store it in variable `e`.

```python
        print(f"❌ Error configuring API: {e}")
```
**Explanation:** Print the error message to help debug what went wrong.

```python
        raise
```
**Explanation:** Re-raise the exception so the program stops. This prevents continuing with a misconfigured API.

---

## Section 3: Model Initialization Function

```python
# ============================================================================
# SECTION 3: Model Initialization
# ============================================================================
```
**Explanation:** Section separator for model initialization.

```python
def initialize_models():
```
**Explanation:** Defines a function that takes no parameters. It will create and return model objects.

```python
    """
    Initialize different models for different use cases
    """
```
**Explanation:** Function docstring.

```python
    print("\n" + "=" * 60)
    print("SECTION 3: Model Initialization")
    print("=" * 60)
```
**Explanation:** Prints section header with spacing and separators.

```python
    # Text-only model
    text_model = genai.GenerativeModel('gemini-pro')
```
**Explanation:** Creates a GenerativeModel object for text-only tasks. The string `'gemini-pro'` specifies which model version to use. Stores it in `text_model` variable.

```python
    print("✅ Gemini Pro (text) model initialized")
```
**Explanation:** Confirms the text model was created successfully.

```python
    print("   Use case: Text generation, chat, code generation")
```
**Explanation:** Explains when to use this model. The spaces indent for better readability.

```python
    # Vision model (for images and video)
    vision_model = genai.GenerativeModel('gemini-pro-vision')
```
**Explanation:** Creates a GenerativeModel object for multimodal tasks (text + images/video). Uses `'gemini-pro-vision'` model version.

```python
    print("✅ Gemini Pro Vision model initialized")
    print("   Use case: Image understanding, video analysis")
```
**Explanation:** Confirms vision model creation and explains its use cases.

```python
    return text_model, vision_model
```
**Explanation:** Returns both model objects as a tuple (comma-separated values). The calling code can unpack these into two variables.

---

## Section 4: Testing Basic Connectivity

```python
# ============================================================================
# SECTION 4: Testing Basic Connectivity
# ============================================================================
```
**Explanation:** Section separator for connectivity testing.

```python
def test_basic_generation(model):
```
**Explanation:** Defines a function that takes a `model` object as parameter. This will test if the model can generate text.

```python
    """
    Test basic text generation to ensure everything is working
    """
```
**Explanation:** Function docstring.

```python
    print("\n" + "=" * 60)
    print("SECTION 4: Testing Basic Connectivity")
    print("=" * 60)
```
**Explanation:** Prints section header.

```python
    try:
```
**Explanation:** Starts try-except block to handle any errors during generation.

```python
        # Simple test prompt
        prompt = "Say 'Hello! The API is working correctly.' in a friendly way."
```
**Explanation:** Creates a test prompt string. This is what we'll send to the AI model.

```python
        print(f"\n📝 Test Prompt: {prompt}")
```
**Explanation:** Prints the prompt so students can see what we're sending to the API. The emoji makes it visually distinct.

```python
        # Generate response
        print("\n⏳ Generating response...")
```
**Explanation:** Prints a status message with hourglass emoji to show we're waiting for the API.

```python
        response = model.generate_content(prompt)
```
**Explanation:** Calls the `generate_content` method on our model object, passing the prompt. This makes an API call to Gemini and stores the response object.

```python
        print("\n✅ Response received successfully!")
```
**Explanation:** If we reach this line, the API call succeeded. Print success message.

```python
        print("\n" + "-" * 60)
```
**Explanation:** Prints a line of dashes to frame the AI response.

```python
        print("🤖 AI Response:")
```
**Explanation:** Header indicating the AI's response follows. Robot emoji makes it clear this is AI output.

```python
        print("-" * 60)
```
**Explanation:** Another separator line.

```python
        print(response.text)
```
**Explanation:** Prints the actual text content from the AI's response. `.text` accesses the text property of the response object.

```python
        print("-" * 60)
```
**Explanation:** Closing separator line to frame the response.

```python
        return True
```
**Explanation:** Returns `True` to indicate the test succeeded.

```python
    except Exception as e:
```
**Explanation:** If any error occurred in the try block, catch it.

```python
        print(f"\n❌ Error during generation: {e}")
```
**Explanation:** Print the error message.

```python
        print("\nCommon issues:")
        print("  1. Invalid API key")
        print("  2. API quota exceeded")
        print("  3. Network connectivity issues")
```
**Explanation:** Provides helpful troubleshooting hints for common problems.

```python
        return False
```
**Explanation:** Returns `False` to indicate the test failed.

---

## Section 5: Display Available Models

```python
# ============================================================================
# SECTION 5: Model Information
# ============================================================================
```
**Explanation:** Section separator.

```python
def display_available_models():
```
**Explanation:** Defines a function to list all available Gemini models.

```python
    """
    List all available models
    """
```
**Explanation:** Function docstring.

```python
    print("\n" + "=" * 60)
    print("SECTION 5: Available Models")
    print("=" * 60)
```
**Explanation:** Prints section header.

```python
    try:
```
**Explanation:** Start try-except block for error handling.

```python
        print("\n📋 Listing available Gemini models:\n")
```
**Explanation:** Prints a header with clipboard emoji.

```python
        for model in genai.list_models():
```
**Explanation:** Loops through all models returned by `genai.list_models()`. Each iteration, `model` holds one model object.

```python
            if 'generateContent' in model.supported_generation_methods:
```
**Explanation:** Checks if this model supports content generation (some models only do embeddings). Only shows generation-capable models.

```python
                print(f"  • {model.name}")
```
**Explanation:** Prints the model's name with a bullet point. Indentation shows this is inside the if/for blocks.

```python
                print(f"    Description: {model.display_name}")
```
**Explanation:** Prints the model's display name (human-readable description).

```python
                print(f"    Input token limit: {model.input_token_limit}")
```
**Explanation:** Prints maximum input size. Tokens are chunks of text (roughly 4 characters each).

```python
                print(f"    Output token limit: {model.output_token_limit}")
```
**Explanation:** Prints maximum output size the model can generate.

```python
                print()
```
**Explanation:** Prints a blank line for spacing between models.

```python
    except Exception as e:
        print(f"❌ Error listing models: {e}")
```
**Explanation:** If listing models fails, catch the error and print it.

---

## Section 6: Error Handling Demonstration

```python
# ============================================================================
# SECTION 6: Error Handling Examples
# ============================================================================
```
**Explanation:** Section separator for error handling demos.

```python
def demonstrate_error_handling(model):
```
**Explanation:** Function to show common errors and best practices.

```python
    """
    Show common errors and how to handle them
    """
```
**Explanation:** Function docstring.

```python
    print("\n" + "=" * 60)
    print("SECTION 6: Error Handling")
    print("=" * 60)
```
**Explanation:** Prints section header.

```python
    # Example 1: Empty prompt
    print("\n1️⃣ Testing empty prompt handling:")
```
**Explanation:** Prints a header for the first example using numbered emoji.

```python
    try:
        response = model.generate_content("")
```
**Explanation:** Attempts to generate content with an empty string. This might cause an error.

```python
        print("   ✅ Response:", response.text[:100])
```
**Explanation:** If successful, print first 100 characters of response.

```python
    except Exception as e:
```
**Explanation:** Catches any error that occurs.

```python
        print(f"   ⚠️  Caught error: {type(e).__name__}")
```
**Explanation:** Prints the type of error (e.g., ValueError, APIError). `type(e).__name__` gets the class name of the exception.

```python
        print(f"   Message: {str(e)[:100]}")
```
**Explanation:** Prints first 100 characters of the error message.

```python
    # Example 2: Very long prompt (simulated)
    print("\n2️⃣ Testing rate limiting awareness:")
```
**Explanation:** Header for second example about rate limiting.

```python
    print("   💡 Always implement rate limiting in production!")
    print("   💡 Add delays between requests if making many calls")
```
**Explanation:** Educational messages about rate limiting best practices. Lightbulb emoji indicates tips.

```python
    # Example 3: Network issues
    print("\n3️⃣ Best practices for production:")
```
**Explanation:** Header for third example about production best practices.

```python
    print("   • Always use try-except blocks")
    print("   • Implement retry logic with exponential backoff")
    print("   • Log errors for debugging")
    print("   • Provide user-friendly error messages")
```
**Explanation:** List of best practices for production code. Each line is a recommendation.

---

## Main Execution Function

```python
# ============================================================================
# MAIN EXECUTION
# ============================================================================
```
**Explanation:** Section separator for the main function.

```python
def main():
```
**Explanation:** Defines the main function that orchestrates all the other functions.

```python
    """
    Main function to run all demonstrations
    """
```
**Explanation:** Function docstring.

```python
    print("\n")
```
**Explanation:** Prints a blank line for spacing.

```python
    print("🎓 " + "=" * 58 + " 🎓")
```
**Explanation:** Prints a decorative header with graduation cap emojis and 58 equal signs.

```python
    print("   GENERATIVE AI SESSION - MODULE 1: MODEL PREPARATION")
```
**Explanation:** Prints the main title of the module.

```python
    print("🎓 " + "=" * 58 + " 🎓")
```
**Explanation:** Closing line of the header.

```python
    try:
```
**Explanation:** Starts try-except block to catch any fatal errors.

```python
        # Step 1: Setup
        api_key = setup_environment()
```
**Explanation:** Calls `setup_environment()` and stores the returned API key. This is step 1 of the setup process.

```python
        # Step 2: Configure
        configure_api(api_key)
```
**Explanation:** Calls `configure_api()` passing the API key. This is step 2.

```python
        # Step 3: Initialize
        text_model, vision_model = initialize_models()
```
**Explanation:** Calls `initialize_models()` and unpacks the returned tuple into two variables. This is step 3.

```python
        # Step 4: Test
        success = test_basic_generation(text_model)
```
**Explanation:** Calls `test_basic_generation()` with the text model and stores the boolean result. This is step 4.

```python
        if success:
```
**Explanation:** Only continue if the test succeeded (returned True).

```python
            # Step 5: Display info
            display_available_models()
```
**Explanation:** Shows all available models.

```python
            # Step 6: Error handling
            demonstrate_error_handling(text_model)
```
**Explanation:** Demonstrates error handling patterns.

```python
            print("\n" + "=" * 60)
            print("✅ ALL CHECKS PASSED - READY FOR NEXT MODULE!")
            print("=" * 60)
```
**Explanation:** Prints a success message indicating everything worked and student can proceed.

```python
        else:
            print("\n⚠️  Please fix the errors above before continuing")
```
**Explanation:** If the test failed, print a warning message.

```python
    except Exception as e:
```
**Explanation:** Catches any fatal error that occurred in the main execution.

```python
        print(f"\n❌ Fatal error: {e}")
        print("Please check your configuration and try again")
```
**Explanation:** Prints the fatal error and asks user to check configuration.

---

## Script Entry Point

```python
if __name__ == "__main__":
```
**Explanation:** This is a special Python idiom. It checks if this file is being run directly (not imported). `__name__` is a special variable that equals `"__main__"` when the script is executed directly.

```python
    main()
```
**Explanation:** If the file is run directly, call the `main()` function to start the program.

```python
    # Teaching tip: After running this, ask students:
    # 1. Why do we use environment variables?
    # 2. What's the difference between gemini-pro and gemini-pro-vision?
    # 3. Why is error handling important?
```
**Explanation:** Comments for instructors with suggested discussion questions to reinforce learning.

---

## Summary

This module demonstrates:
1. **Secure API key management** using environment variables
2. **Function organization** with clear, single-purpose functions
3. **Error handling** with try-except blocks
4. **User feedback** with print statements and emojis
5. **Code structure** with comments and docstrings
6. **Best practices** for production-ready code

Every line serves a purpose: either executing code, handling errors, or providing feedback to the user.
