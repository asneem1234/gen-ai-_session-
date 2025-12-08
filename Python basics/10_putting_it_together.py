"""
Lesson 10: Putting It All Together
A complete Gen AI prompt management system
"""

import json
from datetime import datetime

class PromptManager:
    """Manage prompts for Gen AI applications"""
    
    def __init__(self, config_file="ai_config.json"):
        """Initialize the prompt manager"""
        self.config_file = config_file
        self.config = self.load_config()
        self.history = []
    
    def load_config(self):
        """Load AI configuration from file"""
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Config not found, using defaults")
            return {
                "model": "gpt-4",
                "temperature": 0.7,
                "max_tokens": 1000
            }
    
    def save_config(self):
        """Save current configuration"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
        print("Configuration saved")
    
    def update_config(self, **kwargs):
        """Update configuration parameters"""
        self.config.update(kwargs)
        self.save_config()
    
    def create_prompt(self, system_message, user_message):
        """Create a formatted prompt"""
        prompt = {
            "system": system_message,
            "user": user_message,
            "timestamp": datetime.now().isoformat(),
            "config": self.config.copy()
        }
        return prompt
    
    def validate_prompt(self, prompt):
        """Validate prompt before processing"""
        if not prompt.get("user"):
            raise ValueError("User message cannot be empty")
        
        if len(prompt["user"]) > 10000:
            raise ValueError("Prompt too long")
        
        return True
    
    def simulate_ai_call(self, prompt):
        """Simulate calling an AI API"""
        try:
            self.validate_prompt(prompt)
            
            # Simulate API call
            response = {
                "id": f"resp-{len(self.history) + 1}",
                "model": self.config["model"],
                "content": f"AI response to: {prompt['user'][:50]}...",
                "tokens": len(prompt["user"].split()) * 2,
                "timestamp": datetime.now().isoformat()
            }
            
            # Save to history
            self.history.append({
                "prompt": prompt,
                "response": response
            })
            
            return response
            
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    def get_history(self, limit=None):
        """Get conversation history"""
        if limit:
            return self.history[-limit:]
        return self.history
    
    def save_history(self, filename="history.json"):
        """Save conversation history to file"""
        with open(filename, 'w') as f:
            json.dump(self.history, f, indent=2)
        print(f"History saved to {filename}")
    
    def generate_stats(self):
        """Generate statistics from history"""
        if not self.history:
            return "No history available"
        
        total_calls = len(self.history)
        total_tokens = sum(r["response"].get("tokens", 0) 
                          for r in self.history)
        
        return {
            "total_calls": total_calls,
            "total_tokens": total_tokens,
            "avg_tokens": total_tokens // total_calls if total_calls > 0 else 0
        }


# Demo usage
def main():
    """Demonstrate the Prompt Manager"""
    
    print("=== Gen AI Prompt Manager Demo ===\n")
    
    # Initialize manager
    manager = PromptManager()
    
    # Show current config
    print("Current Configuration:")
    print(json.dumps(manager.config, indent=2))
    
    # Create and send prompts
    prompts = [
        {
            "system": "You are a helpful AI assistant.",
            "user": "What is machine learning?"
        },
        {
            "system": "You are a Python coding expert.",
            "user": "Write a function to read a file"
        },
        {
            "system": "You are a creative writer.",
            "user": "Tell me a short story about AI"
        }
    ]
    
    print("\n=== Processing Prompts ===\n")
    for i, p in enumerate(prompts, 1):
        print(f"Prompt {i}:")
        prompt = manager.create_prompt(p["system"], p["user"])
        response = manager.simulate_ai_call(prompt)
        
        if "error" in response:
            print(f"Error: {response['error']}")
        else:
            print(f"Response: {response['content']}")
            print(f"Tokens: {response['tokens']}")
        print("-" * 50)
    
    # Show statistics
    print("\n=== Statistics ===")
    stats = manager.generate_stats()
    print(json.dumps(stats, indent=2))
    
    # Update configuration
    print("\n=== Updating Configuration ===")
    manager.update_config(temperature=0.9, max_tokens=1500)
    print("Configuration updated!")
    
    # Show recent history
    print("\n=== Recent History ===")
    recent = manager.get_history(limit=2)
    for item in recent:
        print(f"User: {item['prompt']['user'][:50]}...")
        print(f"AI: {item['response']['content']}")
        print()
    
    # Save everything
    manager.save_history()
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
