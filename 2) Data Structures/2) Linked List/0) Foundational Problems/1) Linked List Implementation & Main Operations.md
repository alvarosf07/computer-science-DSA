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
