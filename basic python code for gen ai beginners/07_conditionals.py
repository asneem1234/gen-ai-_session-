"""
Lesson 7: Conditionals (if/else)
Make decisions in your Gen AI code
"""

# Basic if statement
temperature = 0.8

if temperature > 0.7:
    print("High temperature - more creative responses")

# If-else
max_tokens = 500

if max_tokens < 100:
    print("Short response")
else:
    print("Longer response")

# If-elif-else
model = "gpt-4"

if model == "gpt-3.5-turbo":
    print("Using GPT-3.5 - fast and efficient")
elif model == "gpt-4":
    print("Using GPT-4 - most capable")
elif model == "dall-e-3":
    print("Using DALL-E 3 - image generation")
else:
    print("Unknown model")

# Checking content type
prompt = "Generate an image of a cat"

if "image" in prompt.lower():
    print("\nThis requires an image generation model")
elif "code" in prompt.lower():
    print("\nThis requires a code generation model")
else:
    print("\nThis is a text generation task")

# Validating API parameters
def validate_temperature(temp):
    """Validate temperature parameter for AI models"""
    if temp < 0 or temp > 2:
        return False, "Temperature must be between 0 and 2"
    elif temp < 0.3:
        return True, "Very deterministic responses"
    elif temp < 0.7:
        return True, "Balanced responses"
    else:
        return True, "Creative responses"

is_valid, message = validate_temperature(0.7)
print(f"\nValidation: {message}")

# Multiple conditions with and/or
tokens_used = 800
max_allowed = 1000
is_premium = True

if tokens_used < max_allowed and is_premium:
    print("\nContinue processing - within limits and premium user")
elif tokens_used >= max_allowed:
    print("\nToken limit reached!")
else:
    print("\nUpgrade to premium for more tokens")

# Checking response quality
response_length = 150
has_code = True
is_complete = True

if response_length > 100 and has_code and is_complete:
    print("\nHigh quality response generated")
else:
    print("\nResponse needs improvement")

# Ternary operator (short if-else)
role = "user"
prefix = "Q:" if role == "user" else "A:"
print(f"\n{prefix} Sample message")

# Checking for None/empty values
user_input = ""

if not user_input:
    print("\nNo input provided - using default prompt")
else:
    print(f"\nProcessing: {user_input}")

# Nested conditionals
model_type = "text"
model_name = "gpt-4"

if model_type == "text":
    if model_name == "gpt-4":
        print("\nUsing advanced text model")
    else:
        print("\nUsing standard text model")
elif model_type == "image":
    print("\nUsing image generation model")
