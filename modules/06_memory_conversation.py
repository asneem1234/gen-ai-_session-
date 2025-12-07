"""
06 - Text Generation with Memory (Conversation History)
========================================================

This module demonstrates how to build chatbots with conversation memory.
Students will learn:
- Why conversation history matters
- Implementing chat memory
- Managing context windows
- Building stateful chatbots
- Best practices for conversation management

Teaching Points:
- AI models are stateless by default
- We must maintain conversation history manually
- Context windows have size limits
- Proper memory management is crucial
- Different strategies for different use cases
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime
import json

# Setup
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


# ============================================================================
# SECTION 1: Understanding Conversation Memory
# ============================================================================

def memory_concepts():
    """
    Explain why memory is important and how it works
    """
    print("\n" + "=" * 60)
    print("SECTION 1: Understanding Conversation Memory")
    print("=" * 60)
    
    explanation = """
    🧠 WHY CONVERSATION MEMORY MATTERS:
    
    WITHOUT MEMORY (Stateless):
    ---------------------------
    User: "My name is Alex"
    AI: "Nice to meet you, Alex!"
    
    User: "What's my name?"
    AI: "I don't have information about your name."
    
    ❌ Problem: AI forgot the previous exchange!
    
    
    WITH MEMORY (Stateful):
    -----------------------
    User: "My name is Alex"
    AI: "Nice to meet you, Alex!"
    
    User: "What's my name?"
    AI: "Your name is Alex."
    
    ✅ Solution: Conversation history maintained!
    
    
    📋 HOW CONVERSATION MEMORY WORKS:
    
    1. COLLECT HISTORY
       • Store each user message
       • Store each AI response
       • Maintain chronological order
    
    2. PROVIDE CONTEXT
       • Send history with new prompt
       • AI sees full conversation
       • Can reference previous exchanges
    
    3. MANAGE SIZE
       • Limit total history length
       • Truncate old messages when needed
       • Summarize when appropriate
    
    
    💾 DATA STRUCTURE:
    
    Simple List:
    history = [
        {'role': 'user', 'content': 'Hello!'},
        {'role': 'model', 'content': 'Hi there!'},
        {'role': 'user', 'content': 'How are you?'},
        {'role': 'model', 'content': 'I'm doing well!'}
    ]
    
    
    ⚠️ KEY CHALLENGES:
    
    1. Context Window Limits
       • Models have maximum token limits
       • Long conversations exceed limits
       • Must truncate or summarize
    
    2. Memory vs Performance
       • More history = better context
       • More history = slower responses
       • More history = higher costs
    
    3. Privacy & Security
       • Sensitive information in history
       • Must handle data appropriately
       • Consider retention policies
    """
    
    print(explanation)


# ============================================================================
# SECTION 2: Basic Conversation with Memory
# ============================================================================

def basic_conversation_memory():
    """
    Simple implementation of conversation memory
    """
    print("\n" + "=" * 60)
    print("SECTION 2: Basic Conversation with Memory")
    print("=" * 60)
    
    # Initialize chat
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    
    print("\n🧠 Starting conversation with memory...")
    print("💡 The chat object maintains history automatically\n")
    
    # Conversation sequence
    conversations = [
        "Hi! My name is Sarah and I'm learning Python.",
        "What programming language am I learning?",
        "What's my name?",
        "Can you write a simple Python function for me?"
    ]
    
    for i, user_message in enumerate(conversations, 1):
        print(f"\n{'='*60}")
        print(f"Exchange {i}:")
        print(f"{'='*60}")
        print(f"👤 User: {user_message}")
        
        response = chat.send_message(user_message)
        
        print(f"🤖 AI: {response.text}")
        
        # Show history length
        print(f"\n📊 History: {len(chat.history)} messages")
    
    # Display full history
    print(f"\n\n{'='*60}")
    print("FULL CONVERSATION HISTORY:")
    print(f"{'='*60}")
    
    for i, message in enumerate(chat.history):
        role = "👤 User" if message.role == "user" else "🤖 AI"
        print(f"\n{i+1}. {role}:")
        print(f"   {message.parts[0].text}")


# ============================================================================
# SECTION 3: Manual History Management
# ============================================================================

def manual_history_management():
    """
    Manually manage conversation history for more control
    """
    print("\n" + "=" * 60)
    print("SECTION 3: Manual History Management")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro')
    
    # Manual history list
    conversation_history = []
    
    def add_to_history(role, content):
        """Add a message to history"""
        conversation_history.append({
            'role': role,
            'content': content,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    def build_prompt_with_history(new_message):
        """Build a prompt that includes history"""
        prompt = "Previous conversation:\n\n"
        
        for msg in conversation_history:
            if msg['role'] == 'user':
                prompt += f"User: {msg['content']}\n"
            else:
                prompt += f"Assistant: {msg['content']}\n"
        
        prompt += f"\nUser: {new_message}\nAssistant:"
        return prompt
    
    print("\n💬 Manual History Management Demo:\n")
    
    # Message 1
    msg1 = "I have a cat named Whiskers."
    print(f"👤 User: {msg1}")
    
    prompt1 = f"User: {msg1}\nAssistant:"
    response1 = model.generate_content(prompt1)
    
    add_to_history('user', msg1)
    add_to_history('assistant', response1.text)
    
    print(f"🤖 AI: {response1.text}\n")
    
    # Message 2
    msg2 = "What's my pet's name?"
    print(f"👤 User: {msg2}")
    
    prompt2 = build_prompt_with_history(msg2)
    response2 = model.generate_content(prompt2)
    
    add_to_history('user', msg2)
    add_to_history('assistant', response2.text)
    
    print(f"🤖 AI: {response2.text}\n")
    
    # Display history
    print(f"{'='*60}")
    print("STORED HISTORY:")
    print(f"{'='*60}")
    
    for i, msg in enumerate(conversation_history, 1):
        role = "👤 User" if msg['role'] == 'user' else "🤖 Assistant"
        print(f"\n{i}. {role} [{msg['timestamp']}]:")
        print(f"   {msg['content']}")


# ============================================================================
# SECTION 4: Context Window Management
# ============================================================================

def context_window_management():
    """
    Handle context window limits
    """
    print("\n" + "=" * 60)
    print("SECTION 4: Context Window Management")
    print("=" * 60)
    
    print("""
    🔢 CONTEXT WINDOW LIMITS:
    
    • Gemini Pro: ~30,000 tokens (~22,500 words)
    • 1 token ≈ 0.75 words (English)
    • Must manage history size
    
    STRATEGIES:
    
    1️⃣ TRUNCATION (Simple)
       • Keep only last N messages
       • Fast and simple
       • May lose important context
    
    2️⃣ SLIDING WINDOW
       • Always keep first message (system prompt)
       • Keep last N messages
       • Balance between context and relevance
    
    3️⃣ SUMMARIZATION
       • Summarize old messages
       • Keep recent messages verbatim
       • Better context retention
    
    4️⃣ IMPORTANCE-BASED
       • Identify key messages
       • Remove less important ones
       • Most sophisticated approach
    """)
    
    # Demonstration: Truncation
    print("\n" + "="*60)
    print("DEMONSTRATION: Truncation Strategy")
    print("="*60)
    
    MAX_HISTORY = 6  # Keep last 6 messages (3 exchanges)
    
    conversation_history = []
    
    # Simulate a long conversation
    messages = [
        "My favorite color is blue.",
        "I also like red and green.",
        "What colors do I like?",
        "Now let's talk about food.",
        "I love pizza.",
        "What's my favorite food?",
    ]
    
    model = genai.GenerativeModel('gemini-pro')
    
    for msg in messages:
        print(f"\n👤 User: {msg}")
        
        # Build chat with limited history
        chat = model.start_chat(history=conversation_history[-MAX_HISTORY:])
        response = chat.send_message(msg)
        
        print(f"🤖 AI: {response.text}")
        
        # Add to full history
        conversation_history.append({'role': 'user', 'parts': [msg]})
        conversation_history.append({'role': 'model', 'parts': [response.text]})
        
        print(f"📊 Total history: {len(conversation_history)} | Using: {min(len(conversation_history), MAX_HISTORY)}")
    
    print(f"\n💡 Notice: With truncation, older context may be lost!")


# ============================================================================
# SECTION 5: Conversation History Class
# ============================================================================

def conversation_history_class():
    """
    Build a reusable class for managing conversation history
    """
    print("\n" + "=" * 60)
    print("SECTION 5: Conversation History Class")
    print("=" * 60)
    
    class ConversationManager:
        """Manages conversation history with various strategies"""
        
        def __init__(self, max_messages=10):
            self.history = []
            self.max_messages = max_messages
        
        def add_message(self, role, content):
            """Add a message to history"""
            self.history.append({
                'role': role,
                'content': content,
                'timestamp': datetime.now()
            })
        
        def get_recent_history(self, n=None):
            """Get recent N messages"""
            if n is None:
                n = self.max_messages
            return self.history[-n:]
        
        def get_formatted_history(self):
            """Format history for display"""
            formatted = []
            for msg in self.history:
                role = "👤 User" if msg['role'] == 'user' else "🤖 AI"
                time = msg['timestamp'].strftime("%H:%M:%S")
                formatted.append(f"[{time}] {role}: {msg['content']}")
            return "\n".join(formatted)
        
        def clear_history(self):
            """Clear all history"""
            self.history = []
        
        def get_message_count(self):
            """Get total message count"""
            return len(self.history)
        
        def export_history(self, filename):
            """Export history to JSON file"""
            export_data = []
            for msg in self.history:
                export_data.append({
                    'role': msg['role'],
                    'content': msg['content'],
                    'timestamp': msg['timestamp'].isoformat()
                })
            
            with open(filename, 'w') as f:
                json.dump(export_data, f, indent=2)
            
            print(f"✅ History exported to {filename}")
    
    # Demo the class
    print("\n📦 ConversationManager Class Demo:\n")
    
    manager = ConversationManager(max_messages=8)
    
    # Add some messages
    messages = [
        ("user", "Hello! I'm studying AI."),
        ("assistant", "Great! What aspect of AI interests you?"),
        ("user", "Natural language processing."),
        ("assistant", "NLP is fascinating! Are you working on any projects?"),
    ]
    
    for role, content in messages:
        manager.add_message(role, content)
    
    print("📋 Current History:")
    print("-" * 60)
    print(manager.get_formatted_history())
    print()
    
    print(f"📊 Total messages: {manager.get_message_count()}")
    print(f"📊 Max messages: {manager.max_messages}")
    
    # Export
    os.makedirs('outputs', exist_ok=True)
    manager.export_history('outputs/conversation_history.json')
    
    print("\n💻 CLASS CODE:")
    print("-" * 60)
    print("""
class ConversationManager:
    def __init__(self, max_messages=10):
        self.history = []
        self.max_messages = max_messages
    
    def add_message(self, role, content):
        self.history.append({
            'role': role,
            'content': content,
            'timestamp': datetime.now()
        })
    
    def get_recent_history(self, n=None):
        if n is None:
            n = self.max_messages
        return self.history[-n:]
    
    # ... more methods ...
    """)


# ============================================================================
# SECTION 6: Interactive Chat with Memory
# ============================================================================

def interactive_memory_chat():
    """
    Full interactive chat with memory management
    """
    print("\n" + "=" * 60)
    print("SECTION 6: Interactive Chat with Memory")
    print("=" * 60)
    print("\nChat with AI that remembers your conversation!")
    print("Commands:")
    print("  /history - Show conversation history")
    print("  /clear - Clear history")
    print("  /count - Show message count")
    print("  /quit - Exit")
    print()
    
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    
    message_count = 0
    
    while True:
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
        
        # Handle commands
        if user_input == '/quit':
            print("👋 Goodbye!")
            break
        elif user_input == '/history':
            print("\n📋 Conversation History:")
            print("-" * 60)
            for i, msg in enumerate(chat.history, 1):
                role = "👤 User" if msg.role == "user" else "🤖 AI"
                print(f"{i}. {role}: {msg.parts[0].text[:100]}...")
            print("-" * 60 + "\n")
            continue
        elif user_input == '/clear':
            chat = model.start_chat(history=[])
            message_count = 0
            print("🗑️  History cleared!\n")
            continue
        elif user_input == '/count':
            print(f"📊 Total messages: {len(chat.history)}\n")
            continue
        
        # Send message
        try:
            message_count += 1
            response = chat.send_message(user_input)
            print(f"AI: {response.text}\n")
            
            # Show memory indicator every few messages
            if message_count % 3 == 0:
                print(f"💡 Memory: {len(chat.history)} messages stored\n")
                
        except Exception as e:
            print(f"❌ Error: {e}\n")


# ============================================================================
# SECTION 7: Advanced Memory Techniques
# ============================================================================

def advanced_memory_techniques():
    """
    Advanced techniques for conversation memory
    """
    print("\n" + "=" * 60)
    print("SECTION 7: Advanced Memory Techniques")
    print("=" * 60)
    
    techniques = """
    🎓 ADVANCED TECHNIQUES:
    
    1. CONVERSATION SUMMARIZATION
    ==============================
    When history gets too long, summarize older messages:
    
    Old messages:
    - User: "I like Python"
    - AI: "Python is great for beginners"
    - User: "I'm learning Django"
    - AI: "Django is a powerful web framework"
    
    Summarized:
    "User is learning Python and Django for web development"
    
    Code approach:
    def summarize_history(old_messages):
        prompt = f"Summarize this conversation: {old_messages}"
        summary = model.generate_content(prompt)
        return summary.text
    
    
    2. ENTITY TRACKING
    ==================
    Extract and track important entities:
    
    Tracked entities:
    - user_name: "Alex"
    - preferences: ["Python", "Machine Learning"]
    - goals: ["Build a chatbot"]
    
    Benefits:
    • Quickly access key information
    • Personalize responses
    • Maintain consistency
    
    
    3. CONVERSATION BRANCHING
    =========================
    Allow users to explore different paths:
    
    Main thread:
    User: "Tell me about ML" → AI responds
    
    Branch 1:
    User: "More about supervised learning" → AI responds
    
    Branch 2 (backtrack to main):
    User: "Actually, tell me about deep learning" → AI responds
    
    
    4. SEMANTIC SEARCH OVER HISTORY
    ================================
    Instead of keeping all messages, search for relevant ones:
    
    1. Convert all messages to embeddings
    2. When new message comes, find similar past messages
    3. Include only relevant history
    4. More efficient than keeping everything
    
    
    5. SESSION MANAGEMENT
    =====================
    Separate conversations into sessions:
    
    Session 1 (Morning): Work-related questions
    Session 2 (Evening): Personal questions
    
    Benefits:
    • Better organization
    • Clear context boundaries
    • Easy to archive/retrieve
    
    
    6. MEMORY PERSISTENCE
    =====================
    Save conversations for later:
    
    Database storage:
    • User ID
    • Conversation ID
    • Messages with timestamps
    • Metadata (topic, sentiment, etc.)
    
    Benefits:
    • Continue conversations later
    • Analytics and insights
    • User history across sessions
    """
    
    print(techniques)


# ============================================================================
# SECTION 8: Best Practices
# ============================================================================

def memory_best_practices():
    """
    Best practices for conversation memory
    """
    print("\n" + "=" * 60)
    print("SECTION 8: Best Practices")
    print("=" * 60)
    
    practices = """
    ✅ DO:
    
    1. Set reasonable limits
       • Don't store infinite history
       • Balance context vs performance
       • Typical: 10-20 message pairs
    
    2. Handle edge cases
       • Very long messages
       • Empty messages
       • Special characters
       • Multi-language support
    
    3. Provide user control
       • Let users clear history
       • Show history on request
       • Export conversations
       • Privacy controls
    
    4. Optimize performance
       • Cache when possible
       • Lazy load old messages
       • Compress stored data
       • Use efficient data structures
    
    5. Security & Privacy
       • Encrypt sensitive data
       • Don't store credentials
       • Implement retention policies
       • Allow data deletion
    
    
    ❌ DON'T:
    
    1. Store everything forever
       • Wastes resources
       • Privacy concerns
       • Performance degrades
    
    2. Ignore context limits
       • Will cause errors
       • Responses may fail
       • Poor user experience
    
    3. Mix conversations
       • Keep sessions separate
       • Clear boundaries
       • Avoid confusion
    
    4. Forget error handling
       • History corruption
       • API failures
       • Network issues
    
    
    💡 TIPS:
    
    • Test with long conversations
    • Monitor token usage
    • Implement graceful degradation
    • Provide clear feedback to users
    • Document your approach
    • Consider different user needs
    """
    
    print(practices)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main function with menu
    """
    print("\n")
    print("🎓 " + "=" * 58 + " 🎓")
    print("  GENERATIVE AI SESSION - MODULE 6: MEMORY & HISTORY")
    print("🎓 " + "=" * 58 + " 🎓")
    
    menu = """
    Choose a section to run:
    
    1. Understanding Conversation Memory
    2. Basic Conversation with Memory
    3. Manual History Management
    4. Context Window Management
    5. Conversation History Class
    6. Interactive Chat with Memory
    7. Advanced Memory Techniques
    8. Best Practices
    
    all - Run all (except interactive)
    quit - Exit
    
    """
    
    while True:
        print(menu)
        choice = input("Your choice: ").strip().lower()
        
        if choice in ['quit', 'q', 'exit']:
            print("👋 Goodbye!")
            break
        elif choice == '1':
            memory_concepts()
        elif choice == '2':
            basic_conversation_memory()
        elif choice == '3':
            manual_history_management()
        elif choice == '4':
            context_window_management()
        elif choice == '5':
            conversation_history_class()
        elif choice == '6':
            interactive_memory_chat()
        elif choice == '7':
            advanced_memory_techniques()
        elif choice == '8':
            memory_best_practices()
        elif choice == 'all':
            memory_concepts()
            basic_conversation_memory()
            manual_history_management()
            context_window_management()
            conversation_history_class()
            advanced_memory_techniques()
            memory_best_practices()
            print("\n✅ All sections completed!")
            print("💡 Try section 6 separately for interactive chat")
            break
        else:
            print("⚠️  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
    # Teaching Questions:
    # 1. Why do AI models need explicit memory management?
    # 2. What are the trade-offs of keeping more history?
    # 3. How would you design a memory system for a production chatbot?
