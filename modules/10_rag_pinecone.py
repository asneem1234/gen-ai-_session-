"""
10 - RAG with Pinecone Vector Database
========================================

This module demonstrates building production-ready RAG with Pinecone.
Students will learn:
- What vector databases are
- Setting up Pinecone
- Indexing documents at scale
- Efficient similarity search
- Production RAG patterns
- Metadata filtering
- Scaling considerations

Teaching Points:
- Vector databases enable efficient large-scale RAG
- Pinecone handles indexing and search infrastructure
- Essential for production applications
- Much more scalable than basic implementations
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai
from typing import List, Dict
import time

# Setup
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


# ============================================================================
# SECTION 1: Understanding Vector Databases
# ============================================================================

def vector_database_concepts():
    """
    Explain vector databases and why they're needed
    """
    print("\n" + "=" * 60)
    print("SECTION 1: Understanding Vector Databases")
    print("=" * 60)
    
    explanation = """
    🗄️ WHAT ARE VECTOR DATABASES?
    
    Traditional Database:
    • Stores structured data (rows, columns)
    • Searches by exact match or ranges
    • Example: Find users where age > 25
    
    Vector Database:
    • Stores high-dimensional vectors (embeddings)
    • Searches by similarity
    • Example: Find documents similar to query vector
    
    
    ❌ BASIC RAG LIMITATIONS:
    
    1. Scale Issues
       • Slow with 1000+ documents
       • All embeddings in memory
       • Linear search O(n)
    
    2. No Persistence
       • Recompute embeddings each run
       • No efficient updates
       • Can't handle millions of docs
    
    3. No Advanced Features
       • No metadata filtering
       • No hybrid search
       • No distributed architecture
    
    
    ✅ VECTOR DATABASE BENEFITS:
    
    1. Performance
       • Approximate Nearest Neighbor (ANN) search
       • Sub-millisecond queries
       • Scales to billions of vectors
    
    2. Persistence
       • Durable storage
       • Easy updates/deletes
       • Version control
    
    3. Advanced Features
       • Metadata filtering
       • Namespaces for organization
       • Real-time updates
       • Distributed architecture
    
    4. Production Ready
       • High availability
       • Monitoring & analytics
       • Security features
       • API access
    
    
    🏆 POPULAR VECTOR DATABASES:
    
    1. Pinecone 🌲
       • Fully managed (cloud)
       • Easy to use
       • Great performance
       • Free tier available
    
    2. Weaviate
       • Open source
       • Rich features
       • Self-hosted or cloud
    
    3. Qdrant
       • Rust-based
       • Fast
       • Open source
    
    4. Milvus
       • Open source
       • Enterprise features
       • Large scale
    
    5. Chroma
       • Embedded database
       • Great for development
       • Python-first
    
    
    🎯 WHEN TO USE VECTOR DATABASES:
    
    Use Vector DB when:
    • 1000+ documents
    • Production application
    • Need fast queries
    • Frequent updates
    • Multiple users
    
    Basic RAG sufficient for:
    • Small document sets
    • Prototyping
    • Learning
    • Single-user apps
    
    
    📊 PINECONE ARCHITECTURE:
    
    Your App → Pinecone API → Pinecone Index
                                  ↓
                              Vector Storage
                                  ↓
                            ANN Search Engine
                                  ↓
                            Returns Results
    
    Pinecone handles:
    • Storage
    • Indexing
    • Search optimization
    • Scaling
    • High availability
    """
    
    print(explanation)


# ============================================================================
# SECTION 2: Pinecone Setup
# ============================================================================

def pinecone_setup_guide():
    """
    Guide for setting up Pinecone
    """
    print("\n" + "=" * 60)
    print("SECTION 2: Pinecone Setup Guide")
    print("=" * 60)
    
    guide = """
    📝 SETUP STEPS:
    
    1. CREATE ACCOUNT
    ==================
    • Visit: https://www.pinecone.io/
    • Sign up for free tier
    • No credit card required for starter
    
    Free Tier Includes:
    • 1 index
    • 100K vectors (768 dims)
    • Good for learning & prototyping
    
    
    2. GET API KEY
    ==============
    • Dashboard → API Keys
    • Copy your API key
    • Copy your environment (e.g., "us-east-1-aws")
    
    
    3. INSTALL LIBRARY
    ==================
    pip install pinecone-client
    
    
    4. CONFIGURE ENVIRONMENT
    ========================
    Add to .env file:
    
    PINECONE_API_KEY=your_api_key_here
    PINECONE_ENVIRONMENT=your_environment_here
    
    
    5. VERIFY SETUP
    ===============
    Run the connection test in this module!
    
    
    💻 BASIC CODE STRUCTURE:
    
    from pinecone import Pinecone, ServerlessSpec
    
    # Initialize
    pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
    
    # Create index
    pc.create_index(
        name="my-index",
        dimension=768,  # Match your embedding size
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
    
    # Connect to index
    index = pc.Index("my-index")
    
    # Upsert vectors
    index.upsert(vectors=[
        ("id1", [0.1, 0.2, ...], {"text": "content"})
    ])
    
    # Query
    results = index.query(
        vector=[0.1, 0.2, ...],
        top_k=5,
        include_metadata=True
    )
    
    
    ⚙️ KEY CONCEPTS:
    
    • Index: Container for vectors
    • Dimension: Size of your embeddings
    • Metric: cosine, euclidean, or dotproduct
    • Namespace: Logical partition within index
    • Metadata: Additional info stored with vectors
    """
    
    print(guide)
    
    # Test connection
    print("\n\n🔌 CONNECTION TEST:")
    print("-" * 60)
    
    try:
        from pinecone import Pinecone
        
        api_key = os.getenv('PINECONE_API_KEY')
        
        if not api_key:
            print("❌ PINECONE_API_KEY not found in .env file")
            print("\n💡 To use this module:")
            print("   1. Sign up at pinecone.io")
            print("   2. Get your API key")
            print("   3. Add to .env file")
            return False
        
        # Initialize
        pc = Pinecone(api_key=api_key)
        
        # List indexes
        indexes = pc.list_indexes()
        
        print("✅ Connected successfully!")
        print(f"📊 Existing indexes: {len(indexes.indexes)}")
        
        for idx in indexes.indexes:
            print(f"   • {idx.name}")
        
        return True
        
    except ImportError:
        print("❌ Pinecone library not installed")
        print("   Run: pip install pinecone-client")
        return False
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False


# ============================================================================
# SECTION 3: Creating a Pinecone Index
# ============================================================================

def create_pinecone_index():
    """
    Create and configure a Pinecone index
    """
    print("\n" + "=" * 60)
    print("SECTION 3: Creating a Pinecone Index")
    print("=" * 60)
    
    try:
        from pinecone import Pinecone, ServerlessSpec
        
        api_key = os.getenv('PINECONE_API_KEY')
        
        if not api_key:
            print("⚠️  Pinecone API key not configured")
            print("   This section requires a Pinecone account")
            return
        
        pc = Pinecone(api_key=api_key)
        
        index_name = "rag-demo-index"
        
        print(f"\n📝 Creating index: {index_name}")
        print("-" * 60)
        
        # Check if index already exists
        existing_indexes = [idx.name for idx in pc.list_indexes().indexes]
        
        if index_name in existing_indexes:
            print(f"ℹ️  Index '{index_name}' already exists")
            print("   Deleting and recreating...")
            pc.delete_index(index_name)
            time.sleep(1)  # Wait for deletion
        
        # Create index
        print("\n⏳ Creating index...")
        print(f"   • Name: {index_name}")
        print(f"   • Dimension: 768 (Gemini embedding size)")
        print(f"   • Metric: cosine")
        print(f"   • Cloud: AWS")
        
        pc.create_index(
            name=index_name,
            dimension=768,  # Gemini embedding dimension
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
        
        print("\n✅ Index created successfully!")
        print("\n💡 Index configuration:")
        print("   • Serverless: Scales automatically")
        print("   • Cosine similarity: Best for text embeddings")
        print("   • Ready to use immediately")
        
        # Wait for index to be ready
        print("\n⏳ Waiting for index to be ready...")
        time.sleep(5)
        
        # Get index stats
        index = pc.Index(index_name)
        stats = index.describe_index_stats()
        
        print("\n📊 Index Stats:")
        print(f"   • Total vectors: {stats['total_vector_count']}")
        print(f"   • Dimension: {stats['dimension']}")
        
        return index_name
        
    except ImportError:
        print("❌ Pinecone library not installed")
        print("   Run: pip install pinecone-client")
    except Exception as e:
        print(f"❌ Error creating index: {e}")


# ============================================================================
# SECTION 4: Indexing Documents
# ============================================================================

def index_documents():
    """
    Index documents into Pinecone
    """
    print("\n" + "=" * 60)
    print("SECTION 4: Indexing Documents")
    print("=" * 60)
    
    try:
        from pinecone import Pinecone
        
        api_key = os.getenv('PINECONE_API_KEY')
        
        if not api_key:
            print("⚠️  Pinecone API key not configured")
            return
        
        pc = Pinecone(api_key=api_key)
        index_name = "rag-demo-index"
        
        # Check if index exists
        existing_indexes = [idx.name for idx in pc.list_indexes().indexes]
        
        if index_name not in existing_indexes:
            print(f"⚠️  Index '{index_name}' not found")
            print("   Run Section 3 to create it first")
            return
        
        index = pc.Index(index_name)
        
        # Sample documents
        documents = [
            {"id": "doc1", "text": "Python is a high-level programming language created by Guido van Rossum.", "category": "intro"},
            {"id": "doc2", "text": "Python emphasizes code readability with significant indentation.", "category": "syntax"},
            {"id": "doc3", "text": "Django is a popular web framework for Python.", "category": "frameworks"},
            {"id": "doc4", "text": "Flask is a lightweight web framework for Python.", "category": "frameworks"},
            {"id": "doc5", "text": "NumPy provides support for large multi-dimensional arrays.", "category": "data-science"},
            {"id": "doc6", "text": "Pandas is used for data manipulation and analysis.", "category": "data-science"},
            {"id": "doc7", "text": "Scikit-learn is a machine learning library for Python.", "category": "ml"},
            {"id": "doc8", "text": "TensorFlow and PyTorch are deep learning frameworks.", "category": "ml"},
            {"id": "doc9", "text": "Python has a large standard library included by default.", "category": "features"},
            {"id": "doc10", "text": "Python supports multiple programming paradigms.", "category": "features"}
        ]
        
        print(f"\n📚 Indexing {len(documents)} documents...")
        print("-" * 60)
        
        # Generate embeddings and prepare for upsert
        vectors_to_upsert = []
        
        for doc in documents:
            print(f"   Processing: {doc['id']}")
            
            # Generate embedding
            result = genai.embed_content(
                model="models/embedding-001",
                content=doc['text'],
                task_type="retrieval_document"
            )
            embedding = result['embedding']
            
            # Prepare vector with metadata
            vectors_to_upsert.append({
                "id": doc['id'],
                "values": embedding,
                "metadata": {
                    "text": doc['text'],
                    "category": doc['category']
                }
            })
        
        # Upsert to Pinecone
        print("\n⏳ Uploading to Pinecone...")
        index.upsert(vectors=vectors_to_upsert)
        
        print("✅ Upload complete!")
        
        # Wait for indexing
        time.sleep(2)
        
        # Get stats
        stats = index.describe_index_stats()
        print(f"\n📊 Index now contains {stats['total_vector_count']} vectors")
        
        return True
        
    except ImportError:
        print("❌ Pinecone library not installed")
    except Exception as e:
        print(f"❌ Error indexing documents: {e}")
        return False


# ============================================================================
# SECTION 5: Querying Pinecone
# ============================================================================

def query_pinecone():
    """
    Search the Pinecone index
    """
    print("\n" + "=" * 60)
    print("SECTION 5: Querying Pinecone")
    print("=" * 60)
    
    try:
        from pinecone import Pinecone
        
        api_key = os.getenv('PINECONE_API_KEY')
        
        if not api_key:
            print("⚠️  Pinecone API key not configured")
            return
        
        pc = Pinecone(api_key=api_key)
        index = pc.Index("rag-demo-index")
        
        # Test queries
        queries = [
            "Who created Python?",
            "What frameworks can I use for web development?",
            "Tell me about data science libraries"
        ]
        
        for query in queries:
            print(f"\n{'='*60}")
            print(f"🔍 Query: '{query}'")
            print(f"{'='*60}")
            
            # Generate query embedding
            query_result = genai.embed_content(
                model="models/embedding-001",
                content=query,
                task_type="retrieval_query"
            )
            query_embedding = query_result['embedding']
            
            # Search Pinecone
            print("\n⏳ Searching Pinecone...")
            
            results = index.query(
                vector=query_embedding,
                top_k=3,
                include_metadata=True
            )
            
            # Display results
            print(f"\n✅ Found {len(results['matches'])} matches:\n")
            
            for i, match in enumerate(results['matches'], 1):
                score = match['score']
                text = match['metadata']['text']
                category = match['metadata']['category']
                
                print(f"{i}. [Score: {score:.4f}] [Category: {category}]")
                print(f"   {text}\n")
        
    except ImportError:
        print("❌ Pinecone library not installed")
    except Exception as e:
        print(f"❌ Error querying: {e}")


# ============================================================================
# SECTION 6: Complete RAG with Pinecone
# ============================================================================

def complete_rag_pinecone():
    """
    Full RAG pipeline using Pinecone
    """
    print("\n" + "=" * 60)
    print("SECTION 6: Complete RAG Pipeline with Pinecone")
    print("=" * 60)
    
    try:
        from pinecone import Pinecone
        
        api_key = os.getenv('PINECONE_API_KEY')
        
        if not api_key:
            print("⚠️  Pinecone API key not configured")
            return
        
        pc = Pinecone(api_key=api_key)
        index = pc.Index("rag-demo-index")
        model = genai.GenerativeModel('gemini-pro')
        
        def rag_with_pinecone(question: str, top_k: int = 3):
            """Complete RAG pipeline with Pinecone"""
            
            print(f"\n{'='*60}")
            print(f"❓ Question: {question}")
            print(f"{'='*60}")
            
            # Step 1: Generate query embedding
            print("\n1️⃣ Generating query embedding...")
            query_result = genai.embed_content(
                model="models/embedding-001",
                content=question,
                task_type="retrieval_query"
            )
            query_embedding = query_result['embedding']
            print("   ✅ Embedding generated")
            
            # Step 2: Search Pinecone
            print("\n2️⃣ Searching Pinecone index...")
            results = index.query(
                vector=query_embedding,
                top_k=top_k,
                include_metadata=True
            )
            print(f"   ✅ Found {len(results['matches'])} matches")
            
            # Step 3: Extract context
            print("\n3️⃣ Building context from results...")
            contexts = []
            for match in results['matches']:
                text = match['metadata']['text']
                score = match['score']
                contexts.append(f"[Relevance: {score:.2f}] {text}")
            
            context = "\n".join(contexts)
            print(f"   ✅ Context prepared ({len(contexts)} documents)")
            
            # Step 4: Generate response
            print("\n4️⃣ Generating AI response...")
            
            prompt = f"""Based on the following context, answer the question.

Context:
{context}

Question: {question}

Answer: Provide a clear answer based on the context. Cite relevant information."""
            
            response = model.generate_content(prompt)
            print("   ✅ Response generated")
            
            # Display results
            print(f"\n{'='*60}")
            print("📄 RETRIEVED CONTEXT:")
            print(f"{'='*60}")
            for i, ctx in enumerate(contexts, 1):
                print(f"\n{i}. {ctx}")
            
            print(f"\n{'='*60}")
            print("🤖 AI RESPONSE:")
            print(f"{'='*60}")
            print(response.text)
            print()
            
            return response.text
        
        # Test questions
        test_questions = [
            "What is Python known for?",
            "Which Python frameworks should I use for web development?",
            "What libraries are available for machine learning?"
        ]
        
        for question in test_questions:
            rag_with_pinecone(question)
            time.sleep(1)  # Brief pause between queries
        
    except ImportError:
        print("❌ Pinecone library not installed")
    except Exception as e:
        print(f"❌ Error in RAG pipeline: {e}")


# ============================================================================
# SECTION 7: Metadata Filtering
# ============================================================================

def metadata_filtering():
    """
    Demonstrate metadata filtering in Pinecone
    """
    print("\n" + "=" * 60)
    print("SECTION 7: Metadata Filtering")
    print("=" * 60)
    
    print("""
    🏷️ METADATA FILTERING:
    
    Pinecone allows filtering by metadata BEFORE similarity search.
    This enables:
    • Search within specific categories
    • Filter by date, author, source
    • Permissions-based access
    • Multi-tenant applications
    
    Example filters:
    • {"category": "data-science"}
    • {"date": {"$gte": "2023-01-01"}}
    • {"author": "John Doe"}
    """)
    
    try:
        from pinecone import Pinecone
        
        api_key = os.getenv('PINECONE_API_KEY')
        
        if not api_key:
            print("\n⚠️  Pinecone API key not configured")
            return
        
        pc = Pinecone(api_key=api_key)
        index = pc.Index("rag-demo-index")
        
        query = "Tell me about Python"
        
        # Generate query embedding
        query_result = genai.embed_content(
            model="models/embedding-001",
            content=query,
            task_type="retrieval_query"
        )
        query_embedding = query_result['embedding']
        
        # Test different filters
        filters = [
            (None, "No filter (all categories)"),
            ({"category": "frameworks"}, "Only 'frameworks'"),
            ({"category": "data-science"}, "Only 'data-science'")
        ]
        
        for filter_dict, description in filters:
            print(f"\n{'='*60}")
            print(f"🔍 {description}")
            print(f"{'='*60}")
            
            results = index.query(
                vector=query_embedding,
                top_k=3,
                include_metadata=True,
                filter=filter_dict
            )
            
            print(f"\nFound {len(results['matches'])} results:\n")
            
            for i, match in enumerate(results['matches'], 1):
                text = match['metadata']['text']
                category = match['metadata']['category']
                score = match['score']
                
                print(f"{i}. [{category}] (score: {score:.4f})")
                print(f"   {text}\n")
        
    except ImportError:
        print("❌ Pinecone library not installed")
    except Exception as e:
        print(f"❌ Error: {e}")


# ============================================================================
# SECTION 8: Production Best Practices
# ============================================================================

def production_best_practices():
    """
    Best practices for production RAG with Pinecone
    """
    print("\n" + "=" * 60)
    print("SECTION 8: Production Best Practices")
    print("=" * 60)
    
    practices = """
    ✅ INDEXING STRATEGY:
    
    1. Batch Operations
       • Upsert in batches (100-1000 vectors)
       • Parallel processing for speed
       • Use async operations when possible
    
    2. Metadata Design
       • Keep metadata small
       • Index frequently filtered fields
       • Include source information
       • Add timestamps
    
    3. ID Management
       • Use meaningful, unique IDs
       • Include source in ID (e.g., "doc1_chunk3")
       • Enable easy updates/deletes
    
    
    ✅ SEARCH OPTIMIZATION:
    
    1. Top-K Selection
       • Start with 3-5
       • Increase if needed
       • Balance relevance vs cost
    
    2. Reranking
       • Retrieve more (e.g., 20)
       • Rerank to get best 3-5
       • Improves precision
    
    3. Caching
       • Cache common queries
       • Cache embeddings
       • Use CDN for static content
    
    
    ✅ SCALING:
    
    1. Index Organization
       • Use namespaces for logical separation
       • Separate indexes for different domains
       • Consider multi-index architecture
    
    2. Performance Monitoring
       • Track query latency
       • Monitor index size
       • Watch API usage
       • Set up alerts
    
    3. Cost Management
       • Right-size your plan
       • Monitor vector counts
       • Delete unused data
       • Use serverless efficiently
    
    
    ✅ RELIABILITY:
    
    1. Error Handling
       • Retry logic with backoff
       • Handle API errors gracefully
       • Fallback strategies
       • Circuit breakers
    
    2. Testing
       • Unit tests for components
       • Integration tests
       • Load testing
       • Relevance evaluation
    
    3. Monitoring
       • Query success rate
       • Retrieval quality
       • Response times
       • User satisfaction
    
    
    ✅ SECURITY:
    
    1. Access Control
       • Use API keys properly
       • Rotate keys regularly
       • Implement authentication
       • Use namespaces for isolation
    
    2. Data Privacy
       • Encrypt sensitive data
       • PII handling
       • Compliance (GDPR, etc.)
       • Data retention policies
    
    3. Rate Limiting
       • Implement request limits
       • Prevent abuse
       • Fair usage policies
    
    
    💡 EXAMPLE PRODUCTION ARCHITECTURE:
    
    User Request
        ↓
    API Gateway (auth, rate limiting)
        ↓
    Application Server
        ↓
    ├─→ Cache Layer (Redis)
    ├─→ Embedding Service
    │       ↓
    └─→ Pinecone Index
        ↓
    LLM Service (Gemini)
        ↓
    Response
        ↓
    Logging & Monitoring
    
    
    📊 METRICS TO TRACK:
    
    • Query latency (p50, p95, p99)
    • Retrieval precision @ k
    • Answer quality scores
    • Cache hit rate
    • API costs
    • Error rates
    • User satisfaction (feedback)
    
    
    🔧 MAINTENANCE:
    
    1. Regular Updates
       • Add new documents
       • Remove outdated content
       • Update embeddings if model changes
    
    2. Performance Tuning
       • Optimize chunk sizes
       • Adjust top-k
       • Refine metadata
       • A/B test changes
    
    3. Documentation
       • Index schema
       • Metadata fields
       • Query patterns
       • Runbooks for issues
    """
    
    print(practices)


# ============================================================================
# SECTION 9: Cleanup
# ============================================================================

def cleanup_demo():
    """
    Clean up demo resources
    """
    print("\n" + "=" * 60)
    print("SECTION 9: Cleanup")
    print("=" * 60)
    
    try:
        from pinecone import Pinecone
        
        api_key = os.getenv('PINECONE_API_KEY')
        
        if not api_key:
            print("⚠️  Pinecone API key not configured")
            return
        
        pc = Pinecone(api_key=api_key)
        index_name = "rag-demo-index"
        
        choice = input(f"\n⚠️  Delete index '{index_name}'? (yes/no): ").strip().lower()
        
        if choice == 'yes':
            print("\n⏳ Deleting index...")
            pc.delete_index(index_name)
            print("✅ Index deleted successfully!")
            print("\n💡 You can recreate it anytime by running the setup sections")
        else:
            print("\n✅ Index preserved")
            print("\n💡 To manually delete later:")
            print(f"   pc.delete_index('{index_name}')")
        
    except ImportError:
        print("❌ Pinecone library not installed")
    except Exception as e:
        print(f"❌ Error: {e}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main function with menu
    """
    print("\n")
    print("🎓 " + "=" * 58 + " 🎓")
    print("    GENERATIVE AI SESSION - MODULE 10: RAG WITH PINECONE")
    print("🎓 " + "=" * 58 + " 🎓")
    
    menu = """
    Choose a section to run:
    
    1. Understanding Vector Databases
    2. Pinecone Setup Guide
    3. Create Pinecone Index
    4. Index Documents
    5. Query Pinecone
    6. Complete RAG Pipeline
    7. Metadata Filtering
    8. Production Best Practices
    9. Cleanup (Delete Demo Index)
    
    setup - Run setup (sections 2-4)
    demo - Run demo (sections 5-7)
    all - Run all (except cleanup)
    quit - Exit
    
    """
    
    while True:
        print(menu)
        choice = input("Your choice: ").strip().lower()
        
        if choice in ['quit', 'q', 'exit']:
            print("👋 Goodbye!")
            break
        elif choice == '1':
            vector_database_concepts()
        elif choice == '2':
            pinecone_setup_guide()
        elif choice == '3':
            create_pinecone_index()
        elif choice == '4':
            index_documents()
        elif choice == '5':
            query_pinecone()
        elif choice == '6':
            complete_rag_pinecone()
        elif choice == '7':
            metadata_filtering()
        elif choice == '8':
            production_best_practices()
        elif choice == '9':
            cleanup_demo()
        elif choice == 'setup':
            print("\n🔧 Running setup sequence...")
            if pinecone_setup_guide():
                create_pinecone_index()
                index_documents()
            print("\n✅ Setup complete!")
        elif choice == 'demo':
            print("\n🎬 Running demo sequence...")
            query_pinecone()
            complete_rag_pinecone()
            metadata_filtering()
            print("\n✅ Demo complete!")
        elif choice == 'all':
            vector_database_concepts()
            if pinecone_setup_guide():
                create_pinecone_index()
                index_documents()
                query_pinecone()
                complete_rag_pinecone()
                metadata_filtering()
            production_best_practices()
            print("\n✅ All sections completed!")
            break
        else:
            print("⚠️  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
    # Teaching Questions:
    # 1. Why use a vector database vs in-memory search?
    # 2. How does metadata filtering improve RAG?
    # 3. What are key considerations for production RAG?
