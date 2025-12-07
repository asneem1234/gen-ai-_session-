# Quick Start Guide

## Get Started in 5 Minutes! 🚀

### Step 1: Clone/Navigate to Directory
```bash
cd d:\gen-ai-_session-
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment
**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**If you get an error about execution policy:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Set Up Environment Variables
1. Copy the example file:
   ```bash
   copy .env.example .env
   ```

2. Edit `.env` and add your API keys:
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

**Get your Gemini API key:**
- Visit: https://makersuite.google.com/app/apikey
- Sign in with Google account
- Click "Create API Key"
- Copy and paste into `.env`

### Step 6: Test Your Setup
```bash
python 01_model_preparation.py
```

You should see ✅ marks indicating everything is working!

---

## Running the Modules

Each module is independent. Run them in order or pick what interests you:

```bash
# Run any module
python 01_model_preparation.py
python 02_text_chat.py
python 03_image_chat.py
# ... and so on
```

---

## Troubleshooting

### "python command not found"
- Make sure Python 3.9+ is installed
- Try `python3` instead of `python`

### "Cannot activate virtual environment"
- Windows: Use PowerShell (not Command Prompt)
- Check execution policy (see Step 3)

### "API key error"
- Verify `.env` file exists in root directory
- Check no extra spaces in API key
- Ensure key is valid in Google AI Studio

### "Module not found"
- Make sure virtual environment is activated (you should see `(venv)` in prompt)
- Reinstall requirements: `pip install -r requirements.txt`

---

## What's Next?

1. ✅ **Complete Modules 1-5** (Foundation)
2. ✅ **Try Modules 6-8** (Advanced Features)  
3. ✅ **Build RAG System** (Modules 9-10)
4. 🚀 **Build Your Own Project!**

---

## Need Help?

- Read `README.md` for detailed information
- Check `TEACHING_NOTES.md` for instructor guidance
- Review code comments in each module
- Visit Google AI documentation: https://ai.google.dev/docs

---

## Tips for Success

1. **Don't rush** - Understanding is better than speed
2. **Experiment** - Change the code and see what happens
3. **Ask questions** - There are no stupid questions
4. **Build something** - Best way to learn is by doing
5. **Have fun** - AI is amazing, enjoy the journey!

---

Happy coding! 🎉
