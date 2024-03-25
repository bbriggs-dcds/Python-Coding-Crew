
# Week 2 - Variables and Comments

## Table of Contents

1. [Introduction](#introduction)
1. [Comments](#comments)
1. [Variables](#variables)

### 1) Introduction <a name="introduction"></a>

Variables in Python are important for storing data, and having the ability to manipulate it.
They act as containers for different types of data, like numbers or text or Boolean values (True or False). We can create a variable called "name" and assign it a string like "John" to represent a player's name. We could even create one named "age" and assign it a number like 25 to represent a person's age. Variables can be used throughout the program to perform operations like displaying information, or making decisions based on what data is stored.

Commenting code is an important practice to understand what the code is doing. Often times we'll have to refer to code that's been written a long time ago, or even worse, somebody else's. In Python, we use comments to write little notes to ourselves (and others) to help us understand what different parts of our code does. If we're writing a game, we might put a comment next to the part of the code that checks if somebody has won, saying "Check for winner".

### 2) Comments <a name="comments"></a>

#### Comments

- **Definition**:
  - Comments are lines in the code that are not executed by the program.
- **Purpose**:
  - Comments help us keep code readable, and understandable by providing context and by explaining why or how something works.
- In Python, comments begin with "#", and everything after will be ignored.

   ```python
   # This is a comment
   player_score = 100 # Assigning initial score to the player
   ```

#### Doc Strings

- **Definition**:
  - Doc strings are triple-quoted (""") strings placed after the definition of a
    function, module, class or method.
- **Purpse**:
  - Using docstrings provide a way to document the purpose, usage, parameters and/or return
    values of functions.
- Docstrings follow a specific format, including a description of the function's purpose,
  information about it's parameters and it's return value. It could also include basic usage.

  ```python
  def calculate_area(radius):

    """
    Calculate the area of a circle given its radius.

    Parameters:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.

    Example:
        >>> calculate_area(3)
        28.274333882308138
    """

    pi = 3.14159
    area = pi * radius ** 2
    return area

    # Calling the function
    print("Area of the circle:", calculate_area(5))
    ```

### 3) Variables and Data types <a name="variables"></a>

- **Defintion**:
  - A variable is a symbolic name given to pieces of data that can be later referenced or changed when the program runs. Variables help us store information that we can later use or manipulate if needed.
- **Naming Conventions**:
  - Variable names typically start with a lowercase letter or an underscore ("_")
  - Only contains alphanumeric characters (A-z, 0-9 and "_"), no spaces!
  - Use descriptive names, they will help indicate it's purpose or usage.
  - They are case sensitive.

      ```python
      player_name = "Alice"
      player_score = 100
      ```

  - It is best practice to follow a consistent naming style (e.g., camelCase or snake_case). This will help imporve readability in the future when revisiting code.
- **Data Types**:
  - Integers, floats, strings
  - Integers are whole numbers, ie 1 or 3765.
  - Floats are decimal numbers, ie 9.75 or 3.14159
  - Strings is a sequence(s) of characters, ie "Hello World" or "A"
- **How to assign a variable**:
  - To assign a variable we first declare the variable by defining it with a name

      ```python
      var1 = 0
      ```

  - You can nest variables too, by assigning it to another variable.

     ```python
     num1 = 4
     num2 = 2
     sum_of_nums = (num1 * num2)
     print(sum_of_nums)
     ```
