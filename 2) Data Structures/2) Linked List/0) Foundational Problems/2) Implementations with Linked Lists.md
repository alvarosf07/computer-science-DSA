# Implementations with Linked Lists
Several Abstract Data Types (ADTs) and Data Structures (DS) are commonly implemented using linked lists:

### Abstract Data Types (ADTs) Implemented with Arrays:
  * **Stacks -** A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. It supports two main operations: push (to add an element to the top) and pop (to remove the top element).
  * **Queues -** A queue is a linear data structure that follows the First In, First Out (FIFO) principle. It supports two main operations: enqueue (to add an element to the rear) and dequeue (to remove the front element).

### Data Structures (DS) Implemented with Arrays:
  * **Graphs -** Graphs can be implemented using linked lists to represent the adjacency list representation. In this representation, each vertex of the graph is represented as a node in the linked list, and the edges are represented as links between nodes.

<br/>

# 1. Array Implementation of Stacks
As previously introduced, <a href="https://github.com/alvarosf07/computer-science-DSA/tree/DSA-dev/1)%20Abstract%20Data%20Types/4)%20Lists%2C%20Stacks%20%26%20Queues/2)%20Stack">Stacks</a> are collections of data "stacked" one above the previous one. It's only possible to add/remove/modify data on the top of the stack structure (LIFO, Last-In-First-Out).

### Python Implementation of Stacks using Arrays as underlying Data Structure:
Stacks are ideal to implement with arrays in Python because it takes `O(1)` to add/remove the last item of a Python list (while it's more complex to add/remove items in the middle of a Python list, like in the case of implementing queues). 

Stacks in Python can be implemented easily with the `.append()` and `.pop()` methods:

```python
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        """
        Checks if the stack is empty.
        """
        return len(self.stack) == 0

    def push(self, item):
        """
        Adds an item to the top of the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Removes and returns the item from the top of the stack.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def peek(self):
        """
        Returns the item from the top of the stack without removing it.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]
```


<br/>

### C++ Implementation:
In C++, the implementation of a stack (normally) uses the vector container from the Standard Template Library (STL) to store the elements of the stack. The vector provides dynamic array functionality, making it suitable for implementing stacks.
```cpp
#include <iostream>
#include <vector>
#include <stdexcept>

using namespace std;

class Stack {
private:
    vector<int> stack;

public:
    void push(int item) {
        // Adds an item to the top of the stack.
        stack.push_back(item);
    }

    int size() {
        // Returns the number of items in the stack.
        return stack.size();
    }

    int pop() {
        // Removes and returns the item from the top of the stack.
        if (is_empty()) {
            throw out_of_range("Stack is empty");
        }
        int top_item = stack.back();
        stack.pop_back();
        return top_item;
    }

    int peek() {
        // Returns the item from the top of the stack without removing it.
        if (is_empty()) {
            throw out_of_range("Stack is empty");
        }
        return stack.back();
    }

    bool is_empty() {
        // Checks if the stack is empty.
        return stack.empty();
    }

    
};
```

<br/>

# 2. Array Implementation of Queues
As previously introduced, <a href="https://github.com/alvarosf07/computer-science-DSA/tree/DSA-dev/1)%20Abstract%20Data%20Types/4)%20Lists%2C%20Stacks%20%26%20Queues/3)%20Queue">Queues</a> collections of data queued one after the other. It's only possible to add/remove/modify data on the front of the queue structure (FIFO, First-In-First-Out).

### Python Implementation of Queues using Arrays as underlying Data Structure:
It's possible to create queues in Python using a similar strategy as for an array, where the first element added is the first element retrieved (First-In-First-Out). 
To add an item to the end of the queue, use `.append()`. To retrieve an item from the top of the queue, use `.pop(0)` (eliminating the first position).

However, lists are not efficient for this purpose. While appends and pops from the end of lists are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

For this reason, the most efficient way to handle queues as an array in Python is with the package:  `collections.deque`, which is designed to make fast appends and pops from both ends of the Python list:

```python
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        """
        Checks if the queue is empty.
        """
        return len(self.queue) == 0

    def enqueue(self, item):
        """
        Adds an item to the back of the queue.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.popleft()

    def peek(self):
        """
        Returns the item from the front of the queue without removing it.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]

    def size(self):
        """
        Returns the number of items in the queue.
        """
        return len(self.queue)

```

Usage example:

```python
# Creating a new queue
queue = Queue()

# Adding elements to the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Size of the queue
print("Size of the queue:", queue.size())

# Removing elements from the queue
print("Dequeued element:", queue.dequeue())

# Peeking the front element of the queue
print("Front element of the queue:", queue.peek())

# Checking if the queue is empty
print("Is the queue empty?", queue.is_empty())

```

<br/>

### C++ Implementation:
In C++, the implementation of a queue uses the queue container from the Standard Template Library (STL) to store the elements of the queue. The queue container provides FIFO functionality, making it suitable for implementing queues.

```cpp
#include <iostream>
#include <queue>
#include <stdexcept>

using namespace std;

class Queue {
private:
    queue<int> q;

public:
    void enqueue(int item) {
        // Adds an item to the back of the queue.
        q.push(item);
    }

    int dequeue() {
        // Removes and returns the item from the front of the queue.
        if (is_empty()) {
            throw out_of_range("Queue is empty");
        }
        int front_item = q.front();
        q.pop();
        return front_item;
    }

    int peek() {
        // Returns the item from the front of the queue without removing it.
        if (is_empty()) {
            throw out_of_range("Queue is empty");
        }
        return q.front();
    }

    bool is_empty() {
        // Checks if the queue is empty.
        return q.empty();
    }

    int size() {
        // Returns the number of items in the queue.
        return q.size();
    }
};


```

