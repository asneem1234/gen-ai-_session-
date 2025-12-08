"""
Lesson 5: Dictionaries
Perfect for storing API configurations and responses
"""

# Basic dictionary (like JSON)
model_settings = {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 1000,
    "top_p": 0.9
}

print("Model Settings:")
print(model_settings)

# Accessing values
print(f"\nModel: {model_settings['model']}")
print(f"Temperature: {model_settings['temperature']}")

# Using .get() method (safer)
print(f"Max tokens: {model_settings.get('max_tokens')}")
print(f"Stop sequence: {model_settings.get('stop', 'Not set')}")

# Adding/updating values
model_settings["presence_penalty"] = 0.0
model_settings["temperature"] = 0.8  # Update existing
print(f"\nUpdated settings: {model_settings}")

# Looping through dictionary
print("\nAll settings:")
for key, value in model_settings.items():
    print(f"{key}: {value}")

# Nested dictionary (API response simulation)
api_response = {
    "id": "chatcmpl-123",
    "model": "gpt-4",
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "Hello! How can I help you today?"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 10,
        "completion_tokens": 20,
        "total_tokens": 30
    }
}

print("\nAPI Response Structure:")
print(f"Model used: {api_response['model']}")
print(f"Response: {api_response['choices'][0]['message']['content']}")
print(f"Total tokens: {api_response['usage']['total_tokens']}")

# List of dictionaries (multiple conversations)
conversations = [
    {"role": "user", "content": "What is AI?"},
    {"role": "assistant", "content": "AI is artificial intelligence."},
    {"role": "user", "content": "Tell me more."}
]

print("\nConversation History:")
for message in conversations:
    print(f"{message['role'].upper()}: {message['content']}")
