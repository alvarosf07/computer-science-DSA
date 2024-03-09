# Data Structures III - Hash Map

> A Hash-Map is a collection of elements (pre)allocated in NON-contiguous spaces in the computer memory address. Each element in an array occupies the same amount of space in memory.
> 
> Since the elements are NON-contiguously allocated in memory, a hash function is used to transform input data into a position in the memory address.

Hash maps present features of both arrays and linked lists:
* Hash Maps pre-allocate data in memory (like arrays), but they do it in NON-Contiguous Spaces (like linked lists).
  * This requires a bigger chunk of memory allocation at first, but in exchange it provides dynamic sizing (faster addition/deletion, like with linked lists).
* Hash function takes care of allocating data in memory address (instead of index like in arrays)
* Hash-Maps support different data-types

<br/>

## 1.1. Understanding

Visualize a hash map as a dictionary where each word (key) is associated with its definition (value). The hash function determines which "page" of the dictionary to look at based on the word's hash value.

<img src="/Resources/Images/hash_map_visualization.png" width="550">

<br/>

## 1.2. Characteristics

| Characteristic                | Specs           | Description                                                |
|-------------------------------|-----------------|------------------------------------------------------------|
| Memory Time Allocation        | -               | Dynamically allocated as needed                             |
| Memory Spatial Allocation     | Dispersed       | Data is distributed across buckets in the hash table        |
| Memory Address - Space        | Dynamic         | Dynamically allocated, theoretically infinite (only limited by system memory)      |
| Memory Address - Types        | -               | Typically allows any data type                             |
| Memory Address - Reference    | Hash Code       | Keys are transformed into hash codes to determine memory location|
| Element Access                | O(1)            | Direct access to elements using hash code                  |
| Element Modification          | O(1)            | Direct modification using hash code                        |
| Element Insertion             | O(1)            | Typically constant time insertion, but can vary based on hash function|
| Element Deletion              | O(1)            | Typically constant time deletion, but can vary based on hash function|

<br/>

## 1.3. Hash Map Advantages & Disadvantages

#### Advantages:
- **Fast Lookup**: Provides constant-time lookup for accessing elements.
- **Dynamic Size**: Can dynamically grow and shrink as needed, efficiently managing memory.
- **Flexible Key-Value Pairs**: Allows mapping of keys to values of different types and structures.

#### Disadvantages:
- **Collision Resolution**: Handling collisions (two different keys hash to the same index) requires additional processing.
- **Space Overhead**: Requires additional memory for storing hash codes and managing collisions.
- **Hash Function Dependency**: Performance depends on the quality and distribution of the hash function.

#### Hash maps are best used when:
- Fast access to elements is critical.
- Key-value pairs need to be stored and retrieved efficiently.
- The size of the data collection is expected to change dynamically.

<br/>
<br/>

# 2. Hash Functions

> Hash Functions are the mechanism that enables hash search.
> 
> A Hash Function is a special function that takes the data to store as input, and outputs a random-looking number. That number is interpreted as the memory position the item will be stored at.

Hash functions are explained in detail in the <a href="https://github.com/alvarosf07/computer-science-DSA/blob/master/3)%20Algorithms/2)%20Search%20Algorithms/3)%20Hash%20Search/README.md#2-hash-functions">Hash Functions</a> section.

In the image below it's possible to observe how a hash function works in practice. In this example, the hash function maps names to integers from 0 to 15; but there's a collision between two names at memory address number 02.

<img src="/Resources/Images/hash_function_visualization.png" width="400">

<br/>
<br/>

# 3. Types of Hash Maps by Hashing Methodology
Based on the type of hash function, it's possible to find different types of hash maps:

### 3.1. Chaining Hash Map
Chaining Hash Maps use chaining as collision resolution mechanism to handle situations where multiple keys hash to the same index. In Chaining Hash Maps, collisions are handled by maintaining a linked list at each bucket. When a collision occurs, the key-value pair is added to the linked list at that bucket.

### 3.2. Open Addressing Hash Maps
Open addressing is a method used in hash tables to resolve collisions that occur when two different keys hash to the same index. In open addressing, when a collision happens, instead of storing the colliding item in the same slot (index) in the hash table, the algorithm looks for the next available slot (probe sequence) in the table until an empty slot is found. There are several techniques for probe sequences, including linear probing, quadratic probing, and double hashing.

 * **Linear Probing Hash Map** -  The algorithm checks consecutive slots in the table until an empty slot is found.
 * **Quadratic Probing Hash Map** - The algorithm checks slots using a quadratic function until an empty slot is found.
 * **Double Hashing Hash Map** - The algorithm uses a second hash function to determine the step size for probing.

### 3.3. Robin Hood Hash Map
In this variant, keys are stored in a linear array, and when a collision occurs, the key with the longest probe sequence is moved closer to its original hashed position.

### 3.4. Cuckoo Hood Hash Map
This hash map uses multiple hash functions and two or more hash tables. If a collision occurs in one table, the element is moved to its alternative table until a vacant spot is found.

### 3.5. Perfect Hash Map
These hash maps are designed to have minimal or no collisions for a specific set of keys. They are often used when the set of keys is known in advance.


<br/>
