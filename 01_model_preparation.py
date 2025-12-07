"""
01 - AI Model Preparation
=========================

This module demonstrates the fundamental setup for working with Google's Gemini API.
Students will learn:
- How to configure API keys securely
- Initialize the Gemini model
- Test basic connectivity
- Understand model selection
- Handle common errors

Teaching Points:
- Always use environment variables for API keys (never hardcode!)
- Different models for different tasks (gemini-pro vs gemini-pro-vision)
- Importance of error handling in production
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# ============================================================================
# SECTION 1: Environment Setup
# ============================================================================

def setup_environment():
    """
    Load environment variables from .env file
    This is the secure way to handle API keys
    """
    print("=" * 60)
    print("SECTION 1: Environment Setup")
    print("=" * 60)
    
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key:
        raise ValueError(
            "❌ GOOGLE_API_KEY not found!\n"
            "Please create a .env file and add your API key:\n"
            "GOOGLE_API_KEY=your_key_here"
        )
    
    print("✅ Environment variables loaded successfully")
    print(f"✅ API Key found: {api_key[:10]}..." + "*" * 20)
    
    return api_key


# ============================================================================
# SECTION 2: API Configuration
# ============================================================================

def configure_api(api_key):
    """
    Configure the Google Generative AI API with your key
    """
    print("\n" + "=" * 60)
    print("SECTION 2: API Configuration")
    print("=" * 60)
    
    try:
        genai.configure(api_key=api_key)
        print("✅ Gemini API configured successfully")
    except Exception as e:
        print(f"❌ Error configuring API: {e}")
        raise


# ============================================================================
# SECTION 3: Model Initialization
# ============================================================================

def initialize_models():
    """
    Initialize different models for different use cases
    """
    print("\n" + "=" * 60)
    print("SECTION 3: Model Initialization")
    print("=" * 60)
    
    # Text-only model
    text_model = genai.GenerativeModel('gemini-pro')
    print("✅ Gemini Pro (text) model initialized")
    print("   Use case: Text generation, chat, code generation")
    
    # Vision model (for images and video)
    vision_model = genai.GenerativeModel('gemini-pro-vision')
    print("✅ Gemini Pro Vision model initialized")
    print("   Use case: Image understanding, video analysis")
    
    return text_model, vision_model


# ============================================================================
# SECTION 4: Testing Basic Connectivity
# ============================================================================

def test_basic_generation(model):
    """
    Test basic text generation to ensure everything is working
    """
    print("\n" + "=" * 60)
    print("SECTION 4: Testing Basic Connectivity")
    print("=" * 60)
    
    try:
        # Simple test prompt
        prompt = "Say 'Hello! The API is working correctly.' in a friendly way."
        print(f"\n📝 Test Prompt: {prompt}")
        
        # Generate response
        print("\n⏳ Generating response...")
        response = model.generate_content(prompt)
        
        print("\n✅ Response received successfully!")
        print("\n" + "-" * 60)
        print("🤖 AI Response:")
        print("-" * 60)
        print(response.text)
        print("-" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error during generation: {e}")
        print("\nCommon issues:")
        print("  1. Invalid API key")
        print("  2. API quota exceeded")
        print("  3. Network connectivity issues")
        return False


# ============================================================================
# SECTION 5: Model Information
# ============================================================================

def display_available_models():
    """
    List all available models
    """
    print("\n" + "=" * 60)
    print("SECTION 5: Available Models")
    print("=" * 60)
    
    try:
        print("\n📋 Listing available Gemini models:\n")
        
        for model in genai.list_models():
            if 'generateContent' in model.supported_generation_methods:
                print(f"  • {model.name}")
                print(f"    Description: {model.display_name}")
                print(f"    Input token limit: {model.input_token_limit}")
                print(f"    Output token limit: {model.output_token_limit}")
                print()
                
    except Exception as e:
        print(f"❌ Error listing models: {e}")


# ============================================================================
# SECTION 6: Error Handling Examples
# ============================================================================

def demonstrate_error_handling(model):
    """
    Show common errors and how to handle them
    """
    print("\n" + "=" * 60)
    print("SECTION 6: Error Handling")
    print("=" * 60)
    
    # Example 1: Empty prompt
    print("\n1️⃣ Testing empty prompt handling:")
    try:
        response = model.generate_content("")
        print("   ✅ Response:", response.text[:100])
    except Exception as e:
        print(f"   ⚠️  Caught error: {type(e).__name__}")
        print(f"   Message: {str(e)[:100]}")
    
    # Example 2: Very long prompt (simulated)
    print("\n2️⃣ Testing rate limiting awareness:")
    print("   💡 Always implement rate limiting in production!")
    print("   💡 Add delays between requests if making many calls")
    
    # Example 3: Network issues
    print("\n3️⃣ Best practices for production:")
    print("   • Always use try-except blocks")
    print("   • Implement retry logic with exponential backoff")
    print("   • Log errors for debugging")
    print("   • Provide user-friendly error messages")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main function to run all demonstrations
    """
    print("\n")
    print("🎓 " + "=" * 58 + " 🎓")
    print("   GENERATIVE AI SESSION - MODULE 1: MODEL PREPARATION")
    print("🎓 " + "=" * 58 + " 🎓")
    
    try:
        # Step 1: Setup
        api_key = setup_environment()
        
        # Step 2: Configure
        configure_api(api_key)
        
        # Step 3: Initialize
        text_model, vision_model = initialize_models()
        
        # Step 4: Test
        success = test_basic_generation(text_model)
        
        if success:
            # Step 5: Display info
            display_available_models()
            
            # Step 6: Error handling
            demonstrate_error_handling(text_model)
            
            print("\n" + "=" * 60)
            print("✅ ALL CHECKS PASSED - READY FOR NEXT MODULE!")
            print("=" * 60)
        else:
            print("\n⚠️  Please fix the errors above before continuing")
            
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        print("Please check your configuration and try again")


if __name__ == "__main__":
    main()
    
    # Teaching tip: After running this, ask students:
    # 1. Why do we use environment variables?
    # 2. What's the difference between gemini-pro and gemini-pro-vision?
    # 3. Why is error handling important?
