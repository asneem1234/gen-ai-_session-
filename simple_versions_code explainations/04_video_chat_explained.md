# 04 Video Chat - Complete Code Explanation

## 📋 Overview
This code demonstrates Gemini AI's ability to analyze video content by processing multiple frames. While not true video streaming, it shows how to send sequential frames to understand motion, changes, and temporal relationships - the foundation of video understanding.

---

## 💻 Complete Code with Line-by-Line Explanation

```python
import os
# WHY: Import operating system module
# WHAT IT DOES: Provides access to environment variables
# WHEN TO USE: Required for reading API keys securely

from dotenv import load_dotenv
# WHY: Import function to load .env file
# WHAT IT DOES: Reads environment variables from .env
# SECURITY: Keeps sensitive information out of code

import google.generativeai as genai
# WHY: Import Google Generative AI library
# WHAT IT DOES: Provides tools for AI operations
# CAPABILITY: Handles text, images, and frame sequences

from PIL import Image, ImageDraw
# WHY: Import Python Imaging Library modules
# WHAT IT DOES:
#   - Image: Create and manipulate images
#   - ImageDraw: Add shapes and text to images
# PURPOSE: Generate video frames programmatically

load_dotenv()
# WHY: Load environment variables at module level
# WHAT IT DOES: Makes GOOGLE_API_KEY accessible
# TIMING: Called immediately before configuration

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
# WHY: Authenticate with Gemini API
# WHAT IT DOES: Sets up API key for all requests
# REQUIRED: Must be done before any AI operations

def create_video_frames():
    # WHY: Generate a sequence of frames simulating video
    # WHAT IT DOES: Creates multiple images showing progression
    # USE CASE: Testing video understanding without real video files
    # SIMULATES: Time-based changes like a real video
    
    frames = []
    # WHY: Create empty list to store frame images
    # WHAT IT DOES: Initializes container for all frames
    # PURPOSE: Will hold PIL Image objects in sequence
    
    for i in range(5):
        # WHY: Loop 5 times to create 5 frames
        # WHAT IT DOES: Generates frames with index 0-4
        # SIMULATES: 5 frames of a video sequence
        # NOTE: Real videos have 24-60 frames per second
        
        img = Image.new('RGB', (300, 200), color=(i*50, 100, 255-i*50))
        # WHY: Create a new image for this frame
        # WHAT IT DOES:
        #   - 'RGB': Color mode
        #   - (300, 200): Width x Height in pixels
        #   - color=(i*50, 100, 255-i*50): Dynamic color calculation
        # COLOR MATH:
        #   - Red channel: i*50 (increases: 0, 50, 100, 150, 200)
        #   - Green channel: 100 (constant)
        #   - Blue channel: 255-i*50 (decreases: 255, 205, 155, 105, 55)
        # RESULT: Color gradually shifts from blue to red across frames
        
        draw = ImageDraw.Draw(img)
        # WHY: Create drawing context for this frame
        # WHAT IT DOES: Allows adding text to the image
        # PURPOSE: Label each frame with its number
        
        draw.text((100, 90), f"Frame {i+1}", fill='white')
        # WHY: Add text showing frame number
        # WHAT IT DOES:
        #   - (100, 90): X, Y position
        #   - f"Frame {i+1}": Dynamic text (Frame 1, Frame 2, etc.)
        #   - fill='white': Text color
        # PURPOSE: Makes frames distinguishable
        # NOTE: i+1 because humans count from 1, not 0
        
        frames.append(img)
        # WHY: Add this frame to the list
        # WHAT IT DOES: Stores the completed frame
        # BUILDS: Sequential list of all frames
    
    return frames
    # WHY: Return the complete frame sequence
    # WHAT IT DOES: Makes all frames available to caller
    # RETURNS: List of 5 PIL Image objects

def analyze_video_frames():
    # WHY: Demonstrate analyzing a sequence of frames
    # WHAT IT DOES: Sends all frames to AI for temporal analysis
    # USE CASE: Understanding motion, changes over time, video content
    
    model = genai.GenerativeModel('gemini-2.0-flash')
    # WHY: Create AI model instance
    # WHAT IT DOES: Initializes gemini-2.0-flash
    # CAPABILITY: Can process multiple images as sequence
    
    frames = create_video_frames()
    # WHY: Generate the test video frames
    # WHAT IT DOES: Creates 5 frames with color progression
    # RETURNS: List of PIL Image objects
    
    prompt = "Describe what happens across these video frames."
    # WHY: Ask AI to analyze the temporal sequence
    # WHAT IT DOES: Creates instruction for frame analysis
    # FOCUS: Understanding changes over time, not just individual frames
    # KEY: Word "across" indicates temporal relationship
    
    response = model.generate_content([prompt] + frames)
    # WHY: Send prompt and all frames to AI
    # WHAT IT DOES: Makes API call with prompt and frame sequence
    # SYNTAX BREAKDOWN:
    #   - [prompt]: Start with text instruction
    #   - + frames: Concatenate with list of images
    #   - Result: [prompt, frame1, frame2, frame3, frame4, frame5]
    # ORDER MATTERS: Frames analyzed in sequence order
    
    print(f"Response: {response.text}")
    # WHY: Display AI's temporal analysis
    # WHAT IT DOES: Shows understanding of changes across frames
    # EXPECTED: Description of color shift and progression

def video_question_answering():
    # WHY: Demonstrate asking specific questions about video content
    # WHAT IT DOES: Shows targeted analysis of frame sequences
    # USE CASE: Extracting specific information from videos
    
    model = genai.GenerativeModel('gemini-2.0-flash')
    # WHY: Initialize model for Q&A
    # WHAT IT DOES: Creates model instance
    # SAME MODEL: Handles both general and specific queries
    
    frames = create_video_frames()
    # WHY: Generate same test frames
    # WHAT IT DOES: Creates 5-frame sequence
    # CONSISTENT: Same frames allow fair comparison
    
    prompt = "How many frames are there and what changes?"
    # WHY: Ask specific question about the video
    # WHAT IT DOES: Creates focused query
    # TWO PARTS:
    #   1. Count: "How many frames" (quantitative)
    #   2. Change: "what changes" (qualitative)
    # TESTS: Both counting and pattern recognition
    
    response = model.generate_content([prompt] + frames)
    # WHY: Send question with frame sequence
    # WHAT IT DOES: AI analyzes frames to answer specific question
    # CONTEXT: All frames provided for complete understanding
    # FOCUSED: Answer will address specific question asked
    
    print(f"Response: {response.text}")
    # WHY: Display the specific answer
    # WHAT IT DOES: Shows AI's response to question
    # EXPECTED: "5 frames" + description of color changes

if __name__ == "__main__":
    # WHY: Check if script is run directly
    # WHAT IT DOES: Only executes demos when main program
    # BEST PRACTICE: Prevents auto-execution on import
    
    print("1. Analyze Video Frames")
    # WHY: Label the first demo
    # WHAT IT DOES: Prints section header
    # UX: Helps user track demo progress
    
    analyze_video_frames()
    # WHY: Execute general video analysis demo
    # WHAT IT DOES: Runs function that describes frame sequence
    # DEMONSTRATES: Temporal understanding across frames
    
    print("\n2. Video Q&A")
    # WHY: Label the Q&A demo with spacing
    # WHAT IT DOES: Prints header with newline
    # UX: Separates demos visually
    
    video_question_answering()
    # WHY: Execute specific question demo
    # WHAT IT DOES: Asks targeted question about frames
    # DEMONSTRATES: Extracting specific info from sequences
```

---

## 🔄 Code Workflow Diagram

```
┌────────────────────────────────────────────────────────────────────┐
│                        START PROGRAM                                │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  1. IMPORT & CONFIGURE                                              │
│     ├─ Import: os, dotenv, genai, PIL                              │
│     ├─ Load .env file                                              │
│     └─ Configure API key                                           │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  2. DEFINE create_video_frames()                                    │
│     Creates 5 frames with:                                          │
│     ├─ Frame 1: Blue-ish (R:0,   G:100, B:255)                     │
│     ├─ Frame 2: Blue    (R:50,  G:100, B:205)                     │
│     ├─ Frame 3: Purple  (R:100, G:100, B:155)                     │
│     ├─ Frame 4: Purple  (R:150, G:100, B:105)                     │
│     └─ Frame 5: Red-ish (R:200, G:100, B:55)                      │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  3. DEFINE analyze_video_frames()                                   │
│     Purpose: Get AI understanding of frame sequence                 │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  4. DEFINE video_question_answering()                               │
│     Purpose: Ask specific questions about frames                    │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  5. MAIN EXECUTION                                                  │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  6. DEMO 1: Analyze Video Frames                                    │
│     │                                                               │
│     ├─ Create model instance                                       │
│     │                                                               │
│     ├─ Call create_video_frames()                                  │
│     │   │                                                           │
│     │   ├─ Loop i=0: Create Frame 1                                │
│     │   │   ├─ Color: (0, 100, 255) = Bright Blue                  │
│     │   │   ├─ Add text: "Frame 1"                                 │
│     │   │   └─ Add to frames list                                  │
│     │   │                                                           │
│     │   ├─ Loop i=1: Create Frame 2                                │
│     │   │   ├─ Color: (50, 100, 205) = Blue                        │
│     │   │   ├─ Add text: "Frame 2"                                 │
│     │   │   └─ Add to frames list                                  │
│     │   │                                                           │
│     │   ├─ Loop i=2: Create Frame 3                                │
│     │   │   ├─ Color: (100, 100, 155) = Purple-Blue                │
│     │   │   ├─ Add text: "Frame 3"                                 │
│     │   │   └─ Add to frames list                                  │
│     │   │                                                           │
│     │   ├─ Loop i=3: Create Frame 4                                │
│     │   │   ├─ Color: (150, 100, 105) = Purple-Red                 │
│     │   │   ├─ Add text: "Frame 4"                                 │
│     │   │   └─ Add to frames list                                  │
│     │   │                                                           │
│     │   └─ Loop i=4: Create Frame 5                                │
│     │       ├─ Color: (200, 100, 55) = Red-Orange                  │
│     │       ├─ Add text: "Frame 5"                                 │
│     │       └─ Add to frames list                                  │
│     │                                                               │
│     │   Returns: [Frame1, Frame2, Frame3, Frame4, Frame5]          │
│     │                                                               │
│     ├─ Visual Representation:                                      │
│     │   ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐       │
│     │   │ Blue    │→ │ Blue    │→ │ Purple  │→ │ Purple  │→      │
│     │   │Frame 1  │  │Frame 2  │  │Frame 3  │  │Frame 4  │       │
│     │   └─────────┘  └─────────┘  └─────────┘  └─────────┘       │
│     │        ┌─────────┐                                           │
│     │      → │ Red     │                                           │
│     │        │Frame 5  │                                           │
│     │        └─────────┘                                           │
│     │                                                               │
│     ├─ Create prompt: "Describe what happens across..."            │
│     │                                                               │
│     ├─ Build input: [prompt] + frames                              │
│     │   Result: [prompt, Frame1, Frame2, Frame3, Frame4, Frame5]   │
│     │                                                               │
│     ├─ Send to API                                                 │
│     │   └─ AI analyzes sequence temporally                         │
│     │                                                               │
│     └─ Print response                                              │
│         └─> "The frames show a gradual color transition..."        │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  7. DEMO 2: Video Q&A                                               │
│     │                                                               │
│     ├─ Create model instance                                       │
│     ├─ Create same 5 frames again                                  │
│     ├─ Create prompt: "How many frames and what changes?"          │
│     ├─ Send [prompt] + frames to API                               │
│     │   └─ AI counts frames and identifies changes                 │
│     └─ Print response                                              │
│         └─> "There are 5 frames. The color changes from..."        │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│                     PROGRAM COMPLETE ✅                             │
│  Video frame analysis demonstrations complete!                      │
└────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Sample Output

### ✅ Complete Successful Execution

```
1. Analyze Video Frames
Response: The frames show a gradual color transition across the sequence. Starting with a blue-dominated color scheme in Frame 1, the images progressively shift towards a more purple-red hue. Each frame is labeled with "Frame 1" through "Frame 5" in white text. The red channel increases while the blue channel decreases across the sequence, creating a smooth color gradient effect. The green channel remains constant throughout. This demonstrates a transition from cool tones (blue) to warm tones (red/orange).

2. Video Q&A
Response: There are 5 frames in total. The main change across the frames is a color transition: the background color shifts from blue (Frame 1) to progressively more red/orange tones (Frame 5). The blue component decreases while the red component increases in each successive frame, creating a gradient effect from cool to warm colors. Each frame displays its number as white text.
```

---

## 🎯 Key Concepts Explained

### 1. **Video as Frame Sequence**

```python
# Video isn't a special format to the AI
# It's just multiple images in order
frames = [image1, image2, image3, image4, image5]

# Send as sequence
response = model.generate_content([prompt] + frames)
```

**Key Understanding:**
- Videos are sequences of still images
- AI analyzes temporal relationships
- Order of frames matters!
- More frames = better temporal understanding

### 2. **Dynamic Color Generation**

```python
color=(i*50, 100, 255-i*50)
# i=0: (0, 100, 255)     - Blue
# i=1: (50, 100, 205)    - Blue-Purple
# i=2: (100, 100, 155)   - Purple
# i=3: (150, 100, 105)   - Purple-Red
# i=4: (200, 100, 55)    - Red
```

**Creates progression:**
- Red increases (i*50)
- Green constant (100)
- Blue decreases (255-i*50)
- Result: Smooth gradient

### 3. **List Concatenation**

```python
# Method 1: List concatenation
[prompt] + frames  # [prompt, frame1, frame2, frame3, ...]

# Method 2: Explicit list
[prompt, frames[0], frames[1], frames[2], ...]

# Method 3: Unpacking
[prompt, *frames]  # Same result as Method 1
```

### 4. **Temporal vs Spatial Analysis**

**Spatial (single image):**
- "What's in this image?"
- Analyzes content at one moment

**Temporal (video/frames):**
- "What happens across these frames?"
- Analyzes changes over time
- Understands motion and progression

---

## 🚀 What Happens Behind the Scenes

### Frame Sequence Processing:

1. **Upload:** All frames sent to API in order
2. **Individual Analysis:** Each frame analyzed separately
3. **Temporal Correlation:** AI identifies changes between frames
4. **Pattern Recognition:** Detects motion, color shifts, object movements
5. **Synthesis:** Creates coherent description of sequence
6. **Response:** Natural language explanation of temporal changes

### Why Order Matters:

```python
# Correct order: Shows progression
[prompt, frame1, frame2, frame3, frame4, frame5]
# Result: "Color shifts from blue to red"

# Wrong order: Confusing results
[prompt, frame5, frame2, frame4, frame1, frame3]
# Result: "Color changes randomly"
```

---

## 📝 Common Use Cases

### Use Case 1: Video Summarization
```python
def summarize_video(video_frames):
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = "Summarize what happens in this video sequence."
    response = model.generate_content([prompt] + video_frames)
    return response.text
```

### Use Case 2: Motion Detection
```python
def detect_motion(frames):
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = "Describe any movement or motion you see across these frames."
    response = model.generate_content([prompt] + frames)
    return response.text
```

### Use Case 3: Action Recognition
```python
def recognize_action(video_frames):
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = "What action is being performed in this video?"
    response = model.generate_content([prompt] + video_frames)
    return response.text
```

### Use Case 4: Change Detection
```python
def detect_changes(before_frames, after_frames):
    model = genai.GenerativeModel('gemini-2.0-flash')
    all_frames = before_frames + after_frames
    prompt = "What changes occur between the first and second half of these frames?"
    response = model.generate_content([prompt] + all_frames)
    return response.text
```

---

## 🎬 Working with Real Videos

### Extracting Frames from Video File:
```python
import cv2  # OpenCV library

def extract_frames(video_path, num_frames=10):
    """Extract evenly spaced frames from video"""
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    frames = []
    frame_indices = [int(i * total_frames / num_frames) for i in range(num_frames)]
    
    for idx in frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            # Convert BGR to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert to PIL Image
            img = Image.fromarray(frame_rgb)
            frames.append(img)
    
    cap.release()
    return frames

# Use with Gemini
frames = extract_frames('video.mp4', num_frames=10)
model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content(["Describe this video"] + frames)
```

### Sampling Strategy:
```python
# Option 1: Evenly spaced (good for long videos)
every_nth = total_frames // 10

# Option 2: Key frames only (more intelligent)
# Use scene detection algorithms

# Option 3: Fixed interval (e.g., 1 frame per second)
fps = 30  # frames per second
frame_interval = fps  # 1 frame per second
```

---

## 💡 Best Practices

### 1. **Frame Selection**
- Don't send all frames (expensive and slow)
- Sample intelligently (every Nth frame)
- 5-20 frames usually sufficient
- More frames for complex motion

### 2. **Frame Quality**
- Resize large frames to save costs
- 800x600 or 1024x768 typically sufficient
- Balance quality vs processing time

### 3. **Prompt Design**
```python
# Good prompts for video:
"Describe what happens across these frames"
"What action is being performed?"
"Summarize the events in this video"
"What changes from start to end?"

# Poor prompts:
"What is this?" # Too vague
"Describe frame 3" # Not using sequence context
```

### 4. **Cost Optimization**
```python
# Fewer, well-chosen frames
frames = extract_key_frames(video, n=10)  # Good

# Not every single frame
frames = extract_all_frames(video)  # Expensive!
```

---

## ⚠️ Important Notes

1. **Frame Limits:** Gemini can handle up to 16 images per request
2. **Token Cost:** Each frame counts as tokens (more frames = higher cost)
3. **Processing Time:** More frames = longer processing
4. **Order Matters:** Frame sequence is crucial for temporal understanding
5. **Frame Rate:** No real-time processing - designed for pre-recorded sequences
6. **Memory:** Loading many high-res frames uses significant RAM

---

## 🔗 Prerequisites

1. ✅ Completed previous lessons (01-03)
2. ✅ PIL/Pillow installed:
   ```bash
   pip install Pillow
   ```
3. ✅ For real videos, install OpenCV:
   ```bash
   pip install opencv-python
   ```

---

## 🎓 Learning Outcomes

After understanding this code, you should know:

- ✅ How to create sequential frames programmatically
- ✅ How to send multiple frames as video sequence
- ✅ How AI understands temporal relationships
- ✅ The difference between spatial and temporal analysis
- ✅ How to extract frames from real videos
- ✅ Best practices for frame sampling
- ✅ How to optimize costs for video analysis

---

## 🔜 Next Steps

1. Move to `05_streaming.py` to learn about streaming responses
2. Extract frames from a real video file
3. Build a video summarization tool
4. Create an action recognition system
5. Experiment with different frame sampling rates

---

**✨ Fantastic!** You now understand how to work with video/frame sequences in Gemini AI!
