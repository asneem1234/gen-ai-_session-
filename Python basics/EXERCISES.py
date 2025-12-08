"""
Practice Exercises - Test Your Knowledge!
=========================================

Complete these exercises to reinforce what you've learned.
Try to solve them before looking at the solutions file!
"""

# BEGINNER EXERCISES (After Lessons 1-4)
# =======================================

print("=== EXERCISE 1: Personal AI Assistant ===")
"""
Exercise 1: Create variables for your AI assistant
- Store the assistant's name as "AIHelper"
- Store its version as 1.0
- Store whether it's active (True)
- Print a welcome message using f-strings

Expected output:
Welcome to AIHelper v1.0 (Status: Active)
"""

# YOUR CODE HERE:




print("\n=== EXERCISE 2: Prompt Counter ===")
"""
Exercise 2: Count words in prompts
Create 3 different prompts (strings) and print:
- Each prompt
- The number of words in each prompt
- The total number of words across all prompts

Hint: Use .split() to split into words, len() for count
"""

# YOUR CODE HERE:




print("\n=== EXERCISE 3: Model List ===")
"""
Exercise 3: Work with a list of AI models
1. Create a list with these models: "GPT-4", "Claude", "Gemini"
2. Add "DALL-E" to the list
3. Print each model with a number (1. GPT-4, 2. Claude, etc.)
4. Print how many models total

Hint: Use enumerate() for numbering
"""

# YOUR CODE HERE:




# INTERMEDIATE EXERCISES (After Lessons 5-7)
# ===========================================

print("\n=== EXERCISE 4: Configuration Dictionary ===")
"""
Exercise 4: Create and validate model configuration
1. Create a config dictionary with: model, temperature, max_tokens
2. Print all settings in a formatted way
3. Add a new setting: top_p = 0.9
4. Check if temperature is between 0 and 2, print "Valid" or "Invalid"
"""

# YOUR CODE HERE:




print("\n=== EXERCISE 5: Prompt Categorizer ===")
"""
Exercise 5: Categorize prompts by type
Write a function called categorize_prompt(prompt) that:
- Returns "image" if prompt contains "image" or "picture"
- Returns "code" if prompt contains "code" or "function"
- Returns "text" otherwise

Test with these prompts:
- "Generate an image of a cat"
- "Write a Python function"
- "Explain machine learning"
"""

# YOUR CODE HERE:




print("\n=== EXERCISE 6: Temperature Validator ===")
"""
Exercise 6: Validate temperature values
Write a function validate_temp(temp) that:
- Returns "Too low" if temp < 0
- Returns "Low creativity" if 0 <= temp < 0.3
- Returns "Balanced" if 0.3 <= temp < 0.7
- Returns "High creativity" if 0.7 <= temp <= 2
- Returns "Too high" if temp > 2

Test with: -0.1, 0.2, 0.5, 0.9, 2.5
"""

# YOUR CODE HERE:




# ADVANCED EXERCISES (After Lessons 8-10)
# ========================================

print("\n=== EXERCISE 7: Prompt Logger ===")
"""
Exercise 7: Save prompts to file
1. Create a function save_prompt(prompt, filename="prompts.txt")
   that appends the prompt to a file
2. Save at least 3 prompts
3. Create another function read_prompts(filename) that reads and
   returns a list of all prompts
4. Print all saved prompts

Hint: Use 'a' mode for append, 'r' mode for read
"""

# YOUR CODE HERE:




print("\n=== EXERCISE 8: Safe API Call ===")
"""
Exercise 8: Simulate API call with error handling
Create a function call_api(prompt, api_key=None) that:
- Raises ValueError if api_key is None or empty
- Raises ValueError if prompt is empty
- Returns a dictionary with "status": "success" and "response": prompt
- Use try-except to handle errors gracefully

Test with:
- Valid: call_api("Hello", "sk-123")
- Invalid: call_api("", "sk-123")
- Invalid: call_api("Hello")
"""

# YOUR CODE HERE:




print("\n=== EXERCISE 9: Conversation Manager ===")
"""
Exercise 9: Build a simple conversation manager
Create a class ConversationManager that:
1. Has an __init__ method that creates an empty conversation list
2. Has an add_message(role, content) method that adds to conversation
3. Has a get_conversation() method that returns all messages
4. Has a count_messages() method that returns message count
5. Has a clear() method that clears the conversation

Test by adding 3-4 messages and printing the conversation
"""

# YOUR CODE HERE:




print("\n=== EXERCISE 10: Complete Prompt System ===")
"""
Exercise 10: Build a complete system (CHALLENGE!)
Create a mini prompt management system with:

1. A function create_prompt_config(model, temp, tokens) that:
   - Validates all parameters
   - Returns a config dictionary

2. A function save_config(config, filename) that:
   - Saves config as JSON
   - Handles errors

3. A function load_config(filename) that:
   - Loads config from JSON
   - Returns default config if file doesn't exist

4. Test the complete flow:
   - Create a config
   - Save it
   - Load it back
   - Print to verify

This combines everything you've learned!
"""

# YOUR CODE HERE:




print("\n=== All exercises complete! ===")
print("Check the SOLUTIONS file to compare your answers!")
print("Remember: There are many ways to solve each problem.")
print("Your solution might be different but still correct!")
