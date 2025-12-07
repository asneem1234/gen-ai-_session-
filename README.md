# Generative AI Coding Session - Complete Guide

## 🎯 Session Overview
This comprehensive coding session covers practical implementations of generative AI concepts using Google's Gemini API. Students will learn hands-on coding techniques for building AI-powered applications.

## 📋 Prerequisites
- **Theory Knowledge**: Students should understand basic AI/ML concepts, LLMs, embeddings, and vector databases
- **Python Knowledge**: Intermediate level (functions, classes, async/await)
- **Tools Required**:
  - Python 3.9+
  - Google API Key (Gemini API)
  - Pinecone API Key (for advanced RAG section)
  - Code editor (VS Code recommended)

## 🚀 Setup Instructions

### 1. Clone/Download Repository
```bash
cd d:\gen-ai-_session-
```

### 2. Create Virtual Environment
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy the example environment file
copy .env.example .env

# Edit .env and add your API keys:
# GOOGLE_API_KEY=your_gemini_api_key_here
# PINECONE_API_KEY=your_pinecone_api_key_here
# PINECONE_ENVIRONMENT=your_pinecone_environment
```

## 📚 Session Structure (3-4 Hours)

### Part 1: Foundation (45 min)
1. **Model Preparation** (`01_model_preparation.py`)
   - Setting up Gemini API
   - Understanding model initialization
   - Basic configuration
   - Testing connectivity

2. **Text Chat** (`02_text_chat.py`)
   - Simple text generation
   - Question-answering
   - Different prompting techniques

### Part 2: Multimodal AI (45 min)
3. **Image Chat** (`03_image_chat.py`)
   - Image understanding
   - Visual question answering
   - Multiple image analysis

4. **Video Chat** (`04_video_chat.py`)
   - Video frame extraction
   - Temporal understanding
   - Video description generation

### Part 3: Advanced Generation (45 min)
5. **Streaming Concepts** (`05_streaming.py`)
   - Real-time response streaming
   - Token-by-token generation
   - User experience improvements

6. **Text Generation with Memory** (`06_memory_conversation.py`)
   - Conversation history management
   - Context window management
   - Building chatbot memory

### Part 4: Fine-Tuning Generation (45 min)
7. **Model Configurations** (`07_model_configurations.py`)
   - Temperature control
   - Top-P (nucleus sampling)
   - Top-K sampling
   - Max tokens
   - Stop sequences

8. **System Instructions** (`08_system_instructions.py`)
   - Setting AI behavior
   - Role-based prompting
   - Custom personality creation

### Part 5: RAG Systems (45-60 min)
9. **Basic RAG** (`09_rag_basic.py`)
   - Document chunking
   - Embedding generation
   - Similarity search
   - Context injection

10. **RAG with Pinecone** (`10_rag_pinecone.py`) ⭐
    - Vector database setup
    - Efficient storage and retrieval
    - Production-ready RAG
    - Scaling considerations

## 🎓 Learning Objectives

By the end of this session, students will be able to:
- ✅ Set up and configure Gemini API for various use cases
- ✅ Build text-based AI applications with proper error handling
- ✅ Implement multimodal AI features (text, image, video)
- ✅ Create streaming responses for better UX
- ✅ Manage conversation memory and context
- ✅ Fine-tune model behavior with generation parameters
- ✅ Design effective system instructions
- ✅ Build RAG systems with document retrieval
- ✅ Integrate vector databases for production applications

## 📁 Project Structure
```
gen-ai-_session-/
├── README.md                          # This file
├── TEACHING_NOTES.md                  # Instructor guide
├── requirements.txt                   # Python dependencies
├── .env.example                       # Environment template
├── .env                              # Your API keys (not in git)
├── 01_model_preparation.py           # Setup and initialization
├── 02_text_chat.py                   # Basic text generation
├── 03_image_chat.py                  # Image understanding
├── 04_video_chat.py                  # Video processing
├── 05_streaming.py                   # Streaming responses
├── 06_memory_conversation.py         # Chat history management
├── 07_model_configurations.py        # Generation parameters
├── 08_system_instructions.py         # System prompts
├── 09_rag_basic.py                   # RAG implementation
├── 10_rag_pinecone.py               # Advanced RAG with Pinecone
├── data/                             # Sample data files
│   ├── sample_image.jpg
│   ├── sample_video.mp4
│   └── documents/                    # Sample documents for RAG
└── outputs/                          # Generated outputs
```

## 🎯 Running the Examples

Each Python file is standalone and can be run independently:

```bash
# Activate virtual environment first
.\venv\Scripts\Activate.ps1

# Run individual examples
python 01_model_preparation.py
python 02_text_chat.py
python 03_image_chat.py
# ... and so on
```

## 💡 Teaching Tips

1. **Start Simple**: Begin with basic text chat before moving to complex topics
2. **Live Coding**: Type out examples rather than copy-paste to explain each line
3. **Interactive**: Ask students to suggest prompts and parameters to test
4. **Error Handling**: Intentionally show common errors and how to fix them
5. **Real Examples**: Use relatable scenarios (customer service bot, study assistant, etc.)
6. **Pause Often**: Check understanding before moving to next topic

## 🔗 Resources

- [Gemini API Documentation](https://ai.google.dev/docs)
- [Pinecone Documentation](https://docs.pinecone.io/)
- [Python Google Generative AI SDK](https://github.com/google/generative-ai-python)

## 🆘 Common Issues & Solutions

### Issue: API Key Not Working
```python
# Solution: Check .env file and ensure key is loaded correctly
from dotenv import load_dotenv
load_dotenv()
print(os.getenv('GOOGLE_API_KEY'))  # Should not be None
```

### Issue: Rate Limiting
```python
# Solution: Add delays between requests
import time
time.sleep(1)  # Wait 1 second between API calls
```

### Issue: Memory/Context Too Large
```python
# Solution: Truncate history or summarize old messages
max_history = 10  # Keep only last 10 messages
conversation_history = conversation_history[-max_history:]
```

## 📝 Assessment Ideas

1. **Mini Project**: Build a study assistant chatbot with memory
2. **Challenge**: Create a document Q&A system using RAG
3. **Experiment**: Compare different temperature settings for creative writing
4. **Build**: Multimodal app that can analyze images and answer questions

## 🎉 Next Steps

After this session, students should explore:
- Fine-tuning models with custom data
- Building full-stack applications with React/Flask
- Deploying AI apps to cloud platforms
- Exploring other LLM providers (OpenAI, Anthropic, etc.)
- Advanced RAG techniques (hybrid search, reranking)

---

**Good luck with your session! 🚀**

For questions or issues, refer to TEACHING_NOTES.md for detailed instructor guidance.
