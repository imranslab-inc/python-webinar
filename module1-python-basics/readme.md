# -*- Python Basics -*-

- Introduction to Python and its history
- Setting up Python and IDE (e.g., Jupyter Notebook)
- Basic syntax and data types (variables, numbers, strings)
- Printing and user input
- Conditional statements (if, elif, else)
- Loops (for and while)
- Hands-on exercises and coding examples

Here's some content for Module 1: Python Basics. This module covers the fundamental concepts of Python programming.

---

**Module 1: Python Basics (1 hour)**

*Introduction to Python:*

- Python is a high-level, interpreted programming language known for its simplicity and readability. It is widely used for web development, data analysis, machine learning, and more.

*Setting up Python:*

- To get started with Python, you'll need to install it on your computer. You can download Python from the official website (<https://www.python.org/downloads/>). We recommend using the latest stable version.

*Basic Syntax and Data Types:*

- Python uses straightforward syntax. Here are some essential concepts:
  - **Variables:** Containers for storing data.
  - **Numbers:** Integers (whole numbers) and floating-point numbers (decimal numbers).
  - **Strings:** Sequences of characters, enclosed in single (' ') or double (" ") quotes.
  - **Comments:** Lines that start with '#' are comments and are ignored by the interpreter.

Example:

```python
# This is a comment
name = "John"  # Assigning a string to a variable
age = 30       # Assigning an integer to a variable
height = 5.9   # Assigning a float to a variable
```

*Printing and User Input:*

- You can use the `print()` function to display information to the console.

Example:

```python
print("Hello, world!")  # Prints the text to the console
```

- Use `input()` to get user input.

Example:

```python
name = input("Enter your name: ")  # Prompt the user for input
print("Hello, " + name)           # Display a personalized message
```

*Conditional Statements:*

- Conditional statements are used for decision-making in code. Python uses `if`, `elif`, and `else` for this purpose.

Example:

```python
age = 25

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```

*Loops:*

- Loops are used for repetitive tasks. Python has `for` and `while` loops.

Example (for loop):

```python
for i in range(5):
    print(i)
```

Example (while loop):

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

*Hands-on Exercises:*

- Conduct hands-on exercises with participants to practice the concepts covered in this module. For example, you can have them write a Python program that asks for user input and performs some conditional operations based on that input.

---

Feel free to expand upon these topics and provide additional examples or exercises to help participants grasp the basics of Python programming.
