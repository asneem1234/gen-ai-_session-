"""
Lesson 2: Variables and Data Types
Learn about different types of data in Python
"""

# String (text)
name = "ChatGPT"
model = "GPT-4"
print(f"Model name: {name}, Version: {model}")

# Integer (whole numbers)
tokens = 1000
max_tokens = 4096
print(f"Tokens used: {tokens} out of {max_tokens}")

# Float (decimal numbers)
temperature = 0.7
top_p = 0.9
print(f"Temperature: {temperature}, Top P: {top_p}")

# Boolean (True/False)
is_ai_model = True
is_trained = True
print(f"Is AI Model: {is_ai_model}, Is Trained: {is_trained}")

# List (collection of items)
ai_models = ["GPT-4", "DALL-E", "Gemini", "Claude"]
print(f"Available AI Models: {ai_models}")

# Dictionary (key-value pairs)
model_config = {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 1000
}
print(f"Model Configuration: {model_config}")
