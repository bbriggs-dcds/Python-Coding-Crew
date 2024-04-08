
# Week 3 - Lists

## Table of Contents

1. [Introduction](#introduction)
1. [Lists](#lists)

### 1) Introduction <a name="introduction"></a>

Lists are the most commonly used data structures in Python. They're an ordered collection of items, meaning that the items are stored in a speicific order and can be accessed using their index. Lists are mutable, which means they can be changed and manipulated after creation, which allows for dynamic manipulation of data. This means that after creating a list, we can add or remove items from the list.

Lists are 0-index based, meaning that the first item of the list is accesible at index 0, the 2nd item at index 1 and so on.

``` python
# Example: Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Output: apple

# Modifying lists
fruits[1] = "orange"  # Modify element at index 1
fruits.append("grape")  # Add element to the end
```

There are other data structures used in Python, that have more niche uses.

- Tuples
  - Are simliar to lists but are immutable (cannot be changed after creation).
- Sets
  - Somewhat similar to lists and tuples, but they're unordered and unique. (No item can be the same and aren't ordered).
- Dictionaries
  - Similar to sets, each item is unique and unordered, however each item is a key with a corresponding value.

### 2) Lists <a name="lists"></a>

- **Accessing Lists**:
  - You can use index notation to access each element (item) in a list, tuple or even a string.

    ``` python
    # Creating a list
    fruits = ["apples", "bananas", "oranges"]

    # Accessing an element (item) of a list
    print(fruits[0]) # Output: apples

    # Accessing a character of a string
    print(fruits[0][0]) # Output: a

    player_name = "Alice"
    print(player_name[0]) # Output: A
    ```

- **List Manipulation**:
  - To add or remove elements or items from a list, you can call append() or remove()

    ```python
    # Creating a list
    fruits = ["apples", "bananas", "oranges"]

    # Adding another fruit
    fruits.append("grapes")

    # Remove a fruit
    fruits.remove("apples")

    print(fruits)
    ```

    ```bash
    Output:
    ['bananas', 'oranges', 'grapes']
    ```

  - You can also reassign a value, new or old, to an index

      ```python
      # Creating a list
      fruits = ["apples", "bananas", "oranges"]
      fruits[0] = "grapes"

      print(fruits)
      ```

      ```bash
      Output:
      ['grapes', 'bananas', 'oranges']
      ```
