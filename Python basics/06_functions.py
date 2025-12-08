"""
Lesson 6: Functions
Create reusable code for Gen AI operations
"""

# Basic function
def greet_ai():
    """Simple function with no parameters"""
    print("Welcome to Gen AI with Python!")

greet_ai()


# Function with parameters
def create_prompt(task, details):
    """Create a formatted prompt for AI"""
    prompt = f"Task: {task}\nDetails: {details}"
    return prompt

my_prompt = create_prompt("Generate code", "Python function for file reading")
print(f"\n{my_prompt}")


# Function with default parameters
def call_ai_model(prompt, temperature=0.7, max_tokens=100):
    """Simulate calling an AI model with default settings"""
    print(f"\nCalling AI Model:")
    print(f"Prompt: {prompt}")
    print(f"Temperature: {temperature}")
    print(f"Max Tokens: {max_tokens}")
    return "AI response here..."

# Call with defaults
response1 = call_ai_model("What is Python?")

# Call with custom values
response2 = call_ai_model("Explain AI", temperature=0.9, max_tokens=500)


# Function returning multiple values
def analyze_text(text):
    """Analyze text and return statistics"""
    word_count = len(text.split())
    char_count = len(text)
    first_word = text.split()[0] if text else ""
    return word_count, char_count, first_word

prompt = "Generate an image of a beautiful sunset over the ocean"
words, chars, first = analyze_text(prompt)
print(f"\nText Analysis:")
print(f"Words: {words}, Characters: {chars}, First word: {first}")


# Function for prompt engineering
def build_chat_prompt(system_msg, user_msg, examples=None):
    """Build a complete chat prompt with context"""
    messages = [
        {"role": "system", "content": system_msg},
    ]
    
    if examples:
        for example in examples:
            messages.append(example)
    
    messages.append({"role": "user", "content": user_msg})
    
    return messages

system = "You are a helpful Python coding assistant."
user = "Write a function to read a file."
examples = [
    {"role": "user", "content": "How do I print?"},
    {"role": "assistant", "content": "Use print() function"}
]

chat_prompt = build_chat_prompt(system, user, examples)
print("\nChat Prompt Structure:")
for msg in chat_prompt:
    print(f"{msg['role']}: {msg['content']}")


# Lambda functions (short anonymous functions)
count_tokens = lambda text: len(text.split())
text = "This is a sample prompt for AI"
print(f"\nToken estimate: {count_tokens(text)} tokens")
