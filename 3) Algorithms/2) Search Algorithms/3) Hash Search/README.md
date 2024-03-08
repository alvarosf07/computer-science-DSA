# 1. Hash Search

> Hash search is a search algorithm that uses a data structure called a hash table to store and retrieve data in constant time. A hash table is a collection of key-value pairs, where each key is mapped to a unique index in the table using a hash function. This allows for fast retrieval of values based on their associated keys.

<br/>


## 1.1. How Does Hash Search Work?

Hash search works by first computing the hash value of the key using a hash function. This hash value is then used as an index to access the corresponding value in the hash table. If the key is found in the hash table, the associated value is returned; otherwise, the search fails.

<br/>


## 1.2. Key Features of Hash Search:

1. **Efficiency:** Hash search has an average time complexity of O(1) for both insertion and retrieval, making it highly efficient for large datasets.

2. **Fast Lookup:** Hash search allows for fast retrieval of values based on their associated keys, regardless of the size of the dataset.

3. **Flexibility:** Hash tables can store a wide range of data types and allow for efficient storage and retrieval of key-value pairs.

<br/>


## 1.3. Example of Hash Search:

Consider the problem of searching for a specific value (e.g., "apple") in a hash table of fruits:

```python
# Create a hash table of fruits
hash_table = {
    "apple": "A sweet and crunchy fruit",
    "banana": "A yellow tropical fruit",
    "orange": "A juicy citrus fruit"
}

# Search for a specific fruit
fruit = "apple"
if fruit in hash_table:
    print("Description of", fruit + ":", hash_table[fruit])
else:
    print("Fruit not found")
```
<br/>


## 1.4. When to Use Hash Search:
Hash search is most commonly used in scenarios where:

* Fast lookup of values based on keys is required.
* The dataset is relatively large and dynamic.
* Efficient storage and retrieval of key-value pairs are essential.

<br/>

<br/>



# 2. Hash Functions

> Hash Functions are the mechanism that enables hash search.
> 
> A Hash Function is a special function that takes the data to store as input, and outputs a random-looking number. That number is interpreted as the memory position the item will be stored at.

<br/>


## 2.1. Purposes of Hash Functions:

Hash functions have 2 main purposes:

1. **Storing data in memory:**
   1) We introduce as input the data value to store (using a key to name the data value that we want to store in memory)
   2) The Hash function produces a random-like value that indicates the position in the memory address. 

3. **Retrieving data from memory:**
   1) We introduce the name of the data value we want to retrieve.
   2) The given value (key) is run through the hash function, which outputs the position in the memory address.
   3) The memory position is fetched. If the item is stored there, it will be retrieved.


<br/>


## 2.2. Objectives of Hash Functions:

Hash functions must be designed with 3 objectives in mind:

- Efficient to organize data in memory
- Avoid collisions (coincidences of the same data)
- Fast to compute memory addresses from input data

<br/>



## 2.3. Mechanism of Hash Functions:

Hash functions operate by processing the input data through a series of mathematical operations to produce a hash value. The key characteristics of a good hash function include:

- **Deterministic:** A hash function should produce the same hash value for the same input every time it is invoked.
- **Uniformity:** Ideally, a hash function should distribute hash values uniformly across the output space to minimize collisions.
- **Efficiency:** Hash functions should be computationally efficient to ensure fast processing of data.
- **Fixed Output Size:** Hash functions should produce a fixed-size output, regardless of the input size.

<br/>


## 2.4. Collisions:

There is a problem with Hash Tables: sometimes the hash function returns the same memory position for two different inputs. That’s called a hash collision. 

Hash functions aim to minimize collisions, but they are inevitable due to the finite size of the output space compared to the infinite input space. 

### 2.4.1. Avoiding Collisions
A proper hash function will return random-looking values for different inputs. Therefore, the larger the range of values the hash function can output, the more data positions are available, and the less probable it is for a hash collision to happen.

Therefore, is common to ensure at least 50% of the space available to the Hash Table is free. Otherwise, collisions would be too frequent, causing a significant drop in the Hash Table’s performance.


### 2.4.2. Handling Collisions
Hash functions typically handle collisions using one of the following methods:

1. **Separate Chaining:** In this method, each bucket in the hash table contains a linked list of key-value pairs with the same hash value. When a collision occurs, the new key-value pair is appended to the linked list.

2. **Open Addressing:** In this method, when a collision occurs, the algorithm probes for an empty slot (i.e., a slot without a key-value pair) in the hash table and inserts the new key-value pair there. Various probing techniques can be used to find an empty slot:
    * **Linear Probing:** When there is a collision, the key is moved to the next EMPTY index to the right in the array. The main problem with linear probing is that it increases the probability of clustering among highly repeated commands, and that makes it inefficient to go over many occupied arrays every time a collision occurs.
    * **Quadratic Probing** 
    * **Double Hashing:** Divides the Hashing methodology in two functions:
        * **First Hashing Function - Calculating Uncollided item:** Instead of trying with the next EMPTY index to the right, we try with the C-next EMPTY index. Each time we find a collision, we will vary our value C (we may jump 3 indexes for one collision, and jump only 1 index for other). This way we avoid clusters.
        * **Second Hashing Function - Selecting the right index:** We want c to have not common divisors with the length of the hash-map, because that is the only way to go over the full memory array to assign a free index without repetitions.

    * **Robin Hood Hashing:** This method aims to keep the variance in the lengths of the linked lists minimal by stealing from "rich" slots (slots with longer linked lists) and giving to "poor" slots (slots with shorter linked lists).

