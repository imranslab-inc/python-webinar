# Module 3: Data Structures (1 hour)

## Introduction to Data Structures in Python

- Data structures are fundamental for organizing and manipulating data efficiently in Python.
- Python provides several built-in data structures, each with its own characteristics and use cases.

## Lists in Python

- Lists are ordered collections of items enclosed in square brackets, e.g., `[1, 2, 3]`.
- Lists can contain elements of different data types.
- Basic list operations: indexing, slicing, appending, and more.
- List comprehensions for concise list creation.

```python
# Examples of list operations
my_list = [1, 2, 3, 4, 5]
print(my_list[0])       # Accessing the first element
print(my_list[1:3])     # Slicing
my_list.append(6)       # Appending an element
```

## Tuples and Their Immutability

- Tuples are similar to lists but are immutable, meaning their values cannot be changed once defined.
- Tuples are often used to represent fixed collections of data.
- Tuple packing and unpacking.

```python
# Examples of tuples
my_tuple = (1, 2, 3)
x, y, z = my_tuple  # Tuple unpacking
```

## Dictionaries in Python

- Dictionaries are unordered collections of key-value pairs enclosed in curly braces, e.g., `{'name': 'John', 'age': 30}`.
- Keys are unique and immutable, while values can be of any data type.
- Dictionary operations: accessing, adding, modifying, and deleting key-value pairs.

```python
# Examples of dictionaries
my_dict = {'name': 'John', 'age': 30}
print(my_dict['name'])  # Accessing a value by key
my_dict['city'] = 'New York'  # Adding a new key-value pair
del my_dict['age']  # Deleting a key-value pair
```

## Sets in Python

- Sets are unordered collections of unique elements enclosed in curly braces, e.g., `{1, 2, 3}`.
- Sets are used for tasks that involve unique elements or testing membership.
- Set operations: union, intersection, difference, and more.

```python
# Examples of sets
my_set = {1, 2, 3}
my_set.add(4)  # Adding an element to a set
```

## Practical Exercises with Data Structures

- Engage participants with hands-on exercises to reinforce the concepts.
- Tasks could include creating and manipulating lists, tuples, dictionaries, and sets.
- Encourage participants to solve real-world problems using these data structures.

---

Feel free to expand on these topics, provide more examples, and include interactive exercises to make the learning experience engaging and practical for your participants.
