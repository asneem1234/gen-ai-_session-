"""
08 - System Instructions
=========================

This module demonstrates system instructions (system prompts).
Students will learn:
- What system instructions are
- How they shape AI behavior
- Creating effective system prompts
- Different persona examples
- Best practices

Teaching Points:
- System instructions set the AI's role and behavior
- They persist across the conversation
- Very powerful for customizing AI behavior
- Essential for building specific applications
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Setup
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


# ============================================================================
# SECTION 1: Understanding System Instructions
# ============================================================================

def system_instructions_overview():
    """
    Explain what system instructions are and why they matter
    """
    print("\n" + "=" * 60)
    print("SECTION 1: Understanding System Instructions")
    print("=" * 60)
    
    explanation = """
    📜 WHAT ARE SYSTEM INSTRUCTIONS?
    
    System instructions (also called system prompts) are special messages
    that define the AI's role, behavior, and constraints BEFORE the conversation begins.
    
    Think of them as:
    • Job description for the AI
    • Personality settings
    • Rules and guidelines
    • Context that applies to everything
    
    
    🔄 HOW THEY WORK:
    
    Traditional Approach:
    User: "You are a helpful tutor. Now explain Python."
    AI: Responds as tutor
    User: "What is a list?"
    AI: Might forget it's a tutor
    
    With System Instructions:
    System: "You are a helpful Python tutor."
    User: "Explain lists."
    AI: Responds as tutor
    User: "What about dictionaries?"
    AI: Still remembers it's a tutor
    
    
    ✅ BENEFITS:
    
    1. Consistency
       • Behavior persists across conversation
       • Don't need to remind AI of its role
    
    2. Token Efficiency
       • System instructions don't count toward conversation history
       • More room for actual conversation
    
    3. Clear Separation
       • System vs User vs Assistant roles
       • Better structured prompts
    
    4. Customization
       • Create specialized AI assistants
       • Control tone, style, expertise level
    
    
    💡 USE CASES:
    
    • Customer support chatbots
    • Educational tutors
    • Code assistants
    • Writing coaches
    • Domain experts
    • Entertainment (game NPCs, storytellers)
    """
    
    print(explanation)


# ============================================================================
# SECTION 2: Basic System Instructions
# ============================================================================

def basic_system_instructions():
    """
    Simple examples of system instructions
    """
    print("\n" + "=" * 60)
    print("SECTION 2: Basic System Instructions")
    print("=" * 60)
    
    examples = [
        {
            "name": "Default (No System Instruction)",
            "system": None,
            "prompt": "What is Python?"
        },
        {
            "name": "Concise Assistant",
            "system": "You are a helpful assistant. Keep answers brief and to the point.",
            "prompt": "What is Python?"
        },
        {
            "name": "Detailed Explainer",
            "system": "You are an educational assistant. Provide detailed, thorough explanations with examples.",
            "prompt": "What is Python?"
        }
    ]
    
    for example in examples:
        print(f"\n{'='*60}")
        print(f"🎭 {example['name']}")
        print(f"{'='*60}")
        
        if example['system']:
            print(f"\n📜 System Instruction:")
            print(f"   \"{example['system']}\"")
        else:
            print(f"\n📜 System Instruction: (None)")
        
        print(f"\n👤 User: {example['prompt']}")
        print(f"\n🤖 AI Response:")
        print("-" * 60)
        
        # Create model with or without system instruction
        if example['system']:
            model = genai.GenerativeModel(
                'gemini-pro',
                system_instruction=example['system']
            )
        else:
            model = genai.GenerativeModel('gemini-pro')
        
        response = model.generate_content(example['prompt'])
        print(response.text)
        print()


# ============================================================================
# SECTION 3: Persona Examples
# ============================================================================

def persona_examples():
    """
    Different AI personas using system instructions
    """
    print("\n" + "=" * 60)
    print("SECTION 3: AI Personas")
    print("=" * 60)
    
    personas = {
        "🎓 Python Tutor": """You are an experienced Python programming tutor.
You explain concepts clearly for beginners, use simple language,
provide code examples, and encourage learning. Be patient and supportive.""",
        
        "👨‍💼 Professional Assistant": """You are a professional business assistant.
You communicate formally, use proper grammar, focus on efficiency,
and provide structured responses. Be polite and businesslike.""",
        
        "🤖 Code Reviewer": """You are an expert code reviewer.
Analyze code for bugs, suggest improvements, point out best practices,
and explain your reasoning. Be constructive and educational.""",
        
        "✍️ Creative Writer": """You are a creative writing coach.
Help with storytelling, character development, and plot ideas.
Be imaginative, encouraging, and provide specific suggestions.""",
        
        "🧑‍🏫 ELI5 Explainer": """You explain things like I'm 5 years old.
Use simple words, fun analogies, and short sentences.
Make complex topics easy to understand. Be friendly and patient."""
    }
    
    test_prompt = "What is recursion?"
    
    print(f"\n📝 Same question to different personas:")
    print(f"   '{test_prompt}'\n")
    
    for persona_name, system_instruction in personas.items():
        print("=" * 60)
        print(f"{persona_name}")
        print("=" * 60)
        print(f"\n📜 System Instruction:")
        print(f"   {system_instruction[:80]}...")
        
        model = genai.GenerativeModel(
            'gemini-pro',
            system_instruction=system_instruction
        )
        
        response = model.generate_content(test_prompt)
        
        print(f"\n🤖 Response:")
        print("-" * 60)
        print(response.text[:300] + "..." if len(response.text) > 300 else response.text)
        print("\n")


# ============================================================================
# SECTION 4: System Instructions with Constraints
# ============================================================================

def system_instructions_with_constraints():
    """
    Using system instructions to set constraints and rules
    """
    print("\n" + "=" * 60)
    print("SECTION 4: System Instructions with Constraints")
    print("=" * 60)
    
    print("\n💡 System instructions can enforce rules and constraints\n")
    
    # Example 1: Format constraints
    print("1️⃣ FORMAT CONSTRAINTS")
    print("=" * 60)
    
    system1 = """You are an assistant that ALWAYS responds in the following format:
    
[ANSWER]: Your main answer here
[CONFIDENCE]: High/Medium/Low
[SOURCE]: Where this information comes from

Never deviate from this format."""
    
    model1 = genai.GenerativeModel('gemini-pro', system_instruction=system1)
    
    print(f"📜 System: Format must include ANSWER, CONFIDENCE, SOURCE")
    print(f"\n👤 User: What is the capital of Japan?")
    
    response1 = model1.generate_content("What is the capital of Japan?")
    print(f"\n🤖 AI:\n{response1.text}\n")
    
    # Example 2: Length constraints
    print("\n2️⃣ LENGTH CONSTRAINTS")
    print("=" * 60)
    
    system2 = """You are a concise assistant. ALWAYS limit your responses to maximum 2 sentences.
Be brief and to the point. Never exceed 2 sentences."""
    
    model2 = genai.GenerativeModel('gemini-pro', system_instruction=system2)
    
    print(f"📜 System: Maximum 2 sentences per response")
    print(f"\n👤 User: Explain machine learning.")
    
    response2 = model2.generate_content("Explain machine learning.")
    print(f"\n🤖 AI:\n{response2.text}\n")
    
    # Example 3: Knowledge cutoff
    print("\n3️⃣ KNOWLEDGE CONSTRAINTS")
    print("=" * 60)
    
    system3 = """You are a historical AI assistant. You can only discuss events before 1900.
If asked about anything after 1900, politely decline and suggest asking about earlier periods."""
    
    model3 = genai.GenerativeModel('gemini-pro', system_instruction=system3)
    
    print(f"📜 System: Only discuss pre-1900 events")
    print(f"\n👤 User: Tell me about World War II.")
    
    response3 = model3.generate_content("Tell me about World War II.")
    print(f"\n🤖 AI:\n{response3.text}\n")


# ============================================================================
# SECTION 5: Domain-Specific Assistants
# ============================================================================

def domain_specific_assistants():
    """
    Creating specialized domain assistants
    """
    print("\n" + "=" * 60)
    print("SECTION 5: Domain-Specific Assistants")
    print("=" * 60)
    
    domains = {
        "Medical Assistant": {
            "system": """You are a medical information assistant. Provide accurate health information,
but always remind users to consult healthcare professionals for medical advice.
Be clear that you're not a replacement for professional medical care.""",
            "prompt": "What causes headaches?"
        },
        "Legal Assistant": {
            "system": """You are a legal information assistant. Provide general legal information,
but always clarify this is not legal advice. Recommend consulting licensed attorneys for specific cases.
Be precise and cite general legal principles.""",
            "prompt": "What is a contract?"
        },
        "Fitness Coach": {
            "system": """You are an enthusiastic fitness coach. Motivate users, provide workout tips,
and encourage healthy habits. Be energetic and positive. Always emphasize proper form and safety.""",
            "prompt": "How do I start exercising?"
        }
    }
    
    for domain_name, config in domains.items():
        print(f"\n{'='*60}")
        print(f"🎯 {domain_name}")
        print(f"{'='*60}")
        
        print(f"\n📜 System Instruction:\n   {config['system'][:100]}...")
        print(f"\n👤 User: {config['prompt']}")
        
        model = genai.GenerativeModel(
            'gemini-pro',
            system_instruction=config['system']
        )
        
        response = model.generate_content(config['prompt'])
        
        print(f"\n🤖 AI Response:")
        print("-" * 60)
        print(response.text[:400] + "..." if len(response.text) > 400 else response.text)
        print()


# ============================================================================
# SECTION 6: Combining System Instructions with Chat
# ============================================================================

def system_instructions_with_chat():
    """
    Using system instructions in multi-turn conversations
    """
    print("\n" + "=" * 60)
    print("SECTION 6: System Instructions with Chat")
    print("=" * 60)
    
    system_instruction = """You are a friendly Python tutor named PyBot.
You love teaching programming and use emojis occasionally.
Always encourage students and celebrate their progress.
Keep explanations clear and beginner-friendly."""
    
    print(f"\n📜 System Instruction:")
    print(f"   {system_instruction}\n")
    
    model = genai.GenerativeModel(
        'gemini-pro',
        system_instruction=system_instruction
    )
    
    chat = model.start_chat()
    
    conversations = [
        "Hi! I'm new to Python.",
        "Can you explain what a variable is?",
        "Great! Now what's a function?",
        "Thanks PyBot!"
    ]
    
    print("💬 Conversation:")
    print("=" * 60)
    
    for i, user_msg in enumerate(conversations, 1):
        print(f"\n{i}. 👤 User: {user_msg}")
        
        response = chat.send_message(user_msg)
        
        print(f"   🤖 PyBot: {response.text}\n")
    
    print("💡 Notice: The AI maintains its persona throughout the conversation!")


# ============================================================================
# SECTION 7: Best Practices
# ============================================================================

def system_instructions_best_practices():
    """
    Best practices for writing system instructions
    """
    print("\n" + "=" * 60)
    print("SECTION 7: Best Practices for System Instructions")
    print("=" * 60)
    
    practices = """
    ✅ DO:
    
    1. BE SPECIFIC
       ❌ "Be helpful"
       ✅ "You are a helpful Python tutor. Explain concepts clearly for beginners."
    
    2. DEFINE THE ROLE
       ✅ "You are a [role]"
       ✅ State expertise level
       ✅ Mention target audience
    
    3. SET CLEAR CONSTRAINTS
       ✅ Response format
       ✅ Length limits
       ✅ What to avoid
       ✅ What to emphasize
    
    4. INCLUDE TONE/STYLE
       ✅ "Be professional"
       ✅ "Use friendly language"
       ✅ "Be concise"
       ✅ "Be enthusiastic"
    
    5. ADD SAFETY GUIDELINES
       ✅ Disclaimers for sensitive topics
       ✅ When to defer to experts
       ✅ Ethical boundaries
    
    
    ❌ DON'T:
    
    1. Be too vague
       ❌ "Answer questions well"
       
    2. Contradict yourself
       ❌ "Be brief but provide detailed explanations"
       
    3. Overload with instructions
       ❌ 10 paragraphs of rules
       ✅ Keep it focused and clear
       
    4. Forget about context
       ❌ Instructions that don't match use case
    
    
    📝 TEMPLATE:
    
    You are a [ROLE] with expertise in [DOMAIN].
    
    Your goals:
    - [GOAL 1]
    - [GOAL 2]
    
    Guidelines:
    - [RULE 1]
    - [RULE 2]
    
    Style:
    - [TONE/STYLE]
    
    Constraints:
    - [LIMITATION 1]
    - [LIMITATION 2]
    
    
    💡 EXAMPLES:
    
    GOOD - Customer Support:
    "You are a friendly customer support agent for TechCorp.
    Help users troubleshoot issues patiently.
    Always be polite and professional.
    If you can't solve something, direct them to human support.
    Keep responses concise but helpful."
    
    GOOD - Code Reviewer:
    "You are an experienced senior developer reviewing code.
    Focus on:
    - Bug identification
    - Performance issues
    - Best practices
    - Security concerns
    
    Provide constructive feedback with explanations.
    Suggest specific improvements.
    Acknowledge good code too."
    
    
    🎯 TESTING YOUR SYSTEM INSTRUCTIONS:
    
    1. Test with various inputs
    2. Check consistency
    3. Verify constraints are followed
    4. Adjust based on results
    5. Get feedback from users
    """
    
    print(practices)


# ============================================================================
# SECTION 8: Interactive Persona Creator
# ============================================================================

def interactive_persona_creator():
    """
    Let users create and test their own personas
    """
    print("\n" + "=" * 60)
    print("SECTION 8: Interactive Persona Creator")
    print("=" * 60)
    print("\nCreate your own AI persona!")
    print("Type 'quit' to exit\n")
    
    while True:
        print("=" * 60)
        
        role = input("\n1. What role should the AI have? (or 'quit'): ").strip()
        if role.lower() in ['quit', 'exit', 'q']:
            break
        
        if not role:
            continue
        
        tone = input("2. What tone/style? (e.g., friendly, professional): ").strip() or "helpful"
        constraint = input("3. Any constraint? (e.g., brief answers, use examples): ").strip() or "none"
        
        # Build system instruction
        system_instruction = f"You are a {role}. "
        system_instruction += f"Your communication style is {tone}. "
        if constraint != "none":
            system_instruction += f"Important: {constraint}."
        
        print(f"\n📜 Generated System Instruction:")
        print("-" * 60)
        print(system_instruction)
        print("-" * 60)
        
        # Test it
        test_prompt = input("\n4. Test prompt for your persona: ").strip()
        if test_prompt:
            print("\n⏳ Generating response...\n")
            
            model = genai.GenerativeModel(
                'gemini-pro',
                system_instruction=system_instruction
            )
            
            response = model.generate_content(test_prompt)
            
            print("🤖 AI Response:")
            print("-" * 60)
            print(response.text)
            print("-" * 60)
        
        print()


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main function with menu
    """
    print("\n")
    print("🎓 " + "=" * 58 + " 🎓")
    print("  GENERATIVE AI SESSION - MODULE 8: SYSTEM INSTRUCTIONS")
    print("🎓 " + "=" * 58 + " 🎓")
    
    menu = """
    Choose a section to run:
    
    1. Understanding System Instructions
    2. Basic System Instructions
    3. AI Personas
    4. System Instructions with Constraints
    5. Domain-Specific Assistants
    6. System Instructions with Chat
    7. Best Practices
    8. Interactive Persona Creator
    
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
            system_instructions_overview()
        elif choice == '2':
            basic_system_instructions()
        elif choice == '3':
            persona_examples()
        elif choice == '4':
            system_instructions_with_constraints()
        elif choice == '5':
            domain_specific_assistants()
        elif choice == '6':
            system_instructions_with_chat()
        elif choice == '7':
            system_instructions_best_practices()
        elif choice == '8':
            interactive_persona_creator()
        elif choice == 'all':
            system_instructions_overview()
            basic_system_instructions()
            persona_examples()
            system_instructions_with_constraints()
            domain_specific_assistants()
            system_instructions_with_chat()
            system_instructions_best_practices()
            print("\n✅ All sections completed!")
            print("💡 Try section 8 separately for interactive creation")
            break
        else:
            print("⚠️  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
    # Teaching Questions:
    # 1. How do system instructions differ from regular prompts?
    # 2. When would you use system instructions?
    # 3. What makes a good system instruction?
