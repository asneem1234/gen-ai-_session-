# VS Code Documentation: Getting Started for Beginners

Welcome to Visual Studio Code! This guide will help you get started with one of the most popular code editors.

## Table of Contents
1. [What is VS Code?](#what-is-vs-code)
2. [Installation](#installation)
3. [First Steps](#first-steps)
4. [Basic Interface](#basic-interface)
5. [Essential Features](#essential-features)
6. [Keyboard Shortcuts](#keyboard-shortcuts)
7. [Extensions](#extensions)
8. [Working with Files](#working-with-files)
9. [Integrated Terminal](#integrated-terminal)
10. [Tips for Beginners](#tips-for-beginners)

---

## What is VS Code?

Visual Studio Code (VS Code) is a free, open-source code editor developed by Microsoft. It's lightweight, fast, and supports virtually every programming language through extensions.

**Key Benefits:**
- Free and cross-platform (Windows, Mac, Linux)
- Built-in Git integration
- IntelliSense (intelligent code completion)
- Extensive extension marketplace
- Integrated debugging tools
- Customizable themes and settings

---

## Installation

### Download and Install

1. Visit [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Click the download button for your operating system
3. Follow the installation instructions for your OS (see below)

### Windows Installation
1. Run the downloaded installer (.exe file)
2. Follow the setup wizard prompts
3. Check "Add to PATH" option (recommended)
4. Launch VS Code after installation

### Mac Installation
1. Download the .zip file for macOS
2. Double-click the downloaded file to extract it
3. Drag "Visual Studio Code.app" to your Applications folder
4. Launch VS Code from Applications or Spotlight

**Mac Setup Tips:**
- First time opening: Right-click the app and select "Open" if you get a security warning
- Add VS Code to Dock: Right-click the icon in Dock → Options → Keep in Dock
- Install 'code' command: Open Command Palette (`Cmd+Shift+P`) → type "Shell Command: Install 'code' command in PATH"

**Video Tutorials for Mac**: 
- [VS Code Installation on Mac](https://youtu.be/w0xBQHKjoGo?si=weipAA8QUgJYODZx)
- [Python Setup in VS Code on Mac](https://youtu.be/mtCqZZ-7jfg?si=LrAEy_w2nvFBaDhZ)

### Linux Installation
1. Download the appropriate package (.deb, .rpm, or .tar.gz)
2. Install using your package manager
3. Launch from applications menu or terminal with `code`

### System Requirements
- **Windows**: Windows 7, 8, 10, or 11
- **Mac**: macOS 10.11 or higher
- **Linux**: Debian, Ubuntu, Red Hat, Fedora, or SUSE

---

## Setting Up Python

### Python Setup for Windows

If you're planning to do Python development on Windows, follow these steps:

#### 1. Install Python
- Download Python from [python.org](https://www.python.org/downloads/)
- Run the installer
- **Important**: Check "Add Python to PATH" during installation

#### 2. Install Python Extension in VS Code
1. Open VS Code
2. Click Extensions icon (or press `Ctrl+Shift+X`)
3. Search for "Python" by Microsoft
4. Click **Install**

#### 3. Select Python Interpreter
1. Open a Python file (`.py`)
2. Press `Ctrl+Shift+P` → type "Python: Select Interpreter"
3. Choose your installed Python version

#### 4. Verify Setup
Create a test file and run it:
```python
print("Hello, Python on Windows!")
```
Press `Ctrl+Alt+N` or right-click → "Run Python File in Terminal"

**Complete Tutorial**: [Python Setup in VS Code on Windows](https://youtu.be/mIVB-SNycKI?si=6kmmSyiYUWlqRrFK)

---

### Python Setup for Mac

If you're planning to do Python development on Mac, follow these steps:

#### 1. Install Python
- Download Python from [python.org](https://www.python.org/downloads/)
- Or use Homebrew: `brew install python3`

#### 2. Install Python Extension in VS Code
1. Open VS Code
2. Click Extensions icon (or press `Cmd+Shift+X`)
3. Search for "Python" by Microsoft
4. Click **Install**

#### 3. Select Python Interpreter
1. Open a Python file (`.py`)
2. Press `Cmd+Shift+P` → type "Python: Select Interpreter"
3. Choose your installed Python version

#### 4. Verify Setup
Create a test file and run it:
```python
print("Hello, Python on Mac!")
```
Press `Ctrl+Option+N` or right-click → "Run Python File in Terminal"

**Complete Tutorial**: [Python Setup in VS Code on Mac](https://youtu.be/mtCqZZ-7jfg?si=LrAEy_w2nvFBaDhZ)

---

## First Steps

### 1. Open VS Code
Launch the application from your applications menu or desktop shortcut.

### 2. Open a Folder
- Click **File → Open Folder** (or `Ctrl+K Ctrl+O`)
- Select a folder where you want to work
- This folder becomes your "workspace"

### 3. Create Your First File
- Click **File → New File** (or `Ctrl+N`)
- Type some code or text
- Save it with **File → Save** (or `Ctrl+S`)

---

## Basic Interface

VS Code's interface consists of several key areas:

### 1. **Activity Bar** (Left Side)
- **Explorer**: Browse files and folders
- **Search**: Find and replace across files
- **Source Control**: Git integration
- **Run and Debug**: Debug your code
- **Extensions**: Install and manage extensions

### 2. **Side Bar**
Shows different views based on what you select in the Activity Bar.

### 3. **Editor**
The main area where you write and edit code. You can open multiple editors side by side.

### 4. **Status Bar** (Bottom)
Displays information about the current file, line/column numbers, language mode, and more.

### 5. **Panel** (Bottom)
Contains the integrated terminal, output, problems, and debug console.

---

## Essential Features

### 1. IntelliSense
Intelligent code completion that suggests code as you type.
- Triggered automatically or with `Ctrl+Space`
- Shows available methods, parameters, and documentation

### 2. Multi-Cursor Editing
Edit multiple locations at once:
- Hold `Alt` and click to add cursors
- `Ctrl+Alt+Down/Up` to add cursors above/below
- `Ctrl+D` to select next occurrence of current word

### 3. Command Palette
Access all VS Code commands:
- Press `Ctrl+Shift+P` (or `F1`)
- Type to search for any command
- Essential for discovering features

### 4. Quick File Navigation
- `Ctrl+P` to quickly open files by name
- `Ctrl+Tab` to switch between recent files

### 5. Split Editor
View multiple files side by side:
- `Ctrl+\` to split editor
- Drag files to create new editor groups

---

## Keyboard Shortcuts

### Most Important Shortcuts

| Action | Windows/Linux | Mac |
|--------|--------------|-----|
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| Quick Open File | `Ctrl+P` | `Cmd+P` |
| Toggle Terminal | `` Ctrl+` `` | `` Cmd+` `` |
| New File | `Ctrl+N` | `Cmd+N` |
| Save | `Ctrl+S` | `Cmd+S` |
| Save All | `Ctrl+K S` | `Cmd+K S` |
| Find | `Ctrl+F` | `Cmd+F` |
| Replace | `Ctrl+H` | `Cmd+H` |
| Find in Files | `Ctrl+Shift+F` | `Cmd+Shift+F` |
| Toggle Comment | `Ctrl+/` | `Cmd+/` |
| Format Document | `Shift+Alt+F` | `Shift+Option+F` |
| Go to Line | `Ctrl+G` | `Cmd+G` |
| Delete Line | `Ctrl+Shift+K` | `Cmd+Shift+K` |
| Copy Line Down | `Shift+Alt+Down` | `Shift+Option+Down` |
| Move Line Up/Down | `Alt+Up/Down` | `Option+Up/Down` |

### View Shortcuts Cheatsheet
- Go to **Help → Keyboard Shortcuts Reference**
- Or press `Ctrl+K Ctrl+R`

---

## Extensions

Extensions add powerful features to VS Code.

### Installing Extensions

1. Click the Extensions icon in Activity Bar (or `Ctrl+Shift+X`)
2. Search for an extension
3. Click **Install**
4. Reload VS Code if prompted

### Essential Extensions for Beginners

- **Python**: Python language support
- **Prettier**: Code formatter for web development
- **ESLint**: JavaScript linting
- **Live Server**: Launch local development server
- **GitLens**: Enhanced Git integration
- **Bracket Pair Colorizer**: Color-code matching brackets
- **Path Intellisense**: Autocomplete file paths
- **Material Icon Theme**: Better file icons
- **One Dark Pro**: Popular color theme

---

## Working with Files

### Creating Files and Folders
- Right-click in Explorer → **New File** or **New Folder**
- Or use the icons at the top of the Explorer panel

### File Search
- `Ctrl+P` then type filename
- Use fuzzy matching: type parts of the filename

### Find and Replace
- **In current file**: `Ctrl+F` (find), `Ctrl+H` (replace)
- **In all files**: `Ctrl+Shift+F` (find), `Ctrl+Shift+H` (replace)

### File Tabs
- Close tab: `Ctrl+W`
- Close all tabs: `Ctrl+K W`
- Reopen closed tab: `Ctrl+Shift+T`

---

## Integrated Terminal

VS Code includes a built-in terminal.

### Opening the Terminal
- Press `` Ctrl+` `` (backtick)
- Or **View → Terminal**

### Terminal Features
- Run command-line programs without leaving VS Code
- Multiple terminals: click **+** to add more
- Split terminals: click the split icon
- Switch between terminals using the dropdown

### Common Commands
```bash
# Navigate directories
cd folder_name
cd ..

# List files
dir         # Windows
ls          # Mac/Linux

# Run Python file
python script.py

# Install packages
npm install package_name
pip install package_name
```

---

## Tips for Beginners

### 1. Learn the Command Palette
`Ctrl+Shift+P` is your best friend. You can access almost everything from here.

### 2. Customize Your Settings
- Go to **File → Preferences → Settings** (or `Ctrl+,`)
- Search for settings you want to change
- Try different themes: **File → Preferences → Color Theme**

### 3. Use Workspaces
Save your folder setup as a workspace:
- **File → Save Workspace As...**
- Reopen it later with all your settings preserved

### 4. Enable Auto Save
- **File → Auto Save** (toggle on)
- Never lose work again!

### 5. Explore the Marketplace
Browse [marketplace.visualstudio.com](https://marketplace.visualstudio.com/) for extensions.

### 6. Use Zen Mode
- Press `Ctrl+K Z` for distraction-free coding
- Press `Esc Esc` to exit

### 7. Learn Git Basics
VS Code has excellent Git integration. Learn basic Git commands to track your code changes.

### 8. Watch for Notifications
VS Code often suggests helpful extensions based on the files you open.

### 9. Read the Docs
Visit [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs) for comprehensive documentation.

### 10. Practice Makes Perfect
The more you use VS Code, the more efficient you'll become!

---

## Next Steps

Once you're comfortable with the basics:

1. **Learn debugging**: Use breakpoints and the debug panel
2. **Explore snippets**: Create custom code snippets for repetitive code
3. **Configure linters**: Set up code quality tools for your language
4. **Try pair programming**: Use Live Share extension to code with others
5. **Customize keybindings**: Make shortcuts that work for you

---

## Additional Resources

- **Official Docs**: [code.visualstudio.com/docs](https://code.visualstudio.com/docs)
- **Intro Videos**: [code.visualstudio.com/docs/getstarted/introvideos](https://code.visualstudio.com/docs/getstarted/introvideos)
- **Tips and Tricks**: [code.visualstudio.com/docs/getstarted/tips-and-tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
- **Keyboard Shortcuts**: [code.visualstudio.com/shortcuts](https://code.visualstudio.com/shortcuts)

---

## Need Help?

- Press `F1` and search for "Help"
- Visit the [VS Code Community](https://github.com/microsoft/vscode/discussions)
- Check [Stack Overflow](https://stackoverflow.com/questions/tagged/visual-studio-code)

---

**Happy Coding!** 🚀
