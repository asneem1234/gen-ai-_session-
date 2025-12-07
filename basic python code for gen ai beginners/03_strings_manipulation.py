"""
Lesson 3: String Manipulation
Working with text is crucial for Gen AI applications
"""

# Basic string operations
prompt = "Generate an image of a sunset"
print(f"Original prompt: {prompt}")
print(f"Length: {len(prompt)}")
print(f"Uppercase: {prompt.upper()}")
print(f"Lowercase: {prompt.lower()}")

# String concatenation
system_message = "You are a helpful AI assistant."
user_message = "What is machine learning?"
full_prompt = system_message + " " + user_message
print(f"\nFull prompt: {full_prompt}")

# String formatting
model_name = "GPT-4"
num_parameters = 1.7
print(f"\n{model_name} has approximately {num_parameters} trillion parameters")

# String methods useful for AI
text = "  Hello, AI World!  "
print(f"\nOriginal: '{text}'")
print(f"Stripped: '{text.strip()}'")
print(f"Replaced: '{text.replace('AI', 'Generative AI')}'")

# Splitting strings (useful for tokenization)
sentence = "Artificial Intelligence is amazing"
words = sentence.split()
print(f"\nWords: {words}")
print(f"Number of words: {len(words)}")

# Checking content
prompt = "Generate a python function"
if "python" in prompt.lower():
    print("\nThis prompt is about Python!")
