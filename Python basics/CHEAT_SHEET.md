# Cheat Sheet: Python for Gen AI Beginners

## Quick Reference Guide

### 1. PRINTING OUTPUT
```python
print("Hello")                    # Print text
print(variable_name)              # Print variable value
print(f"Value: {variable}")       # Print with variable inside (f-string)
```

### 2. VARIABLES (Storing Data)
```python
# Strings (text)
name = "ChatGPT"
prompt = "Generate a story"

# Numbers
age = 25                          # Integer (whole number)
temperature = 0.7                 # Float (decimal)

# Boolean (True/False)
is_active = True
is_complete = False

# Lists (multiple items)
models = ["GPT-4", "Claude", "Gemini"]

# Dictionaries (key-value pairs)
config = {
    "model": "gpt-4",
    "temperature": 0.7
}
```

### 3. STRING OPERATIONS
```python
text = "Hello World"
text.upper()                      # "HELLO WORLD"
text.lower()                      # "hello world"
text.strip()                      # Remove spaces from ends
text.replace("World", "AI")       # "Hello AI"
text.split()                      # ["Hello", "World"]
len(text)                         # 11 (length)
"World" in text                   # True (check if contains)
```

### 4. LISTS
```python
items = ["a", "b", "c"]
items[0]                          # "a" (first item)
items[-1]                         # "c" (last item)
items.append("d")                 # Add to end
len(items)                        # 4 (length)

# Loop through list
for item in items:
    print(item)
```

### 5. DICTIONARIES
```python
person = {
    "name": "John",
    "age": 30
}

person["name"]                    # "John"
person["age"]                     # 30
person["city"] = "NYC"            # Add new key

# Loop through dictionary
for key, value in person.items():
    print(f"{key}: {value}")
```

### 6. CONDITIONALS (If/Else)
```python
if temperature > 0.7:
    print("High creativity")
elif temperature > 0.3:
    print("Medium creativity")
else:
    print("Low creativity")
```

### 7. FUNCTIONS
```python
# Define function
def greet(name):
    return f"Hello, {name}!"

# Call function
message = greet("Alice")          # "Hello, Alice!"

# Function with default parameter
def call_ai(prompt, temp=0.7):
    print(f"Prompt: {prompt}, Temp: {temp}")
    
call_ai("Hello")                  # Uses temp=0.7
call_ai("Hello", 0.9)             # Uses temp=0.9
```

### 8. LOOPS
```python
# For loop (repeat for each item)
for i in range(5):                # 0, 1, 2, 3, 4
    print(i)

# While loop (repeat while condition is true)
count = 0
while count < 5:
    print(count)
    count += 1
```

### 9. FILE OPERATIONS
```python
# Write to file
with open("data.txt", "w") as f:
    f.write("Hello World")

# Read from file
with open("data.txt", "r") as f:
    content = f.read()

# Work with JSON
import json

# Save JSON
data = {"model": "gpt-4"}
with open("config.json", "w") as f:
    json.dump(data, f)

# Load JSON
with open("config.json", "r") as f:
    data = json.load(f)
```

### 10. ERROR HANDLING
```python
try:
    result = 10 / 0              # This will cause error
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Always runs")
```

### 11. COMMON GEN AI PATTERNS

#### API Configuration
```python
config = {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 1000,
    "top_p": 0.9
}
```

#### Conversation Format
```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is AI?"},
    {"role": "assistant", "content": "AI is artificial intelligence."},
    {"role": "user", "content": "Tell me more."}
]
```

#### Prompt Template
```python
def create_prompt(task, context=""):
    return f"""
Task: {task}
Context: {context}

Please provide a detailed response.
"""

prompt = create_prompt("Generate code", "Python function")
```

#### Validate Input
```python
def validate_temperature(temp):
    if temp < 0 or temp > 2:
        return False, "Temperature must be between 0 and 2"
    return True, "Valid"
```

### 12. USEFUL BUILT-IN FUNCTIONS
```python
len(items)                        # Length of list/string
type(variable)                    # Check type
str(123)                          # Convert to string
int("123")                        # Convert to integer
float("3.14")                     # Convert to float
range(5)                          # 0, 1, 2, 3, 4
enumerate(items)                  # Get index and item
zip(list1, list2)                 # Combine lists
```

### 13. LIST COMPREHENSION (Advanced)
```python
# Instead of:
squares = []
for x in range(5):
    squares.append(x ** 2)

# You can write:
squares = [x ** 2 for x in range(5)]   # [0, 1, 4, 9, 16]

# With condition:
evens = [x for x in range(10) if x % 2 == 0]   # [0, 2, 4, 6, 8]
```

### 14. STRING FORMATTING
```python
name = "Alice"
age = 30

# F-strings (modern, preferred)
print(f"Name: {name}, Age: {age}")

# Format method
print("Name: {}, Age: {}".format(name, age))

# % formatting (old style)
print("Name: %s, Age: %d" % (name, age))
```

### 15. COMMON ERRORS & SOLUTIONS

#### IndentationError
```python
# Wrong:
if True:
print("Hello")

# Right:
if True:
    print("Hello")
```

#### NameError (variable not defined)
```python
# Wrong:
print(message)                    # message doesn't exist

# Right:
message = "Hello"
print(message)
```

#### TypeError (wrong type)
```python
# Wrong:
"5" + 5                          # Can't add string and number

# Right:
int("5") + 5                     # Convert to int first
"5" + str(5)                     # Or convert to string
```

#### KeyError (dictionary key doesn't exist)
```python
# Wrong:
data = {"name": "John"}
print(data["age"])               # Key doesn't exist

# Right:
print(data.get("age", "Unknown"))  # Use .get() with default
```

---

## Quick Tips

1. **Use print() to debug**: When confused, print variables to see their values
2. **Read error messages**: They tell you exactly what's wrong and where
3. **Google errors**: Copy error message to Google for solutions
4. **Use meaningful names**: `user_prompt` is better than `x`
5. **Add comments**: Explain WHY, not just WHAT
6. **Test often**: Run your code frequently to catch errors early
7. **Use VS Code IntelliSense**: Press Ctrl+Space for suggestions

---

## Keyboard Shortcuts (VS Code)

- `Ctrl + S`: Save file
- `Ctrl + /`: Comment/uncomment line
- `Ctrl + D`: Select next occurrence
- `Alt + Up/Down`: Move line up/down
- `Shift + Alt + F`: Format code
- `F5`: Run with debugger
- `Ctrl + \``: Toggle terminal

---

## Keep This Handy!

Save this file and refer to it whenever you forget syntax.
Happy coding! 🚀
