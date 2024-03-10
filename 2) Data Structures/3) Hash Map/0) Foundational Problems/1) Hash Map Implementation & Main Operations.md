
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
