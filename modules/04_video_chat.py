"""
04 - Video Chat (Video Understanding)
======================================

This module demonstrates video processing and understanding with AI.
Students will learn:
- Extracting frames from video
- Analyzing video content
- Temporal understanding
- Video description generation
- Practical video AI applications

Teaching Points:
- Videos are processed as sequences of frames
- Frame selection strategy impacts results
- Balance between detail (more frames) and efficiency
- Video understanding enables powerful applications

Note: For actual video files, you'll need opencv-python (cv2)
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image, ImageDraw, ImageFont
import io

# Setup
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


# ============================================================================
# SECTION 1: Understanding Video Processing
# ============================================================================

def video_processing_concepts():
    """
    Explain video processing concepts
    """
    print("\n" + "=" * 60)
    print("SECTION 1: Video Processing Concepts")
    print("=" * 60)
    
    concepts = """
    🎬 HOW VIDEO AI WORKS:
    
    1. VIDEO = SEQUENCE OF FRAMES
       • Videos are collections of still images (frames)
       • Typical: 24-30 frames per second (fps)
       • AI analyzes selected frames to understand content
    
    2. FRAME EXTRACTION STRATEGIES:
       • Uniform sampling: Every Nth frame (e.g., 1 per second)
       • Keyframe detection: Important moments only
       • Scene changes: When content shifts significantly
    
    3. TEMPORAL UNDERSTANDING:
       • AI can track changes across frames
       • Understands motion and progression
       • Can describe events and actions
    
    4. EFFICIENCY CONSIDERATIONS:
       • More frames = better understanding but slower
       • Fewer frames = faster but may miss details
       • Balance based on use case
    
    5. USE CASES:
       • Video summarization
       • Action recognition
       • Content moderation
       • Automated captioning
       • Scene detection
       • Sports analysis
    """
    
    print(concepts)


# ============================================================================
# SECTION 2: Creating Simulated Video Frames
# ============================================================================

def create_sample_video_frames():
    """
    Create a sequence of frames that simulate a video
    This simulates a ball moving across the screen
    """
    print("\n" + "=" * 60)
    print("SECTION 2: Creating Sample Video Frames")
    print("=" * 60)
    
    os.makedirs('outputs/video_frames', exist_ok=True)
    
    frames = []
    num_frames = 6
    
    print(f"\n📹 Creating {num_frames} frames simulating motion...")
    
    for i in range(num_frames):
        # Create frame
        img = Image.new('RGB', (400, 300), color=(200, 220, 255))
        draw = ImageDraw.Draw(img)
        
        # Draw ground
        draw.rectangle([0, 250, 400, 300], fill=(100, 200, 100))
        
        # Draw moving ball (moves left to right)
        ball_x = 50 + (i * 60)
        ball_y = 150
        draw.ellipse([ball_x-20, ball_y-20, ball_x+20, ball_y+20], 
                     fill=(255, 50, 50), outline=(0, 0, 0), width=2)
        
        # Add frame number
        draw.text((10, 10), f"Frame {i+1}/{num_frames}", fill=(0, 0, 0))
        
        # Save frame
        frame_path = f'outputs/video_frames/frame_{i:03d}.png'
        img.save(frame_path)
        frames.append(img)
        
        print(f"  ✅ Frame {i+1} created: Ball at position {ball_x}")
    
    print(f"\n✅ All frames saved to: outputs/video_frames/")
    return frames


# ============================================================================
# SECTION 3: Analyzing Video Frames
# ============================================================================

def analyze_video_frames():
    """
    Analyze the sequence of frames as a video
    """
    print("\n" + "=" * 60)
    print("SECTION 3: Analyzing Video Frames")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro-vision')
    
    # Create sample frames
    frames = create_sample_video_frames()
    
    # Analysis 1: Describe what's happening
    print("\n1️⃣ Video Description:")
    print("-" * 60)
    prompt = """Analyze these sequential frames from a video.
Describe what is happening in the video. What motion or action do you observe?"""
    
    # Send all frames with the prompt
    content = [prompt] + frames
    response = model.generate_content(content)
    print(f"🤖 AI Description:\n{response.text}")
    
    # Analysis 2: Specific questions
    print("\n\n2️⃣ Specific Analysis:")
    print("-" * 60)
    prompt2 = """Looking at these video frames, answer:
1. What object is moving?
2. In which direction is it moving?
3. What is the background/setting?
4. Is the motion smooth or jerky?"""
    
    content2 = [prompt2] + frames
    response2 = model.generate_content(content2)
    print(f"🤖 Detailed Analysis:\n{response2.text}")
    
    # Analysis 3: Frame-by-frame
    print("\n\n3️⃣ Frame-by-Frame Description:")
    print("-" * 60)
    prompt3 = "Describe each frame individually, noting the differences between them."
    
    content3 = [prompt3] + frames
    response3 = model.generate_content(content3)
    print(f"🤖 Frame Analysis:\n{response3.text}")


# ============================================================================
# SECTION 4: Video Frame Extraction (Real Video)
# ============================================================================

def extract_frames_from_video_demo():
    """
    Demonstrate how to extract frames from real video files
    (Requires opencv-python to be installed)
    """
    print("\n" + "=" * 60)
    print("SECTION 4: Video Frame Extraction (Code Demo)")
    print("=" * 60)
    
    print("\n📝 CODE: How to extract frames from real video files\n")
    
    code = '''
import cv2
import os

def extract_video_frames(video_path, output_folder, frames_per_second=1):
    """
    Extract frames from a video file
    
    Args:
        video_path: Path to video file
        output_folder: Where to save frames
        frames_per_second: How many frames to extract per second
    """
    # Open video
    video = cv2.VideoCapture(video_path)
    
    # Get video properties
    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps
    
    print(f"Video: {duration:.2f}s, {fps:.2f} FPS, {total_frames} frames")
    
    # Calculate frame interval
    frame_interval = int(fps / frames_per_second)
    
    # Create output folder
    os.makedirs(output_folder, exist_ok=True)
    
    frame_count = 0
    saved_count = 0
    
    while True:
        success, frame = video.read()
        
        if not success:
            break
        
        # Save frame at intervals
        if frame_count % frame_interval == 0:
            output_path = f"{output_folder}/frame_{saved_count:04d}.jpg"
            cv2.imwrite(output_path, frame)
            saved_count += 1
            print(f"Saved frame {saved_count}")
        
        frame_count += 1
    
    video.release()
    print(f"\\nExtracted {saved_count} frames to {output_folder}")
    return saved_count

# Usage example:
# extract_video_frames("my_video.mp4", "output_frames", frames_per_second=2)
'''
    
    print(code)
    
    print("\n💡 TIPS:")
    print("  • Install: pip install opencv-python")
    print("  • Adjust frames_per_second based on video length")
    print("  • More frames = better understanding but slower")
    print("  • For 1-minute video at 1 fps = 60 frames")


# ============================================================================
# SECTION 5: Advanced Video Understanding
# ============================================================================

def advanced_video_analysis():
    """
    More sophisticated video analysis
    """
    print("\n" + "=" * 60)
    print("SECTION 5: Advanced Video Understanding")
    print("=" * 60)
    
    model = genai.GenerativeModel('gemini-pro-vision')
    
    # Create a more complex animation
    print("\n📹 Creating a story-based animation...")
    frames = []
    
    # Scene 1: Day (frames 0-1)
    for i in range(2):
        img = Image.new('RGB', (400, 300), color=(135, 206, 235))  # Sky blue
        draw = ImageDraw.Draw(img)
        draw.rectangle([0, 200, 400, 300], fill=(34, 139, 34))  # Grass
        draw.ellipse([320, 30, 370, 80], fill=(255, 255, 0))  # Sun
        draw.text((150, 250), "DAY", fill=(0, 0, 0))
        frames.append(img)
    
    # Scene 2: Sunset (frames 2-3)
    for i in range(2):
        img = Image.new('RGB', (400, 300), color=(255, 150, 100))  # Orange sky
        draw = ImageDraw.Draw(img)
        draw.rectangle([0, 200, 400, 300], fill=(34, 100, 34))  # Darker grass
        draw.ellipse([320, 100, 370, 150], fill=(255, 100, 50))  # Setting sun
        draw.text((140, 250), "SUNSET", fill=(50, 50, 50))
        frames.append(img)
    
    # Scene 3: Night (frames 4-5)
    for i in range(2):
        img = Image.new('RGB', (400, 300), color=(25, 25, 112))  # Night blue
        draw = ImageDraw.Draw(img)
        draw.rectangle([0, 200, 400, 300], fill=(20, 60, 20))  # Dark grass
        draw.ellipse([340, 40, 370, 70], fill=(240, 240, 240))  # Moon
        # Stars
        for _ in range(15):
            import random
            x, y = random.randint(10, 390), random.randint(10, 190)
            draw.point((x, y), fill=(255, 255, 255))
        draw.text((150, 250), "NIGHT", fill=(200, 200, 200))
        frames.append(img)
    
    os.makedirs('outputs/video_frames', exist_ok=True)
    for i, frame in enumerate(frames):
        frame.save(f'outputs/video_frames/scene_{i:03d}.png')
    
    print("✅ Scene frames created")
    
    # Analyze the progression
    print("\n🎬 Analyzing video progression...")
    prompt = """Analyze this video sequence. It shows a time progression.

Please identify:
1. What time progression is shown? (time of day)
2. How many distinct scenes/phases are there?
3. What changes between scenes?
4. What story or concept is being communicated?
5. How would you title this short video?"""
    
    content = [prompt] + frames
    response = model.generate_content(content)
    
    print("\n" + "=" * 60)
    print("🤖 AI Video Analysis:")
    print("=" * 60)
    print(response.text)


# ============================================================================
# SECTION 6: Practical Applications
# ============================================================================

def practical_video_applications():
    """
    Real-world use cases for video AI
    """
    print("\n" + "=" * 60)
    print("SECTION 6: Practical Video Applications")
    print("=" * 60)
    
    applications = """
    🎯 REAL-WORLD USE CASES:
    
    1. 📺 VIDEO SUMMARIZATION
       • Generate text summaries of long videos
       • Create chapter markers automatically
       • Extract key moments
       
       Example: "Summarize this 1-hour lecture in 5 bullet points"
    
    2. ♿ ACCESSIBILITY
       • Auto-generate video descriptions for blind users
       • Create detailed captions
       • Identify important visual information
       
       Example: Sports commentary for visually impaired viewers
    
    3. 🎓 EDUCATION
       • Analyze educational videos for content
       • Quiz generation from video lessons
       • Identify when key concepts are explained
       
       Example: "What topics are covered in this tutorial?"
    
    4. 🛡️ CONTENT MODERATION
       • Detect inappropriate content
       • Flag policy violations
       • Monitor live streams
       
       Example: Identify violent or harmful content
    
    5. 🏃 SPORTS & FITNESS
       • Form analysis for athletes
       • Movement tracking
       • Performance metrics
       
       Example: "Is the runner's form correct?"
    
    6. 🎬 MEDIA & ENTERTAINMENT
       • Scene detection for editing
       • Automatic highlight generation
       • Content-based search
       
       Example: "Find all scenes with person X"
    
    7. 🏪 RETAIL & SECURITY
       • Customer behavior analysis
       • Inventory monitoring
       • Security incident detection
       
       Example: Detect shoplifting or safety hazards
    
    8. 🚗 AUTONOMOUS SYSTEMS
       • Object detection for self-driving
       • Action recognition
       • Environment understanding
       
       Example: "Is a pedestrian crossing the street?"
    """
    
    print(applications)


# ============================================================================
# SECTION 7: Best Practices
# ============================================================================

def video_best_practices():
    """
    Best practices for working with video AI
    """
    print("\n" + "=" * 60)
    print("SECTION 7: Best Practices for Video AI")
    print("=" * 60)
    
    practices = """
    ✅ FRAME SELECTION:
       • Short videos (<1 min): 1-2 frames per second
       • Medium videos (1-5 min): 1 frame per 2-3 seconds
       • Long videos (>5 min): Sample key moments or scenes
       • Action-heavy: More frames needed
       • Static content: Fewer frames sufficient
    
    ✅ PREPROCESSING:
       • Ensure good video quality (resolution, lighting)
       • Consider frame resizing for efficiency
       • Remove duplicate/similar frames
       • Handle different aspect ratios
    
    ✅ PROMPTING:
       • Be specific about what to look for
       • Mention if temporal order matters
       • Ask about changes between frames
       • Specify detail level needed
    
    ✅ PERFORMANCE:
       • Processing time ∝ number of frames
       • Balance accuracy vs. speed
       • Consider batch processing for efficiency
       • Cache results when possible
    
    ✅ LIMITATIONS:
       • May miss very fast actions
       • Text in video may be hard to read
       • Low-quality video affects results
       • Very long videos need strategic sampling
    
    ✅ ETHICAL CONSIDERATIONS:
       • Privacy: Blur faces when needed
       • Consent: Get permission for surveillance
       • Bias: AI may misinterpret cultural context
       • Transparency: Disclose AI usage
    """
    
    print(practices)


# ============================================================================
# SECTION 8: Complete Example Workflow
# ============================================================================

def complete_video_workflow():
    """
    End-to-end video processing example
    """
    print("\n" + "=" * 60)
    print("SECTION 8: Complete Video Analysis Workflow")
    print("=" * 60)
    
    print("\n📋 WORKFLOW STEPS:\n")
    
    workflow = """
    STEP 1: VIDEO PREPARATION
    -------------------------
    • Load video file using cv2.VideoCapture()
    • Check video properties (fps, duration, resolution)
    • Decide on frame sampling rate
    
    STEP 2: FRAME EXTRACTION
    ------------------------
    • Extract frames at chosen intervals
    • Save frames or keep in memory
    • Optionally resize for efficiency
    
    STEP 3: FRAME PREPARATION
    -------------------------
    • Convert frames to PIL Image objects
    • Ensure correct format (RGB)
    • Optionally preprocess (resize, enhance)
    
    STEP 4: AI ANALYSIS
    -------------------
    • Initialize gemini-pro-vision model
    • Create prompt based on use case
    • Send frames + prompt to model
    • Handle response
    
    STEP 5: POST-PROCESSING
    -----------------------
    • Parse AI response
    • Extract relevant information
    • Format for user/application
    • Store results if needed
    
    STEP 6: ACTION
    --------------
    • Generate summary report
    • Trigger alerts if needed
    • Update database/UI
    • Provide user feedback
    """
    
    print(workflow)
    
    print("\n💻 SAMPLE CODE STRUCTURE:\n")
    
    code = """
def process_video(video_path):
    # 1. Extract frames
    frames = extract_frames(video_path, sample_rate=1)
    
    # 2. Prepare for AI
    pil_frames = [frame_to_pil(f) for f in frames]
    
    # 3. Analyze with AI
    model = genai.GenerativeModel('gemini-pro-vision')
    prompt = "Summarize what happens in this video"
    response = model.generate_content([prompt] + pil_frames)
    
    # 4. Process results
    summary = response.text
    
    # 5. Return or display
    return {
        'summary': summary,
        'frame_count': len(frames),
        'duration': calculate_duration(video_path)
    }
"""
    
    print(code)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main function with menu
    """
    print("\n")
    print("🎓 " + "=" * 58 + " 🎓")
    print("     GENERATIVE AI SESSION - MODULE 4: VIDEO CHAT")
    print("🎓 " + "=" * 58 + " 🎓")
    
    menu = """
    Choose a section to run:
    
    1. Video Processing Concepts
    2. Create Sample Video Frames
    3. Analyze Video Frames
    4. Frame Extraction Code Demo
    5. Advanced Video Understanding
    6. Practical Applications
    7. Best Practices
    8. Complete Workflow Example
    
    all - Run all sections
    quit - Exit
    
    """
    
    while True:
        print(menu)
        choice = input("Your choice: ").strip().lower()
        
        if choice in ['quit', 'q', 'exit']:
            print("👋 Goodbye!")
            break
        elif choice == '1':
            video_processing_concepts()
        elif choice == '2':
            create_sample_video_frames()
        elif choice == '3':
            analyze_video_frames()
        elif choice == '4':
            extract_frames_from_video_demo()
        elif choice == '5':
            advanced_video_analysis()
        elif choice == '6':
            practical_video_applications()
        elif choice == '7':
            video_best_practices()
        elif choice == '8':
            complete_video_workflow()
        elif choice == 'all':
            video_processing_concepts()
            create_sample_video_frames()
            analyze_video_frames()
            extract_frames_from_video_demo()
            advanced_video_analysis()
            practical_video_applications()
            video_best_practices()
            complete_video_workflow()
            print("\n✅ All sections completed!")
            break
        else:
            print("⚠️  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
    # Teaching Questions:
    # 1. How does AI "understand" video?
    # 2. Why is frame selection important?
    # 3. What are trade-offs between accuracy and speed?
