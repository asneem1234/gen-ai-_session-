import os
from dotenv import load_dotenv
import google.generativeai as genai
import numpy as np

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def create_knowledge_base():
    return {
        "Python Basics": "Python is a high-level programming language known for its simplicity and readability.",
        "Machine Learning": "ML is a subset of AI that enables systems to learn from data without explicit programming.",
        "Neural Networks": "Neural networks are computing systems inspired by biological neural networks in animal brains.",
        "Deep Learning": "Deep learning uses neural networks with multiple layers to learn from large amounts of data."
    }

def simple_embedding(text):
    return np.random.rand(10)

def find_similar(query, knowledge_base):
    query_emb = simple_embedding(query)
    
    similarities = {}
    for topic, content in knowledge_base.items():
        content_emb = simple_embedding(content)
        similarity = np.dot(query_emb, content_emb)
        similarities[topic] = similarity
    
    best_topic = max(similarities, key=similarities.get)
    return knowledge_base[best_topic]

def rag_query(query, knowledge_base):
    relevant_context = find_similar(query, knowledge_base)
    
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = f"""Context: {relevant_context}

Question: {query}

Answer based on the context provided:"""
    
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    kb = create_knowledge_base()
    
    print("Knowledge Base:")
    for topic in kb.keys():
        print(f"  - {topic}")
    
    queries = [
        "What is Python?",
        "Tell me about machine learning",
        "How do neural networks work?"
    ]
    
    print("\nRAG Queries:")
    for query in queries:
        print(f"\nQ: {query}")
        answer = rag_query(query, kb)
        print(f"A: {answer}")
