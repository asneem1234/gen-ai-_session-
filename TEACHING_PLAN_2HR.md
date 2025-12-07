# 2-Hour AI Session - Simple Teaching Script

**Goal**: Take ChatGPT users and turn them into AI builders in 2 hours.

**Story**: We're building "DocuMind" - an AI that can chat, see images, remember conversations, and search documents.

---

---

## OPENING (5 min)

**Say**: "Who uses ChatGPT daily?" (hands up) "Who writes code that calls AI?" (few hands) "Today you go from USER to BUILDER."

**Do**: 
- Run `06_memory_conversation.py` - show chatbot
- Run `09_rag_basic.py` - show document search
- Say: "This is what you'll build in 2 hours."

---

## MODULE 1: First AI Call (10 min)

**Say**: "ChatGPT = restaurant. API = your kitchen."

**Code together** (`01_model_preparation.py`):
```python
import google.generativeai as genai
genai.configure(api_key="YOUR_KEY")
model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content("Hello!")
print(response.text)
```

**Say**: "5 lines. You just called AI from your code!"

---

## MODULE 2: Text Chat (15 min)

**Ask**: "What should we ask the AI?" - Take 3 suggestions, run them live.

**Show**:
```python
# Bad: "Write about Python"
# Good: "Explain Python in 3 sentences for a 10-year-old"
```

**Challenge**: "Make AI write a haiku about coding" - students do it, share results.

---

## MODULE 3: Image Vision (15 min)

**Show** an image. **Say**: "What if AI could SEE this?"

**Code**:
```python
from PIL import Image
image = Image.open('photo.jpg')
model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content(["What's in this?", image])
```

**Do**: Students use THEIR image. AI describes it. Magic moment!

---

## MODULE 4: Video (10 min - QUICK)

**Say**: "Video = many images. Send frames to AI."

**Show pattern** (don't code everything):
```python
frames = extract_frames(video)
response = model.generate_content(["Describe video", *frames])
```

**Say**: "Details in materials. Same concept as images."

---

## MODULE 5: Streaming (10 min)

**Demo**: No streaming = wait...wait...DUMP. Streaming = word-by-word (like ChatGPT!)

**The magic**:
```python
response = model.generate_content(prompt, stream=True)
for chunk in response:
    print(chunk.text, end='')
```

**Say**: "One line = ChatGPT experience!"

---

## MODULE 6: Memory (10 min)

**Problem**: AI forgets. Ask "My name is John" → "What's my name?" → "I don't know"

**Solution**:
```python
chat = model.start_chat()
chat.send_message("Hi, I'm John")
chat.send_message("What's my name?")  # Remembers!
```

---

## MODULE 7+8: Settings (10 min COMBINED)

**Temperature** (5 min):
```python
temperature=0.1  # Factual
temperature=1.5  # Creative
```
**Poll**: "Code helper - low or high?" (Low!) "Story writer?" (High!)

**Personality** (5 min):
```python
model = GenerativeModel('gemini-2.0-flash',
    system_instruction="You are a pirate")
```
**Demo**: Change personality 3 times, same question. Students laugh!

---

## MODULE 9: RAG - THE BIG ONE (25 min)

**Problem**: "What's in my company report?" - ChatGPT can't answer. Doesn't know YOUR docs.

**RAG = THE SOLUTION**

**Analogy**: AI = smart person with amnesia. RAG = give them notes before asking.

**Build it**:
```python
# Your docs
docs = ["Python created by Guido", "Django is a framework"]

# 1. Convert to vectors
embeddings = [genai.embed_content(content=doc) for doc in docs]

# 2. Question to vector
question = "Who created Python?"
query_emb = genai.embed_content(content=question)

# 3. Find similar doc
best_doc = find_most_similar(query_emb, embeddings, docs)

# 4. Give AI the doc
prompt = f"Context: {best_doc}\nQuestion: {question}"
response = model.generate_content(prompt)
```

**Magic**: Students use THEIR docs. AI answers about THEIR content!

---

## MODULE 10: Pinecone (5 min - PREVIEW ONLY)

**Say**: "Module 9 = small scale. Pinecone = millions of docs. Same 4 steps, bigger."

**Assignment**: "Try Module 10 after class. Same pattern, just scaled."

---

## CLOSING (5 min)

**Say**: 
"2 hours ago, you USED AI. Now you can BUILD AI.

You built:
✅ Text generation
✅ Image vision
✅ Streaming
✅ Memory
✅ Personalities
✅ Document search (RAG)

Real apps use these:
- ChatGPT = Streaming + Memory
- Perplexity = RAG + Generation
- GitHub Copilot = Code RAG

Now go build YOUR idea!"

---

## QUICK TIPS

**Teaching Style**:
- Show FIRST, explain after
- Run code, see magic, then how it works
- Take suggestions from students every 10 min
- Use funny examples (pirate AI!)

**If Time Runs Out**: Skip Module 4 details, Module 10 demo

**Before Class**:
- Test all 10 scripts work
- Have sample images ready
- Large fonts for screen sharing
- Backup API keys

**Send Students (1 day before)**:
- Install Python 3.9+
- `pip install -r requirements.txt`
- Get Gemini API key
- Test: Run `01_model_preparation.py`
