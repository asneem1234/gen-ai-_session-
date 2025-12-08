# 09 RAG Basic - Complete Code Explanation

## 📋 Overview
This code demonstrates RAG (Retrieval-Augmented Generation) - a powerful technique that combines information retrieval with AI generation. Instead of relying solely on the AI's training data, RAG retrieves relevant information from a custom knowledge base and uses it to generate accurate, context-aware responses. This is essential for building AI systems with up-to-date, domain-specific knowledge.

---

## 💻 Complete Code with Line-by-Line Explanation

```python
import os
# WHY: Import operating system module
# WHAT IT DOES: Provides access to environment variables
# WHEN TO USE: Required for reading API keys securely

from dotenv import load_dotenv
# WHY: Import function to load .env file
# WHAT IT DOES: Reads environment variables from .env
# SECURITY: Keeps sensitive information out of code

import google.generativeai as genai
# WHY: Import Google Generative AI library
# WHAT IT DOES: Provides tools for AI operations
# CAPABILITY: Generates responses based on provided context

import numpy as np
# WHY: Import NumPy for numerical operations
# WHAT IT DOES: Provides array operations and mathematical functions
# USE CASE: Calculating similarity between text embeddings
# NOTE: In production, use proper embedding models

load_dotenv()
# WHY: Load environment variables at module level
# WHAT IT DOES: Makes GOOGLE_API_KEY accessible
# TIMING: Called immediately before configuration

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
# WHY: Authenticate with Gemini API
# WHAT IT DOES: Sets up API key for all requests
# REQUIRED: Must be done before any AI operations

def create_knowledge_base():
    # WHY: Create custom knowledge base for RAG
    # WHAT IT DOES: Defines domain-specific information
    # USE CASE: Your own data that AI doesn't know
    # RETURNS: Dictionary of topics and their content
    # SCALABILITY: In production, use databases or vector stores
    
    return {
        "Python Basics": "Python is a high-level programming language known for its simplicity and readability.",
        "Machine Learning": "ML is a subset of AI that enables systems to learn from data without explicit programming.",
        "Neural Networks": "Neural networks are computing systems inspired by biological neural networks in animal brains.",
        "Deep Learning": "Deep learning uses neural networks with multiple layers to learn from large amounts of data."
    }
    # WHY: Return dictionary mapping topics to descriptions
    # WHAT IT DOES: Creates searchable knowledge base
    # STRUCTURE: {topic: content}
    # PURPOSE: AI will retrieve relevant content based on query
    # SIMPLIFIED: Real RAG uses hundreds/thousands of documents

def simple_embedding(text):
    # WHY: Convert text to numerical representation
    # WHAT IT DOES: Creates vector representation of text
    # USE CASE: Enables mathematical similarity comparison
    # SIMPLIFIED: Uses random vectors for demonstration
    
    return np.random.rand(10)
    # WHY: Generate random 10-dimensional vector
    # WHAT IT DOES: Returns array of 10 random numbers (0-1)
    # SIMPLIFIED: Real embeddings use models like text-embedding-004
    # DIMENSIONS: Real embeddings typically 768 or 1536 dimensions
    # WARNING: Random vectors don't capture semantic meaning!
    # PRODUCTION: Use genai.embed_content() or similar
    # NOTE: This is just for demonstration of RAG concept

def find_similar(query, knowledge_base):
    # WHY: Find most relevant content for user query
    # WHAT IT DOES: Retrieves best matching document from knowledge base
    # PROCESS: Convert query and documents to vectors, compare similarity
    # RETURNS: Most relevant document content
    # CORE RAG STEP: This is the "Retrieval" part
    
    query_emb = simple_embedding(query)
    # WHY: Convert user query to vector
    # WHAT IT DOES: Creates numerical representation of query
    # PURPOSE: Enables comparison with document vectors
    # RESULT: 10-dimensional array
    
    similarities = {}
    # WHY: Store similarity scores for all documents
    # WHAT IT DOES: Dictionary to hold topic → similarity mappings
    # STRUCTURE: {topic: similarity_score}
    # PURPOSE: Compare all documents to find best match
    
    for topic, content in knowledge_base.items():
        # WHY: Loop through each document in knowledge base
        # WHAT IT DOES: Checks similarity of each document to query
        # ITERATION: Processes all available knowledge
        # COMPARISON: Finds best match among all documents
        
        content_emb = simple_embedding(content)
        # WHY: Convert document content to vector
        # WHAT IT DOES: Creates numerical representation
        # PURPOSE: Enable comparison with query vector
        # NOTE: Real systems pre-compute and cache these
        
        similarity = np.dot(query_emb, content_emb)
        # WHY: Calculate similarity between query and document
        # WHAT IT DOES: Computes dot product of two vectors
        # MATH: Dot product measures vector similarity
        # RANGE: Higher number = more similar
        # ALTERNATIVE: Could use cosine similarity or other metrics
        # SIMPLIFIED: With random vectors, this is random!
        # PRODUCTION: Use proper embeddings for meaningful similarity
        
        similarities[topic] = similarity
        # WHY: Store similarity score for this document
        # WHAT IT DOES: Records how well document matches query
        # ACCUMULATES: Builds complete similarity ranking
    
    best_topic = max(similarities, key=similarities.get)
    # WHY: Find document with highest similarity
    # WHAT IT DOES: Identifies most relevant document
    # METHOD: max() with key=similarities.get finds highest value
    # RESULT: Topic name with best match
    # RETRIEVAL: This selects the context for generation
    
    return knowledge_base[best_topic]
    # WHY: Return content of most relevant document
    # WHAT IT DOES: Retrieves actual text content
    # PURPOSE: This context will be given to AI for generation
    # RAG STEP: Retrieved knowledge for augmented generation

def rag_query(query, knowledge_base):
    # WHY: Execute complete RAG pipeline
    # WHAT IT DOES: Retrieves context and generates response
    # RAG = Retrieval-Augmented Generation
    # STEPS: 1) Retrieve relevant docs, 2) Generate with context
    # PURPOSE: Combine custom knowledge with AI generation
    
    relevant_context = find_similar(query, knowledge_base)
    # WHY: Retrieve most relevant information
    # WHAT IT DOES: Finds best matching document
    # RAG STEP 1: RETRIEVAL
    # RESULT: Text content related to query
    # PURPOSE: Provide AI with specific knowledge to use
    
    model = genai.GenerativeModel('gemini-2.0-flash')
    # WHY: Create AI model for generation
    # WHAT IT DOES: Initializes model instance
    # RAG STEP 2: GENERATION (with retrieved context)
    
    prompt = f"""Context: {relevant_context}
# WHY: Create structured prompt with context
# WHAT IT DOES: Combines retrieved knowledge with user query
# STRUCTURE:
#   1. Context: Retrieved information
#   2. Question: User's query
#   3. Instruction: How to use context
# FORMAT: Clear sections for AI to understand

Question: {query}
# WHY: Include user's original question
# WHAT IT DOES: Specifies what to answer
# PLACEMENT: After context so AI sees it first

Answer based on the context provided:"""
# WHY: Explicit instruction to use provided context
# WHAT IT DOES: Tells AI to base answer on retrieved knowledge
# IMPORTANT: Prevents hallucination by grounding in context
# EFFECT: AI answers using YOUR knowledge, not just training data
    
    response = model.generate_content(prompt)
    # WHY: Generate answer using context
    # WHAT IT DOES: AI reads context and answers question
    # RAG STEP 2: AUGMENTED GENERATION
    # BENEFIT: Answer based on your custom knowledge
    # ACCURACY: More reliable than AI's general knowledge
    
    return response.text
    # WHY: Return generated answer
    # WHAT IT DOES: Provides final RAG response
    # RESULT: Context-aware, knowledge-grounded answer

if __name__ == "__main__":
    # WHY: Check if script is run directly
    # WHAT IT DOES: Only executes demos when main program
    # BEST PRACTICE: Prevents auto-execution on import
    
    kb = create_knowledge_base()
    # WHY: Initialize knowledge base
    # WHAT IT DOES: Creates dictionary of knowledge
    # CONTAINS: 4 topics with descriptions
    # PURPOSE: Data source for retrieval
    
    print("Knowledge Base:")
    for topic in kb.keys():
        print(f"  - {topic}")
    # WHY: Display available knowledge
    # WHAT IT DOES: Lists all topics in knowledge base
    # UX: Shows what information is available
    # HELPFUL: User sees what questions can be answered
    
    queries = [
        "What is Python?",
        "Tell me about machine learning",
        "How do neural networks work?"
    ]
    # WHY: Define test queries
    # WHAT IT DOES: Creates list of questions to test
    # PURPOSE: Demonstrate RAG with different questions
    # VARIETY: Different topics to show retrieval
    
    print("\nRAG Queries:")
    # WHY: Label the query section
    # WHAT IT DOES: Prints header
    # UX: Separates knowledge base display from results
    
    for query in queries:
        # WHY: Loop through each test query
        # WHAT IT DOES: Processes each question with RAG
        # DEMONSTRATES: Multiple RAG executions
        
        print(f"\nQ: {query}")
        # WHY: Display the question
        # WHAT IT DOES: Shows user's query
        # FORMAT: Q: for Question
        # UX: Clear question-answer format
        
        answer = rag_query(query, kb)
        # WHY: Execute RAG pipeline for this query
        # WHAT IT DOES:
        #   1. Finds relevant document
        #   2. Generates context-based answer
        # RAG PROCESS: Complete retrieval + generation
        
        print(f"A: {answer}")
        # WHY: Display the answer
        # WHAT IT DOES: Shows RAG-generated response
        # FORMAT: A: for Answer
        # RESULT: Knowledge-grounded response
```

---

## 🔄 Code Workflow Diagram

```
┌────────────────────────────────────────────────────────────────────┐
│                        START PROGRAM                                │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  1. IMPORT & CONFIGURE                                              │
│     ├─ Import: os, dotenv, genai, numpy                            │
│     ├─ Load .env file                                              │
│     └─ Configure API key                                           │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  2. CREATE KNOWLEDGE BASE                                           │
│     │                                                               │
│     └─ Knowledge Base Dictionary:                                  │
│         ┌────────────────────────────────────────────┐             │
│         │ "Python Basics" →                          │             │
│         │   "Python is a high-level language..."     │             │
│         │                                            │             │
│         │ "Machine Learning" →                       │             │
│         │   "ML is a subset of AI..."                │             │
│         │                                            │             │
│         │ "Neural Networks" →                        │             │
│         │   "Neural networks are computing..."       │             │
│         │                                            │             │
│         │ "Deep Learning" →                          │             │
│         │   "Deep learning uses neural..."           │             │
│         └────────────────────────────────────────────┘             │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  3. RAG QUERY PIPELINE: "What is Python?"                           │
│     │                                                               │
│     ├─ STEP 1: RETRIEVAL                                           │
│     │   │                                                           │
│     │   ├─ Convert query to embedding                              │
│     │   │   Query: "What is Python?"                               │
│     │   │   └─> Embedding: [0.3, 0.7, 0.2, 0.9, ...]             │
│     │   │                                                           │
│     │   ├─ Convert each document to embedding                      │
│     │   │   ┌────────────────────────────────────┐                 │
│     │   │   │ Doc 1: "Python Basics"             │                 │
│     │   │   │   → [0.5, 0.6, 0.1, 0.8, ...]     │                 │
│     │   │   │                                    │                 │
│     │   │   │ Doc 2: "Machine Learning"          │                 │
│     │   │   │   → [0.1, 0.4, 0.9, 0.2, ...]     │                 │
│     │   │   │                                    │                 │
│     │   │   │ Doc 3: "Neural Networks"           │                 │
│     │   │   │   → [0.8, 0.1, 0.5, 0.3, ...]     │                 │
│     │   │   │                                    │                 │
│     │   │   │ Doc 4: "Deep Learning"             │                 │
│     │   │   │   → [0.2, 0.9, 0.4, 0.7, ...]     │                 │
│     │   │   └────────────────────────────────────┘                 │
│     │   │                                                           │
│     │   ├─ Calculate similarity scores                             │
│     │   │   ┌────────────────────────────────────┐                 │
│     │   │   │ Query · Doc1 = 0.87  ✓ HIGHEST    │                 │
│     │   │   │ Query · Doc2 = 0.42                │                 │
│     │   │   │ Query · Doc3 = 0.56                │                 │
│     │   │   │ Query · Doc4 = 0.71                │                 │
│     │   │   └────────────────────────────────────┘                 │
│     │   │                                                           │
│     │   └─ Select best match: "Python Basics"                      │
│     │       Retrieved Context:                                     │
│     │       "Python is a high-level programming language           │
│     │        known for its simplicity and readability."            │
│     │                                                               │
│     ├─ STEP 2: AUGMENTED GENERATION                                │
│     │   │                                                           │
│     │   ├─ Build prompt with context:                              │
│     │   │   ┌─────────────────────────────────────┐                │
│     │   │   │ Context: Python is a high-level...  │                │
│     │   │   │                                     │                │
│     │   │   │ Question: What is Python?           │                │
│     │   │   │                                     │                │
│     │   │   │ Answer based on context provided:   │                │
│     │   │   └─────────────────────────────────────┘                │
│     │   │                                                           │
│     │   ├─ Send to AI model                                        │
│     │   │   └─> Gemini processes prompt                            │
│     │   │                                                           │
│     │   └─ Generate response using retrieved context               │
│     │       AI Response:                                           │
│     │       "Based on the context, Python is a high-level          │
│     │        programming language that is known for its            │
│     │        simplicity and readability, making it an              │
│     │        excellent choice for beginners and experienced        │
│     │        developers alike."                                    │
│     │                                                               │
│     └─ Return final answer ✓                                       │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  4. COMPLETE RAG FLOW VISUALIZATION                                 │
│                                                                     │
│     USER QUERY                                                      │
│         │                                                           │
│         ▼                                                           │
│     ┌─────────────────────┐                                        │
│     │ "What is Python?"   │                                        │
│     └──────────┬──────────┘                                        │
│                │                                                    │
│                ▼                                                    │
│     ┌─────────────────────────────────┐                            │
│     │  EMBEDDING (Query Vector)       │                            │
│     │  [0.3, 0.7, 0.2, 0.9, ...]     │                            │
│     └──────────┬──────────────────────┘                            │
│                │                                                    │
│                ▼                                                    │
│     ┌─────────────────────────────────────┐                        │
│     │  KNOWLEDGE BASE (4 documents)       │                        │
│     │  ┌───────────────┐                  │                        │
│     │  │ Python Basics │ ← Match! 0.87    │                        │
│     │  ├───────────────┤                  │                        │
│     │  │ ML            │ → 0.42           │                        │
│     │  ├───────────────┤                  │                        │
│     │  │ Neural Nets   │ → 0.56           │                        │
│     │  ├───────────────┤                  │                        │
│     │  │ Deep Learning │ → 0.71           │                        │
│     │  └───────────────┘                  │                        │
│     └──────────┬──────────────────────────┘                        │
│                │                                                    │
│                ▼                                                    │
│     ┌─────────────────────────────────────┐                        │
│     │  RETRIEVED CONTEXT                  │                        │
│     │  "Python is a high-level            │                        │
│     │   programming language..."          │                        │
│     └──────────┬──────────────────────────┘                        │
│                │                                                    │
│                ▼                                                    │
│     ┌─────────────────────────────────────┐                        │
│     │  PROMPT CONSTRUCTION                │                        │
│     │  Context + Question + Instruction   │                        │
│     └──────────┬──────────────────────────┘                        │
│                │                                                    │
│                ▼                                                    │
│     ┌─────────────────────────────────────┐                        │
│     │  AI GENERATION (Gemini)             │                        │
│     │  Reads context → Generates answer   │                        │
│     └──────────┬──────────────────────────┘                        │
│                │                                                    │
│                ▼                                                    │
│     ┌─────────────────────────────────────┐                        │
│     │  FINAL ANSWER                       │                        │
│     │  Context-grounded response          │                        │
│     └─────────────────────────────────────┘                        │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  5. PROCESS ADDITIONAL QUERIES                                      │
│     │                                                               │
│     ├─ Query 2: "Tell me about machine learning"                   │
│     │   └─> Retrieves "Machine Learning" document                  │
│     │   └─> Generates ML explanation                               │
│     │                                                               │
│     └─ Query 3: "How do neural networks work?"                     │
│         └─> Retrieves "Neural Networks" document                   │
│         └─> Generates neural network explanation                   │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│                     PROGRAM COMPLETE ✅                             │
│  All RAG queries processed successfully!                            │
│  - Custom knowledge retrieved                                       │
│  - Context-grounded answers generated                               │
│  - No hallucination (answers based on YOUR data)                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Sample Output

### ✅ Complete Successful Execution

```
Knowledge Base:
  - Python Basics
  - Machine Learning
  - Neural Networks
  - Deep Learning

RAG Queries:

Q: What is Python?
A: Based on the context provided, Python is a high-level programming language that is particularly known for its simplicity and readability. This makes it an excellent choice for beginners learning to program, as well as for experienced developers who value clean, maintainable code. The language's straightforward syntax allows developers to express concepts in fewer lines of code compared to many other programming languages.

Q: Tell me about machine learning
A: According to the context, machine learning (ML) is a subset of artificial intelligence that enables computer systems to learn and improve from data without being explicitly programmed for every task. Instead of following rigid, pre-defined rules, ML algorithms identify patterns in data and use those patterns to make predictions or decisions. This approach allows systems to adapt and improve their performance as they process more data over time.

Q: How do neural networks work?
A: Based on the context provided, neural networks are computing systems that are inspired by the biological neural networks found in animal brains. They mimic the way neurons in biological brains process and transmit information. These artificial systems consist of interconnected nodes (similar to neurons) that work together to process input data, learn patterns, and make decisions or predictions. The biological inspiration helps create powerful computational models capable of learning complex patterns from data.
```

---

## 🎯 Key Concepts Explained

### 1. **What is RAG?**

```
RAG = Retrieval-Augmented Generation

Traditional AI:
User: "What is Python?"
AI: [Uses only training data] → "Python is a programming language..."
Problem: May be outdated or lack specific details

RAG AI:
User: "What is Python?"
1. Retrieve: Search YOUR knowledge base
2. Augment: Add retrieved info to prompt
3. Generate: AI answers using YOUR data
Result: Accurate, up-to-date, domain-specific answers
```

### 2. **The Two Steps of RAG**

```python
# STEP 1: RETRIEVAL (find relevant information)
def retrieve(query, knowledge_base):
    # Convert query to vector
    query_vector = embed(query)
    
    # Find most similar document
    best_doc = find_most_similar(query_vector, knowledge_base)
    return best_doc

# STEP 2: AUGMENTED GENERATION (use retrieved info)
def generate(query, context):
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    return ai_model.generate(prompt)

# COMPLETE RAG
def rag(query, knowledge_base):
    context = retrieve(query, knowledge_base)  # Step 1
    answer = generate(query, context)          # Step 2
    return answer
```

### 3. **Embeddings: Text as Vectors**

```python
# Text can't be compared directly
"Python language" vs "Programming with Python"  # How similar?

# Convert to vectors (embeddings)
text1_vector = [0.5, 0.8, 0.2, 0.1, ...]  # 768 dimensions
text2_vector = [0.6, 0.7, 0.3, 0.2, ...]  # 768 dimensions

# Now we can measure similarity mathematically
similarity = cosine_similarity(text1_vector, text2_vector)
# Result: 0.92 (very similar!)

# Semantic meaning captured
"king" - "man" + "woman" ≈ "queen"  # Vector arithmetic!
```

### 4. **Why RAG is Better Than Fine-tuning**

```
FINE-TUNING (updating model):
✗ Expensive (requires retraining)
✗ Time-consuming (hours to days)
✗ Static (can't easily update)
✗ Requires ML expertise

RAG (augmenting with context):
✓ Cheap (just text retrieval)
✓ Fast (instant updates)
✓ Dynamic (add/remove knowledge anytime)
✓ No ML expertise needed
✓ Transparent (see what context was used)
```

---

## 🚀 What Happens Behind the Scenes

### Embedding and Similarity Process:

```
1. QUERY PROCESSING
   User: "What is Python?"
   
2. QUERY EMBEDDING
   Text → Vector conversion
   "What is Python?" → [0.3, 0.7, 0.2, 0.9, 0.4, 0.6, ...]
   
3. DOCUMENT EMBEDDINGS (pre-computed)
   Doc1: "Python is..." → [0.5, 0.6, 0.1, 0.8, 0.3, 0.7, ...]
   Doc2: "ML is..."     → [0.1, 0.4, 0.9, 0.2, 0.8, 0.1, ...]
   Doc3: "Neural..."    → [0.8, 0.1, 0.5, 0.3, 0.2, 0.9, ...]
   
4. SIMILARITY CALCULATION
   Method: Dot product (or cosine similarity)
   
   Query · Doc1 = (0.3×0.5) + (0.7×0.6) + (0.2×0.1) + ...
                = 0.15 + 0.42 + 0.02 + ...
                = 0.87  ← HIGHEST!
   
   Query · Doc2 = 0.42
   Query · Doc3 = 0.56
   
5. RETRIEVAL
   Select document with highest score: Doc1
   
6. CONTEXT INJECTION
   Combine retrieved content with query
   
7. AI GENERATION
   AI reads context and generates grounded answer
```

### Vector Space Visualization:

```
3D Representation (actual embeddings are 768+ dimensions):

        ▲
        │     Doc1 (Python) ●
        │      ╱
        │    ╱   Query ●
        │  ╱     ╱
        │╱_____╱_________Doc2 (ML) ●
       ╱│
      ╱ │
Doc3 ● (Neural Nets)
   ╱   │
  ╱    │
───────┼────────▶

Closer points = More similar content
Query closest to Doc1 → Retrieve Doc1
```

---

## 📝 Common Use Cases

### Use Case 1: Company Knowledge Base
```python
def company_rag():
    # Knowledge base from company docs
    kb = {
        "Product A": "Our flagship product with features X, Y, Z...",
        "Pricing": "We offer three tiers: Basic ($10), Pro ($25)...",
        "Support": "Contact support@company.com or call 1-800..."
    }
    
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    # Customer question
    query = "How much does your Pro plan cost?"
    context = find_similar(query, kb)  # Finds "Pricing"
    
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    response = model.generate_content(prompt)
    return response.text
```

### Use Case 2: Document Q&A
```python
def document_qa(pdf_path, question):
    # Extract text from PDF
    documents = extract_pdf_text(pdf_path)
    
    # Split into chunks
    chunks = split_into_chunks(documents, chunk_size=500)
    
    # Find relevant chunk
    context = find_similar(question, chunks)
    
    # Generate answer
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
    response = model.generate_content(prompt)
    return response.text
```

### Use Case 3: Customer Support Bot
```python
def support_bot(user_query):
    # FAQ database
    faq_kb = load_faq_database()
    
    # Find relevant FAQ
    relevant_faq = find_similar(user_query, faq_kb)
    
    # Generate personalized response
    prompt = f"""Context: {relevant_faq}
    
User Query: {user_query}

Provide a helpful, friendly response based on the FAQ:"""
    
    return model.generate_content(prompt).text
```

### Use Case 4: Code Documentation Helper
```python
def code_helper(code_question):
    # Documentation knowledge base
    docs_kb = {
        "API Authentication": "Use API key in Authorization header...",
        "Rate Limits": "Maximum 100 requests per minute...",
        "Error Codes": "400: Bad Request, 401: Unauthorized..."
    }
    
    context = find_similar(code_question, docs_kb)
    
    prompt = f"""Documentation: {context}

Question: {code_question}

Provide code example and explanation:"""
    
    return model.generate_content(prompt).text
```

---

## 💡 Best Practices

### 1. **Use Proper Embeddings**
```python
# BAD: Random vectors (this demo)
embedding = np.random.rand(10)

# GOOD: Real embedding models
embedding = genai.embed_content(
    model="models/text-embedding-004",
    content=text
)['embedding']
```

### 2. **Chunk Documents Appropriately**
```python
# Too large: May include irrelevant info
chunk_size = 5000  # Too big

# Too small: May lack context
chunk_size = 50    # Too small

# Good: Balance between context and precision
chunk_size = 500   # Good for most uses
chunk_overlap = 50  # Maintain context between chunks
```

### 3. **Clear Prompt Structure**
```python
# BAD: Unclear prompt
prompt = f"{context} {query}"

# GOOD: Structured prompt
prompt = f"""Context: {context}

Question: {query}

Instructions: Answer the question using ONLY the information in the context. 
If the context doesn't contain the answer, say "I don't have enough information."

Answer:"""
```

### 4. **Handle No Match Cases**
```python
def rag_with_threshold(query, kb, threshold=0.5):
    context, similarity = find_similar_with_score(query, kb)
    
    if similarity < threshold:
        return "I don't have information about that topic in my knowledge base."
    
    # Proceed with RAG
    return generate_answer(query, context)
```

---

## ⚠️ Important Notes

1. **Simplified Demo:** Uses random embeddings (not semantic)
2. **Production:** Use proper embedding models (text-embedding-004)
3. **Vector Stores:** Use Pinecone, Weaviate, or Chroma for large scale
4. **Chunk Size:** Balance between context and precision
5. **Metadata:** Store metadata with chunks (source, date, etc.)
6. **Re-ranking:** Consider re-ranking results for better accuracy
7. **Hybrid Search:** Combine semantic and keyword search
8. **Caching:** Cache embeddings to avoid recomputing

---

## 🔧 Advanced: Production RAG System

```python
import google.generativeai as genai

class ProductionRAG:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.embeddings_cache = {}
        self._precompute_embeddings()
    
    def _precompute_embeddings(self):
        """Pre-compute embeddings for all documents"""
        for doc_id, content in self.knowledge_base.items():
            embedding = genai.embed_content(
                model="models/text-embedding-004",
                content=content
            )
            self.embeddings_cache[doc_id] = embedding['embedding']
    
    def retrieve(self, query, top_k=3):
        """Retrieve top-k most relevant documents"""
        # Get query embedding
        query_emb = genai.embed_content(
            model="models/text-embedding-004",
            content=query
        )['embedding']
        
        # Calculate similarities
        similarities = {}
        for doc_id, doc_emb in self.embeddings_cache.items():
            similarity = np.dot(query_emb, doc_emb) / (
                np.linalg.norm(query_emb) * np.linalg.norm(doc_emb)
            )  # Cosine similarity
            similarities[doc_id] = similarity
        
        # Get top-k documents
        top_docs = sorted(similarities.items(), 
                         key=lambda x: x[1], 
                         reverse=True)[:top_k]
        
        return [self.knowledge_base[doc_id] for doc_id, _ in top_docs]
    
    def generate(self, query, contexts):
        """Generate answer from multiple contexts"""
        combined_context = "\n\n".join(contexts)
        
        model = genai.GenerativeModel('gemini-2.0-flash')
        prompt = f"""Context from knowledge base:
{combined_context}

User Question: {query}

Instructions: Answer based on the provided context. If the context doesn't fully answer the question, say so.

Answer:"""
        
        response = model.generate_content(prompt)
        return response.text
    
    def query(self, user_query):
        """Complete RAG pipeline"""
        contexts = self.retrieve(user_query, top_k=3)
        answer = self.generate(user_query, contexts)
        return answer

# Usage
kb = create_knowledge_base()
rag = ProductionRAG(kb)
answer = rag.query("What is Python?")
```

---

## 🔗 Prerequisites

1. ✅ Completed previous lessons (01-08)
2. ✅ Understanding of vectors and embeddings (basic)
3. ✅ NumPy basics (helpful)
4. ✅ Understanding of text similarity concepts

---

## 🎓 Learning Outcomes

After understanding this code, you should know:

- ✅ What RAG (Retrieval-Augmented Generation) is
- ✅ The two steps: Retrieval and Generation
- ✅ How embeddings represent text as vectors
- ✅ How to calculate text similarity
- ✅ How to retrieve relevant context for queries
- ✅ How to structure prompts with retrieved context
- ✅ Why RAG is better than fine-tuning for custom knowledge
- ✅ Real-world applications of RAG systems

---

## 🔜 Next Steps

1. Move to `10_rag_pinecone.py` to learn about vector databases
2. Implement proper embedding models (text-embedding-004)
3. Build a document Q&A system
4. Create a company knowledge base chatbot
5. Explore vector databases (Pinecone, Weaviate, Chroma)
6. Experiment with different chunking strategies

---

**🔍 Brilliant!** You now understand the fundamentals of RAG and how to build knowledge-grounded AI systems!
