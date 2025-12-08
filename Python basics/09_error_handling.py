"""
Lesson 9: Error Handling
Handle errors gracefully in Gen AI applications
"""

# Basic try-except
def safe_divide(a, b):
    """Safely divide two numbers"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))


# Multiple exception types
def parse_temperature(value):
    """Parse temperature parameter with error handling"""
    try:
        temp = float(value)
        if temp < 0 or temp > 2:
            raise ValueError("Temperature must be between 0 and 2")
        return temp
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except TypeError:
        print("Error: Temperature must be a number")
        return None

print(f"\n{parse_temperature(0.7)}")
print(f"{parse_temperature('invalid')}")
print(f"{parse_temperature(3.0)}")


# Try-except-else-finally
def read_api_key(filename="api_key.txt"):
    """Read API key from file with complete error handling"""
    try:
        with open(filename, 'r') as f:
            api_key = f.read().strip()
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read {filename}")
        return None
    else:
        print("API key loaded successfully")
        return api_key
    finally:
        print("File operation completed")

api_key = read_api_key()


# Custom exception for AI operations
class InvalidPromptError(Exception):
    """Custom exception for invalid prompts"""
    pass

def validate_prompt(prompt):
    """Validate prompt before sending to AI"""
    try:
        if not prompt or len(prompt.strip()) == 0:
            raise InvalidPromptError("Prompt cannot be empty")
        if len(prompt) > 10000:
            raise InvalidPromptError("Prompt too long (max 10000 chars)")
        return True
    except InvalidPromptError as e:
        print(f"Validation Error: {e}")
        return False

print(f"\n{validate_prompt('Valid prompt')}")
print(f"{validate_prompt('')}")
print(f"{validate_prompt('a' * 10001)}")


# API call error simulation
def call_ai_api(prompt, api_key=None):
    """Simulate AI API call with error handling"""
    try:
        if not api_key:
            raise ValueError("API key is required")
        
        if len(prompt) == 0:
            raise InvalidPromptError("Prompt cannot be empty")
        
        # Simulate API call
        print("Calling AI API...")
        # Simulate successful response
        return {"response": "AI generated response", "status": "success"}
        
    except ValueError as e:
        return {"error": str(e), "status": "auth_error"}
    except InvalidPromptError as e:
        return {"error": str(e), "status": "validation_error"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}", "status": "error"}

result1 = call_ai_api("Tell me about AI", "sk-123456")
print(f"\nResult 1: {result1}")

result2 = call_ai_api("", "sk-123456")
print(f"Result 2: {result2}")

result3 = call_ai_api("Hello")
print(f"Result 3: {result3}")


# Retry logic for API calls
import time

def call_with_retry(prompt, max_retries=3):
    """Call API with automatic retry on failure"""
    for attempt in range(1, max_retries + 1):
        try:
            print(f"\nAttempt {attempt}...")
            
            # Simulate occasional failures
            import random
            if random.random() < 0.3:  # 30% chance of failure
                raise ConnectionError("Network error")
            
            print("Success!")
            return {"response": "AI response", "status": "success"}
            
        except ConnectionError as e:
            print(f"Error: {e}")
            if attempt < max_retries:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("Max retries reached")
                return {"error": "Connection failed", "status": "error"}

result = call_with_retry("Generate text")
print(f"\nFinal result: {result}")
