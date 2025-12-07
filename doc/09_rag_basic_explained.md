# Module 09 - RAG (Retrieval-Augmented Generation) - Basic - Detailed Code Explanation

This document explains every line of code in the RAG Basic module, with in-depth explanations of how to build intelligent search and question-answering systems.

---

## 📊 Visual Overview: RAG Architecture

```
┌───────────────────────────────────────────────────────────────────┐
│              RAG = AI + YOUR DOCUMENTS = SMART ANSWERS            │
└───────────────────────────────────────────────────────────────────┘

THE PROBLEM RAG SOLVES:
───────────────────────

WITHOUT RAG:
User: "What's in our Q3 report?"
  ↓
┌─────────────────────────────┐
│ AI Model                    │
│ (Only knows training data)  │  → "I don't have access
└─────────────────────────────┘     to your Q3 report"
                                    ❌ Can't help


WITH RAG:
User: "What's in our Q3 report?"
  ↓
┌──────────────────────────────────────┐
│ 1. SEARCH your documents             │ → Find Q3 report
│ 2. RETRIEVE relevant sections        │ → Get key info
│ 3. INJECT into AI prompt             │ → Add context
│ 4. GENERATE answer                   │ → "Q3 revenue
└──────────────────────────────────────┘    was $5M..."
                                           ✅ Accurate!


FULL RAG PIPELINE:
──────────────────

┌─────────────────────────────────────────────────────────────────┐
│                        RAG SYSTEM FLOW                          │
└─────────────────────────────────────────────────────────────────┘

PHASE 1: INDEXING (One-time setup)
───────────────────────────────────

Your Documents:
┌──────────────────────────────────┐
│ • company_docs.pdf               │
│ • product_specs.docx             │
│ • q3_report.txt                  │
└─────────────┬────────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│  STEP 1: Load & Chunk           │
│  ─────────────────              │
│  Break into small pieces:       │
│                                 │
│  "Q3 revenue was $5M..."  ────► Chunk 1
│  "Customer count: 1,200"  ────► Chunk 2
│  "New product launch..."  ────► Chunk 3
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│  STEP 2: Create Embeddings      │
│  ──────────────────             │
│  Convert text → numbers:        │
│                                 │
│  Chunk 1 → [0.23, 0.87, ...]   │
│  Chunk 2 → [0.45, 0.12, ...]   │
│  Chunk 3 → [0.91, 0.33, ...]   │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│  STEP 3: Store in Database      │
│  ──────────────────             │
│  (Vector Store)                 │
│                                 │
│  Chunk 1 + Embedding 1          │
│  Chunk 2 + Embedding 2          │
│  Chunk 3 + Embedding 3          │
└─────────────────────────────────┘
              │
              ▼
        ✅ Ready for queries!


PHASE 2: QUERYING (Every user question)
────────────────────────────────────────

User Question:
"What was Q3 revenue?"
        │
        ▼
┌─────────────────────────────────┐
│  STEP 4: Embed Question         │
│  ───────────────                │
│  "What was Q3 revenue?"         │
│       ↓                         │
│  [0.25, 0.89, 0.44, ...]        │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│  STEP 5: Similarity Search      │
│  ──────────────────             │
│  Compare question embedding     │
│  to all chunk embeddings        │
│                                 │
│  Question: [0.25, 0.89, ...]    │
│     vs                          │
│  Chunk 1:  [0.23, 0.87, ...]  ✅ 95% similar
│  Chunk 2:  [0.45, 0.12, ...]    78% similar
│  Chunk 3:  [0.91, 0.33, ...]    42% similar
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│  STEP 6: Retrieve Top Chunks    │
│  ────────────────────           │
│  Get most relevant:             │
│                                 │
│  ✅ Chunk 1: "Q3 revenue $5M"   │
│  ✅ Chunk 2: "Customer: 1,200"  │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│  STEP 7: Build Enhanced Prompt  │
│  ──────────────────────         │
│                                 │
│  Context: "Q3 revenue was $5M.  │
│            Customer count 1,200"│
│                                 │
│  Question: "What was Q3 revenue?"│
│                                 │
│  Instruction: "Answer using     │
│  only the context provided"     │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│  STEP 8: AI Generation          │
│  ──────────────                 │
│  AI reads context + answers:    │
│                                 │
│  "Based on the Q3 report,       │
│   revenue was $5M with 1,200    │
│   customers."                   │
└─────────────────────────────────┘
              │
              ▼
        📝 Answer delivered!
```

---

## 🔍 What Are Embeddings?

```
EMBEDDINGS = MEANING AS NUMBERS
────────────────────────────────

Text cannot be compared mathematically.
Numbers can be compared mathematically.
→ Convert text to numbers = embeddings!


CONCEPTUAL EXAMPLE:
───────────────────

Words:         Embeddings (simplified):
"cat"    →     [0.9, 0.1, 0.3]  ← High "animal" score
"dog"    →     [0.8, 0.2, 0.4]  ← High "animal" score
"car"    →     [0.1, 0.9, 0.7]  ← High "vehicle" score
"truck"  →     [0.2, 0.8, 0.6]  ← High "vehicle" score

Similarity:
"cat" vs "dog"   → Very similar embeddings ✅
"cat" vs "car"   → Different embeddings ❌


REAL EMBEDDINGS:
────────────────

Actual embeddings are MUCH longer vectors:
- Google's embedding model: 768 dimensions
- OpenAI ada-002: 1536 dimensions

Example (simplified):
"Python programming" → 
[0.234, -0.891, 0.456, 0.123, -0.567, 0.789, ...]
  ↑      ↑       ↑      ↑       ↑       ↑
768 numbers total (we show 6)


SEMANTIC SIMILARITY:
────────────────────

Similar meaning = Similar numbers:

"Python coding"        [0.23, 0.45, 0.67, ...]
"Python programming"   [0.25, 0.43, 0.69, ...]
                       ↑ Very close numbers!

"Pizza recipe"         [0.91, -0.34, 0.12, ...]
"Python programming"   [0.25, 0.43, 0.69, ...]
                       ↑ Different numbers


DISTANCE CALCULATION:
─────────────────────

Cosine Similarity (most common):

Text A: [0.5, 0.8, 0.3]
Text B: [0.6, 0.7, 0.4]
         ↓
Similarity Score: 0.95 (95% similar)

Text A: [0.5, 0.8, 0.3]
Text C: [0.1, 0.2, 0.9]
         ↓
Similarity Score: 0.42 (42% similar)


VISUAL REPRESENTATION:
──────────────────────

Imagine 2D space (real embeddings are 768D):

        High "Animal"
              ↑
              │
     🐱 cat   │   🐕 dog
              │
              │
─────────────────────────────► High "Technology"
              │
              │
     🚗 car   │   🚚 truck
              │
              ↓

Words with similar meanings cluster together!
```

---

## 📦 Document Chunking Strategies

```
WHY CHUNK DOCUMENTS?
────────────────────

Problem: Documents are too large
- Entire book = too much context
- Single paragraph = too little context
- Need: Just-right sized pieces ✅

Solution: Split into chunks!


CHUNKING STRATEGY COMPARISON:
──────────────────────────────

1. FIXED SIZE (Simple)
   ───────────────────
   Split every N characters/words
   
   Example: 500 characters per chunk
   
   Document: "The quick brown fox jumps over..."
            ↓
   Chunk 1: "The quick brown fox jumps over..." (500 chars)
   Chunk 2: "...the lazy dog. The fox was very..." (500 chars)
   
   ✅ Simple, predictable
   ❌ May cut mid-sentence
   ❌ No semantic awareness


2. SENTENCE-BASED (Better)
   ────────────────────────
   Keep complete sentences together
   
   Example: 3-5 sentences per chunk
   
   Document: "Python is great. It's easy to learn.
              It has many libraries. It's very popular."
            ↓
   Chunk 1: "Python is great. It's easy to learn.
             It has many libraries."
   Chunk 2: "It's very popular. [next sentences...]"
   
   ✅ Natural boundaries
   ✅ Complete thoughts
   ❌ Variable chunk sizes


3. PARAGRAPH-BASED (Good)
   ───────────────────────
   One chunk = one paragraph
   
   Document:
   "Paragraph 1: Introduction...
   
    Paragraph 2: Main content...
    
    Paragraph 3: Conclusion..."
            ↓
   Chunk 1: "Paragraph 1: Introduction..."
   Chunk 2: "Paragraph 2: Main content..."
   Chunk 3: "Paragraph 3: Conclusion..."
   
   ✅ Semantic coherence
   ✅ Natural structure
   ❌ Inconsistent sizes


4. OVERLAP STRATEGY (Best)
   ────────────────────────
   Chunks share some content
   
   Chunk size: 500 chars
   Overlap: 100 chars
   
   Document: "ABCDEFGHIJ..."
            ↓
   Chunk 1: "ABCDE"
   Chunk 2:     "DEFGH"  ← "DE" overlaps
   Chunk 3:         "GHIJK"  ← "GH" overlaps
   
   ✅ Captures context across boundaries
   ✅ No missed information
   ❌ More storage needed


RECOMMENDED APPROACH:
─────────────────────

For general RAG:
┌─────────────────────────────┐
│ • Chunk size: 500-1000 chars│
│ • Overlap: 100-200 chars    │
│ • Method: Sentence-aware    │
└─────────────────────────────┘


CHUNKING EXAMPLE:
─────────────────

Original Document (1,500 chars):
┌──────────────────────────────────────────┐
│ Python is a high-level programming       │
│ language. It was created by Guido van    │
│ Rossum in 1991. Python emphasizes code   │
│ readability with significant whitespace. │
│                                          │
│ Python supports multiple programming     │
│ paradigms including OOP and functional.  │
│ It has a comprehensive standard library. │
│                                          │
│ Python is widely used in web development,│
│ data science, and machine learning.      │
└──────────────────────────────────────────┘

After Chunking (500 chars, 100 overlap):
┌──────────────────────────────────────────┐
│ Chunk 1 (500 chars):                     │
│ "Python is a high-level programming      │
│  language. It was created by Guido van   │
│  Rossum in 1991. Python emphasizes..."   │
├──────────────────────────────────────────┤
│ Chunk 2 (500 chars, overlaps 100):      │
│ "...emphasizes code readability with     │
│  significant whitespace. Python supports │
│  multiple programming paradigms..."      │
├──────────────────────────────────────────┤
│ Chunk 3 (500 chars, overlaps 100):      │
│ "...paradigms including OOP and          │
│  functional. It has comprehensive        │
│  standard library. Python is widely..."  │
└──────────────────────────────────────────┘
```

---

## 🏗️ Code Structure Map

```
09_rag_basic.py
│
├── 📦 IMPORTS
│   ├── os, dotenv
│   ├── google.generativeai
│   └── numpy (for similarity calculations)
│
├── 🔧 SETUP
│   ├── load_dotenv()
│   ├── genai.configure()
│   └── Initialize models
│
├── 🎯 FUNCTION 1: create_embeddings()
│   ├── Input: text or list of texts
│   ├── Call: genai.embed_content()
│   └── Output: embedding vectors
│
├── 🎯 FUNCTION 2: chunk_text()
│   ├── Split text into chunks
│   ├── Apply overlap strategy
│   └── Return: list of chunks
│
├── 🎯 FUNCTION 3: cosine_similarity()
│   ├── Calculate vector similarity
│   ├── Formula: dot(A,B) / (norm(A)*norm(B))
│   └── Return: similarity score (0-1)
│
├── 🎯 FUNCTION 4: find_relevant_chunks()
│   ├── Embed query
│   ├── Compare with all chunks
│   ├── Sort by similarity
│   └── Return: top N chunks
│
├── 🎯 FUNCTION 5: build_rag_prompt()
│   ├── Format: Context + Question
│   ├── Add instructions
│   └── Return: complete prompt
│
├── 🎯 FUNCTION 6: rag_query()
│   ├── Find relevant chunks
│   ├── Build prompt
│   ├── Call AI model
│   └── Return: answer
│
├── 🎯 FUNCTION 7: create_knowledge_base()
│   ├── Load documents
│   ├── Chunk all docs
│   ├── Create embeddings
│   └── Store: chunks + embeddings
│
└── 🚀 MAIN DEMO
    ├── Create sample documents
    ├── Build knowledge base
    ├── Run example queries
    └── Display results
```

---

## 🔄 RAG vs Regular AI

```
COMPARISON:
───────────

Question: "What did the CEO say in the meeting?"

REGULAR AI (No RAG):
────────────────────
User: "What did the CEO say?"
  ↓
┌─────────────────────────┐
│ AI Model                │
│ (No access to meeting)  │  → "I don't have information
└─────────────────────────┘     about that meeting."
                                ❌ Cannot answer


RAG AI (With Documents):
────────────────────────
User: "What did the CEO say?"
  ↓
┌──────────────────────────────────────┐
│ 1. Search meeting transcripts        │
│ 2. Find: "CEO mentioned Q4 goals..."│
│ 3. Add to AI prompt                  │
│ 4. Generate answer                   │
└──────────────────────────────────────┘
  ↓
"The CEO outlined three Q4 goals:
 1. Increase revenue by 20%
 2. Launch new product line
 3. Expand to European market"
✅ Accurate, grounded answer


BENEFITS OF RAG:
────────────────

✅ Access to YOUR specific documents
✅ Overcomes knowledge cutoff dates
✅ Reduces hallucinations (AI making up facts)
✅ Answers grounded in real data
✅ Can cite sources
✅ Easily updatable (add new docs)


WITHOUT RAG:
───────────

AI Knowledge = Training Data Only
┌─────────────────────────────────┐
│ ✅ General knowledge (Wikipedia) │
│ ✅ Common facts                  │
│ ❌ Your company docs             │
│ ❌ Recent events (after cutoff)  │
│ ❌ Private information           │
└─────────────────────────────────┘


WITH RAG:
─────────

AI Knowledge = Training Data + YOUR Docs
┌─────────────────────────────────┐
│ ✅ General knowledge             │
│ ✅ Common facts                  │
│ ✅ Your company docs         NEW!│
│ ✅ Recent events (in docs)   NEW!│
│ ✅ Private information       NEW!│
└─────────────────────────────────┘
```

---

## 📊 Similarity Search Visualization

```
FINDING RELEVANT CHUNKS:
────────────────────────

Knowledge Base (5 chunks):
┌─────────────────────────────────────────────┐
│ Chunk 1: "Python is a programming language" │
│ Embedding: [0.2, 0.8, 0.3, ...]            │
├─────────────────────────────────────────────┤
│ Chunk 2: "Dogs are loyal pets"             │
│ Embedding: [0.7, 0.2, 0.9, ...]            │
├─────────────────────────────────────────────┤
│ Chunk 3: "Machine learning uses Python"    │
│ Embedding: [0.3, 0.7, 0.4, ...]            │
├─────────────────────────────────────────────┤
│ Chunk 4: "Pizza recipe with cheese"        │
│ Embedding: [0.9, 0.1, 0.2, ...]            │
├─────────────────────────────────────────────┤
│ Chunk 5: "Python libraries for AI"         │
│ Embedding: [0.2, 0.7, 0.5, ...]            │
└─────────────────────────────────────────────┘

User Query: "How to use Python for AI?"
Query Embedding: [0.25, 0.75, 0.45, ...]

Similarity Calculation:
┌──────────────────────────────────────────────┐
│ Query vs Chunk 1: 0.78  (78% similar)   ⭐   │
│ Query vs Chunk 2: 0.32  (32% similar)       │
│ Query vs Chunk 3: 0.92  (92% similar)   ⭐⭐⭐│
│ Query vs Chunk 4: 0.15  (15% similar)       │
│ Query vs Chunk 5: 0.89  (89% similar)   ⭐⭐ │
└──────────────────────────────────────────────┘

Top 3 Retrieved:
1. Chunk 3: "Machine learning uses Python" (92%)
2. Chunk 5: "Python libraries for AI" (89%)
3. Chunk 1: "Python is a programming..." (78%)

These become the CONTEXT for the AI!


SIMILARITY FORMULA:
───────────────────

Cosine Similarity:

Vector A = [a₁, a₂, a₃]
Vector B = [b₁, b₂, b₃]

           a₁×b₁ + a₂×b₂ + a₃×b₃
Similarity = ─────────────────────────────
             √(a₁²+a₂²+a₃²) × √(b₁²+b₂²+b₃²)

Result: 0.0 (totally different) to 1.0 (identical)

Example:
A = [1, 0, 1]  "Python programming"
B = [1, 0, 1]  "Python programming"
Similarity = 1.0 (identical)

A = [1, 0, 1]  "Python programming"
C = [0, 1, 0]  "Pizza recipe"
Similarity = 0.0 (completely different)
```

---

## 🎯 RAG Prompt Structure

```
ANATOMY OF RAG PROMPT:
──────────────────────

Standard AI Prompt:
┌──────────────────────────┐
│ User: "What is Python?"  │
└──────────────────────────┘
Simple, but AI uses only training data


RAG-Enhanced Prompt:
┌────────────────────────────────────────────┐
│ [1. SYSTEM INSTRUCTION]                    │
│ You are a helpful assistant. Answer using  │
│ only the provided context.                 │
│                                            │
│ [2. CONTEXT]                               │
│ --- Retrieved Information ---              │
│ Python is a high-level programming         │
│ language created in 1991. It emphasizes    │
│ code readability and has extensive         │
│ libraries for various applications.        │
│ --- End of Context ---                     │
│                                            │
│ [3. INSTRUCTION]                           │
│ Based ONLY on the context above, answer:   │
│                                            │
│ [4. USER QUESTION]                         │
│ What is Python?                            │
└────────────────────────────────────────────┘

AI now has SPECIFIC information to use!


COMPONENT BREAKDOWN:
────────────────────

1. System Instruction:
   ┌─────────────────────────────────────┐
   │ Purpose: Set AI behavior            │
   │ Key phrase: "Use only the context"  │
   │ Why: Prevents hallucinations        │
   └─────────────────────────────────────┘

2. Context (Retrieved Chunks):
   ┌─────────────────────────────────────┐
   │ Source: Similarity search results   │
   │ Format: Clear delimiters            │
   │ Why: Provides grounded facts        │
   └─────────────────────────────────────┘

3. Instruction:
   ┌─────────────────────────────────────┐
   │ Purpose: Reinforce context usage    │
   │ Prevents: AI inventing information  │
   │ Why: Ensures faithfulness to docs   │
   └─────────────────────────────────────┘

4. User Question:
   ┌─────────────────────────────────────┐
   │ Original query                      │
   │ Unchanged from user input           │
   └─────────────────────────────────────┘


EXAMPLE COMPARISON:
───────────────────

Without Context:
┌────────────────────────────────────────┐
│ Q: "What's our Q4 revenue target?"     │
│ A: "I don't have access to your        │
│     company's Q4 targets."             │
└────────────────────────────────────────┘


With RAG Context:
┌────────────────────────────────────────┐
│ Context: "Board approved Q4 target     │
│           of $12M revenue, 15% growth" │
│                                        │
│ Q: "What's our Q4 revenue target?"     │
│ A: "According to the board decision,   │
│     the Q4 revenue target is $12M,     │
│     representing 15% growth."          │
└────────────────────────────────────────┘
```

---

## ⚙️ RAG Implementation Steps

```
STEP-BY-STEP IMPLEMENTATION:
────────────────────────────

PHASE 1: SETUP (One-time)
─────────────────────────

Step 1: Prepare Documents
┌─────────────────────────────┐
│ • Collect all docs          │
│ • Clean/format text         │
│ • Remove unnecessary parts  │
└─────────────────────────────┘

Step 2: Chunk Documents
┌─────────────────────────────┐
│ for doc in documents:       │
│     chunks = chunk_text(    │
│         doc,                │
│         size=500,           │
│         overlap=100         │
│     )                       │
└─────────────────────────────┘

Step 3: Create Embeddings
┌─────────────────────────────┐
│ embeddings = []             │
│ for chunk in chunks:        │
│     emb = model.embed(      │
│         chunk               │
│     )                       │
│     embeddings.append(emb)  │
└─────────────────────────────┘

Step 4: Store in Database
┌─────────────────────────────┐
│ knowledge_base = {          │
│     'chunks': chunks,       │
│     'embeddings': embeddings│
│ }                           │
└─────────────────────────────┘


PHASE 2: QUERY (Every request)
───────────────────────────────

Step 5: Embed User Query
┌──────────────────────────────┐
│ query = "What is Python?"    │
│ query_emb = model.embed(     │
│     query                    │
│ )                            │
└──────────────────────────────┘

Step 6: Find Similar Chunks
┌──────────────────────────────┐
│ similarities = []            │
│ for emb in embeddings:       │
│     sim = cosine_similarity( │
│         query_emb, emb       │
│     )                        │
│     similarities.append(sim) │
│                              │
│ top_indices = get_top_k(     │
│     similarities, k=3        │
│ )                            │
└──────────────────────────────┘

Step 7: Build Context
┌──────────────────────────────┐
│ context = ""                 │
│ for idx in top_indices:      │
│     context += chunks[idx]   │
│     context += "\n\n"        │
└──────────────────────────────┘

Step 8: Create RAG Prompt
┌──────────────────────────────┐
│ prompt = f"""                │
│ Context: {context}           │
│                              │
│ Question: {query}            │
│                              │
│ Answer based on context:     │
│ """                          │
└──────────────────────────────┘

Step 9: Generate Answer
┌──────────────────────────────┐
│ response = model.generate(   │
│     prompt                   │
│ )                            │
│                              │
│ return response.text         │
└──────────────────────────────┘


COMPLETE FLOW:
──────────────

User Query
    ↓
Embed Query
    ↓
Similarity Search
    ↓
Retrieve Top Chunks
    ↓
Build Context
    ↓
Create Prompt
    ↓
Generate Answer
    ↓
Return to User
```

---

## 💡 RAG Best Practices

```
CHUNKING:
─────────

✅ DO:
• Use 500-1000 character chunks
• Include 10-20% overlap
• Preserve sentence boundaries
• Keep semantic units together

❌ DON'T:
• Make chunks too small (< 200 chars)
• Make chunks too large (> 2000 chars)
• Split mid-sentence
• Ignore document structure


EMBEDDING:
──────────

✅ DO:
• Use consistent embedding model
• Batch embed for efficiency
• Cache embeddings
• Use domain-specific models if available

❌ DON'T:
• Mix different embedding models
• Re-embed unnecessarily
• Ignore embedding dimensions


RETRIEVAL:
──────────

✅ DO:
• Retrieve 3-5 top chunks
• Set similarity threshold (e.g., > 0.7)
• Re-rank results if needed
• Include metadata (source, date)

❌ DON'T:
• Retrieve too many chunks (> 10)
• Include low-similarity chunks
• Ignore source diversity


PROMPT DESIGN:
──────────────

✅ DO:
• Clearly mark context boundaries
• Instruct to use only context
• Include source citations
• Handle "no relevant info" case

❌ DON'T:
• Mix context with question
• Allow hallucinations
• Exceed token limits
• Ignore formatting


EXAMPLE CONFIGURATIONS:
───────────────────────

General Q&A:
┌─────────────────────────┐
│ Chunk size: 800 chars  │
│ Overlap: 150 chars     │
│ Top-K: 3 chunks        │
│ Min similarity: 0.7    │
└─────────────────────────┘

Technical Documentation:
┌─────────────────────────┐
│ Chunk size: 1200 chars │
│ Overlap: 200 chars     │
│ Top-K: 5 chunks        │
│ Min similarity: 0.75   │
└─────────────────────────┘

Short Answers:
┌─────────────────────────┐
│ Chunk size: 400 chars  │
│ Overlap: 100 chars     │
│ Top-K: 2 chunks        │
│ Min similarity: 0.8    │
└─────────────────────────┘
```

---

## Module Documentation Block

```python
"""
09 - RAG (Retrieval-Augmented Generation) - Basic
===================================================
```
**Explanation:** Module about RAG - one of the MOST IMPORTANT patterns in modern AI applications. RAG enables AI to access external knowledge.

```python
This module demonstrates building a RAG system from scratch.
Students will learn:
- What RAG is and why it's important
- Document chunking strategies
- Creating embeddings
- Similarity search
- Context injection into prompts
- Building a basic RAG pipeline
```
**Explanation:** Learning objectives. RAG is THE solution for giving AI access to your specific documents/data.

```python
Teaching Points:
- RAG enables AI to access external knowledge
- Overcomes knowledge cutoff limitations
- More accurate than pure generation
- Foundation for intelligent search systems
"""
```
**Explanation:** **KEY INSIGHT**: RAG solves the fundamental problem that AI models don't know about YOUR specific documents, recent events, or proprietary data.

---

## Import Statements

```python
import os
```
**Explanation:** File/directory operations.

```python
from dotenv import load_dotenv
```
**Explanation:** Environment variables for API keys.

```python
import google.generativeai as genai
```
**Explanation:** Google's Generative AI SDK.

```python
import numpy as np
```
**Explanation:** **CRITICAL**: NumPy for vector operations. Embeddings are vectors (arrays of numbers), and we need to calculate similarity between vectors using dot products and norms.

```python
from typing import List, Dict
```
**Explanation:** Type hints for better code documentation.

```python
# Setup
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
```
**Explanation:** Standard initialization.

---

## Section 1: Understanding RAG

```python
# ============================================================================
# SECTION 1: Understanding RAG
# ============================================================================
```
**Explanation:** Conceptual foundation.

```python
def rag_concepts():
    """
    Explain what RAG is and how it works
    """
```
**Explanation:** Educational overview of the RAG paradigm.

```python
    print("\n" + "=" * 60)
    print("SECTION 1: Understanding RAG")
    print("=" * 60)
    
    explanation = """
    🔍 WHAT IS RAG?
    
    RAG = Retrieval-Augmented Generation
    
    Combines:
    1. RETRIEVAL: Finding relevant information
    2. GENERATION: Creating response using that information
```
**Explanation:** **CORE CONCEPT**: RAG is TWO steps combined. First FIND relevant information, then GENERATE response using it.

```python
    ❌ WITHOUT RAG:
    ---------------
    User: "What's in our latest product documentation?"
    AI: "I don't have access to your documentation."
    
    • Limited to training data
    • No access to private/recent information
    • Can't answer company-specific questions
```
**Explanation:** **THE PROBLEM**: 
- AI models are frozen at training time
- Don't know about documents created after training
- Don't have access to private company data
- Can't answer questions like "What's in our Q3 report?" or "Who is our new CTO?"

```python
    ✅ WITH RAG:
    ------------
    User: "What's in our latest product documentation?"
    System:
      1. Search documentation
      2. Find relevant sections
      3. Provide to AI as context
    AI: "According to your documentation: [answer]"
    
    • Can access any documents
    • Works with private/recent data
    • More accurate, grounded responses
```
**Explanation:** **THE SOLUTION**: 
- Retrieve relevant document chunks
- Include them in the prompt
- AI generates answer BASED ON provided context
- Result: AI can "know" about YOUR specific documents

```python
    🔄 HOW RAG WORKS:
    
    Step 1: INDEXING (Done once)
    ----------------------------
    Documents → Split into chunks → Create embeddings → Store in database
    
    Example:
    "Python Guide" → 
      Chunk 1: "Python is a programming language..."
      Chunk 2: "Variables store data..."
      Chunk 3: "Functions are reusable..."
    
    Each chunk gets an embedding (vector representation)
```
**Explanation:** **INDEXING PHASE** (offline, one-time):
1. **Chunking**: Break large documents into smaller pieces (paragraphs/sections)
2. **Embedding**: Convert each chunk into a vector (array of numbers)
3. **Storage**: Save chunks and their embeddings in a database

**Why chunks?** Documents are too large to fit in prompts. We need small, focused pieces.

```python
    Step 2: RETRIEVAL (For each query)
    -----------------------------------
    User query → Create query embedding → Find similar chunks → Retrieve
    
    Example:
    Query: "How do I create a function in Python?"
    → Search for similar chunks
    → Find Chunk 3: "Functions are reusable..."
```
**Explanation:** **RETRIEVAL PHASE** (online, per-query):
1. **Query embedding**: Convert user question to vector
2. **Similarity search**: Find chunks with similar vectors (semantic similarity)
3. **Retrieve**: Get the most similar chunks

**How similarity works**: Vectors that point in similar directions = semantically similar. "cat" and "dog" vectors are closer than "cat" and "car".

```python
    Step 3: AUGMENTATION
    --------------------
    Take retrieved chunks + user query → Build enhanced prompt
    
    Enhanced prompt:
    "Context: Functions are reusable blocks of code...
     
     User question: How do I create a function in Python?
     
     Answer based on the context:"
```
**Explanation:** **AUGMENTATION PHASE**: Construct a prompt that includes:
- Retrieved context (the relevant chunks)
- User's original question
- Instructions to answer based on context

This is the "magic" - we're giving the AI the information it needs!

```python
    Step 4: GENERATION
    ------------------
    Send enhanced prompt to AI → Get grounded response
```
**Explanation:** **GENERATION PHASE**: Send augmented prompt to LLM, get answer that's grounded in the provided context.

```python
    🎯 USE CASES:
    
    • Question answering over documents
    • Customer support with knowledge bases
    • Research assistants
    • Legal/medical document analysis
    • Internal company wikis
    • Educational tutoring
    • Code documentation search
```
**Explanation:** **REAL-WORLD APPLICATIONS**: RAG is used everywhere - customer support chatbots, internal company Q&A, research tools, code assistants, etc.

```python
    💡 KEY BENEFITS:
    
    • Up-to-date information
    • Private/proprietary data access
    • Reduced hallucinations
    • Verifiable sources
    • Domain-specific knowledge
    • Cost-effective vs fine-tuning
    """
```
**Explanation:** **ADVANTAGES**:
- **Up-to-date**: Add new documents anytime, no retraining
- **Private data**: Works with confidential docs
- **Fewer hallucinations**: AI answers from provided context, not imagination
- **Verifiable**: Can show which document chunk answer came from
- **Cost-effective**: Much cheaper than fine-tuning a model

```python
    print(explanation)
```
**Explanation:** Display concepts.

---

## Section 2: Document Chunking

```python
# ============================================================================
# SECTION 2: Document Chunking
# ============================================================================
```
**Explanation:** How to split documents effectively.

```python
def document_chunking():
    """
    Demonstrate different chunking strategies
    """
```
**Explanation:** **CRITICAL SKILL**: Bad chunking = bad retrieval. Must preserve semantic meaning.

```python
    print("\n" + "=" * 60)
    print("SECTION 2: Document Chunking")
    print("=" * 60)
    
    # Sample document
    sample_doc = """
Python is a high-level, interpreted programming language known for its simplicity and readability. 
It was created by Guido van Rossum and first released in 1991.

Python supports multiple programming paradigms including procedural, object-oriented, and functional programming.
The language emphasizes code readability with its use of significant indentation.

Python has a comprehensive standard library and a vast ecosystem of third-party packages available through PyPI.
This makes it suitable for various applications from web development to data science and machine learning.

Popular frameworks include Django for web development, NumPy and Pandas for data analysis, and TensorFlow for machine learning.
Python's versatility and ease of learning make it an excellent choice for beginners and professionals alike.
"""
```
**Explanation:** Sample document with multiple paragraphs for demonstrating chunking strategies.

```python
    print("\n📄 Sample Document:")
    print("-" * 60)
    print(sample_doc.strip())
    print("-" * 60)
    
    # Strategy 1: Fixed size chunking
    print("\n\n1️⃣ FIXED SIZE CHUNKING")
    print("="*60)
    
    def chunk_by_size(text: str, chunk_size: int = 200) -> List[str]:
        """Split text into fixed-size chunks"""
        words = text.split()
        chunks = []
        current_chunk = []
        current_length = 0
```
**Explanation:** **STRATEGY 1: Fixed Size**. Split by character/word count.

```python
        for word in words:
            current_length += len(word) + 1
            if current_length > chunk_size:
                chunks.append(' '.join(current_chunk))
                current_chunk = [word]
                current_length = len(word)
            else:
                current_chunk.append(word)
```
**Explanation:** **ALGORITHM**:
- Track current length
- Add words until reaching size limit
- Start new chunk when limit exceeded
- `len(word) + 1` accounts for spaces

```python
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        
        return chunks
```
**Explanation:** Don't forget last chunk! Common bug to omit remaining words.

```python
    fixed_chunks = chunk_by_size(sample_doc, 200)
    print(f"\nCreated {len(fixed_chunks)} chunks (max 200 chars each):\n")
    for i, chunk in enumerate(fixed_chunks, 1):
        print(f"Chunk {i} ({len(chunk)} chars):")
        print(f"  {chunk[:100]}...\n")
```
**Explanation:** Generate and display fixed-size chunks.

**Pros**: Simple, predictable size
**Cons**: Can split mid-sentence, breaks semantic meaning

```python
    # Strategy 2: Sentence-based chunking
    print("\n2️⃣ SENTENCE-BASED CHUNKING")
    print("="*60)
    
    def chunk_by_sentences(text: str, sentences_per_chunk: int = 2) -> List[str]:
        """Split text by sentences"""
        sentences = text.replace('\n', ' ').split('.')
        sentences = [s.strip() + '.' for s in sentences if s.strip()]
```
**Explanation:** **STRATEGY 2: Sentence-Based**. 
- Split by periods (sentence boundaries)
- Replace newlines with spaces
- Re-add periods (removed by split)
- Filter empty strings

```python
        chunks = []
        for i in range(0, len(sentences), sentences_per_chunk):
            chunk = ' '.join(sentences[i:i+sentences_per_chunk])
            chunks.append(chunk)
        
        return chunks
```
**Explanation:** Group sentences together. `range(..., sentences_per_chunk)` steps by that amount, so we get groups of N sentences.

```python
    sentence_chunks = chunk_by_sentences(sample_doc, 2)
    print(f"\nCreated {len(sentence_chunks)} chunks (2 sentences each):\n")
    for i, chunk in enumerate(sentence_chunks, 1):
        print(f"Chunk {i}:")
        print(f"  {chunk}\n")
```
**Explanation:** Display sentence-based chunks.

**Pros**: Preserves sentence meaning
**Cons**: Variable size, simple period splitting fails on abbreviations (Dr. Smith)

```python
    # Strategy 3: Paragraph-based chunking
    print("\n3️⃣ PARAGRAPH-BASED CHUNKING")
    print("="*60)
    
    def chunk_by_paragraphs(text: str) -> List[str]:
        """Split text by paragraphs"""
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        return paragraphs
```
**Explanation:** **STRATEGY 3: Paragraph-Based**. Split on double newlines (`\n\n`). Natural semantic units.

```python
    para_chunks = chunk_by_paragraphs(sample_doc)
    print(f"\nCreated {len(para_chunks)} chunks (by paragraphs):\n")
    for i, chunk in enumerate(para_chunks, 1):
        print(f"Chunk {i}:")
        print(f"  {chunk[:100]}...\n")
```
**Explanation:** Display paragraph chunks.

**Pros**: Best semantic units, preserves topic coherence
**Cons**: Variable size, some paragraphs might be too large

```python
    print("\n💡 CHOOSING A CHUNKING STRATEGY:")
    print("-" * 60)
    print("""
    • Fixed Size: Simple, consistent size, may break context
    • Sentences: Preserves meaning, variable size
    • Paragraphs: Best semantic units, can be too large
    • Hybrid: Combine strategies for best results
    
    Typical chunk sizes: 200-500 tokens (150-375 words)
    """)
```
**Explanation:** **BEST PRACTICES**: 
- **200-500 tokens**: Sweet spot for most applications
- **Hybrid**: Often best - try paragraph first, split if too large
- **Domain-specific**: Code needs different chunking than prose

---

## Section 3: Creating Embeddings

```python
# ============================================================================
# SECTION 3: Creating Embeddings
# ============================================================================
```
**Explanation:** Converting text to vectors.

```python
def creating_embeddings():
    """
    Generate embeddings for text chunks
    """
```
**Explanation:** Embeddings are THE KEY to semantic search.

```python
    print("\n" + "=" * 60)
    print("SECTION 3: Creating Embeddings")
    print("=" * 60)
    
    print("\n📊 What are embeddings?")
    print("-" * 60)
    print("""
    Embeddings convert text into numerical vectors (arrays of numbers).
    Similar meanings → Similar vectors
    
    Example:
    "cat" → [0.2, 0.8, 0.1, ...]
    "dog" → [0.25, 0.75, 0.12, ...] (similar to cat)
    "car" → [0.9, 0.1, 0.8, ...] (different from cat/dog)
    """)
```
**Explanation:** **FUNDAMENTAL CONCEPT**: 
- Text → Vector (array of numbers)
- Semantically similar text → Similar vectors (close in vector space)
- Example: "king" - "man" + "woman" ≈ "queen" (famous example)

**Why vectors?** Can't do math on words, but CAN calculate distance/similarity between vectors.

```python
    # Sample texts
    texts = [
        "Python is a programming language",
        "JavaScript is used for web development",
        "Machine learning models need training data",
        "Deep learning is a subset of machine learning",
        "Cats are popular pets"
    ]
```
**Explanation:** Sample texts with varying semantic relatedness to demonstrate similarity.

```python
    print("\n🔄 Generating embeddings...")
    print("-" * 60)
    
    # Generate embeddings using Gemini
    embeddings = []
    for i, text in enumerate(texts, 1):
        result = genai.embed_content(
            model="models/embedding-001",
            content=text,
            task_type="retrieval_document"
        )
```
**Explanation:** **EMBEDDING API CALL**:
- `model="models/embedding-001"`: Google's embedding model
- `content=text`: What to embed
- `task_type="retrieval_document"`: Optimize for document storage (vs "retrieval_query" for queries)

**Why different task types?** Queries and documents have different characteristics. Optimizing separately improves retrieval.

```python
        embedding = result['embedding']
        embeddings.append(embedding)
        
        print(f"\n{i}. Text: \"{text}\"")
        print(f"   Embedding: [{embedding[0]:.4f}, {embedding[1]:.4f}, {embedding[2]:.4f}, ... ] ({len(embedding)} dimensions)")
```
**Explanation:** Display first 3 dimensions and total dimension count. Typical: 768 or 1536 dimensions.

```python
    # Calculate similarity
    print("\n\n📏 Similarity Scores (Cosine Similarity):")
    print("-" * 60)
    
    def cosine_similarity(a, b):
        """Calculate cosine similarity between two vectors"""
        dot_product = np.dot(a, b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        return dot_product / (norm_a * norm_b)
```
**Explanation:** **COSINE SIMILARITY FORMULA**:
- **Dot product**: a·b = sum of element-wise multiplications
- **Norm**: ||a|| = sqrt(sum of squared elements) = vector length
- **Cosine similarity**: (a·b) / (||a|| × ||b||)

**Range**: -1 to 1 (usually 0 to 1 for embeddings)
- 1 = identical direction (very similar)
- 0 = perpendicular (unrelated)
- -1 = opposite direction (antonyms)

**Why cosine?** Measures angle between vectors, independent of magnitude. Perfect for semantic similarity.

```python
    # Compare some pairs
    comparisons = [
        (0, 1, "Python vs JavaScript"),
        (2, 3, "ML vs Deep Learning"),
        (0, 4, "Python vs Cats"),
        (2, 4, "ML vs Cats")
    ]
    
    for idx1, idx2, label in comparisons:
        similarity = cosine_similarity(embeddings[idx1], embeddings[idx2])
        print(f"\n{label}:")
        print(f"  '{texts[idx1]}'")
        print(f"  vs")
        print(f"  '{texts[idx2]}'")
        print(f"  Similarity: {similarity:.4f} {'🔥 High' if similarity > 0.7 else '❄️ Low'}")
```
**Explanation:** Compare pairs to show:
- **Related topics** (Python vs JavaScript, ML vs Deep Learning) = HIGH similarity
- **Unrelated topics** (Programming vs Cats) = LOW similarity

---

## Section 4: Similarity Search

```python
# ============================================================================
# SECTION 4: Similarity Search
# ============================================================================
```
**Explanation:** Finding relevant documents.

```python
def similarity_search():
    """
    Implement basic similarity search
    """
```
**Explanation:** The retrieval component of RAG.

```python
    print("\n" + "=" * 60)
    print("SECTION 4: Similarity Search")
    print("=" * 60)
    
    # Knowledge base
    knowledge_base = [
        "Python was created by Guido van Rossum in 1991.",
        "Python is known for its simple and readable syntax.",
        "Python supports multiple programming paradigms.",
        "Django is a popular Python web framework.",
        "NumPy is used for numerical computing in Python.",
        "Machine learning can be done with Python using libraries like scikit-learn.",
        "Python has a large standard library included by default.",
        "Python code uses indentation for structure instead of braces."
    ]
```
**Explanation:** Our "database" of knowledge. In production, this would be thousands/millions of documents.

```python
    print("\n📚 Knowledge Base:")
    print("-" * 60)
    for i, doc in enumerate(knowledge_base, 1):
        print(f"{i}. {doc}")
    
    # Generate embeddings for knowledge base
    print("\n\n🔄 Generating embeddings for knowledge base...")
    
    kb_embeddings = []
    for doc in knowledge_base:
        result = genai.embed_content(
            model="models/embedding-001",
            content=doc,
            task_type="retrieval_document"
        )
        kb_embeddings.append(result['embedding'])
    
    print("✅ Embeddings created!")
```
**Explanation:** **INDEXING**: Create embeddings for all documents. This is done ONCE (offline), not per-query.

```python
    # Search function
    def search(query: str, top_k: int = 3) -> List[Dict]:
        """Search for most similar documents"""
        # Generate query embedding
        query_result = genai.embed_content(
            model="models/embedding-001",
            content=query,
            task_type="retrieval_query"
        )
        query_embedding = query_result['embedding']
```
**Explanation:** **KEY DIFFERENCE**: `task_type="retrieval_query"` for queries (vs "retrieval_document" for documents). Optimizes embedding for query-document matching.

```python
        # Calculate similarities
        similarities = []
        for i, doc_embedding in enumerate(kb_embeddings):
            similarity = np.dot(query_embedding, doc_embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(doc_embedding)
            )
```
**Explanation:** **BRUTE FORCE SEARCH**: Calculate cosine similarity between query and EVERY document. 

**In production**: Use vector databases (Pinecone, Weaviate, Chroma) with approximate nearest neighbor search for speed.

```python
            similarities.append({
                'index': i,
                'document': knowledge_base[i],
                'similarity': similarity
            })
        
        # Sort and return top k
        similarities.sort(key=lambda x: x['similarity'], reverse=True)
        return similarities[:top_k]
```
**Explanation:** 
- Sort by similarity (highest first)
- Return top K results
- `top_k=3`: Typical value, balances context richness vs noise

```python
    # Test queries
    test_queries = [
        "Who created Python?",
        "What is Python used for in data science?",
        "How is Python code structured?"
    ]
    
    for query in test_queries:
        print(f"\n\n{'='*60}")
        print(f"🔍 Query: '{query}'")
        print(f"{'='*60}")
        
        results = search(query, top_k=3)
        
        print("\nTop 3 Most Relevant Documents:")
        for i, result in enumerate(results, 1):
            print(f"\n{i}. [Similarity: {result['similarity']:.4f}]")
            print(f"   {result['document']}")
```
**Explanation:** Test queries demonstrate semantic search:
- "Who created Python?" → finds "Python was created by Guido van Rossum"
- Doesn't need exact keyword match
- Understands semantic intent

---

## Section 5: Basic RAG Pipeline

```python
# ============================================================================
# SECTION 5: Basic RAG Pipeline
# ============================================================================
```
**Explanation:** Complete end-to-end RAG system.

```python
def basic_rag_pipeline():
    """
    Complete RAG implementation
    """
```
**Explanation:** **THE FULL PIPELINE**: Retrieval + Augmentation + Generation.

```python
    print("\n" + "=" * 60)
    print("SECTION 5: Basic RAG Pipeline")
    print("=" * 60)
    
    # Knowledge base
    documents = [
        "Python is a high-level programming language created by Guido van Rossum in 1991.",
        "Python emphasizes code readability with significant indentation.",
        "Python supports object-oriented, procedural, and functional programming paradigms.",
        "The Django framework is used for building web applications in Python.",
        "Flask is a lightweight web framework for Python.",
        "NumPy provides support for large, multi-dimensional arrays and matrices.",
        "Pandas is a data analysis library that offers data structures like DataFrames.",
        "Scikit-learn is a machine learning library for Python.",
        "TensorFlow and PyTorch are deep learning frameworks available in Python.",
        "Python's pip package manager makes it easy to install third-party libraries."
    ]
```
**Explanation:** Richer knowledge base covering various Python topics.

```python
    print("\n📚 Loading knowledge base...")
    print(f"   {len(documents)} documents loaded")
    
    # Generate embeddings
    print("\n🔄 Creating embeddings...")
    
    doc_embeddings = []
    for doc in documents:
        result = genai.embed_content(
            model="models/embedding-001",
            content=doc,
            task_type="retrieval_document"
        )
        doc_embeddings.append(result['embedding'])
    
    print("   ✅ Embeddings created!")
```
**Explanation:** **INDEXING PHASE**: One-time embedding generation.

```python
    # RAG function
    def rag_query(question: str, top_k: int = 3) -> str:
        """
        Complete RAG pipeline:
        1. Retrieve relevant documents
        2. Augment prompt with context
        3. Generate response
        """
```
**Explanation:** **COMPLETE RAG FUNCTION**: All three phases in one.

```python
        # Step 1: Retrieve
        print(f"\n🔍 Retrieving relevant documents...")
        
        query_result = genai.embed_content(
            model="models/embedding-001",
            content=question,
            task_type="retrieval_query"
        )
        query_embedding = query_result['embedding']
        
        # Calculate similarities
        similarities = []
        for i, doc_emb in enumerate(doc_embeddings):
            sim = np.dot(query_embedding, doc_emb) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(doc_emb)
            )
            similarities.append((i, sim))
        
        # Get top k
        similarities.sort(key=lambda x: x[1], reverse=True)
        top_docs = [documents[i] for i, _ in similarities[:top_k]]
        
        print(f"   ✅ Retrieved {len(top_docs)} documents")
```
**Explanation:** **RETRIEVAL**: Same as before - find top K most similar documents.

```python
        # Step 2: Augment
        print(f"\n📝 Building augmented prompt...")
        
        context = "\n".join([f"- {doc}" for doc in top_docs])
        
        augmented_prompt = f"""Based on the following context, answer the question.
        
Context:
{context}

Question: {question}

Answer: Provide a clear, concise answer based ONLY on the context above. If the context doesn't contain the answer, say so."""
```
**Explanation:** **AUGMENTATION**: Build prompt with:
1. **Clear instruction**: "Based on the following context..."
2. **Context section**: Retrieved documents
3. **Question**: User's query
4. **Constraint**: "based ONLY on the context" (reduces hallucinations)

**Critical**: Format matters! Clear separation between context and question helps the model.

```python
        # Step 3: Generate
        print(f"\n🤖 Generating response...")
        
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(augmented_prompt)
        
        return response.text, top_docs
```
**Explanation:** **GENERATION**: Send augmented prompt to LLM, get grounded response.

```python
    # Test the RAG system
    test_questions = [
        "Who created Python and when?",
        "What web frameworks are available for Python?",
        "What libraries can I use for data analysis?"
    ]
    
    for question in test_questions:
        print("\n" + "="*60)
        print(f"❓ Question: {question}")
        print("="*60)
        
        answer, retrieved_docs = rag_query(question)
        
        print("\n📄 Retrieved Context:")
        for i, doc in enumerate(retrieved_docs, 1):
            print(f"   {i}. {doc}")
        
        print(f"\n✅ Answer:")
        print("-"*60)
        print(answer)
        print()
```
**Explanation:** Test queries demonstrate complete RAG pipeline. Shows which documents were retrieved and the final answer.

---

## Section 6: RAG vs Non-RAG Comparison

```python
# ============================================================================
# SECTION 6: RAG vs Non-RAG Comparison
# ============================================================================
```
**Explanation:** Showing RAG's value.

```python
def rag_comparison():
    """
    Compare RAG vs non-RAG responses
    """
```
**Explanation:** Side-by-side comparison to demonstrate RAG benefits.

```python
    print("\n" + "=" * 60)
    print("SECTION 6: RAG vs Non-RAG Comparison")
    print("=" * 60)
    
    # Specific company knowledge
    company_docs = [
        "Our company, TechCorp, was founded in 2020 by Jane Smith.",
        "TechCorp specializes in AI-powered customer service solutions.",
        "Our main product is ChatAssist, launched in January 2023.",
        "ChatAssist has helped over 5000 businesses improve customer satisfaction.",
        "TechCorp is headquartered in San Francisco with 150 employees."
    ]
```
**Explanation:** **COMPANY-SPECIFIC DATA**: Information the model CAN'T know (not in training data). Perfect for demonstrating RAG.

```python
    # Generate embeddings
    doc_embeddings = []
    for doc in company_docs:
        result = genai.embed_content(
            model="models/embedding-001",
            content=doc,
            task_type="retrieval_document"
        )
        doc_embeddings.append(result['embedding'])
    
    question = "When was TechCorp founded and by whom?"
    
    model = genai.GenerativeModel('gemini-pro')
    
    # Without RAG
    print("\n❌ WITHOUT RAG:")
    print("-"*60)
    print(f"Question: {question}\n")
    
    response_no_rag = model.generate_content(question)
    print(f"Answer: {response_no_rag.text}")
    print("\n💡 Notice: Generic answer or says it doesn't know")
```
**Explanation:** **WITHOUT RAG**: AI doesn't know about TechCorp. Will either:
- Say "I don't have information about TechCorp"
- Hallucinate (make up) an answer
- Give generic response

```python
    # With RAG
    print("\n\n✅ WITH RAG:")
    print("-"*60)
    print(f"Question: {question}\n")
    
    # Retrieve
    query_result = genai.embed_content(
        model="models/embedding-001",
        content=question,
        task_type="retrieval_query"
    )
    
    similarities = []
    for i, doc_emb in enumerate(doc_embeddings):
        sim = np.dot(query_result['embedding'], doc_emb) / (
            np.linalg.norm(query_result['embedding']) * np.linalg.norm(doc_emb)
        )
        similarities.append((i, sim))
    
    similarities.sort(key=lambda x: x[1], reverse=True)
    relevant_doc = company_docs[similarities[0][0]]
    
    print(f"Retrieved Context: {relevant_doc}\n")
    
    # Generate with context
    rag_prompt = f"Context: {relevant_doc}\n\nQuestion: {question}\n\nAnswer based on the context:"
    response_rag = model.generate_content(rag_prompt)
    
    print(f"Answer: {response_rag.text}")
    print("\n💡 Notice: Specific, accurate answer based on provided context")
```
**Explanation:** **WITH RAG**: AI gets the relevant document as context and provides accurate answer: "TechCorp was founded in 2020 by Jane Smith."

**The difference is DRAMATIC**: RAG enables AI to answer questions it couldn't answer otherwise.

---

## Section 7: Best Practices

```python
# ============================================================================
# SECTION 7: Best Practices
# ============================================================================
```
**Explanation:** Production guidelines.

```python
def rag_best_practices():
    """
    Best practices for building RAG systems
    """
```
**Explanation:** Accumulated wisdom for production RAG systems.

```python
    print("\n" + "=" * 60)
    print("SECTION 7: RAG Best Practices")
    print("=" * 60)
    
    practices = """
    ✅ DOCUMENT PREPARATION:
    
    1. Clean your documents
       • Remove irrelevant content
       • Fix formatting issues
       • Standardize structure
```
**Explanation:** **GARBAGE IN = GARBAGE OUT**: Clean documents = better retrieval. Remove boilerplate, fix OCR errors, standardize formatting.

```python
    2. Choose appropriate chunk size
       • Too small: Loses context
       • Too large: Less precise retrieval
       • Sweet spot: 200-500 tokens
```
**Explanation:** **CHUNK SIZE TRADE-OFF**:
- **Too small** (< 100 tokens): Loses surrounding context
- **Too large** (> 1000 tokens): Retrieved chunk might contain irrelevant info
- **Sweet spot** (200-500 tokens): Enough context, precise retrieval

```python
    3. Add metadata
       • Source, date, author
       • Helps with filtering
       • Improves traceability
```
**Explanation:** **METADATA**: Store source info with chunks. Enables:
- Filtering ("only 2023 documents")
- Citation ("According to Q3 report...")
- Freshness scoring (prioritize recent)

```python
    ✅ EMBEDDING STRATEGY:
    
    1. Use domain-specific models when possible
    2. Consistent embedding model for index and query
    3. Consider embedding costs at scale
    4. Cache embeddings for reuse
```
**Explanation:** **EMBEDDING TIPS**:
- **Domain-specific**: Medical/legal embeddings understand jargon better
- **Consistency**: MUST use same model for documents and queries
- **Costs**: Embedding costs add up at scale
- **Caching**: Don't re-embed same text

```python
    ✅ RETRIEVAL:
    
    1. Tune top_k parameter
       • More context vs noise
       • Typical: 3-5 documents
```
**Explanation:** **TOP_K TUNING**:
- **Too low** (1-2): Might miss relevant info
- **Too high** (10+): Adds noise, costs more tokens
- **Sweet spot** (3-5): Good coverage without overload

```python
    2. Implement hybrid search
       • Semantic (embeddings)
       • Keyword (BM25)
       • Combined scoring
```
**Explanation:** **HYBRID SEARCH**: Combine semantic and keyword search. Semantic finds conceptually similar, keyword finds exact matches. Best of both worlds.

```python
    3. Use reranking
       • Initial retrieval: Fast, broad
       • Reranking: Slow, precise
       • Best of both worlds
```
**Explanation:** **TWO-STAGE RETRIEVAL**:
1. **Fast retrieval**: Get top 50 candidates (quick, approximate)
2. **Slow reranking**: Score top 50 carefully, return best 5
Result: Speed + accuracy

```python
    ✅ PROMPT ENGINEERING:
    
    1. Clear instructions
       "Answer based on context"
       "Cite sources when possible"
       "Say 'I don't know' if context insufficient"
```
**Explanation:** **PROMPT INSTRUCTIONS**: Tell the model:
- Use context (not general knowledge)
- Cite sources (for verification)
- Admit uncertainty (don't hallucinate)

```python
    2. Format context clearly
       Separate context from question
       Number or bullet points
       Include source references
```
**Explanation:** **FORMATTING MATTERS**: Clear separation helps model understand what's context vs question.

```python
    3. Handle edge cases
       No relevant documents found
       Contradictory information
       Outdated information
```
**Explanation:** **EDGE CASES**:
- **No results**: Graceful degradation, ask user to rephrase
- **Contradictory**: Present both, note contradiction
- **Outdated**: Prioritize recent, note date

```python
    ✅ SYSTEM DESIGN:
    
    1. Caching
       • Cache embeddings
       • Cache common queries
       • Reduce API calls
```
**Explanation:** **CACHING**: Huge cost/latency savings:
- **Embedding cache**: Don't re-embed same chunks
- **Query cache**: Store popular query results

```python
    2. Error handling
       • Embedding failures
       • Search failures
       • Generation failures
       • Graceful degradation
```
**Explanation:** **ROBUSTNESS**: Handle failures gracefully. If embedding API down, fall back to keyword search.

```python
    3. Monitoring
       • Query patterns
       • Retrieval quality
       • Response quality
       • User feedback
```
**Explanation:** **OBSERVABILITY**: Track:
- What users ask (identify gaps)
- Retrieval accuracy (A/B test chunking strategies)
- Response quality (user thumbs up/down)

```python
    4. Updating knowledge base
       • Regular updates
       • Version control
       • Incremental indexing
       • Remove outdated info
```
**Explanation:** **MAINTENANCE**: Knowledge base needs care:
- **Regular updates**: Add new docs
- **Version control**: Track changes
- **Incremental**: Don't re-index everything
- **Cleanup**: Remove obsolete docs

```python
    ⚠️ COMMON PITFALLS:
    
    1. Context overflow
       • Too many retrieved docs
       • Exceeds token limit
       • Solution: Summarize or truncate
```
**Explanation:** **PITFALL 1**: Retrieving 10 long documents might exceed model's context window. Solution: Retrieve more, use fewer, or summarize.

```python
    2. Poor chunking
       • Breaks semantic meaning
       • Solution: Semantic-aware splitting
```
**Explanation:** **PITFALL 2**: Splitting mid-sentence or separating related info. Solution: Use paragraph/section boundaries.

```python
    3. Ignoring recency
       • Old information prioritized
       • Solution: Weight by date
```
**Explanation:** **PITFALL 3**: 2020 doc ranked same as 2024 doc. Solution: Boost similarity score by recency.

```python
    4. No source attribution
       • Can't verify claims
       • Solution: Include sources in response
```
**Explanation:** **PITFALL 4**: Can't verify where answer came from. Solution: "According to [Document X]..."

```python
    💡 EVALUATION:
    
    1. Retrieval quality
       • Are relevant docs retrieved?
       • Precision and recall
    
    2. Answer quality
       • Factually correct?
       • Based on context?
       • Well-formatted?
    
    3. User satisfaction
       • Helpful?
       • Accurate?
       • Fast enough?
    """
```
**Explanation:** **METRICS**:
- **Retrieval**: Are right docs found?
- **Generation**: Is answer correct and grounded?
- **UX**: Is user happy?

```python
    print(practices)
```
**Explanation:** Display all practices.

---

## Main Function

```python
# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main function with menu
    """
    print("\n")
    print("🎓 " + "=" * 58 + " 🎓")
    print("      GENERATIVE AI SESSION - MODULE 9: RAG (BASIC)")
    print("🎓 " + "=" * 58 + " 🎓")
```
**Explanation:** Standard main setup.

```python
    menu = """
    Choose a section to run:
    
    1. Understanding RAG
    2. Document Chunking
    3. Creating Embeddings
    4. Similarity Search
    5. Basic RAG Pipeline
    6. RAG vs Non-RAG Comparison
    7. Best Practices
    
    all - Run all sections
    quit - Exit
    
    """
```
**Explanation:** Menu with 7 sections.

```python
    while True:
        print(menu)
        choice = input("Your choice: ").strip().lower()
        
        if choice in ['quit', 'q', 'exit']:
            print("👋 Goodbye!")
            break
        elif choice == '1':
            rag_concepts()
        # ... [rest of choices] ...
```
**Explanation:** Standard menu loop.

```python
        elif choice == 'all':
            rag_concepts()
            document_chunking()
            creating_embeddings()
            similarity_search()
            basic_rag_pipeline()
            rag_comparison()
            rag_best_practices()
            print("\n✅ All sections completed!")
            break
```
**Explanation:** 'all' runs all sections sequentially.

```python
        else:
            print("⚠️  Invalid choice. Please try again.")
```
**Explanation:** Invalid input handling.

---

## Script Entry Point

```python
if __name__ == "__main__":
    main()
    
    # Teaching Questions:
    # 1. What problem does RAG solve?
    # 2. How does chunking affect retrieval quality?
    # 3. When would you use RAG vs fine-tuning?
```
**Explanation:** Entry point with discussion questions.

---

## Summary

This module teaches **RAG (Retrieval-Augmented Generation)** - THE most important pattern for building AI systems that work with your specific documents and data.

### The RAG Problem:

AI models are **frozen at training time**:
- Don't know about documents created after training
- No access to private/proprietary data
- Can't answer company-specific questions
- Limited to general knowledge

### The RAG Solution:

**Four-Phase Pipeline:**

1. **Indexing** (offline, once):
   - Chunk documents (200-500 tokens)
   - Generate embeddings (text → vectors)
   - Store in vector database

2. **Retrieval** (online, per-query):
   - Embed user query
   - Find similar chunks (cosine similarity)
   - Retrieve top K results

3. **Augmentation**:
   - Build prompt: Context + Question
   - Format clearly for the model

4. **Generation**:
   - Send augmented prompt to LLM
   - Get grounded response

### Key Concepts:

**Embeddings**: Text → numerical vectors (arrays). Semantically similar text → similar vectors.

**Cosine Similarity**: Measures angle between vectors. Formula: (a·b) / (||a|| × ||b||). Range 0-1, higher = more similar.

**Chunking Strategies**:
- **Fixed size**: Simple, may break context
- **Sentences**: Preserves meaning, variable size  
- **Paragraphs**: Best semantic units, can be large
- **Sweet spot**: 200-500 tokens

### Implementation Pattern:

```python
# 1. Index (once)
embeddings = [embed(chunk) for chunk in chunks]

# 2. Retrieve (per query)
query_emb = embed(query)
top_chunks = find_similar(query_emb, embeddings, k=3)

# 3. Augment
prompt = f"Context: {top_chunks}\n\nQ: {query}\n\nA:"

# 4. Generate
response = model.generate(prompt)
```

### Best Practices:

**Document Prep**:
- Clean formatting
- Optimal chunk size (200-500 tokens)
- Add metadata (source, date, author)

**Retrieval**:
- top_k = 3-5 (sweet spot)
- Hybrid search (semantic + keyword)
- Two-stage (fast retrieval + slow reranking)

**Prompting**:
- Clear instructions ("Answer based on context")
- Format separation (context vs question)
- Handle edge cases ("Say 'I don't know' if uncertain")

**System Design**:
- Cache embeddings and queries
- Error handling and fallbacks
- Monitor retrieval/answer quality
- Regular knowledge base updates

### Common Pitfalls:

❌ **Context overflow**: Too many docs → exceeds token limit
❌ **Poor chunking**: Breaks semantic meaning
❌ **Ignoring recency**: Old docs ranked same as new
❌ **No attribution**: Can't verify answer source

### Use Cases:

- Customer support (company knowledge base)
- Internal Q&A (company wiki, docs)
- Research assistants (papers, reports)
- Code assistants (documentation)
- Legal/medical (case law, records)

### RAG vs Alternatives:

**RAG vs Fine-tuning**:
- **RAG**: Dynamic, updatable, source attribution, cheaper
- **Fine-tuning**: Static knowledge, no sources, expensive

**When to use RAG**:
- Frequently changing information
- Need source attribution
- Private/proprietary data
- Quick deployment

**Key insight**: RAG transforms AI from "frozen knowledge" to "dynamic knowledge with sources". It's THE pattern enabling AI to work with YOUR specific data!