# Implementations with Trees
Several Abstract Data Types (ADTs) and Data Structures (DS) are commonly implemented using trees:

### Abstract Data Types (ADTs) Implemented with Hash Maps:
  * **Priority Queues -** A set is a collection of distinct elements where each element is unique. Hash maps can be used to implement sets by associating each element with a key in the hash map, effectively storing only the unique elements and allowing for fast membership tests and operations such as insertion, deletion, and intersection.
  * **Dictionaries -** Dictionaries are data structures that stores key-value pairs. They can be understood as an abstraction of hash maps. However, dictionaries can also be implemented with a tree structure. This typically involves using a self-balancing binary search tree (BST) such as AVL tree, Red-Black tree, or B-tree. 

### Other Structures implemented with Hash Maps:
  * **Binary Search Algorithms -** A counter is a data structure that keeps track of the frequency of elements in a collection. Hash maps can be used to implement counters by associating each unique element with its count (frequency) in the hash map. This allows for efficient counting of occurrences and manipulation of element frequencies.
  * **Tries -** A trie is a tree-like data structure used to store a dynamic set of strings or keys where each node represents a common prefix of its children. Tries are commonly used in string-related problems, such as autocomplete systems and dictionary implementations.

<br/>
<br/>

# 1. Heap Implementation of Priority Queue
A priority queue is a data structure that maintains a collection of elements in order with associated priorities. Elements with higher priorities are dequeued before elements with lower priorities. 

As previously introduced, a binary heap is a complete binary tree where the value of each parent node is less than or equal to the values of its children (min-heap), or greater than or equal to the values of its children (max-heap).

Priority queues can be efficiently implemented using heap-based data structures, such as binary heaps.

### Python Implementation of Priority Queues using Heaps as underlying Data Structure:
In Python, the `heapq` module provides a simple and efficient implementation of priority queues using the heap data structure. We'll use the `heapq` functions `heappush` to insert elements into the priority queue and `heappop` to remove the element with the highest priority.

* First we define a PriorityQueue class with methods `push`, `pop`, `is_empty`, and `__len__`.
* The `push` method takes an item and its priority, assigns an index to maintain the order of insertion, and pushes a tuple containing the priority, index, and item into the heap.
* The `pop` method removes and returns the item with the highest priority from the heap.
* The `is_empty` method checks if the priority queue is empty.
* The `__len__` method returns the size of the priority queue.

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0

    def __len__(self):
        return len(self._queue)
```

Example Usage:
* We create a `PriorityQueue` object `pq`.
* We push elements ('Task 1', 'Task 2', 'Task 3') into the priority queue with corresponding priorities (5, 1, 3).
* We pop elements from the priority queue, and they are dequeued based on their priorities (lowest priority first).

```python
# Create a priority queue
pq = PriorityQueue()

# Push elements with priorities
pq.push('Task 1', 5)
pq.push('Task 2', 1)
pq.push('Task 3', 3)

# Pop elements with highest priorities
print(pq.pop())  # Output: Task 2
print(pq.pop())  # Output: Task 3
print(pq.pop())  # Output: Task 1
```

<details>
 <summary> What happens behind the scenes of the `heapq` module?</summary>

1. **Binary Heap**:
    - A binary heap is a complete binary tree where each node satisfies the heap property. In a min-heap, the value of each node is less than or equal to the values of its children. In a max-heap, the value of each node is greater than or equal to the values of its children.
    - Binary heaps are typically implemented using arrays, where the root of the heap is at index 0, and for any node at index `i`, its left child is at index `2*i + 1` and its right child is at index `2*i + 2`.

2. **Heap Operations**:
    - The `heapq` module provides functions to perform heap operations on lists in Python.
    - `heapq.heappush(heap, item)`: This function inserts `item` into the `heap`, maintaining the heap property.
    - `heapq.heappop(heap)`: This function removes and returns the smallest element from the `heap`, maintaining the heap property.
    - Other functions provided by `heapq` include `heapify`, `heappushpop`, `heapreplace`, etc.

3. **Heapify Operation**:
    - The `heapify` function transforms a list into a heap, in linear time, without requiring additional space. It rearranges the elements of the list so that they satisfy the heap property.
    - This operation is used to create a heap from an unsorted list, or to restore the heap property after modifications to the heap.

4. **Underlying Data Structure**:
    - The underlying data structure used by `heapq` is a list, which represents the binary heap.
    - The binary heap is stored in a list, where the element at index `i` corresponds to the node at position `i` in the binary tree.

5. **Performance**:
    - The `heapq` module provides efficient implementations of heap operations with time complexity:
        - `heappush`: O(log n)
        - `heappop`: O(log n)
        - `heapify`: O(n)
    - These operations ensure that the heap maintains its properties and supports efficient insertion and deletion of elements with minimum overhead.

Overall, the `heapq` module provides a simple and efficient way to work with heap-based data structures in Python, allowing for fast insertion, deletion, and manipulation of elements while maintaining the heap property.

</details>

<br/>
<br/>

# 2. Tree Implementation of Dictionary
An example of dictionary implementation with a tree is the following implementation of an AVL. This type of self-balancing binary search tree provides dictionary-like functionality with key-value pairs. The `insert` method inserts a key-value pair into the tree, while the `search` method looks up a value based on a key. The `inorder_traversal` method returns all key-value pairs in sorted order:

### AVL Tree-Based Dictionary Implementation in Python
We need to create two classes:

#### TreeNode Class:
- Represents a node in the AVL tree.
- Attributes:
  - `key`: Key of the node.
  - `value`: Value associated with the key.
  - `left`: Reference to the left child node.
  - `right`: Reference to the right child node.
  - `height`: Height of the node in the AVL tree.

#### AVLTree Class:
1. **Constructor (`__init__`)**:
   - Initializes an empty AVL tree with `root` set to `None`.

2. **Helper Methods**:
   - `_height(node)`: Returns the height of a given node. If the node is `None`, it returns 0.
   - `_balance_factor(node)`: Calculates the balance factor of a given node, which is the difference in height between its left and right subtrees.
   - `_fix_height(node)`: Updates the height of a node based on the heights of its left and right children.
   - `_rotate_right(y)`: Performs a right rotation on the subtree rooted at node `y` to maintain AVL tree balance.
   - `_rotate_left(x)`: Performs a left rotation on the subtree rooted at node `x` to maintain AVL tree balance.

3. **Insertion Method (`insert(key, value)`)**:
   - Inserts a new key-value pair into the AVL tree.
   - If the tree is empty, creates a new node and sets it as the root.
   - Otherwise, recursively inserts the node into the appropriate subtree based on the key.
   - After insertion, checks and performs rotations if necessary to maintain AVL tree balance.

4. **Search Method (`search(key)`)**:
   - Searches for a key in the AVL tree.
   - Begins the search from the root node, recursively traversing the tree until the key is found or the end of the tree is reached.
   - Returns the value associated with the key if found, otherwise returns `None`.

5. **Inorder Traversal Method (`inorder_traversal()`)**:
   - Performs an inorder traversal of the AVL tree.
   - Traverses the tree recursively, visiting nodes in the order: left subtree, current node, right subtree.
   - Returns a list of key-value pairs in sorted order.

```python
class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _fix_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._fix_height(y)
        self._fix_height(x)

        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self._fix_height(x)
        self._fix_height(y)

        return y

    def _insert(self, node, key, value):
        if node is None:
            return TreeNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        self._fix_height(node)

        balance = self._balance_factor(node)

        if balance > 1:
            if key < node.left.key:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        elif balance < -1:
            if key > node.right.key:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append((node.key, node.value))
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
```


#### Example usage:
To try the previous implementation, we can first createe an instance of `AVLTree`. Then we insert different key-value pairs into the tree using the `insert` method. After printing certain elements (searching by keys using the method `tree.search()`), we can obserce how the tree retrieves all key-value pairs in sorted order using the `inorder_traversal` method.

```python
tree = AVLTree()
tree.insert(5, "apple")
tree.insert(3, "banana")
tree.insert(7, "orange")

print(tree.search(5))  # Output: apple
print(tree.search(3))  # Output: banana
print(tree.search(7))  # Output: orange

print(tree.inorder_traversal())  # Output: [(3, 'banana'), (5, 'apple'), (7, 'orange')]
```

