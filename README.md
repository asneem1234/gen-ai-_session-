# 🚀 Generative AI Learning Guide - From Zero to Production

> A complete, hands-on guide to building AI applications with Google's Gemini API

## 📖 What You'll Find Here

This repository contains **10 progressive lessons** teaching you how to build real-world AI applications. Each lesson includes:
- ✅ **Python scripts** (`simple_versions/`) - Clean, runnable code
- ✅ **Google Colab notebooks** (`google_colab_versions/`) - Interactive learning
- ✅ **Detailed explanations** (`doc/`) - Deep-dive documentation

## 🎯 Who Is This For?

- **Beginners**: Start with lesson 1, follow the progression
- **Intermediate**: Jump to specific topics you need
- **Experienced**: Use as reference or teaching material
- **Instructors**: Use the teaching plans in `plan/` folder

## 🚀 Quick Start (3 Simple Steps)

### Option 1: Run in Google Colab (Easiest - No Setup!)
1. Get a free [Google API key](https://aistudio.google.com/app/apikey)
2. Open any notebook in `google_colab_versions/`
3. Upload to Google Colab and run!

### Option 2: Run Locally
1. **Get API Key**: [Get your free Gemini API key](https://aistudio.google.com/app/apikey)
2. **Install Dependencies**:
   ```bash
   pip install google-generativeai python-dotenv pillow numpy
   ```
3. **Set API Key**:
   ```bash
   # Windows PowerShell
   $env:GOOGLE_API_KEY="your_api_key_here"
   
   # Or create .env file with:
   # GOOGLE_API_KEY=your_api_key_here
   ```
4. **Run Any Lesson**:
   ```bash
   python simple_versions/01_model_preparation.py
   ```

## 📚 Learning Path (10 Lessons)

### 🟢 **Beginner Level** (Start Here!)

#### Lesson 1: Model Preparation
- 📂 `simple_versions/01_model_preparation.py`
- 📓 `google_colab_versions/01_model_preparation.ipynb`
- 📖 `doc/01_model_preparation_explained.md`
- **What you'll learn**: API setup, basic configuration, first AI interaction
- **Time**: 15 minutes

#### Lesson 2: Text Chat
- 📂 `simple_versions/02_text_chat.py`
- 📓 `google_colab_versions/02_text_chat.ipynb`
- 📖 `doc/02_text_chat_explained.md`
- **What you'll learn**: Asking questions, getting answers, prompt engineering basics
- **Time**: 20 minutes

#### Lesson 3: Image Chat
- 📂 `simple_versions/03_image_chat.py`
- 📓 `google_colab_versions/03_image_chat.ipynb`
- 📖 `doc/03_image_chat_explained.md`
- **What you'll learn**: Visual understanding, image Q&A, multi-image analysis
- **Time**: 25 minutes

#### Lesson 4: Video Chat
- 📂 `simple_versions/04_video_chat.py`
- 📓 `google_colab_versions/04_video_chat.ipynb`
- 📖 `doc/04_video_chat_explained.md`
- **What you'll learn**: Video frame analysis, temporal understanding, motion tracking
- **Time**: 25 minutes

### 🟡 **Intermediate Level**

#### Lesson 5: Streaming
- 📂 `simple_versions/05_streaming.py`
- 📓 `google_colab_versions/05_streaming.ipynb`
- 📖 `doc/05_streaming_explained.md`
- **What you'll learn**: Real-time responses, better UX, performance optimization
- **Time**: 20 minutes

#### Lesson 6: Memory & Conversation
- 📂 `simple_versions/06_memory_conversation.py`
- 📓 `google_colab_versions/06_memory_conversation.ipynb`
- 📖 `doc/06_memory_conversation_explained.md`
- **What you'll learn**: Chat history, context management, building chatbots
- **Time**: 30 minutes

#### Lesson 7: Model Configurations
- 📂 `simple_versions/07_model_configurations.py`
- 📓 `google_colab_versions/07_model_configurations.ipynb`
- 📖 `doc/07_model_configurations_explained.md`
- **What you'll learn**: Temperature, top_p, top_k, controlling creativity vs accuracy
- **Time**: 25 minutes

### 🔴 **Advanced Level**

#### Lesson 8: System Instructions
- 📂 `simple_versions/08_system_instructions.py`
- 📓 `google_colab_versions/08_system_instructions.ipynb`
- 📖 `doc/08_system_instructions_explained.md`
- **What you'll learn**: AI personas, role-based assistants, behavior control
- **Time**: 25 minutes

#### Lesson 9: RAG Basic
- 📂 `simple_versions/09_rag_basic.py`
- 📓 `google_colab_versions/09_rag_basic.ipynb`
- 📖 `doc/09_rag_basic_explained.md`
- **What you'll learn**: Document retrieval, embeddings, similarity search, context injection
- **Time**: 35 minutes

#### Lesson 10: RAG with Pinecone ⭐
- 📂 `simple_versions/10_rag_pinecone.py`
- 📓 `google_colab_versions/10_rag_pinecone.ipynb`
- 📖 `doc/10_rag_pinecone_explained.md`
- **What you'll learn**: Vector databases, production RAG, scaling, metadata filtering
- **Time**: 40 minutes
- **Note**: Optional Pinecone API key for full features

## 📁 Repository Structure

```
gen-ai-_session-/
├── 📄 README.md                    # You are here! Start here
├── 📄 QUICKSTART.md                # 5-minute getting started guide
├── 📄 requirements.txt             # All dependencies
│
├── 📂 simple_versions/             # Clean Python scripts (run directly)
│   ├── 01_model_preparation.py
│   ├── 02_text_chat.py
│   ├── 03_image_chat.py
│   ├── 04_video_chat.py
│   ├── 05_streaming.py
│   ├── 06_memory_conversation.py
│   ├── 07_model_configurations.py
│   ├── 08_system_instructions.py
│   ├── 09_rag_basic.py
│   └── 10_rag_pinecone.py
│
├── 📂 google_colab_versions/       # Interactive Jupyter notebooks
│   ├── 01_model_preparation.ipynb
│   ├── 02_text_chat.ipynb
│   ├── 03_image_chat.ipynb
│   ├── 04_video_chat.ipynb
│   ├── 05_streaming.ipynb
│   ├── 06_memory_conversation.ipynb
│   ├── 07_model_configurations.ipynb
│   ├── 08_system_instructions.ipynb
│   ├── 09_rag_basic.ipynb
│   └── 10_rag_pinecone.ipynb
│
├── 📂 doc/                         # Detailed explanations
│   ├── 01_model_preparation_explained.md
│   ├── 02_text_chat_explained.md
│   ├── 03_image_chat_explained.md
│   ├── 04_video_chat_explained.md
│   ├── 05_streaming_explained.md
│   ├── 06_memory_conversation_explained.md
│   ├── 07_model_configurations_explained.md
│   ├── 08_system_instructions_explained.md
│   ├── 09_rag_basic_explained.md
│   └── 10_rag_pinecone_explained.md
│
└── 📂 plan/                        # For instructors/teachers
    ├── TEACHING_NOTES.md
    └── TEACHING_PLAN_2HR.md
```

## 🎯 How to Use This Repository

### For Self-Learners:
1. **Start with lesson 1** (`simple_versions/01_model_preparation.py`)
2. **Read the explanation** (`doc/01_model_preparation_explained.md`)
3. **Try the interactive notebook** (`google_colab_versions/01_model_preparation.ipynb`)
4. **Move to lesson 2** and repeat

### For Instructors:
1. Review `plan/TEACHING_PLAN_2HR.md` for session structure
2. Check `plan/TEACHING_NOTES.md` for tips and gotchas
3. Use Google Colab notebooks for live demonstrations
4. Students follow along with simple_versions scripts

### For Quick Reference:
- Jump to any lesson directly
- All scripts are standalone and runnable
- Use `doc/` folder for detailed explanations

## 💡 Learning Approaches

### 🎓 **Structured Path** (Recommended for beginners)
Follow lessons 1 → 10 in order. Each builds on previous concepts.
- **Estimated time**: 4-5 hours total
- **Best for**: Complete beginners, systematic learners

### ⚡ **Topic-Based** (For intermediate users)
Jump to topics you need:
- Need chatbot? → Lessons 2, 6, 8
- Need image AI? → Lessons 3
- Need RAG? → Lessons 9, 10
- Need performance? → Lessons 5, 7

### 🔬 **Experimental** (For advanced users)
- Use notebooks in `google_colab_versions/`
- Modify code, test parameters
- Build your own projects
- Use `simple_versions/` as templates

## 🎓 What You'll Learn

After completing all lessons:

### Core Skills:
- ✅ Set up and use Google Gemini API
- ✅ Build text-based AI applications
- ✅ Process images and videos with AI
- ✅ Create streaming, real-time responses
- ✅ Manage conversation history and context
- ✅ Control AI behavior and creativity
- ✅ Design custom AI personas

### Advanced Skills:
- ✅ Build RAG (Retrieval-Augmented Generation) systems
- ✅ Use vector databases for semantic search
- ✅ Create production-ready AI applications
- ✅ Optimize for performance and cost
- ✅ Handle errors and edge cases

### Real-World Projects You Can Build:
- 🤖 Chatbots with memory
- 📚 Document Q&A systems
- 🖼️ Image analysis tools
- 🎥 Video understanding apps
- 📊 Data extraction from documents
- 💬 Customer support automation
- 📝 Content generation tools

## 🔗 Essential Resources

### Getting Started:
- 🔑 [Get Free Gemini API Key](https://aistudio.google.com/app/apikey)
- 📖 [Official Gemini API Docs](https://ai.google.dev/docs)
- 🐍 [Python SDK Reference](https://github.com/google/generative-ai-python)

### Advanced Topics:
- 🗄️ [Pinecone Vector Database](https://docs.pinecone.io/) (for lesson 10)
- 📚 [RAG Best Practices](https://ai.google.dev/docs/retrieval_augmented_generation)
- 🧠 [Prompt Engineering Guide](https://ai.google.dev/docs/prompt_best_practices)

### Community:
- 💬 [Google AI Discord](https://discord.gg/google-ai)
- 🐦 Follow [@GoogleDevs](https://twitter.com/googledevs)
- 📺 [Google AI YouTube](https://www.youtube.com/@GoogleDevelopers)

## 🆘 Troubleshooting

### ❌ "API key not found"
```python
# Solution 1: Set environment variable
import os
os.environ['GOOGLE_API_KEY'] = 'your_key_here'

# Solution 2: Create .env file
# Add: GOOGLE_API_KEY=your_key_here
```

### ❌ "Rate limit exceeded"
```python
# Solution: Add delays between requests
import time
time.sleep(1)  # Wait 1 second
```

### ❌ "Module not found"
```bash
# Solution: Install dependencies
pip install google-generativeai python-dotenv pillow numpy
```

### ❌ "Context too long"
```python
# Solution: Reduce conversation history
history = history[-10:]  # Keep last 10 messages
```

### ❌ "Notebook won't run in Colab"
- Make sure you set your API key in the notebook
- Use the "Google Colab Secrets" method for security
- Restart runtime if needed

## 📱 Quick Command Reference

```bash
# Install everything
pip install -r requirements.txt

# Run any lesson
python simple_versions/01_model_preparation.py

# Check your setup
python simple_versions/01_model_preparation.py

# Install just core dependencies
pip install google-generativeai python-dotenv

# For image lessons
pip install pillow

# For RAG lessons
pip install numpy sentence-transformers

# For Pinecone (lesson 10)
pip install pinecone-client
```

## 🎯 Suggested Learning Paths

### Path 1: "I'm Brand New to AI" (Start Here!)
```
Day 1: Lessons 1-2 (Setup + Text Chat)
Day 2: Lessons 3-4 (Images + Video)
Day 3: Lessons 5-6 (Streaming + Memory)
Day 4: Lessons 7-8 (Configurations + Instructions)
Day 5: Lessons 9-10 (RAG + Production)
```

### Path 2: "I Know AI, Show Me the Code" (Fast Track)
```
Hour 1: Lessons 1-4 (Skim basics, focus on code)
Hour 2: Lessons 5-8 (Advanced features)
Hour 3: Lessons 9-10 (RAG systems)
```

### Path 3: "I Want to Build a Chatbot"
```
Essential: Lessons 1, 2, 6, 8
Optional: Lessons 5, 7 (for better UX)
Advanced: Lessons 9, 10 (for knowledge base)
```

### Path 4: "I Want to Build RAG Applications"
```
Essential: Lessons 1, 2, 9, 10
Optional: Lessons 6, 7, 8 (for chat + control)
```

## 🚀 What's Next After This Course?

### Immediate Next Steps:
1. ✅ Build your own project combining multiple lessons
2. ✅ Try other Gemini models (gemini-pro, gemini-ultra)
3. ✅ Explore multimodal combinations (text + image + video)
4. ✅ Deploy your first AI app

### Advanced Topics to Explore:
- 🔧 Fine-tuning models with custom data
- 🌐 Building full-stack AI apps (React + FastAPI)
- ☁️ Cloud deployment (Google Cloud, AWS, Azure)
- 🔄 Advanced RAG (hybrid search, reranking)
- 🛡️ Safety and content filtering
- 💰 Cost optimization strategies
- 📊 Monitoring and analytics

### Other AI Platforms to Try:
- OpenAI GPT-4 and ChatGPT API
- Anthropic Claude
- Mistral AI
- Local models with Ollama/LM Studio

## 💬 Contributing & Feedback

Found an issue? Have suggestions?
- 🐛 Open an issue on GitHub
- 💡 Submit a pull request
- 📧 Contact the maintainers

---

## 📜 License

This project is for educational purposes. Feel free to use, modify, and share!

---

**🎉 Ready to start? Go to lesson 1 or check out QUICKSTART.md!**

*Happy coding! 🚀*
