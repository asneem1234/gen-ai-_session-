import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

class SimpleVectorDB:
    def __init__(self):
        self.documents = []
        self.embeddings = []
    
    def add_document(self, doc_id, text):
        self.documents.append({"id": doc_id, "text": text})
        print(f"Added document: {doc_id}")
    
    def search(self, query, top_k=3):
        print(f"Searching for: {query}")
        return self.documents[:top_k]

def create_vector_store():
    db = SimpleVectorDB()
    
    documents = {
        "doc1": "Python is a versatile programming language used for web development, data science, and automation.",
        "doc2": "Machine learning algorithms can learn patterns from data to make predictions.",
        "doc3": "Neural networks consist of layers of interconnected nodes that process information.",
        "doc4": "Deep learning models require large amounts of data and computational power.",
        "doc5": "Natural language processing enables computers to understand human language."
    }
    
    for doc_id, text in documents.items():
        db.add_document(doc_id, text)
    
    return db

def rag_with_vector_db(query, vector_db):
    results = vector_db.search(query, top_k=2)
    
    context = "\n".join([doc["text"] for doc in results])
    
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = f"""Use the following context to answer the question.

Context:
{context}

Question: {query}

Answer:"""
    
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("Creating Vector Store...")
    db = create_vector_store()
    
    queries = [
        "What is Python used for?",
        "How do neural networks work?",
        "What is machine learning?"
    ]
    
    print("\n" + "="*60)
    print("RAG with Vector Database")
    print("="*60)
    
    for query in queries:
        print(f"\nQuery: {query}")
        answer = rag_with_vector_db(query, db)
        print(f"Answer: {answer}")
        print("-"*60)
