
# Week 4 - Conditionals and Loops

## Table of Contents

1. [Introduction](#introduction)
2. [Comparisons](#comparisons)
3. [Conditionals](#conditionals)
4. [Looping](#looping)

### 1) Introduction <a name="introduction"></a>

Conditionals are used in programming to make decisions. In Python, we have "if", "elif" (short for "else if" and "else" statements that help us control the flow of the program based on if certain conditions.

Loops are used to repeat blocks of code multiple times. In Python, we have two main looping methods: "for" and "while" loops.

### 2) Comparisons <a name="comparisons"></a>

Comparisons involve evaluating conditions or relationships between values or expressions. They help us determine whether a condition is true or false based on the comparison result. Some common comparison operators include:

- `==` (equal to)
- `!=` (not equal to)
- `<` (less than)
- `>` (greater than)
- `<=` (less than or equal to)
- `>=` (greater than or equal to)

Operators are used to compare values and produce a Boolean (True or False) result.

### 3) Conditionals <a name="conditionals"></a>

#### If/Elif/Else Statements

- If/Elif/Else statements allows us to execute (run) different blocks of code based on whether or not a certain condition has been met. If "if" statement checks if a condition is true or not, and runs the block of code following it. If the condition is false, then the program moves onto the next segment, the "elif" (short for "else if") statement, which checks if another condition is met. If none of those conditions are met, then the program moves onto the last segment, the else statement.

    ``` python
    # Example: Determine if a number is positive, negative, or zero
    num = 10

    if num > 0:
        print("The number is positive")
    elif num < 0:
        print("The number is negative")
    else:
        print("The number is zero")
    ```

#### Match Statements

- Match statements are essentially a bigger if/elif/else statement. They compare a value against a series of patterns and then execute the corresponding blocks of code. They help simplifiy complex conditional statements, and makes things readable and more concise.
  
    ```python
    # Example: Match statement to categorize a value
    value = 3

    match value:
        case 0:
            print("Value is zero")
        case 1 | 2 | 3:
            print("Value is between 1 and 3")
        case str() as s:
            print(f"Value is a string: {s}")
        case _:
            print("Value does not match any pattern")
    ```

### 4) Looping <a name="looping"></a>

#### For Loops
  
- For loops are used to iterate over a sequence. Such as data structures, like lists or dictionaries, or a string. They consist of a loop variable that iterates over each item in the sequence. For loops are suitable when you know the number of iterations in advance, or when you want to iterate over a specific sequence.

    ```python
    # Example: For loop to iterate over a list of numbers
    numbers = [1, 2, 3, 4, 5]

    for num in numbers:
        print(num)
    ```

#### While Loops

- While loops are used to execute a block of code repeatedly, as long as the condition is true. They consist of a condition that's checked before each iteration. If the condition evaluates to true, then the block of code inside the loop is executed. The loop continues iterating until the condition is false. While loops are suitable for when you don't know the exact number of iterations in advance, or when you want to repeat a block of code until a certain condition is met.

    ```python
    # Example: While loop to count down from 5 to 1
    count = 5

    while count > 0:
        print(count)
        count -= 1
    ```
