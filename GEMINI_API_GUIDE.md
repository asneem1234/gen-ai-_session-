# 🔑 Gemini API Key Guide

> Complete guide to getting your API key, choosing models, and understanding which model to use

---

## 📋 Table of Contents
1. [Getting Your API Key](#getting-your-api-key)
2. [Available Models](#available-models)
3. [Model Comparison Table](#model-comparison-table)
4. [How to Choose the Right Model](#how-to-choose-the-right-model)
5. [Model Performance Benchmarks](#model-performance-benchmarks)
6. [Pricing Guide](#pricing-guide)
7. [Rate Limits](#rate-limits)
8. [Best Practices](#best-practices)

---

## 🔐 Getting Your API Key

### Step 1: Visit Google AI Studio
Go to: **[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)**

### Step 2: Sign In
- Use your Google account
- No credit card required for free tier!

### Step 3: Create API Key
1. Click **"Create API Key"**
2. Choose **"Create API key in new project"** (recommended for beginners)
   - Or select an existing Google Cloud project if you have one
3. Copy your API key (starts with `AIza...`)

### Step 4: Store Securely
```bash
# Option 1: Environment Variable (Recommended)
# Windows PowerShell:
$env:GOOGLE_API_KEY="your_api_key_here"

# Windows CMD:
set GOOGLE_API_KEY=your_api_key_here

# Linux/Mac:
export GOOGLE_API_KEY="your_api_key_here"

# Option 2: .env File (Best for Projects)
# Create a file named .env in your project folder
GOOGLE_API_KEY=your_api_key_here
```

### Step 5: Test Your Key
```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash-exp')
response = model.generate_content("Say hello!")
print(response.text)
```

✅ **Success!** If you see a response, your API key is working!

---

## 🤖 Available Models

### Current Models (December 2025)

| Model Name | Status | Description |
|------------|--------|-------------|
| **gemini-2.0-flash-exp** | 🟢 Latest | Fastest, experimental, cutting-edge features |
| **gemini-1.5-flash** | 🟢 Stable | Fast, efficient, production-ready |
| **gemini-1.5-flash-8b** | 🟢 Stable | Lightweight, cost-effective |
| **gemini-1.5-pro** | 🟢 Stable | Most capable, highest quality |
| **gemini-pro** | 🟡 Legacy | Older, still supported |
| **gemini-pro-vision** | 🟡 Legacy | Image understanding (use 1.5 models instead) |

---

## 📊 Model Comparison Table

### Quick Comparison

| Feature | gemini-2.0-flash-exp | gemini-1.5-flash | gemini-1.5-flash-8b | gemini-1.5-pro |
|---------|---------------------|------------------|---------------------|----------------|
| **Speed** | ⚡⚡⚡ Fastest | ⚡⚡ Fast | ⚡⚡⚡ Very Fast | ⚡ Moderate |
| **Quality** | 🌟🌟🌟🌟 Excellent | 🌟🌟🌟 Good | 🌟🌟 Decent | 🌟🌟🌟🌟🌟 Best |
| **Cost** | 💰 Low | 💰 Low | 💰 Lowest | 💰💰 Higher |
| **Context Window** | 1M tokens | 1M tokens | 1M tokens | 2M tokens |
| **Best For** | Experiments | Production | High-volume | Complex tasks |
| **Multimodal** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Stability** | 🧪 Experimental | ✅ Stable | ✅ Stable | ✅ Stable |

### Detailed Comparison

#### 🚀 **gemini-2.0-flash-exp** (Recommended for this course)
- **Latest experimental model** with cutting-edge features
- **Fastest response times** - Great for interactive apps
- **Excellent quality** - Nearly matches Pro performance
- **Free tier friendly** - Lower cost than Pro
- **Multimodal** - Handles text, images, video, audio
- **⚠️ Note**: "exp" means experimental - API may change

**Use When:**
- ✅ Learning and experimenting
- ✅ Building prototypes
- ✅ Need fast responses
- ✅ Want latest features
- ❌ Avoid for: Critical production apps (use stable versions)

#### ⚡ **gemini-1.5-flash** (Best for Production)
- **Production-ready** and stable
- **Fast and efficient** - Great balance
- **Reliable** - Consistent performance
- **Well-documented** - Extensive guides
- **1M token context** - Can handle long documents

**Use When:**
- ✅ Production applications
- ✅ Customer-facing apps
- ✅ Need reliability
- ✅ Moderate complexity tasks
- ✅ Multimodal needs

#### 🪶 **gemini-1.5-flash-8b** (Most Cost-Effective)
- **Smallest and fastest** Flash model
- **Lowest cost** - Great for high-volume
- **8B parameters** - Lighter than other models
- **Good for simple tasks** - Not for complex reasoning

**Use When:**
- ✅ High-volume applications
- ✅ Simple queries
- ✅ Budget constraints
- ✅ Speed is critical
- ❌ Avoid for: Complex reasoning, critical accuracy

#### 🏆 **gemini-1.5-pro** (Highest Quality)
- **Most capable** model available
- **Best quality** - Top-tier reasoning
- **2M token context** - Largest context window
- **Superior for complex tasks** - Advanced reasoning
- **Higher cost** - But worth it for quality

**Use When:**
- ✅ Complex reasoning required
- ✅ Highest quality needed
- ✅ Long documents (up to 2M tokens)
- ✅ Critical applications
- ✅ Advanced code generation
- ❌ Avoid for: Simple tasks (overkill)

---

## 🎯 How to Choose the Right Model

### Decision Tree

```
START: What's your use case?
│
├─ 🧪 Learning/Experimenting?
│  └─ ✅ Use: gemini-2.0-flash-exp
│
├─ 🚀 Production app?
│  │
│  ├─ Simple tasks? (FAQs, basic chat)
│  │  └─ ✅ Use: gemini-1.5-flash-8b
│  │
│  ├─ Medium complexity? (Chat, analysis)
│  │  └─ ✅ Use: gemini-1.5-flash
│  │
│  └─ Complex reasoning? (Code, research)
│     └─ ✅ Use: gemini-1.5-pro
│
└─ 💰 Budget-constrained + high volume?
   └─ ✅ Use: gemini-1.5-flash-8b
```

### By Use Case

| Use Case | Recommended Model | Why? |
|----------|------------------|------|
| **Learning AI** | gemini-2.0-flash-exp | Latest features, fast, great for tutorials |
| **Chatbot (simple)** | gemini-1.5-flash-8b | Cost-effective, fast enough |
| **Chatbot (advanced)** | gemini-1.5-flash | Good balance, reliable |
| **Code Generation** | gemini-1.5-pro | Best reasoning, complex logic |
| **Image Analysis** | gemini-1.5-flash | Good multimodal, fast |
| **Document Q&A** | gemini-1.5-pro | Large context, complex understanding |
| **Content Creation** | gemini-1.5-flash | Creative, fast, good quality |
| **Data Extraction** | gemini-1.5-flash | Structured output, reliable |
| **High-Volume API** | gemini-1.5-flash-8b | Lowest cost, acceptable quality |
| **Research/Analysis** | gemini-1.5-pro | Best reasoning, deep analysis |

### By Task Complexity

#### Simple Tasks (Use Flash-8B or Flash)
- Basic Q&A
- Simple classification
- Short summaries
- Basic chat responses
- Sentiment analysis

#### Medium Tasks (Use Flash or Pro)
- Conversational AI
- Content generation
- Image understanding
- Code explanation
- Multi-step reasoning

#### Complex Tasks (Use Pro)
- Advanced code generation
- Complex reasoning chains
- Long document analysis (>100K tokens)
- Research synthesis
- Critical business logic

---

## 📈 Model Performance Benchmarks

### Response Speed (Average)

| Model | Simple Query | Complex Query | With Images | With Long Context |
|-------|-------------|---------------|-------------|-------------------|
| gemini-2.0-flash-exp | 0.5s | 1.2s | 1.5s | 2.5s |
| gemini-1.5-flash | 0.6s | 1.5s | 1.8s | 3.0s |
| gemini-1.5-flash-8b | 0.4s | 1.0s | 1.3s | 2.2s |
| gemini-1.5-pro | 1.2s | 3.5s | 4.0s | 6.0s |

### Quality Scores (Higher is better)

| Benchmark | Flash-8B | Flash | Flash-Exp 2.0 | Pro |
|-----------|----------|-------|---------------|-----|
| MMLU (Knowledge) | 68% | 78% | 82% | 85% |
| HumanEval (Code) | 55% | 72% | 78% | 84% |
| GSM8K (Math) | 70% | 82% | 86% | 90% |
| VQA (Vision) | 72% | 80% | 84% | 88% |

*Scores are approximate and may vary by version*

### Cost Efficiency (Queries per dollar)

| Model | Approximate Cost |
|-------|-----------------|
| gemini-1.5-flash-8b | Most queries per $ |
| gemini-1.5-flash | Good value |
| gemini-2.0-flash-exp | Good value |
| gemini-1.5-pro | Premium pricing |

---

## 💰 Pricing Guide

### Free Tier Limits (as of December 2025)

| Model | Free Quota | Rate Limit |
|-------|-----------|------------|
| Flash models | 15 requests/minute | 1,500 requests/day |
| Pro models | 2 requests/minute | 50 requests/day |

**Note**: Free tier is perfect for learning and small projects!

### When You Need Paid Tier

You'll need to upgrade when:
- ❌ Exceeding daily request limits
- ❌ Building production apps with many users
- ❌ Need higher rate limits
- ❌ Require SLA guarantees

**Good News**: Most learners never hit free tier limits! 🎉

---

## ⚡ Rate Limits

### Understanding Rate Limits

| Model | RPM (Free) | RPM (Paid) | TPM (Tokens/Min) |
|-------|-----------|-----------|------------------|
| gemini-1.5-flash-8b | 15 | 2000 | 4M |
| gemini-1.5-flash | 15 | 2000 | 4M |
| gemini-2.0-flash-exp | 15 | 1000 | 4M |
| gemini-1.5-pro | 2 | 360 | 4M |

**RPM** = Requests Per Minute  
**TPM** = Tokens Per Minute

### Handling Rate Limits in Code

```python
import time
from google.api_core import retry

# Simple delay
def safe_generate(model, prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        if "429" in str(e):  # Rate limit error
            print("Rate limited, waiting 60 seconds...")
            time.sleep(60)
            return safe_generate(model, prompt)
        raise e

# With exponential backoff
@retry.Retry(predicate=retry.if_exception_type(Exception))
def generate_with_retry(model, prompt):
    return model.generate_content(prompt)
```

---

## 🎓 Best Practices

### 1. **Start with gemini-2.0-flash-exp**
For this course, we use `gemini-2.0-flash-exp` because:
- ✅ Latest features
- ✅ Fast responses (good for learning)
- ✅ Free tier friendly
- ✅ Great quality

### 2. **Switch Models Based on Needs**
```python
# Easy model switching
def get_model(complexity="medium"):
    models = {
        "simple": "gemini-1.5-flash-8b",
        "medium": "gemini-1.5-flash",
        "complex": "gemini-1.5-pro",
        "experimental": "gemini-2.0-flash-exp"
    }
    return genai.GenerativeModel(models[complexity])

# Usage
model = get_model("complex")  # For hard tasks
```

### 3. **Monitor Your Usage**
Check your usage at: [https://aistudio.google.com/app/prompts](https://aistudio.google.com/app/prompts)

### 4. **Use Appropriate Model for Task**
```python
# ❌ Bad: Using Pro for simple tasks
model = genai.GenerativeModel('gemini-1.5-pro')
response = model.generate_content("What's 2+2?")  # Overkill!

# ✅ Good: Right model for task
model = genai.GenerativeModel('gemini-1.5-flash-8b')
response = model.generate_content("What's 2+2?")  # Perfect!
```

### 5. **Test with Free Tier First**
- Prototype with free tier
- Optimize your prompts
- Estimate costs
- Upgrade only when needed

---

## 🔍 How to Know Which Model is Better?

### Method 1: Test with Your Use Case
```python
import time

def compare_models(prompt):
    models = [
        "gemini-1.5-flash-8b",
        "gemini-1.5-flash", 
        "gemini-2.0-flash-exp",
        "gemini-1.5-pro"
    ]
    
    results = {}
    for model_name in models:
        model = genai.GenerativeModel(model_name)
        
        # Measure speed
        start = time.time()
        response = model.generate_content(prompt)
        elapsed = time.time() - start
        
        results[model_name] = {
            "response": response.text,
            "time": elapsed
        }
        
        print(f"\n{'='*60}")
        print(f"Model: {model_name}")
        print(f"Time: {elapsed:.2f}s")
        print(f"Response: {response.text[:200]}...")
        
    return results

# Test
compare_models("Explain quantum computing in simple terms")
```

### Method 2: Check Benchmarks
Look at official benchmarks:
- **MMLU**: General knowledge
- **HumanEval**: Coding ability
- **GSM8K**: Math reasoning
- **MMMU**: Multimodal understanding

Higher scores = Better performance

### Method 3: Consider These Factors

| Factor | What to Check | How to Measure |
|--------|---------------|----------------|
| **Speed** | Response time | Use `time.time()` |
| **Quality** | Answer accuracy | Manual review + benchmarks |
| **Cost** | Price per request | Check pricing page |
| **Reliability** | Error rate | Track failures |
| **Context** | Max input size | Test with long inputs |

### Method 4: A/B Testing in Production

```python
import random

def smart_model_selection(task_complexity, user_tier):
    """Route requests to appropriate model"""
    
    if task_complexity == "simple":
        return "gemini-1.5-flash-8b"
    
    elif task_complexity == "medium":
        # A/B test: 80% Flash, 20% Flash-Exp
        return random.choice([
            "gemini-1.5-flash",
            "gemini-1.5-flash",
            "gemini-1.5-flash",
            "gemini-1.5-flash",
            "gemini-2.0-flash-exp"
        ])
    
    else:  # complex
        if user_tier == "premium":
            return "gemini-1.5-pro"
        else:
            return "gemini-1.5-flash"
```

---

## 🎯 Quick Start Guide

### For This Course: Use This Setup

```python
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

# Use this model for all lessons
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# Test it
response = model.generate_content("Hello! Introduce yourself.")
print(response.text)
```

### If You Want to Experiment

```python
# Try different models
models_to_try = [
    "gemini-1.5-flash-8b",
    "gemini-1.5-flash",
    "gemini-2.0-flash-exp",
    "gemini-1.5-pro"
]

for model_name in models_to_try:
    print(f"\nTesting: {model_name}")
    model = genai.GenerativeModel(model_name)
    response = model.generate_content("Write a haiku about coding")
    print(response.text)
```

---

## 📚 Additional Resources

### Video Tutorial
- 🎥 **[Getting Started with Gemini API - Video Guide](https://youtu.be/6BRyynZkvf0?si=I2Chvh3hA0qY8ZX9)** - Complete walkthrough of API setup and usage

### Official Documentation
- 🔗 [Google AI Studio](https://aistudio.google.com/)
- 🔗 [Gemini API Docs](https://ai.google.dev/docs)
- 🔗 [Model Comparison](https://ai.google.dev/models/gemini)
- 🔗 [Pricing Calculator](https://ai.google.dev/pricing)

### Community
- 💬 [Google AI Discord](https://discord.gg/google-ai)
- 🐦 [Follow @GoogleDevs](https://twitter.com/googledevs)
- 📺 [YouTube Tutorials](https://www.youtube.com/@GoogleDevelopers)

### Tools
- 🛠️ [API Key Management](https://aistudio.google.com/app/apikey)
- 📊 [Usage Dashboard](https://aistudio.google.com/app/prompts)
- 🧪 [Model Playground](https://aistudio.google.com/)

---

## ❓ FAQ

### Q: Which model should I use for this course?
**A:** Use `gemini-2.0-flash-exp` - it's fast, capable, and perfect for learning.

### Q: Can I change models mid-project?
**A:** Yes! Just change the model name in `GenerativeModel()`. Your code stays the same.

### Q: Will my API key work for all models?
**A:** Yes! One API key works for all Gemini models.

### Q: What if I hit the rate limit?
**A:** Add `time.sleep(4)` between requests (15 req/min = 1 per 4 seconds).

### Q: Is the free tier enough?
**A:** Yes! For learning and small projects, the free tier is plenty.

### Q: How do I upgrade to paid tier?
**A:** Visit [Google Cloud Console](https://console.cloud.google.com/) and enable billing.

### Q: Can I use multiple API keys?
**A:** Yes, but usually not needed. Upgrade to paid tier for higher limits instead.

---

## 🎉 You're Ready!

You now know:
- ✅ How to get your API key
- ✅ Which models exist
- ✅ How to choose the right model
- ✅ How to test and compare models
- ✅ Best practices for using the API

**Next Steps:**
1. Get your API key from [aistudio.google.com](https://aistudio.google.com/app/apikey)
2. Set it up in your environment
3. Start with lesson 01!

---

*Last updated: December 8, 2025*  
*For the latest model info, check: [ai.google.dev/models](https://ai.google.dev/models)*
