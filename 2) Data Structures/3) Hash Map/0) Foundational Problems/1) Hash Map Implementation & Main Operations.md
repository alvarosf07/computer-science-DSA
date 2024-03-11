
# 1. Hash Map Implementation & Main Operations - Python

### Hash Map Implementation
```python
class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def display(self):
        for i, bucket in enumerate(self.buckets):
            if bucket:
                print(f"Bucket {i}: {bucket}")
            else:
                print(f"Bucket {i}: None")
```
### Hash Map Operation I - Element Access
Accessing elements in a hash map is done by computing the hash of the key and then retrieving the value from the corresponding bucket:
```python
def get(self, key):
    index = self.hash_function(key)
    if self.buckets[index]:
        for k, v in self.buckets[index]:
            if k == key:
                return v
    return None

```

### Hash Map Operation II - Element Modification
Modifying elements in a hash map is similar to inserting elements. First, we compute the hash of the key to find the correct bucket, then we search for the key in the bucket, and finally, we update its value:
```python
def put(self, key, value):
    index = self.hash_function(key)
    if not self.buckets[index]:
        self.buckets[index] = []
    for i, (k, v) in enumerate(self.buckets[index]):
        if k == key:
            self.buckets[index][i] = (key, value)
            return
    self.buckets[index].append((key, value))
```

### Hash Map Operation III - Element Insertion
Inserting elements into a hash map involves computing the hash of the key to determine the bucket where the key-value pair will be stored. If the bucket is empty, we create a new list. Then, we insert the key-value pair into the list:
```python
def put(self, key, value):
    index = self.hash_function(key)
    if not self.buckets[index]:
        self.buckets[index] = []
    self.buckets[index].append((key, value))
```

### Hash Map Operation IV - Element Deletion
Deleting elements from a hash map is similar to modifying elements. We first compute the hash of the key to find the correct bucket, then we search for the key in the bucket, and finally, we delete the key-value pair if it exists:
```python
def remove(self, key):
    index = self.hash_function(key)
    if self.buckets[index]:
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]
                return
```

<br/>
<br/>

# 2. Hash Map Implementation & Main Operations - C++
```cpp
#include <iostream>
#include <vector>
#include <list>
#include <stdexcept>

using namespace std;

// HashEntry represents each key-value pair in the hash map
template<typename K, typename V>
class HashEntry {
public:
    K key;
    V value;

    // Constructor to initialize HashEntry with key and value
    HashEntry(const K& key, const V& value) : key(key), value(value) {}
};

// HashMap class manages the operations related to the hash map
template<typename K, typename V>
class HashMap {
private:
    vector<list<HashEntry<K, V>>> buckets; // Vector of linked lists (buckets) to store key-value pairs
    size_t size;                           // Number of key-value pairs in the hash map

    // Function to calculate the hash value for a given key
    size_t hash(const K& key) const {
        return hash<K>{}(key) % buckets.size();
    }

public:
    // Constructor to initialize an empty hash map with default capacity
    HashMap(size_t capacity = 10) : buckets(capacity), size(0) {}

    // Function to get the value associated with a given key
    V get(const K& key) const {
        size_t index = hash(key);
        for (const auto& entry : buckets[index]) {
            if (entry.key == key) {
                return entry.value;
            }
        }
        throw out_of_range("Key not found");
    }

    // Function to put a key-value pair into the hash map
    void put(const K& key, const V& value) {
        size_t index = hash(key);
        for (auto& entry : buckets[index]) {
            if (entry.key == key) {
                entry.value = value; // Key already exists, update the value
                return;
            }
        }
        // Key not found, insert a new entry into the bucket
        buckets[index].emplace_back(key, value);
        ++size;
    }

    // Function to remove a key-value pair from the hash map
    void remove(const K& key) {
        size_t index = hash(key);
        auto& bucket = buckets[index];
        for (auto it = bucket.begin(); it != bucket.end(); ++it) {
            if (it->key == key) {
                bucket.erase(it);
                --size;
                return;
            }
        }
        throw out_of_range("Key not found");
    }

    // Function to check if the hash map contains a given key
    bool contains(const K& key) const {
        size_t index = hash(key);
        for (const auto& entry : buckets[index]) {
            if (entry.key == key) {
                return true;
            }
        }
        return false;
    }
};

```

<br/>
<br/>

# 3. Hash Map Implementation & Main Operations - JAVA
```java
import java.util.*;

// HashMap class manages the operations related to the hash map
class MyHashMap<K, V> {
    private static final int DEFAULT_CAPACITY = 16; // Default capacity of the hash map
    private static final double LOAD_FACTOR = 0.75;  // Load factor threshold for resizing

    // Node class represents each key-value pair in the hash map
    static class Node<K, V> {
        K key;
        V value;
        Node<K, V> next;

        Node(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }

    private Node<K, V>[] buckets; // Array of linked lists (buckets) to store key-value pairs
    private int size;              // Number of key-value pairs in the hash map
    private int capacity;          // Capacity of the hash map

    // Constructor to initialize an empty hash map with default capacity
    MyHashMap() {
        this(DEFAULT_CAPACITY);
    }

    // Constructor to initialize an empty hash map with specified capacity
    MyHashMap(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.buckets = new Node[capacity];
    }

    // Function to calculate the hash value for a given key
    private int hash(K key) {
        return Objects.hashCode(key) % capacity;
    }

    // Function to get the value associated with a given key
    public V get(K key) {
        int index = hash(key);
        Node<K, V> node = buckets[index];
        while (node != null) {
            if (Objects.equals(node.key, key)) {
                return node.value;
            }
            node = node.next;
        }
        return null; // Key not found
    }

    // Function to put a key-value pair into the hash map
    public void put(K key, V value) {
        int index = hash(key);
        Node<K, V> node = buckets[index];
        while (node != null) {
            if (Objects.equals(node.key, key)) {
                node.value = value; // Key already exists, update the value
                return;
            }
            node = node.next;
        }
        // Key not found, insert a new node at the beginning of the bucket's linked list
        Node<K, V> newNode = new Node<>(key, value);
        newNode.next = buckets[index];
        buckets[index] = newNode;
        ++size;

        // Check if resizing is needed
        if ((double) size / capacity >= LOAD_FACTOR) {
            resize();
        }
    }

    // Function to remove a key-value pair from the hash map
    public void remove(K key) {
        int index = hash(key);
        Node<K, V> prev = null;
        Node<K, V> curr = buckets[index];
        while (curr != null) {
            if (Objects.equals(curr.key, key)) {
                if (prev != null) {
                    prev.next = curr.next;
                } else {
                    buckets[index] = curr.next;
                }
                --size;
                return;
            }
            prev = curr;
            curr = curr.next;
        }
    }

    // Function to resize the hash map when load factor exceeds the threshold
    private void resize() {
        capacity *= 2;
        Node<K, V>[] newBuckets = new Node[capacity];
        for (Node<K, V> node : buckets) {
            while (node != null) {
                Node<K, V> next = node.next;
                int index = hash(node.key);
                node.next = newBuckets[index];
                newBuckets[index] = node;
                node = next;
            }
        }
        buckets = newBuckets;
    }
}

```
