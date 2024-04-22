
# Week 5 - Functions

## Table of Contents

1. [Introduction](#introduction)
2. [Functions](#functions)

### 1) Introduction <a name="introduction"></a>

Functions in Python are resuable blocks of code, that performs a specific task. They allow you to organize code into seperable units, making it easier to manage, reuse and debug.

### 2) Functions <a name="functions"></a>

#### Defining Functions

To define a function, we use the "def" keyword, followed by the name of the function, and parentheses "()". Any parameters, or arguments, that a function takes are lissed within the parentheses. The code block inside the function is indented (just like if/elif/else statements!) and contains the instructions to execute when the function is called.

Functions are a fundamental concept in programming. It helps allow you to break down large, complex tasks into smaller, manageable pieces.

```python
def greet(name):
    print("Hello, " + name + "!")
```

#### Calling Functions

To execute a function, you simply just need to write its name followed by the parentheses "()" with any required arguments, or parameters inside.

```python
greet("Alice")
```

```bash
Output:
"Hello, Alice!"
```

#### Returning Values

Functions can also return values, using the "return" statement. This allows the function to compute a result and pass it back to the caller.

```python
def add(a, b):
    return a + b

print(add(7,5))
```

```bash
Output:
12
```

#### Function Documentation

It's good practice to document your functions using docstrings. This can help provide information about the purpose of the function, its parameters (or arguments) and its return value.

```python
def add(a, b):
    """Add two numbers, A and B, and return the result"""
    return a + b
```
