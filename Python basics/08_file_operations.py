"""
Lesson 8: File Operations
Reading and writing files for Gen AI (prompts, responses, configs)
"""

# Writing to a file
def save_prompt(prompt, filename="prompt.txt"):
    """Save a prompt to a text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(prompt)
    print(f"Prompt saved to {filename}")

prompt = "Generate a creative story about AI and humans working together"
save_prompt(prompt)


# Reading from a file
def read_prompt(filename="prompt.txt"):
    """Read a prompt from a text file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "File not found"

saved_prompt = read_prompt()
print(f"\nRead from file: {saved_prompt}")


# Appending to a file (conversation history)
def log_conversation(role, message, filename="conversation.txt"):
    """Append conversation to a log file"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"{role.upper()}: {message}\n")

log_conversation("user", "What is machine learning?")
log_conversation("assistant", "Machine learning is a subset of AI...")


# Reading multiple lines
def read_prompts_list(filename="prompts_list.txt"):
    """Read multiple prompts from file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            prompts = f.readlines()
        return [prompt.strip() for prompt in prompts]
    except FileNotFoundError:
        return []

# Create sample file first
with open("prompts_list.txt", 'w', encoding='utf-8') as f:
    f.write("What is AI?\n")
    f.write("Explain deep learning\n")
    f.write("Generate Python code\n")

prompts = read_prompts_list("prompts_list.txt")
print(f"\nPrompts list: {prompts}")


# Working with JSON (common for API configs)
import json

def save_config(config, filename="config.json"):
    """Save configuration as JSON"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)
    print(f"Config saved to {filename}")

config = {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 1000,
    "api_key": "your-api-key-here"
}

save_config(config)


def load_config(filename="config.json"):
    """Load configuration from JSON"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

loaded_config = load_config()
print(f"\nLoaded config: {loaded_config}")


# Saving AI responses
def save_response(prompt, response, filename="ai_responses.txt"):
    """Save prompt and response pair"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"PROMPT: {prompt}\n")
        f.write(f"RESPONSE: {response}\n")
        f.write("-" * 50 + "\n")

save_response(
    "What is Python?",
    "Python is a high-level programming language..."
)

print("\nResponse saved to file")


# Reading and processing large files
def process_prompts_batch(filename):
    """Process prompts from file one by one"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                prompt = line.strip()
                if prompt:  # Skip empty lines
                    print(f"Processing prompt {line_num}: {prompt[:50]}...")
    except FileNotFoundError:
        print(f"File {filename} not found")

process_prompts_batch("prompts_list.txt")
