# 🤖 Gemini API Model Selection Guide

## 📋 Table of Contents
- [Free Tier Models](#-free-tier-models)
- [Model Recommendations by Use Case](#-model-recommendations-by-use-case)
- [API Key Setup](#-api-key-setup)
- [Pricing Overview](#-pricing-overview)
- [Rate Limits & Quotas](#-rate-limits--quotas)

---

## ✅ Free Tier Models

### 🥇 **Recommended Free Models (Best for Most Use Cases)**

| Model Name | Best For | Speed | Context Window |
|------------|----------|-------|----------------|
| `gemini-2.5-flash-lite` | ⭐ General chat, Q&A, small tasks | Very Fast | 1M tokens |
| `gemini-2.5-flash` | Complex reasoning, coding, analysis | Fast | 1M tokens |
| `gemini-2.0-flash-lite` | Stable, predictable responses | Fast | 1M tokens |
| `gemini-2.0-flash` | Production apps, reliable performance | Fast | 1M tokens |

### 🎯 **All Free Tier Models (Complete List)**

#### **1️⃣ Gemini 2.5 Flash Family** (Fully Free ✅)
```
gemini-2.5-flash
gemini-2.5-flash-preview
gemini-2.5-flash-lite
gemini-2.5-flash-lite-preview
gemini-2.5-flash-native-audio-preview
gemini-2.5-flash-image (image generation)
gemini-2.5-flash-preview-tts (text-to-speech)
```

#### **2️⃣ Gemini 2.0 Flash Family** (Fully Free ✅)
```
gemini-2.0-flash
gemini-2.0-flash-lite
```

#### **3️⃣ Gemini 2.5 Pro** (Limited Free ⚠️)
```
gemini-2.5-pro
gemini-2.5-pro-preview-tts
```
**Limitations:**
- ❌ No grounding support
- ❌ No batch API
- ⚠️ Very low RPM (requests per minute)
- Use only for small-scale development

#### **4️⃣ Gemini 3 Pro Preview** (Studio Only ⚠️)
```
gemini-3-pro-preview
gemini-3-pro-image-preview
```
**Note:** Free in AI Studio but NOT free in API usage

#### **5️⃣ Specialized Models** (Preview/Free ✅)
```
gemini-robotics-er-1.5-preview
gemini-2.5-computer-use-preview
gemini-embedding-001 (embeddings)
```

#### **6️⃣ Open Models** (Completely Free ✅)
```
gemma-3
gemma-3n
```

---

## 🎯 Model Recommendations by Use Case

### 💬 **Chat & Conversation**
**Best Choice:** `gemini-2.5-flash-lite`
- Fast responses
- Low rate limits
- Great for interactive chat

**Alternative:** `gemini-2.0-flash-lite`

### 🧠 **Complex Reasoning & Analysis**
**Best Choice:** `gemini-2.5-flash`
- Better reasoning capabilities
- Handles complex queries
- Good for multi-step tasks

**Alternative:** `gemini-2.5-pro` (if within rate limits)

### 💻 **Coding & Development**
**Best Choice:** `gemini-2.5-flash`
- Strong code generation
- Good debugging capabilities
- Understands multiple languages

**Alternative:** `gemini-2.0-flash`

### 📄 **Document Analysis & RAG**
**Best Choice:** `gemini-2.5-flash`
- Large context window (1M tokens)
- Good at extracting information
- Works with long documents

**Embeddings:** `gemini-embedding-001`

### 🖼️ **Image Understanding**
**Best Choice:** `gemini-2.5-flash`
- Multimodal capabilities
- Can analyze images
- Free tier includes image input

### 🎤 **Audio & TTS**
**Best Choice:**
- `gemini-2.5-flash-native-audio-preview`
- `gemini-2.5-flash-preview-tts`

### 🎨 **Image Generation**
**Best Choice:** `gemini-2.5-flash-image`
**Note:** Limited preview - may have restrictions

---

## 🔑 API Key Setup

### **Step 1: Get Your Free API Key**

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Get API Key"** or **"Create API Key"**
4. Copy your API key (format: `AIzaSy...`)

### **Step 2: Store API Key Securely**

Create a `.env` file in your project root:

```bash
GOOGLE_API_KEY=your_api_key_here
```

**⚠️ IMPORTANT:** Add `.env` to your `.gitignore` to keep it secure!

### **Step 3: Use in Python**

```python
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

# Configure the SDK
genai.configure(api_key=api_key)

# Use the model
model = genai.GenerativeModel('gemini-2.5-flash-lite')
response = model.generate_content("Hello!")
print(response.text)
```

---

## 💰 Pricing Overview

### **Free Tier Limits (as of Dec 2025)**

| Resource | Free Tier Limit | What This Means |
|----------|----------------|-----------------|
| **Requests per Minute (RPM)** | 15 RPM (Flash models) | You can make 15 API calls every minute |
| **Requests per Day (RPD)** | 1,500 RPD | You can make 1,500 API calls every day |
| **Input Tokens per Minute (TPM)** | 1 million TPM | You can send ~1 million words as input per minute |
| **Output Tokens per Minute (TPM)** | 4,000 TPM | Model can generate ~4,000 words output per minute |
| **Grounded Prompts** | 500 per day | 500 searches with Google Search grounding per day |
| **Context Caching** | Free (Flash models) | Store conversation history for free |

### **Understanding the Terms**

- **RPM (Requests Per Minute)**: How many times you can call the API in 60 seconds
- **RPD (Requests Per Day)**: Total API calls allowed in 24 hours
- **TPM (Tokens Per Minute)**: Number of words/tokens processed per minute (roughly 1 token ≈ 0.75 words)
- **Token**: A piece of text (a word or part of a word) that the model processes
- **Grounding**: Using Google Search to find real-time information
- **Context Caching**: Storing conversation history to maintain context

### **What's Free vs Paid**

#### ✅ **FREE in API:**
- All Flash 2.5 & 2.0 models
- Gemini 2.5 Pro (limited)
- Embedding models
- Gemma open models
- Text, image, audio input
- Context caching

#### ❌ **NOT FREE (Paid Only):**
- Imagen (image generation models 3 & 4)
- Veo (video generation models)
- Batch API
- High-volume production usage
- Grounding beyond 500/day

---

## 📊 Rate Limits & Quotas

### **Understanding Rate Limits**

When you see this error:
```
google.api_core.exceptions.ResourceExhausted: 429 You exceeded your current quota
```

**This means:**
- You've hit your free tier limit
- Need to wait (usually 11-60 seconds)
- Consider upgrading to paid tier for production

### **How to Avoid Rate Limits**

1. **Use Lite Models**: `gemini-2.5-flash-lite` has better limits
2. **Add Retry Logic**: Implement exponential backoff
3. **Cache Responses**: Store common queries
4. **Monitor Usage**: Check [AI Studio Usage Dashboard](https://ai.dev/usage?tab=rate-limit)

### **Retry Logic Example**

```python
import time
from google.api_core import retry

@retry.Retry(predicate=retry.if_exception_type(Exception))
def generate_with_retry(model, prompt):
    try:
        return model.generate_content(prompt)
    except Exception as e:
        if "429" in str(e):
            print("Rate limit hit, waiting...")
            time.sleep(60)
            raise
        else:
            raise
```

---

## 🚀 Quick Start Template

```python
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Setup
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Choose your model based on use case:
# - For chat: 'gemini-2.5-flash-lite'
# - For reasoning: 'gemini-2.5-flash'
# - For stability: 'gemini-2.0-flash-lite'

model = genai.GenerativeModel('gemini-2.5-flash-lite')

# Generate content
response = model.generate_content("Your prompt here")
print(response.text)
```

---

## 📚 Additional Resources

- **Official Pricing**: [https://ai.google.dev/pricing](https://ai.google.dev/pricing)
- **Rate Limits Documentation**: [https://ai.google.dev/gemini-api/docs/rate-limits](https://ai.google.dev/gemini-api/docs/rate-limits)
- **API Documentation**: [https://ai.google.dev/docs](https://ai.google.dev/docs)
- **AI Studio**: [https://aistudio.google.com](https://aistudio.google.com)
- **Usage Monitoring**: [https://ai.dev/usage](https://ai.dev/usage)

---

## 🎓 Model Selection Decision Tree

```
Need API access?
├── Yes
│   ├── Simple tasks? → gemini-2.5-flash-lite ⭐
│   ├── Complex reasoning? → gemini-2.5-flash
│   ├── Need stability? → gemini-2.0-flash-lite
│   └── Image generation? → gemini-2.5-flash-image
│
└── Just testing in Studio?
    └── Try gemini-3-pro-preview
```

---

## ⚠️ Important Notes

1. **Free tier is for development/testing** - For production apps, consider paid tier
2. **Rate limits can change** - Always check current limits at [https://ai.google.dev/pricing](https://ai.google.dev/pricing)
3. **Keep your API key secure** - Never commit it to version control
4. **Monitor your usage** - Check the usage dashboard regularly
5. **Lite models are better for free tier** - Lower rate limit issues

---

**Last Updated:** December 11, 2025
**Current Working Model:** `gemini-2.5-flash-lite` ✅
