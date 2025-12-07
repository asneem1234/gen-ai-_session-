"""
09 - RAG (Retrieval-Augmented Generation) - Basic
===================================================

This module demonstrates building a RAG system from scratch.
Students will learn:
- What RAG is and why it's important
- Document chunking strategies
- Creating embeddings
- Similarity search
- Context injection into prompts
- Building a basic RAG pipeline

Teaching Points:
- RAG enables AI to access external knowledge
- Overcomes knowledge cutoff limitations
- More accurate than pure generation
- Foundation for intelligent search systems
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai
import numpy as np
from typing import List, Dict

# Setup
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


# ============================================================================
# SECTION 1: Understanding RAG
# ============================================================================

def rag_concepts():
    """
    Explain what RAG is and how it works
    """
    print("\n" + "=" * 60)
    print("SECTION 1: Understanding RAG")
    print("=" * 60)
    
    explanation = """
    🔍 WHAT IS RAG?
    
    RAG = Retrieval-Augmented Generation
    
    Combines:
    1. RETRIEVAL: Finding relevant information
    2. GENERATION: Creating response using that information
    
    
    ❌ WITHOUT RAG:
    ---------------
    User: "What's in our latest product documentation?"
    AI: "I don't have access to your documentation."
    
    • Limited to training data
    • No access to private/recent information
    • Can't answer company-specific questions
    
    
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
    
    
    Step 2: RETRIEVAL (For each query)
    -----------------------------------
    User query → Create query embedding → Find similar chunks → Retrieve
    
    Example:
    Query: "How do I create a function in Python?"
    → Search for similar chunks
    → Find Chunk 3: "Functions are reusable..."
    
    
    Step 3: AUGMENTATION
    --------------------
    Take retrieved chunks + user query → Build enhanced prompt
    
    Enhanced prompt:
    "Context: Functions are reusable blocks of code...
     
     User question: How do I create a function in Python?
     
     Answer based on the context:"
    
    
    Step 4: GENERATION
    ------------------
    Send enhanced prompt to AI → Get grounded response
    
    
    🎯 USE CASES:
    
    • Question answering over documents
    • Customer support with knowledge bases
    • Research assistants
    • Legal/medical document analysis
    • Internal company wikis
    • Educational tutoring
    • Code documentation search
    
    
    💡 KEY BENEFITS:
    
    • Up-to-date information
    • Private/proprietary data access
    • Reduced hallucinations
    • Verifiable sources
    • Domain-specific knowledge
    • Cost-effective vs fine-tuning
    """
    
    print(explanation)


# ============================================================================
# SECTION 2: Document Chunking
# ============================================================================

def document_chunking():
    """
    Demonstrate different chunking strategies
    """
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
        
        for word in words:
            current_length += len(word) + 1
            if current_length > chunk_size:
                chunks.append(' '.join(current_chunk))
                current_chunk = [word]
                current_length = len(word)
            else:
                current_chunk.append(word)
        
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        
        return chunks
    
    fixed_chunks = chunk_by_size(sample_doc, 200)
    print(f"\nCreated {len(fixed_chunks)} chunks (max 200 chars each):\n")
    for i, chunk in enumerate(fixed_chunks, 1):
        print(f"Chunk {i} ({len(chunk)} chars):")
        print(f"  {chunk[:100]}...\n")
    
    # Strategy 2: Sentence-based chunking
    print("\n2️⃣ SENTENCE-BASED CHUNKING")
    print("="*60)
    
    def chunk_by_sentences(text: str, sentences_per_chunk: int = 2) -> List[str]:
        """Split text by sentences"""
        sentences = text.replace('\n', ' ').split('.')
        sentences = [s.strip() + '.' for s in sentences if s.strip()]
        
        chunks = []
        for i in range(0, len(sentences), sentences_per_chunk):
            chunk = ' '.join(sentences[i:i+sentences_per_chunk])
            chunks.append(chunk)
        
        return chunks
    
    sentence_chunks = chunk_by_sentences(sample_doc, 2)
    print(f"\nCreated {len(sentence_chunks)} chunks (2 sentences each):\n")
    for i, chunk in enumerate(sentence_chunks, 1):
        print(f"Chunk {i}:")
        print(f"  {chunk}\n")
    
    # Strategy 3: Paragraph-based chunking
    print("\n3️⃣ PARAGRAPH-BASED CHUNKING")
    print("="*60)
    
    def chunk_by_paragraphs(text: str) -> List[str]:
        """Split text by paragraphs"""
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        return paragraphs
    
    para_chunks = chunk_by_paragraphs(sample_doc)
    print(f"\nCreated {len(para_chunks)} chunks (by paragraphs):\n")
    for i, chunk in enumerate(para_chunks, 1):
        print(f"Chunk {i}:")
        print(f"  {chunk[:100]}...\n")
    
    print("\n💡 CHOOSING A CHUNKING STRATEGY:")
    print("-" * 60)
    print("""
    • Fixed Size: Simple, consistent size, may break context
    • Sentences: Preserves meaning, variable size
    • Paragraphs: Best semantic units, can be too large
    • Hybrid: Combine strategies for best results
    
    Typical chunk sizes: 200-500 tokens (150-375 words)
    """)


# ============================================================================
# SECTION 3: Creating Embeddings
# ============================================================================

def creating_embeddings():
    """
    Generate embeddings for text chunks
    """
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
    
    # Sample texts
    texts = [
        "Python is a programming language",
        "JavaScript is used for web development",
        "Machine learning models need training data",
        "Deep learning is a subset of machine learning",
        "Cats are popular pets"
    ]
    
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
        embedding = result['embedding']
        embeddings.append(embedding)
        
        print(f"\n{i}. Text: \"{text}\"")
        print(f"   Embedding: [{embedding[0]:.4f}, {embedding[1]:.4f}, {embedding[2]:.4f}, ... ] ({len(embedding)} dimensions)")
    
    # Calculate similarity
    print("\n\n📏 Similarity Scores (Cosine Similarity):")
    print("-" * 60)
    
    def cosine_similarity(a, b):
        """Calculate cosine similarity between two vectors"""
        dot_product = np.dot(a, b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        return dot_product / (norm_a * norm_b)
    
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


# ============================================================================
# SECTION 4: Similarity Search
# ============================================================================

def similarity_search():
    """
    Implement basic similarity search
    """
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
        
        # Calculate similarities
        similarities = []
        for i, doc_embedding in enumerate(kb_embeddings):
            similarity = np.dot(query_embedding, doc_embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(doc_embedding)
            )
            similarities.append({
                'index': i,
                'document': knowledge_base[i],
                'similarity': similarity
            })
        
        # Sort and return top k
        similarities.sort(key=lambda x: x['similarity'], reverse=True)
        return similarities[:top_k]
    
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


# ============================================================================
# SECTION 5: Basic RAG Pipeline
# ============================================================================

def basic_rag_pipeline():
    """
    Complete RAG implementation
    """
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
    
    # RAG function
    def rag_query(question: str, top_k: int = 3) -> str:
        """
        Complete RAG pipeline:
        1. Retrieve relevant documents
        2. Augment prompt with context
        3. Generate response
        """
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
        
        # Step 2: Augment
        print(f"\n📝 Building augmented prompt...")
        
        context = "\n".join([f"- {doc}" for doc in top_docs])
        
        augmented_prompt = f"""Based on the following context, answer the question.
        
Context:
{context}

Question: {question}

Answer: Provide a clear, concise answer based ONLY on the context above. If the context doesn't contain the answer, say so."""
        
        # Step 3: Generate
        print(f"\n🤖 Generating response...")
        
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(augmented_prompt)
        
        return response.text, top_docs
    
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


# ============================================================================
# SECTION 6: RAG vs Non-RAG Comparison
# ============================================================================

def rag_comparison():
    """
    Compare RAG vs non-RAG responses
    """
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


# ============================================================================
# SECTION 7: Best Practices
# ============================================================================

def rag_best_practices():
    """
    Best practices for building RAG systems
    """
    print("\n" + "=" * 60)
    print("SECTION 7: RAG Best Practices")
    print("=" * 60)
    
    practices = """
    ✅ DOCUMENT PREPARATION:
    
    1. Clean your documents
       • Remove irrelevant content
       • Fix formatting issues
       • Standardize structure
    
    2. Choose appropriate chunk size
       • Too small: Loses context
       • Too large: Less precise retrieval
       • Sweet spot: 200-500 tokens
    
    3. Add metadata
       • Source, date, author
       • Helps with filtering
       • Improves traceability
    
    
    ✅ EMBEDDING STRATEGY:
    
    1. Use domain-specific models when possible
    2. Consistent embedding model for index and query
    3. Consider embedding costs at scale
    4. Cache embeddings for reuse
    
    
    ✅ RETRIEVAL:
    
    1. Tune top_k parameter
       • More context vs noise
       • Typical: 3-5 documents
    
    2. Implement hybrid search
       • Semantic (embeddings)
       • Keyword (BM25)
       • Combined scoring
    
    3. Use reranking
       • Initial retrieval: Fast, broad
       • Reranking: Slow, precise
       • Best of both worlds
    
    
    ✅ PROMPT ENGINEERING:
    
    1. Clear instructions
       "Answer based on context"
       "Cite sources when possible"
       "Say 'I don't know' if context insufficient"
    
    2. Format context clearly
       Separate context from question
       Number or bullet points
       Include source references
    
    3. Handle edge cases
       No relevant documents found
       Contradictory information
       Outdated information
    
    
    ✅ SYSTEM DESIGN:
    
    1. Caching
       • Cache embeddings
       • Cache common queries
       • Reduce API calls
    
    2. Error handling
       • Embedding failures
       • Search failures
       • Generation failures
       • Graceful degradation
    
    3. Monitoring
       • Query patterns
       • Retrieval quality
       • Response quality
       • User feedback
    
    4. Updating knowledge base
       • Regular updates
       • Version control
       • Incremental indexing
       • Remove outdated info
    
    
    ⚠️ COMMON PITFALLS:
    
    1. Context overflow
       • Too many retrieved docs
       • Exceeds token limit
       • Solution: Summarize or truncate
    
    2. Poor chunking
       • Breaks semantic meaning
       • Solution: Semantic-aware splitting
    
    3. Ignoring recency
       • Old information prioritized
       • Solution: Weight by date
    
    4. No source attribution
       • Can't verify claims
       • Solution: Include sources in response
    
    
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
    print("      GENERATIVE AI SESSION - MODULE 9: RAG (BASIC)")
    print("🎓 " + "=" * 58 + " 🎓")
    
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
    
    while True:
        print(menu)
        choice = input("Your choice: ").strip().lower()
        
        if choice in ['quit', 'q', 'exit']:
            print("👋 Goodbye!")
            break
        elif choice == '1':
            rag_concepts()
        elif choice == '2':
            document_chunking()
        elif choice == '3':
            creating_embeddings()
        elif choice == '4':
            similarity_search()
        elif choice == '5':
            basic_rag_pipeline()
        elif choice == '6':
            rag_comparison()
        elif choice == '7':
            rag_best_practices()
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
        else:
            print("⚠️  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
    # Teaching Questions:
    # 1. What problem does RAG solve?
    # 2. How does chunking affect retrieval quality?
    # 3. When would you use RAG vs fine-tuning?
