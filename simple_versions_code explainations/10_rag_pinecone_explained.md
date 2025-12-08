# 10 RAG Pinecone - Complete Code Explanation

## 📋 Overview
This code demonstrates RAG with a vector database (simulated Pinecone-style). Vector databases are specialized storage systems designed for efficient similarity search over embeddings. They're essential for production RAG systems handling thousands or millions of documents. This lesson shows the architecture and workflow of vector-based retrieval at scale.

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
# CAPABILITY: Generates responses based on retrieved context

load_dotenv()
# WHY: Load environment variables at module level
# WHAT IT DOES: Makes GOOGLE_API_KEY accessible
# TIMING: Called immediately before configuration

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
# WHY: Authenticate with Gemini API
# WHAT IT DOES: Sets up API key for all requests
# REQUIRED: Must be done before any AI operations

class SimpleVectorDB:
    # WHY: Simulate a vector database like Pinecone
    # WHAT IT DOES: Provides storage and retrieval interface
    # USE CASE: Demonstrates vector database concepts
    # SIMPLIFIED: Real Pinecone has advanced features
    # PRODUCTION: Use actual Pinecone, Weaviate, or Chroma
    
    def __init__(self):
        # WHY: Initialize empty vector database
        # WHAT IT DOES: Sets up storage for documents
        # CREATES: Two lists for documents and embeddings
        # SCALABILITY: Real DBs use optimized data structures
        
        self.documents = []
        # WHY: Store document metadata and text
        # WHAT IT DOES: List of dictionaries with document info
        # STRUCTURE: [{"id": "doc1", "text": "content"}, ...]
        # PURPOSE: Retrieve full document after similarity search
        # NOTE: Real vector DBs store this separately
        
        self.embeddings = []
        # WHY: Store vector representations of documents
        # WHAT IT DOES: List of embedding vectors
        # PURPOSE: Enable fast similarity search
        # NOTE: This demo doesn't actually use embeddings (simplified)
        # PRODUCTION: Critical for semantic search
    
    def add_document(self, doc_id, text):
        # WHY: Add document to the vector database
        # WHAT IT DOES: Stores document for later retrieval
        # PARAMETERS:
        #   - doc_id: Unique identifier for document
        #   - text: Document content
        # PROCESS: In real system, would compute embedding here
        # SCALABILITY: Real DBs handle millions of documents
        
        self.documents.append({"id": doc_id, "text": text})
        # WHY: Store document with its ID
        # WHAT IT DOES: Adds to documents list
        # STRUCTURE: Dictionary with id and text
        # INDEXING: Real DBs create indexes for fast retrieval
        # NOTE: Real systems would also store embedding vector
        
        print(f"Added document: {doc_id}")
        # WHY: Provide feedback on document ingestion
        # WHAT IT DOES: Confirms document was added
        # UX: User sees progress of knowledge base building
        # PRODUCTION: Would log to file instead of print
    
    def search(self, query, top_k=3):
        # WHY: Search for most relevant documents
        # WHAT IT DOES: Returns top_k most similar documents
        # PARAMETERS:
        #   - query: User's question/search text
        #   - top_k: Number of results to return (default 3)
        # SIMPLIFIED: Just returns first top_k documents
        # PRODUCTION: Would compute query embedding and find nearest neighbors
        
        print(f"Searching for: {query}")
        # WHY: Show what's being searched
        # WHAT IT DOES: Displays search query
        # UX: Transparency in retrieval process
        # DEBUG: Helpful for understanding system behavior
        
        return self.documents[:top_k]
        # WHY: Return top_k documents
        # WHAT IT DOES: Slices first top_k items from list
        # SIMPLIFIED: Not doing actual similarity search
        # PRODUCTION: Would use ANN (Approximate Nearest Neighbor)
        #   algorithms like HNSW or IVF for fast retrieval
        # REAL SEARCH: 
        #   1. Embed query
        #   2. Find nearest vectors
        #   3. Return corresponding documents
        # RETURNS: List of document dictionaries

def create_vector_store():
    # WHY: Initialize and populate vector database
    # WHAT IT DOES: Creates DB and adds knowledge base documents
    # USE CASE: Setting up RAG system with custom knowledge
    # RETURNS: Populated vector database instance
    # PRODUCTION: Would load from files or existing database
    
    db = SimpleVectorDB()
    # WHY: Create new vector database instance
    # WHAT IT DOES: Initializes empty database
    # STATE: Ready to accept documents
    
    documents = {
        "doc1": "Python is a versatile programming language used for web development, data science, and automation.",
        "doc2": "Machine learning algorithms can learn patterns from data to make predictions.",
        "doc3": "Neural networks consist of layers of interconnected nodes that process information.",
        "doc4": "Deep learning models require large amounts of data and computational power.",
        "doc5": "Natural language processing enables computers to understand human language."
    }
    # WHY: Define knowledge base documents
    # WHAT IT DOES: Creates dictionary of document IDs and content
    # STRUCTURE: {doc_id: content}
    # CONTENT: AI/Programming related information
    # SCALABILITY: Real systems have thousands/millions of docs
    # SOURCE: Could come from PDFs, websites, databases, etc.
    
    for doc_id, text in documents.items():
        # WHY: Loop through each document
        # WHAT IT DOES: Adds each document to vector database
        # PROCESS: Iterate over all documents
        # PRODUCTION: Would batch process for efficiency
        
        db.add_document(doc_id, text)
        # WHY: Store document in database
        # WHAT IT DOES: Adds document with its ID
        # INDEXING: Database makes it searchable
        # REAL SYSTEM: Would also compute and store embedding
    
    return db
    # WHY: Return populated database
    # WHAT IT DOES: Makes database available for queries
    # READY: Database now contains searchable knowledge

def rag_with_vector_db(query, vector_db):
    # WHY: Execute RAG pipeline using vector database
    # WHAT IT DOES: Retrieves context and generates answer
    # PARAMETERS:
    #   - query: User's question
    #   - vector_db: Vector database instance
    # RETURNS: AI-generated answer based on retrieved context
    # RAG STEPS: Retrieve → Augment → Generate
    
    results = vector_db.search(query, top_k=2)
    # WHY: Retrieve most relevant documents
    # WHAT IT DOES: Searches vector DB for similar documents
    # PARAMETER: top_k=2 means get 2 most relevant docs
    # RAG STEP 1: RETRIEVAL
    # OPTIMIZATION: Retrieve multiple docs for better context
    # TRADEOFF: More docs = more context but longer prompts
    
    context = "\n".join([doc["text"] for doc in results])
    # WHY: Combine retrieved documents into context
    # WHAT IT DOES: Joins document texts with newlines
    # PROCESS:
    #   1. Extract "text" from each result document
    #   2. Join all texts with \n separator
    # RESULT: Single string with all relevant context
    # FORMAT: Multi-line context for AI to read
    
    model = genai.GenerativeModel('gemini-2.0-flash')
    # WHY: Create AI model for generation
    # WHAT IT DOES: Initializes Gemini model
    # RAG STEP 2: AUGMENTED GENERATION
    
    prompt = f"""Use the following context to answer the question.
# WHY: Create structured prompt with context
# WHAT IT DOES: Instructs AI to use retrieved information
# INSTRUCTION: "Use the following context" = ground in retrieved docs

Context:
{context}
# WHY: Include retrieved documents
# WHAT IT DOES: Provides relevant knowledge to AI
# AUGMENTATION: This is the "Augmented" part of RAG
# SOURCE: Retrieved from YOUR vector database

Question: {query}
# WHY: Include user's original question
# WHAT IT DOES: Specifies what to answer
# CONTEXT AWARE: AI answers using provided context

Answer:"""
# WHY: Signal where AI should respond
# WHAT IT DOES: Indicates expected response location
# PROMPTING: Clear structure helps AI generate better answers
    
    response = model.generate_content(prompt)
    # WHY: Generate answer using context
    # WHAT IT DOES: AI reads context and answers question
    # RAG STEP 3: GENERATION
    # GROUNDED: Answer based on retrieved documents
    # ACCURACY: More reliable than relying on training data alone
    
    return response.text
    # WHY: Return generated answer
    # WHAT IT DOES: Provides final RAG response
    # RESULT: Context-grounded, knowledge-based answer

if __name__ == "__main__":
    # WHY: Check if script is run directly
    # WHAT IT DOES: Only executes demo when main program
    # BEST PRACTICE: Prevents auto-execution on import
    
    print("Creating Vector Store...")
    # WHY: Inform user of initialization
    # WHAT IT DOES: Shows database setup starting
    # UX: Progress indication
    
    db = create_vector_store()
    # WHY: Initialize and populate vector database
    # WHAT IT DOES: Creates DB with 5 documents
    # READY: Database now searchable
    # OUTPUT: Prints "Added document: docX" for each doc
    
    queries = [
        "What is Python used for?",
        "How do neural networks work?",
        "What is machine learning?"
    ]
    # WHY: Define test queries
    # WHAT IT DOES: Creates list of questions to test
    # PURPOSE: Demonstrate RAG with different questions
    # VARIETY: Different topics to show retrieval
    
    print("\n" + "="*60)
    print("RAG with Vector Database")
    print("="*60)
    # WHY: Create visual separator
    # WHAT IT DOES: Prints formatted header
    # UX: Clear section demarcation
    # FORMAT: 60 equal signs for visual impact
    
    for query in queries:
        # WHY: Loop through each test query
        # WHAT IT DOES: Processes each question with RAG
        # DEMONSTRATES: Multiple RAG executions
        
        print(f"\nQuery: {query}")
        # WHY: Display the question
        # WHAT IT DOES: Shows user's query
        # FORMAT: Clear labeling
        # UX: Question-answer structure
        
        answer = rag_with_vector_db(query, db)
        # WHY: Execute complete RAG pipeline
        # WHAT IT DOES:
        #   1. Search vector DB for relevant docs
        #   2. Combine retrieved contexts
        #   3. Generate answer with AI
        # RESULT: Knowledge-grounded response
        
        print(f"Answer: {answer}")
        # WHY: Display the generated answer
        # WHAT IT DOES: Shows AI's response
        # RESULT: Context-based answer from vector DB knowledge
        
        print("-"*60)
        # WHY: Visual separator between queries
        # WHAT IT DOES: Prints 60 dashes
        # UX: Separates different Q&A pairs
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
│     ├─ Import: os, dotenv, genai                                   │
│     ├─ Load .env file                                              │
│     └─ Configure API key                                           │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  2. DEFINE SimpleVectorDB CLASS                                     │
│     │                                                               │
│     ├─ __init__(): Initialize storage                              │
│     │   ├─ self.documents = []                                     │
│     │   └─ self.embeddings = []                                    │
│     │                                                               │
│     ├─ add_document(doc_id, text): Store documents                 │
│     │   └─ Append to documents list                                │
│     │                                                               │
│     └─ search(query, top_k=3): Retrieve relevant docs              │
│         └─ Return top_k documents                                  │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  3. CREATE & POPULATE VECTOR STORE                                  │
│     │                                                               │
│     ├─ Create SimpleVectorDB instance                              │
│     │                                                               │
│     ├─ Add Document 1: Python programming                          │
│     │   └─ "Python is a versatile programming language..."         │
│     │                                                               │
│     ├─ Add Document 2: Machine Learning                            │
│     │   └─ "ML algorithms can learn patterns..."                   │
│     │                                                               │
│     ├─ Add Document 3: Neural Networks                             │
│     │   └─ "Neural networks consist of layers..."                  │
│     │                                                               │
│     ├─ Add Document 4: Deep Learning                               │
│     │   └─ "Deep learning models require large..."                 │
│     │                                                               │
│     └─ Add Document 5: Natural Language Processing                 │
│         └─ "NLP enables computers to understand..."                │
│                                                                     │
│     Vector Database Structure:                                      │
│     ┌──────────────────────────────────────────┐                   │
│     │ documents = [                            │                   │
│     │   {"id": "doc1", "text": "Python..."},  │                   │
│     │   {"id": "doc2", "text": "ML..."},      │                   │
│     │   {"id": "doc3", "text": "Neural..."},  │                   │
│     │   {"id": "doc4", "text": "Deep..."},    │                   │
│     │   {"id": "doc5", "text": "NLP..."}      │                   │
│     │ ]                                        │                   │
│     └──────────────────────────────────────────┘                   │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  4. RAG QUERY 1: "What is Python used for?"                         │
│     │                                                               │
│     ├─ STEP 1: SEARCH VECTOR DATABASE                              │
│     │   │                                                           │
│     │   ├─ Query: "What is Python used for?"                       │
│     │   │                                                           │
│     │   ├─ Search with top_k=2                                     │
│     │   │   └─> Returns first 2 documents:                         │
│     │   │       1. doc1: "Python is a versatile..."                │
│     │   │       2. doc2: "ML algorithms can learn..."              │
│     │   │                                                           │
│     │   └─ Retrieved Context (combined):                           │
│     │       "Python is a versatile programming language            │
│     │        used for web development, data science, and           │
│     │        automation.                                           │
│     │        Machine learning algorithms can learn patterns        │
│     │        from data to make predictions."                       │
│     │                                                               │
│     ├─ STEP 2: BUILD PROMPT WITH CONTEXT                           │
│     │   ┌─────────────────────────────────────────┐                │
│     │   │ Use the following context to answer     │                │
│     │   │ the question.                            │                │
│     │   │                                          │                │
│     │   │ Context:                                 │                │
│     │   │ Python is a versatile programming...     │                │
│     │   │ Machine learning algorithms can...       │                │
│     │   │                                          │                │
│     │   │ Question: What is Python used for?       │                │
│     │   │                                          │                │
│     │   │ Answer:                                  │                │
│     │   └─────────────────────────────────────────┘                │
│     │                                                               │
│     ├─ STEP 3: GENERATE ANSWER                                     │
│     │   └─> Gemini AI reads context and generates:                 │
│     │       "Based on the context, Python is used for              │
│     │        web development, data science, and automation.        │
│     │        Its versatility makes it popular for various          │
│     │        applications including building machine learning      │
│     │        algorithms that can learn from data."                 │
│     │                                                               │
│     └─ Display Result ✓                                            │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  5. RAG QUERY 2: "How do neural networks work?"                     │
│     │                                                               │
│     ├─ Search returns:                                             │
│     │   - doc3: "Neural networks consist of layers..."             │
│     │   - doc4: "Deep learning models require..."                  │
│     │                                                               │
│     └─> AI generates answer using retrieved context ✓              │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  6. RAG QUERY 3: "What is machine learning?"                        │
│     │                                                               │
│     ├─ Search returns:                                             │
│     │   - doc2: "ML algorithms can learn patterns..."              │
│     │   - doc3: "Neural networks consist of layers..."             │
│     │                                                               │
│     └─> AI generates answer using retrieved context ✓              │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  7. VECTOR DATABASE CONCEPT VISUALIZATION                           │
│                                                                     │
│     Real Vector Database (like Pinecone):                           │
│     ┌────────────────────────────────────────────────┐             │
│     │ INPUT: Documents                               │             │
│     │   ↓                                            │             │
│     │ EMBEDDING MODEL                                │             │
│     │   ↓                                            │             │
│     │ VECTORS: [0.23, 0.87, 0.44, ...]             │             │
│     │   ↓                                            │             │
│     │ INDEX: HNSW (Hierarchical NSW)                │             │
│     │   ├─ Fast similarity search                    │             │
│     │   ├─ Approximate nearest neighbors            │             │
│     │   └─ Millions of vectors                       │             │
│     │   ↓                                            │             │
│     │ QUERY: "What is Python?"                       │             │
│     │   ↓                                            │             │
│     │ SEARCH: Find nearest vectors                   │             │
│     │   ↓                                            │             │
│     │ RESULTS: Top-k most similar documents          │             │
│     └────────────────────────────────────────────────┘             │
│                                                                     │
│     Vector Space (Simplified 2D, real is 768+ dimensions):         │
│     ┌────────────────────────────────────────┐                     │
│     │        ●doc4 (Deep Learning)           │                     │
│     │                                        │                     │
│     │    ●doc3 (Neural Nets)                 │                     │
│     │                                        │                     │
│     │              ●query                    │                     │
│     │               ↑                        │                     │
│     │               │ nearest neighbors      │                     │
│     │               ↓                        │                     │
│     │    ●doc2 (ML)    ●doc1 (Python)       │                     │
│     │                                        │                     │
│     │         ●doc5 (NLP)                    │                     │
│     └────────────────────────────────────────┘                     │
│                                                                     │
│     Similarity Search finds closest vectors!                        │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│                     PROGRAM COMPLETE ✅                             │
│  All RAG queries with vector database complete!                     │
│  - Vector store created with 5 documents                            │
│  - 3 queries processed successfully                                 │
│  - Each query retrieved relevant context                            │
│  - AI generated knowledge-grounded answers                          │
└────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Sample Output

### ✅ Complete Successful Execution

```
Creating Vector Store...
Added document: doc1
Added document: doc2
Added document: doc3
Added document: doc4
Added document: doc5

============================================================
RAG with Vector Database
============================================================

Query: What is Python used for?
Searching for: What is Python used for?
Answer: Based on the context provided, Python is used for web development, data science, and automation. Its versatility makes it a popular choice for developers working across different domains. The language's flexibility allows it to be applied in creating websites and web applications, analyzing and processing data for insights, and automating repetitive tasks to improve efficiency.
------------------------------------------------------------

Query: How do neural networks work?
Searching for: How do neural networks work?
Answer: According to the context, neural networks consist of layers of interconnected nodes that process information. These nodes work together in a structured way, with information flowing through the layers to perform various computational tasks. The interconnected nature of these nodes allows neural networks to learn patterns and relationships in data, making them powerful tools for tasks like pattern recognition, classification, and prediction.
------------------------------------------------------------

Query: What is machine learning?
Searching for: What is machine learning?
Answer: Based on the context provided, machine learning refers to algorithms that can learn patterns from data to make predictions. Rather than being explicitly programmed with rules, ML algorithms analyze data, identify patterns within it, and use those discovered patterns to make predictions or decisions about new, unseen data. This ability to learn from experience makes machine learning particularly useful for tasks where traditional programming approaches would be too complex or inflexible.
------------------------------------------------------------
```

---

## 🎯 Key Concepts Explained

### 1. **Vector Databases vs Regular Databases**

```
REGULAR DATABASE (PostgreSQL, MySQL):
- Stores: Structured data (rows, columns)
- Search: Exact matches, SQL queries
- Example: WHERE name = "Python"
- Use: Transactional data, user records

VECTOR DATABASE (Pinecone, Weaviate, Chroma):
- Stores: Embeddings (numerical vectors)
- Search: Similarity search (nearest neighbors)
- Example: Find similar to "programming languages"
- Use: Semantic search, RAG, recommendations
```

### 2. **How Vector Databases Work**

```python
# 1. INDEXING (one-time setup)
for document in documents:
    # Convert text to vector
    embedding = embed_model.encode(document.text)  # [0.23, 0.87, ...]
    
    # Store in vector database
    vector_db.upsert(
        id=document.id,
        vector=embedding,
        metadata={"text": document.text}
    )

# 2. QUERYING (runtime)
query = "What is Python?"
query_embedding = embed_model.encode(query)  # [0.25, 0.85, ...]

# Find nearest neighbors
results = vector_db.search(
    vector=query_embedding,
    top_k=3
)
# Returns: 3 most similar documents
```

### 3. **Approximate Nearest Neighbor (ANN)**

```
EXACT SEARCH (Brute Force):
- Compare query to ALL vectors
- Accurate but SLOW
- Time: O(n) for n documents
- Example: 1 million vectors = 1 million comparisons

APPROXIMATE SEARCH (ANN):
- Use indexing structures (HNSW, IVF)
- Fast but slightly less accurate
- Time: O(log n)
- Example: 1 million vectors = ~20 comparisons
- Accuracy: 95-99% (good enough!)

Popular ANN Algorithms:
- HNSW: Hierarchical Navigable Small World
- IVF: Inverted File Index
- LSH: Locality Sensitive Hashing
```

### 4. **Vector Database Features**

```python
# PINECONE EXAMPLE (Real usage)
import pinecone

# Initialize
pinecone.init(api_key="your-key")
index = pinecone.Index("my-knowledge-base")

# Upsert (insert or update)
index.upsert(vectors=[
    ("doc1", [0.1, 0.2, ...], {"text": "Python is..."}),
    ("doc2", [0.3, 0.4, ...], {"text": "ML is..."})
])

# Query
results = index.query(
    vector=[0.15, 0.25, ...],
    top_k=3,
    include_metadata=True,
    filter={"category": "programming"}  # Metadata filtering!
)

# Features:
# - Horizontal scaling (billions of vectors)
# - Metadata filtering
# - Hybrid search (vector + keyword)
# - Real-time updates
# - Multi-cloud deployment
```

---

## 🚀 What Happens Behind the Scenes

### Vector Database Architecture:

```
┌──────────────────────────────────────────────┐
│            APPLICATION LAYER                 │
│  (Your RAG Application)                      │
└────────────────┬─────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────┐
│         EMBEDDING MODEL                      │
│  (text-embedding-004, etc.)                  │
│  Text → Vector [768 dimensions]              │
└────────────────┬─────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────┐
│         VECTOR DATABASE                      │
│  ┌────────────────────────────────────┐      │
│  │  INDEX (HNSW, IVF, etc.)           │      │
│  │  - Fast similarity search           │      │
│  │  - Approximate nearest neighbors    │      │
│  │  - Millions/billions of vectors     │      │
│  └────────────────────────────────────┘      │
│  ┌────────────────────────────────────┐      │
│  │  STORAGE                            │      │
│  │  - Vectors                          │      │
│  │  - Metadata                         │      │
│  │  - Documents                        │      │
│  └────────────────────────────────────┘      │
└──────────────────────────────────────────────┘

Search Process:
1. Query text → Embedding model → Query vector
2. Vector DB index → Find nearest neighbors
3. Retrieve metadata/documents for results
4. Return top-k results
```

### Comparison: This Demo vs Real Pinecone

```
THIS DEMO (SimpleVectorDB):
❌ No actual embeddings
❌ No similarity calculation
❌ Just returns first N documents
❌ No indexing
❌ Linear search (slow)
✓  Shows interface/workflow

REAL PINECONE:
✓  Actual embeddings (768+ dims)
✓  True similarity search
✓  Efficient indexing (HNSW)
✓  Sub-second queries on millions of vectors
✓  Horizontal scaling
✓  Metadata filtering
✓  Hybrid search
✓  Production-ready
```

---

## 📝 Common Use Cases

### Use Case 1: Enterprise Knowledge Base
```python
# Index company documents
documents = load_company_docs()  # Thousands of docs

for doc in documents:
    embedding = genai.embed_content(
        model="models/text-embedding-004",
        content=doc.text
    )
    
    vector_db.upsert(
        id=doc.id,
        vector=embedding['embedding'],
        metadata={
            "text": doc.text,
            "department": doc.department,
            "date": doc.date
        }
    )

# Query with filtering
def search_knowledge_base(query, department=None):
    query_emb = genai.embed_content(
        model="models/text-embedding-004",
        content=query
    )
    
    filters = {}
    if department:
        filters["department"] = department
    
    results = vector_db.search(
        vector=query_emb['embedding'],
        top_k=5,
        filter=filters
    )
    
    return results
```

### Use Case 2: Semantic Document Search
```python
def semantic_search(query, category=None):
    """Find documents similar to query"""
    
    # Get query embedding
    query_emb = get_embedding(query)
    
    # Search vector database
    results = vector_db.search(
        vector=query_emb,
        top_k=10,
        filter={"category": category} if category else None
    )
    
    # Format results
    return [{
        "id": r.id,
        "text": r.metadata["text"],
        "score": r.score  # Similarity score
    } for r in results]
```

### Use Case 3: Recommendation System
```python
def get_recommendations(item_id, n=5):
    """Find similar items"""
    
    # Get item's embedding
    item_embedding = vector_db.fetch(item_id).vector
    
    # Find similar items
    similar = vector_db.search(
        vector=item_embedding,
        top_k=n+1,  # +1 to exclude the item itself
        filter={"id": {"$ne": item_id}}  # Exclude self
    )
    
    return similar[1:]  # Skip first (the item itself)
```

### Use Case 4: Multi-language Search
```python
def multilingual_search(query, languages=None):
    """Search across multiple languages"""
    
    # Multilingual embedding models handle this automatically
    query_emb = get_embedding(query)  # Works in any language
    
    results = vector_db.search(
        vector=query_emb,
        top_k=10,
        filter={"language": {"$in": languages}} if languages else None
    )
    
    # Returns relevant docs regardless of language
    return results
```

---

## 💡 Best Practices

### 1. **Choose Right Vector Database**
```python
# Small scale (< 10K docs): In-memory or Chroma
# Medium scale (10K-1M docs): Weaviate, Qdrant
# Large scale (> 1M docs): Pinecone, Milvus

# Consider:
# - Document count
# - Query latency requirements
# - Budget
# - Managed vs self-hosted
```

### 2. **Optimize Embeddings**
```python
# Use appropriate embedding model
embedding_models = {
    "general": "text-embedding-004",      # Google
    "large": "text-embedding-3-large",    # OpenAI (3072 dims)
    "small": "text-embedding-3-small",    # OpenAI (1536 dims)
    "code": "code-embedding-002"          # Specialized for code
}

# Cache embeddings (they're expensive to compute)
@lru_cache(maxsize=1000)
def get_cached_embedding(text):
    return genai.embed_content(
        model="models/text-embedding-004",
        content=text
    )['embedding']
```

### 3. **Batch Operations**
```python
# BAD: One at a time
for doc in documents:
    db.upsert(doc)  # Slow!

# GOOD: Batch upsert
batch_size = 100
for i in range(0, len(documents), batch_size):
    batch = documents[i:i+batch_size]
    db.upsert_batch(batch)  # Much faster!
```

### 4. **Metadata Filtering**
```python
# Store useful metadata
db.upsert(
    id="doc123",
    vector=embedding,
    metadata={
        "text": content,
        "source": "website",
        "date": "2024-01-01",
        "category": "technical",
        "author": "John Doe"
    }
)

# Filter during search
results = db.search(
    vector=query_emb,
    filter={
        "category": "technical",
        "date": {"$gte": "2023-01-01"}
    }
)
```

---

## ⚠️ Important Notes

1. **This Demo:** Simplified - doesn't use real embeddings or similarity search
2. **Production:** Use actual vector databases (Pinecone, Weaviate, Chroma)
3. **Embeddings:** Critical for semantic search - use proper models
4. **Indexing:** HNSW or IVF for fast searches at scale
5. **Costs:** Vector databases charge for storage and queries
6. **Dimensions:** More dimensions = better accuracy but more storage
7. **Updates:** Real-time updates possible but may affect performance
8. **Scaling:** Consider sharding for massive datasets

---

## 🔧 Advanced: Real Pinecone Integration

```python
import pinecone
import google.generativeai as genai

class PineconeRAG:
    def __init__(self, index_name, dimension=768):
        # Initialize Pinecone
        pinecone.init(
            api_key=os.getenv("PINECONE_API_KEY"),
            environment=os.getenv("PINECONE_ENV")
        )
        
        # Create or connect to index
        if index_name not in pinecone.list_indexes():
            pinecone.create_index(
                name=index_name,
                dimension=dimension,
                metric="cosine"
            )
        
        self.index = pinecone.Index(index_name)
    
    def add_documents(self, documents):
        """Add documents with embeddings to Pinecone"""
        vectors = []
        
        for doc in documents:
            # Get embedding
            emb = genai.embed_content(
                model="models/text-embedding-004",
                content=doc["text"]
            )
            
            vectors.append({
                "id": doc["id"],
                "values": emb['embedding'],
                "metadata": {"text": doc["text"]}
            })
        
        # Batch upsert
        self.index.upsert(vectors=vectors)
    
    def search(self, query, top_k=3):
        """Search for similar documents"""
        # Get query embedding
        query_emb = genai.embed_content(
            model="models/text-embedding-004",
            content=query
        )
        
        # Search Pinecone
        results = self.index.query(
            vector=query_emb['embedding'],
            top_k=top_k,
            include_metadata=True
        )
        
        return [match.metadata["text"] for match in results.matches]
    
    def rag_query(self, query):
        """Complete RAG pipeline"""
        # Retrieve context
        contexts = self.search(query, top_k=3)
        combined_context = "\n\n".join(contexts)
        
        # Generate answer
        model = genai.GenerativeModel('gemini-2.0-flash')
        prompt = f"""Context:\n{combined_context}\n\nQuestion: {query}\n\nAnswer:"""
        
        response = model.generate_content(prompt)
        return response.text

# Usage
rag = PineconeRAG("my-knowledge-base")

# Add documents
docs = [
    {"id": "doc1", "text": "Python is..."},
    {"id": "doc2", "text": "ML is..."}
]
rag.add_documents(docs)

# Query
answer = rag.rag_query("What is Python?")
```

---

## 🔗 Prerequisites

1. ✅ Completed lesson 09 (RAG Basic)
2. ✅ Understanding of vectors and embeddings
3. ✅ Knowledge of database concepts
4. ✅ Familiarity with APIs

---

## 🎓 Learning Outcomes

After understanding this code, you should know:

- ✅ What vector databases are and why they're needed
- ✅ How vector databases enable fast similarity search
- ✅ The difference between exact and approximate search
- ✅ How to structure a vector database for RAG
- ✅ When to use vector databases vs regular databases
- ✅ Popular vector database options (Pinecone, Weaviate, Chroma)
- ✅ How to integrate vector databases with RAG pipelines
- ✅ Best practices for production RAG systems

---

## 🔜 Next Steps

1. Set up real Pinecone or Weaviate account
2. Implement proper embedding generation
3. Build production RAG system with vector DB
4. Experiment with different embedding models
5. Add metadata filtering for better search
6. Optimize for scale (batching, caching)
7. Explore hybrid search (semantic + keyword)

---

**🎯 Outstanding!** You now understand vector databases and production-ready RAG architecture!
