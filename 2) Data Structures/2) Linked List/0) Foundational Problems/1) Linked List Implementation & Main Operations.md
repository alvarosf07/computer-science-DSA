# 1. Linked List Implementation & Main Operations - Python

### Linked List Implementation
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
```
### Linked List Operation I - Element Access
Accessing elements in a linked list is done by traversing the list until reaching the desired node:
```python
def access_element(self, index):
    current = self.head
    count = 0
    while current:
        if count == index:
            return current.data
        count += 1
        current = current.next
    return None
```

### Linked List Operation II - Element Modification
Modifying elements in a linked list is done by traversing the list until reaching the desired node and updating its data:
```python
def modify_element(self, index, new_data):
    current = self.head
    count = 0
    while current:
        if count == index:
            current.data = new_data
            return True
        count += 1
        current = current.next
    return False
```

### Linked List Operation III - Element Insertion
Inserting elements into a linked list can be done at the beginning, end, or at any specified position. When a new element is inserted, references to the previous and next nodes need to be updated:
```python
def insert_element(self, index, new_data):
    if index == 0:
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        return True
    current = self.head
    count = 0
    while current:
        if count == index - 1:
            new_node = Node(new_data)
            new_node.next = current.next
            current.next = new_node
            return True
        count += 1
        current = current.next
    return False
```

### Linked List Operation IV - Element Deletion
Deleting elements from a linked list can be done at the beginning, end, or at any specified position. When a new element is deleted, references to the previous and next nodes need to be updated:
```python
# Deleting elements
def delete_element(self, index):
    if index == 0:
        if self.head:
            self.head = self.head.next
            return True
        return False
    current = self.head
    count = 0
    while current:
        if count == index - 1 and current.next:
            current.next = current.next.next
            return True
        count += 1
        current = current.next
    return False
```
<br/>
<br/>

# 2. Linked List Implementation & Main Operations - C++

```c++
#include <iostream>
#include <stdexcept>

using namespace std;

// Node class represents each element (node) in the linked list
class Node {
public:
    int data;   // Data stored in the node
    Node* next; // Pointer to the next node

    // Constructor to initialize node with data and nullptr for next pointer
    Node(int val) : data(val), next(nullptr) {}
};

// LinkedList class manages the operations related to the linked list
class LinkedList {
private:
    Node* head; // Pointer to the head of the linked list

public:
    // Constructor to initialize an empty linked list with nullptr head
    LinkedList() : head(nullptr) {}

    // Function to access an element at a specific index
    int get(int index) {
        if (index < 0 || index >= size()) {
            throw out_of_range("Index out of range");
        }
        Node* curr = head;
        for (int i = 0; i < index; ++i) {
            curr = curr->next;
        }
        return curr->data;
    }

    // Function to modify an element at a specific index
    void set(int index, int val) {
        if (index < 0 || index >= size()) {
            throw out_of_range("Index out of range");
        }
        Node* curr = head;
        for (int i = 0; i < index; ++i) {
            curr = curr->next;
        }
        curr->data = val;
    }

    // Function to insert an element at a specific index
    void insert(int index, int val) {
        if (index < 0 || index > size()) {
            throw out_of_range("Index out of range");
        }
        if (index == 0) {
            push_front(val);
            return;
        }
        Node* curr = head;
        for (int i = 0; i < index - 1; ++i) {
            curr = curr->next;
        }
        Node* newNode = new Node(val);
        newNode->next = curr->next;
        curr->next = newNode;
    }

    // Function to delete an element at a specific index
    void remove(int index) {
        if (index < 0 || index >= size()) {
            throw out_of_range("Index out of range");
        }
        if (index == 0) {
            pop_front();
            return;
        }
        Node* curr = head;
        for (int i = 0; i < index - 1; ++i) {
            curr = curr->next;
        }
        Node* temp = curr->next;
        curr->next = temp->next;
        delete temp;
    }

    // Function to push a new element to the front of the linked list
    void push_front(int val) {
        Node* newNode = new Node(val);
        newNode->next = head;
        head = newNode;
    }

    // Function to pop the first element from the linked list
    void pop_front() {
        if (head == nullptr) {
            throw out_of_range("List is empty");
        }
        Node* temp = head;
        head = head->next;
        delete temp;
    }

    // Function to return the size of the linked list
    int size() {
        int count = 0;
        Node* curr = head;
        while (curr != nullptr) {
            ++count;
            curr = curr->next;
        }
        return count;
    }
};

```

<br/>
<br/>

# 2. Linked List Implementation & Main Operations - JAVA

```java
import java.util.NoSuchElementException;

// Node class represents each element (node) in the linked list
class Node {
    int data;   // Data stored in the node
    Node next;  // Reference to the next node

    // Constructor to initialize node with data and null for next reference
    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

// LinkedList class manages the operations related to the linked list
class LinkedList {
    private Node head; // Reference to the head of the linked list

    // Constructor to initialize an empty linked list with null head
    LinkedList() {
        this.head = null;
    }

    // Function to access an element at a specific index
    int get(int index) {
        if (index < 0 || index >= size()) {
            throw new IndexOutOfBoundsException("Index out of range");
        }
        Node curr = head;
        for (int i = 0; i < index; ++i) {
            curr = curr.next;
        }
        return curr.data;
    }

    // Function to modify an element at a specific index
    void set(int index, int val) {
        if (index < 0 || index >= size()) {
            throw new IndexOutOfBoundsException("Index out of range");
        }
        Node curr = head;
        for (int i = 0; i < index; ++i) {
            curr = curr.next;
        }
        curr.data = val;
    }

    // Function to insert an element at a specific index
    void insert(int index, int val) {
        if (index < 0 || index > size()) {
            throw new IndexOutOfBoundsException("Index out of range");
        }
        if (index == 0) {
            pushFront(val);
            return;
        }
        Node newNode = new Node(val);
        Node prev = head;
        for (int i = 0; i < index - 1; ++i) {
            prev = prev.next;
        }
        newNode.next = prev.next;
        prev.next = newNode;
    }

    // Function to delete an element at a specific index
    void remove(int index) {
        if (index < 0 || index >= size()) {
            throw new IndexOutOfBoundsException("Index out of range");
        }
        if (index == 0) {
            popFront();
            return;
        }
        Node prev = head;
        for (int i = 0; i < index - 1; ++i) {
            prev = prev.next;
        }
        Node temp = prev.next;
        prev.next = temp.next;
        temp.next = null; // Remove reference to prevent memory leak
    }

    // Function to push a new element to the front of the linked list
    void pushFront(int val) {
        Node newNode = new Node(val);
        newNode.next = head;
        head = newNode;
    }

    // Function to pop the first element from the linked list
    void popFront() {
        if (head == null) {
            throw new NoSuchElementException("List is empty");
        }
        head = head.next;
    }

    // Function to return the size of the linked list
    int size() {
        int count = 0;
        Node curr = head;
        while (curr != null) {
            ++count;
            curr = curr.next;
        }
        return count;
    }
}
```
