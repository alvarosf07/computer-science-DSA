# Implementations with Linked Lists
Several Abstract Data Types (ADTs) and Data Structures (DS) are commonly implemented using linked lists:

### Abstract Data Types (ADTs) Implemented with Linked Lists:
  * **Stacks -** A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. It supports two main operations: push (to add an element to the top) and pop (to remove the top element).
  * **Queues -** A queue is a linear data structure that follows the First In, First Out (FIFO) principle. It supports two main operations: enqueue (to add an element to the rear) and dequeue (to remove the front element).

### Data Structures (DS) Implemented with Linked Lists:
  * **Graphs -** Graphs can be implemented using linked lists to represent the adjacency list representation. In this representation, each vertex of the graph is represented as a node in the linked list, and the edges are represented as links between nodes.

<br/>

# 1. Linked List Implementation of Stacks
As previously introduced, <a href="https://github.com/alvarosf07/computer-science-DSA/tree/DSA-dev/1)%20Abstract%20Data%20Types/4)%20Lists%2C%20Stacks%20%26%20Queues/2)%20Stack">Stacks</a> are collections of data "stacked" one above the previous one. It's only possible to add/remove/modify data on the top of the stack structure (LIFO, Last-In-First-Out).

### Python Implementation of Stacks using Linked Lists as underlying Data Structure:
Implementing a stack using a linked list involves creating a class for the stack and another class for the nodes of the linked list.

* The `Node` class represents each node in the linked list. Each node has a data attribute to store the element and a next attribute to point to the next node in the list.
* The `Stack` class implements the stack data structure using a linked list. It has methods to push, pop, and peek elements, as well as check if the stack is empty and display its contents.
  * When pushing an element onto the stack, a new node is created and added to the top of the stack by setting its next attribute to the current top node and updating the top reference to the new node.
  * When popping an element from the stack, the top element is removed by updating the top reference to point to the next node in the list, and its data is returned.
* The `peek` method returns the top element of the stack without removing it.
* The `display` method traverses the linked list from the top to the bottom, printing each element.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack elements:")
stack.display()  # Output: 3 -> 2 -> 1 -> None

print("Peek:", stack.peek())  # Output: Peek: 3

print("Pop:", stack.pop())    # Output: Pop: 3
print("Stack elements after pop:")
stack.display()  # Output: 2 -> 1 -> None

```


<br/>

### C++ Implementation:
In C++, the implementation of a stack (normally) uses the vector container from the Standard Template Library (STL) to store the elements of the stack. The vector provides dynamic array functionality, making it suitable for implementing stacks.
```cpp
#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int val) {
        data = val;
        next = nullptr;
    }
};

class Stack {
private:
    Node* top;

public:
    Stack() {
        top = nullptr;
    }

    bool isEmpty() {
        return top == nullptr;
    }

    void push(int val) {
        Node* newNode = new Node(val);
        newNode->next = top;
        top = newNode;
    }

    int pop() {
        if (isEmpty()) {
            cout << "Stack underflow" << endl;
            exit(1);
        }
        int data = top->data;
        Node* temp = top;
        top = top->next;
        delete temp;
        return data;
    }

    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty" << endl;
            exit(1);
        }
        return top->data;
    }

    void display() {
        Node* current = top;
        while (current != nullptr) {
            cout << current->data << " -> ";
            current = current->next;
        }
        cout << "nullptr" << endl;
    }
};

int main() {
    Stack stack;

    stack.push(1);
    stack.push(2);
    stack.push(3);

    cout << "Stack elements: ";
    stack.display();  // Output: 3 -> 2 -> 1 -> nullptr

    cout << "Peek: " << stack.peek() << endl;  // Output: Peek: 3

    cout << "Pop: " << stack.pop() << endl;    // Output: Pop: 3
    cout << "Stack elements after pop: ";
    stack.display();  // Output: 2 -> 1 -> nullptr

    return 0;
}

```

<br/>

# 2. Linked List Implementation of Queues
As previously introduced, <a href="https://github.com/alvarosf07/computer-science-DSA/tree/DSA-dev/1)%20Abstract%20Data%20Types/4)%20Lists%2C%20Stacks%20%26%20Queues/3)%20Queue">Queues</a> collections of data queued one after the other. It's only possible to add/remove/modify data on the front of the queue structure (FIFO, First-In-First-Out).

### Python Implementation of Queues using Linked Lists as underlying Data Structure:
Implementing a queue using a linked list involves creating a class for the queue and another class for the nodes of the linked list.

* The `Node` class represents each node in the linked list. Each node has a data attribute to store the element and a next attribute to point to the next node in the list.
* The `Queue` class implements the queue data structure using a linked list. It has methods to enqueue (add an element to the rear), dequeue (remove an element from the front), and peek (get the element at the front without removing it), as well as check if the queue is empty and display its contents.
  * When enqueueing an element into the queue, a new node is created and added to the rear of the queue. If the queue is empty, both the front and rear pointers are updated to point to the new node.
  * When dequeuing an element from the queue, the element at the front is removed, and the front pointer is updated to point to the next node in the list. If the queue becomes empty after dequeuing, both the front and rear pointers are set to None.
* The `peek` method returns the element at the front of the queue without removing it.
* The `display` method traverses the linked list from the front to the rear, printing each element.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue elements:")
queue.display()  # Output: 1 -> 2 -> 3 -> None

print("Peek:", queue.peek())  # Output: Peek: 1

print("Dequeue:", queue.dequeue())  # Output: Dequeue: 1
print("Queue elements after dequeue:")
queue.display()  # Output: 2 -> 3 -> None


```

<br/>

### C++ Implementation:

```cpp
#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int val) {
        data = val;
        next = nullptr;
    }
};

class Queue {
private:
    Node* front;
    Node* rear;

public:
    Queue() {
        front = rear = nullptr;
    }

    bool isEmpty() {
        return front == nullptr;
    }

    void enqueue(int val) {
        Node* newNode = new Node(val);
        if (isEmpty()) {
            front = rear = newNode;
        } else {
            rear->next = newNode;
            rear = newNode;
        }
    }

    int dequeue() {
        if (isEmpty()) {
            cout << "Queue underflow" << endl;
            exit(1);
        }
        int data = front->data;
        Node* temp = front;
        front = front->next;
        delete temp;
        if (front == nullptr) {
            rear = nullptr;
        }
        return data;
    }

    int peek() {
        if (isEmpty()) {
            cout << "Queue is empty" << endl;
            exit(1);
        }
        return front->data;
    }

    void display() {
        Node* current = front;
        while (current != nullptr) {
            cout << current->data << " -> ";
            current = current->next;
        }
        cout << "nullptr" << endl;
    }
};

int main() {
    Queue queue;

    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);

    cout << "Queue elements: ";
    queue.display();  // Output: 1 -> 2 -> 3 -> nullptr

    cout << "Peek: " << queue.peek() << endl;  // Output: Peek: 1

    cout << "Dequeue: " << queue.dequeue() << endl;  // Output: Dequeue: 1
    cout << "Queue elements after dequeue: ";
    queue.display();  // Output: 2 -> 3 -> nullptr

    return 0;
}

```

