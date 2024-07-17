### Module 1: Introduction to Data Types in Python

**Objective**: Understand the basic data types in Python and their usage.


#### 1. Overview of Data Types

Python has a rich set of data types that can be broadly categorized into primitive (basic) and non-primitive (complex) types.

**Primitive Data Types**:
- **int**: Integer numbers
- **float**: Floating-point numbers
- **bool**: Boolean values (`True` or `False`)

**Non-Primitive Data Types**:
- **tuple**: Immutable ordered collection
- **dict**: Mutable unordered collection of key-value pairs
- **list**: Mutable ordered collection
- **object**: Instances of user-defined classes

---

#### 2. Integers (`int`)

- **Definition**: Whole numbers, positive or negative, without decimals.
- **Usage**: Used for counting, indexing, and as loop counters.

**Example**:
```python
a = 10
b = -5
c = 0
```

**Operations**:
- Addition: `a + b`
- Subtraction: `a - b`
- Multiplication: `a * b`
- Division: `a / b` (results in a float)
- Floor Division: `a // b` (integer result)
- Modulus: `a % b` (remainder)
- Exponentiation: `a ** b` (a raised to the power of b)

---

#### 3. Floating-Point Numbers (`float`)

- **Definition**: Numbers with decimal points.
- **Usage**: Used for precise calculations and scientific computations.

**Example**:
```python
x = 10.5
y = -3.14
z = 0.0
```

**Operations**:
Similar to integers but results are floats.

---

#### 4. Boolean (`bool`)

- **Definition**: Represents one of two values: `True` or `False`.
- **Usage**: Used for conditional testing and logic operations.

**Example**:
```python
is_valid = True
has_value = False
```

**Logical Operations**:
- AND: `a and b`
- OR: `a or b`
- NOT: `not a`

---

#### 5. Tuples (`tuple`)

- **Definition**: Immutable ordered collection of items.
- **Usage**: Used for fixed collections of items.

**Example**:
```python
my_tuple = (1, 2, 3, "hello", 4.5)
```

**Accessing Elements**:
```python
print(my_tuple[0])    # Output: 1
print(my_tuple[-1])   # Output: 4.5
```

**Slicing**:
```python
print(my_tuple[1:3])  # Output: (2, 3)
```

**Immutability**: 
Tuples cannot be changed after creation.

---

#### 6. Dictionaries (`dict`)

- **Definition**: Mutable unordered collection of key-value pairs.
- **Usage**: Used for mapping unique keys to values.

**Example**:
```python
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
```

**Accessing Values**:
```python
print(my_dict["name"])  # Output: Alice
```

**Modifying Values**:
```python
my_dict["age"] = 26
```

**Adding Key-Value Pairs**:
```python
my_dict["email"] = "alice@example.com"
```

**Removing Key-Value Pairs**:
```python
del my_dict["city"]
```

---

#### 7. Lists (`list`)

- **Definition**: Mutable ordered collection of items.
- **Usage**: Used for storing collections of items that can be changed.

**Example**:
```python
my_list = [1, 2, 3, "hello", 4.5]
```

**Accessing Elements**:
```python
print(my_list[0])    # Output: 1
print(my_list[-1])   # Output: 4.5
```

**Modifying Elements**:
```python
my_list[1] = "world"
```

**Adding Elements**:
```python
my_list.append(6)
```

**Removing Elements**:
```python
my_list.remove("hello")
```

---

#### 8. Objects (`object`)

- **Definition**: Instances of user-defined classes.
- **Usage**: Used to encapsulate data and functionality together.

**Example**:
```python
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_object = MyClass("Alice", 25)
```

**Accessing Attributes**:
```python
print(my_object.name)  # Output: Alice
```

**Modifying Attributes**:
```python
my_object.age = 26
```

---

### Activities

1. **Hands-on Exercises for Each Data Type**:
   - Create examples using different data types and perform operations on them.
   
2. **Small Projects**:
   - Create a contact book using dictionaries, where each contact has attributes like name, phone number, and email.

