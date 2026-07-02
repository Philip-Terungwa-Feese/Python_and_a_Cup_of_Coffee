# 3rd NELIREF Data Science and AI Summer School 2026

## Instructor (s)

Peter Denen Tsaha

## Python Programming Basics for Beginners

A comprehensive repository introducing fundamental Python programming concepts with clear explanations, practical examples, and hands-on exercises.

## Overview

This interactive notebooks are designed for absolute beginners who want to learn Python from scratch. It covers essential concepts and provides a foundation for further programming studies.

## What You'll Learn

- **Variables and Data Types** - Understand how to store and work with different types of data
- **Operators** - Learn arithmetic, comparison, and logical operations
- **Control Flow** - Master if/else statements to make decisions in code
- **Loops** - Repeat code efficiently with for and while loops
- **Functions** - Write reusable code blocks with functions and parameters
- **Data Structures** - Work with lists and dictionaries
- **Best Practices** - Learn Python coding conventions and patterns

## Table of Contents

1. Variables and Data Types
2. Operators (Arithmetic, Comparison, Logical)
3. Control Flow (if/elif/else)
4. Loops (for, while, break, continue)
5. Functions (Definition, Parameters, Return Values)
6. Lists and Dictionaries
7. Practice Exercises

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Jupyter Notebook or JupyterLab installed

### Installation

#### Option 1: Install Jupyter with Anaconda (Recommended for beginners)
```bash
# Download Anaconda from https://www.anaconda.com/download
# Follow the installation instructions for your operating system

# Then open Anaconda Navigator and launch Jupyter Notebook
```

#### Option 2: Install with pip
```bash
pip install jupyter notebook
```

#### Option 3: Use Google Colab (No installation needed!)
1. Go to https://colab.research.google.com/
2. Click "File" → "Upload notebook"
3. Select the Python_Basics_for_Beginners.ipynb file
4. Start learning immediately!

### Running the Notebook

```bash
# Navigate to the notebook directory
cd path/to/notebook/directory

# Start Jupyter Notebook
jupyter notebook

# Click on Python_Basics_for_Beginners.ipynb to open it
```

## How to Use This Notebook

1. **Read the explanations** - Each section starts with clear explanations of concepts
2. **Run the examples** - Execute code cells to see outputs immediately
3. **Experiment** - Modify code examples and see what happens
4. **Take notes** - Add your own markdown cells with notes
5. **Complete exercises** - Work through the practice problems at the end

### Keyboard Shortcuts (Jupyter)

| Action | Shortcut |
|--------|----------|
| Run cell | `Shift + Enter` |
| Add cell below | `B` |
| Delete cell | `D D` (press D twice) |
| Switch to markdown | `M` |
| Switch to code | `Y` |
| Edit mode | `Enter` |
| Command mode | `Esc` |

## Practice Exercises

The notebook includes 5 progressive exercises:

1. **Temperature Converter** - Convert Celsius to Fahrenheit using functions
2. **Sum Calculator** - Create a function to sum a list of numbers
3. **Letter Counter** - Count character frequency using dictionaries
4. **Even Number Filter** - Filter even numbers from a list
5. **Rock-Paper-Scissors Game** - Build an interactive game with user input

**Solutions** - Try solving these yourself first! If you get stuck, ask for hints or look up similar examples in the notebook.

## Learning Path

```
Week 1: Variables → Operators → Control Flow
Week 2: Loops → Functions
Week 3: Lists & Dictionaries → Practice Exercises
Week 4: Build your own project!
```

## Resources for Further Learning

### Official Documentation
- [Python Official Docs](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)

### Interactive Learning
- [Python.org Interactive Shell](https://www.python.org/)
- [Replit](https://replit.com/) - Free online IDE
- [LeetCode](https://leetcode.com/) - Coding challenges

### Books
- *Python Crash Course* by Eric Matthes
- *Automate the Boring Stuff with Python* by Al Sweigart (free online)

### YouTube Channels
- [Corey Schafer](https://www.youtube.com/c/Coreyms)
- [Tech with Tim](https://www.youtube.com/c/TechWithTim)
- [Programming with Mosh](https://www.youtube.com/c/programmingwithmosh)

## Tips for Success

**Code along** - Type the examples yourself, don't just copy-paste  
**Break things** - Experiment and make mistakes; that's how you learn  
**Debug systematically** - Read error messages carefully  
**Practice daily** - Even 15 minutes a day compounds over time  
**Build projects** - Apply what you learn to real problems  
**Join communities** - Connect with other learners for support  

## Common Python Patterns

### Variable Naming Convention
```python
# Use lowercase with underscores (snake_case)
my_variable = 10
user_name = "Alice"

# Avoid single letters except in loops
# i, j, k are OK for loop counters
```

### Commenting Best Practices
```python
# Use comments to explain WHY, not WHAT
# Good: Convert temperature to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32

# Avoid: Add 32 to the result
```

### Function Naming
```python
# Functions should describe what they do
def calculate_total_price(items):
    pass

def is_even(number):
    pass

def get_user_input():
    pass
```

## Troubleshooting

### "ModuleNotFoundError" when importing libraries
```bash
pip install module_name
# Example: pip install numpy pandas
```

### Code runs but output is confusing
- Add `print()` statements to see intermediate values
- Use `type()` to check variable types
- Break complex operations into smaller steps

### Jupyter kernel keeps crashing
- Restart the kernel: Kernel → Restart
- Close other applications using RAM
- Update Jupyter: `pip install --upgrade jupyter`

## Contributing

Found an error? Have a suggestion?
1. Fork this repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This notebook is released under the MIT License - feel free to use, modify, and share!

## Getting Help

- **In the notebook** - Hover over error messages and read them carefully
- **Online** - Search your error message on Stack Overflow
- **Communities** - Ask on Reddit (/r/learnprogramming), Discord servers
- **Official Docs** - Python's documentation is excellent

## What's Next After This Notebook?

Once you've mastered the basics:

1. **Object-Oriented Programming (OOP)** - Classes and objects
2. **File I/O** - Read and write files
3. **Libraries** - NumPy, Pandas, Matplotlib for data science
4. **Web Development** - Flask or Django frameworks
5. **Automation** - Scripts to automate tasks
6. **Data Science** - Machine learning with scikit-learn
7. **Competitive Programming** - Solve algorithmic challenges

## Author

Created for beginners learning Python programming.

---

**Happy Coding!**

Questions? Issues? Create an issue on GitHub or reach out!

Remember: Every expert was once a beginner. Keep practicing, stay curious, and enjoy the learning journey!
