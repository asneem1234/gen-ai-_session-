"""
Common Mistakes & How to Fix Them
==================================

This file shows common beginner mistakes and their solutions.
Read through these to avoid frustration!
"""

print("=== COMMON MISTAKE #1: Indentation Errors ===\n")

# WRONG - No indentation
"""
if True:
print("Hello")  # IndentationError!
"""

# RIGHT - Proper indentation (4 spaces or 1 tab)
if True:
    print("Hello")  # ✓ Correct!

print("Tip: Python uses indentation to define code blocks.")
print("Always indent after: if, for, while, def, class, etc.\n")


print("=== COMMON MISTAKE #2: Quotes Mismatch ===\n")

# WRONG - Mixed quotes
# text = "Hello'  # SyntaxError!

# RIGHT - Matching quotes
text = "Hello"   # ✓ Both double quotes
text = 'Hello'   # ✓ Both single quotes

print("Tip: Start and end strings with the same quote type.\n")


print("=== COMMON MISTAKE #3: Forgetting Colons ===\n")

# WRONG - No colon
"""
if temperature > 0.7  # SyntaxError!
    print("High")
"""

# RIGHT - Colon after condition
if True:  # ✓ Colon here!
    print("High")

print("Tip: Always add : after if, for, while, def, etc.\n")


print("=== COMMON MISTAKE #4: Using = Instead of == ===\n")

temperature = 0.7

# WRONG - Assignment in condition
# if temperature = 0.7:  # SyntaxError!

# RIGHT - Comparison operator
if temperature == 0.7:  # ✓ Two equals signs!
    print("Temperature is exactly 0.7")

print("Tip: = assigns, == compares\n")


print("=== COMMON MISTAKE #5: Undefined Variables ===\n")

# WRONG - Using before defining
"""
print(message)  # NameError: name 'message' is not defined
message = "Hello"
"""

# RIGHT - Define before use
message = "Hello"  # ✓ Define first
print(message)     # ✓ Then use

print("Tip: Always define variables before using them.\n")


print("=== COMMON MISTAKE #6: String + Number ===\n")

age = 25

# WRONG - Can't directly add string and number
# result = "Age: " + age  # TypeError!

# RIGHT - Convert to string first
result = "Age: " + str(age)  # ✓ Convert with str()
result = f"Age: {age}"       # ✓ Or use f-string (better!)

print(result)
print("Tip: Use f-strings or convert numbers to strings.\n")


print("=== COMMON MISTAKE #7: List Index Out of Range ===\n")

models = ["GPT-4", "Claude", "Gemini"]

# WRONG - Index doesn't exist
# print(models[5])  # IndexError: list index out of range

# RIGHT - Check length or use safe index
print(models[0])   # ✓ First item (index 0)
print(models[-1])  # ✓ Last item
if len(models) > 3:
    print(models[3])
else:
    print("Index doesn't exist")

print("Tip: Lists start at index 0. Last index is len(list)-1.\n")


print("=== COMMON MISTAKE #8: Dictionary KeyError ===\n")

config = {"model": "gpt-4", "temperature": 0.7}

# WRONG - Key doesn't exist
# print(config["max_tokens"])  # KeyError: 'max_tokens'

# RIGHT - Use .get() with default
print(config.get("max_tokens", 1000))  # ✓ Returns 1000 if key missing

# Or check first
if "max_tokens" in config:
    print(config["max_tokens"])
else:
    print("Key not found")

print("Tip: Use .get() to avoid KeyError.\n")


print("=== COMMON MISTAKE #9: Forgetting return in Functions ===\n")

# WRONG - No return statement
def add_numbers(a, b):
    result = a + b
    # Missing return!

# RIGHT - Return the value
def add_numbers(a, b):
    result = a + b
    return result  # ✓ Return the result

total = add_numbers(5, 3)
print(f"Total: {total}")
print("Tip: Use 'return' to get values from functions.\n")


print("=== COMMON MISTAKE #10: Not Closing Parentheses/Brackets ===\n")

# WRONG - Missing closing bracket
# config = {"model": "gpt-4", "temp": 0.7  # SyntaxError!

# RIGHT - All brackets closed
config = {"model": "gpt-4", "temp": 0.7}  # ✓ Closed!

print("Tip: Every ( needs ), every [ needs ], every { needs }.\n")


print("=== COMMON MISTAKE #11: Wrong Indentation Level ===\n")

# WRONG - Inconsistent indentation
"""
def my_function():
    print("Line 1")
      print("Line 2")  # IndentationError - too much indent
"""

# RIGHT - Consistent indentation
def my_function():
    print("Line 1")  # ✓ Same level
    print("Line 2")  # ✓ Same level

print("Tip: Keep same indentation level for code at same 'level'.\n")


print("=== COMMON MISTAKE #12: Modifying List While Looping ===\n")

items = [1, 2, 3, 4, 5]

# WRONG - Modifying list during loop
"""
for item in items:
    items.remove(item)  # Can cause issues!
"""

# RIGHT - Loop over copy
for item in items.copy():  # ✓ Loop over copy
    items.remove(item)

print("Tip: Don't modify a list while looping through it.\n")


print("=== COMMON MISTAKE #13: Forgetting to Call Functions ===\n")

def greet():
    return "Hello"

# WRONG - Missing parentheses
# message = greet  # This is the function object, not the result!

# RIGHT - Call the function
message = greet()  # ✓ Parentheses execute the function
print(message)

print("Tip: Functions need () to execute.\n")


print("=== COMMON MISTAKE #14: Mutable Default Arguments ===\n")

# WRONG - Mutable default (can cause unexpected behavior)
def add_item(item, items=[]):  # Don't do this!
    items.append(item)
    return items

# RIGHT - Use None and create new list
def add_item(item, items=None):  # ✓ Better!
    if items is None:
        items = []
    items.append(item)
    return items

print("Tip: Don't use [] or {} as default arguments.\n")


print("=== COMMON MISTAKE #15: Not Using Error Handling for File Operations ===\n")

# WRONG - No error handling
"""
with open("nonexistent.txt", "r") as f:  # FileNotFoundError!
    content = f.read()
"""

# RIGHT - Handle potential errors
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")  # ✓ Graceful handling
    content = ""

print("Tip: Always handle file errors with try-except.\n")


print("\n" + "="*50)
print("Remember These Tips:")
print("="*50)
print("1. Read error messages carefully - they tell you what's wrong")
print("2. Check indentation - Python is strict about it")
print("3. Match quotes, parentheses, and brackets")
print("4. Define before you use")
print("5. Use print() to debug - see what's happening")
print("6. Google errors - you're not the first to encounter them!")
print("7. Use VS Code's error highlighting - red squiggles help!")
print("8. Test often - catch errors early")
print("9. Comment your code - future you will thank you")
print("10. Practice! The more you code, the fewer mistakes you make")
print("="*50)
