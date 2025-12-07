"""
Lesson 4: Lists and Loops
Essential for processing multiple prompts and responses
"""

# Creating lists
ai_tasks = ["text generation", "image creation", "code writing", "translation"]
print("AI Tasks:")
print(ai_tasks)

# Accessing list items
print(f"\nFirst task: {ai_tasks[0]}")
print(f"Last task: {ai_tasks[-1]}")

# Adding items to list
ai_tasks.append("summarization")
print(f"\nUpdated tasks: {ai_tasks}")

# For loop - iterate through items
print("\nAll AI Tasks:")
for task in ai_tasks:
    print(f"- {task}")

# For loop with index
print("\nNumbered AI Tasks:")
for i, task in enumerate(ai_tasks, 1):
    print(f"{i}. {task}")

# List comprehension (advanced but useful)
prompts = ["What is AI?", "Explain ML", "Define NLP"]
uppercase_prompts = [prompt.upper() for prompt in prompts]
print(f"\nUppercase prompts: {uppercase_prompts}")

# Processing multiple responses
responses = [
    "AI is artificial intelligence",
    "ML is machine learning",
    "NLP is natural language processing"
]

print("\nQ&A Pairs:")
for question, answer in zip(prompts, responses):
    print(f"Q: {question}")
    print(f"A: {answer}\n")

# While loop
token_count = 0
max_tokens = 100
print("Simulating token generation:")
while token_count < max_tokens:
    token_count += 10
    print(f"Tokens generated: {token_count}")
