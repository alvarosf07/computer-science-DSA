# Data Structure II - Linked List

<br/>

> A linked list is a collection of elements stored in a chain of nodes that don't need to be at sequential memory addresses. 
> Each node can take as much memory as needed, and will contain two pieces of data: its value, and a pointer to the next node. 
A cell with an empty pointer marks the end of the chain.
<br/>

## 1.1. Understanding

Imagine a chain of interconnected nodes, where each node holds a piece of data and a pointer to the next node. 
Visualizing a linked list as a train of data compartments can help understand the concept:

<img src="/Resources/Images/linkedlist_visualization.png" width="600">

<br/>

## 1.2. Characteristics

| Characteristic                | Linked List Specs | Description                                                |
|-------------------------------|-----------------|------------------------------------------------------------|
| Memory Time Allocation        | -               | Compiled at runtime (memory is not pre-allocated)                    |
| Memory Spatial Allocation     | Dispersed       | Nodes are not necessarily stored in contiguous memory      |
| Memory Address - Space        | Dynamic         | Dynamically allocated, theoretically infinite (only limited by memory space)       |
| Memory Address - Types        | -               | Typically allows any data type                             |
| Memory Address - Reference    | Pointer         | Nodes reference the next node using pointers                |
| Element Access                | O(n)            | Sequential traversal required for access                   |
| Element Modification          | O(n)            | Requires traversal to find and modify specific element     |
| Element Insertion             | O(1)            | Insertion at the beginning (if head is known), otherwise O(n)|
| Element Deletion              | O(1)            | Deletion at the beginning (if head is known), otherwise O(n)|

<br/>

## 1.3. Linked List Advantages & Disadvantages

#### Advantages:
- **Memory Spatial Allocation**: Linked lists can accommodate elements of different data types and sizes.
- **Dynamic Size**: Linked lists can grow and shrink in size dynamically, unlike arrays with fixed size.
- **Efficient Insertion and Deletion**: Insertion and deletion operations can be performed efficiently, especially at the beginning of the list.


#### Disadvantages:
- **Sequential Element Access**: Accessing elements requires sequential traversal, which can be inefficient for large lists.
- **Pointer Complexity**: Managing pointers can introduce complexity and potential errors.
- **Memory Overhead**: Additional memory is required to store pointers for each node, leading to higher overhead compared to arrays.


#### Linked lists are best used when:
- The size of the data collection is unknown or varies.
- Frequent insertion and deletion operations are expected.
- Random access to elements is not a primary requirement.

<br/>
<br/>

# 2. Double-Linked List

> A Double-Linked List is a Linked List in which nodes have two pointers, one to the following node and other to the previous node.

#### Advantages of Double-Linked Lists:
  1. **Node Deletion -** Double-Linked Lists facilitate element deletion in case we're only given the address of a node. We just need to go to the node that we want to delete, use the backward pointer to go to the previous node, and then update the "next" pointer from the current node (the one we want to delete) to the following node.
  2. **Navigation -** Double-Linked Lists facilitate the navigation of the chain in both directions.

#### Disadvantages of Double Linked Lists:
  1. **Extra Space -** Double-Linked lists need to store two pointers in every node, which increases the memory space used per node.

<br/>

## 1.1. Understanding

* A Double-Linked List is a collection of elements stored in a chain of nodes that don't need to be at sequential memory addresses.
* Each node can take as much memory as needed, and will contain three pieces of data: its value, and a pointer to the next node, and a pointer to the previous node.
* A cell with an empty pointer marks the end of the chain.

<br/>

<img src="/Resources/Images/doublelinkedlist_visualization.png" width="600">

<br/>
<br/>

# 3. Circular-Linked List

> A circular linked list is a variation of the linked list data structure where the last node points back to the first node (instead of pointing to a NULL value), forming a circular loop.

#### Advantages of Circular Linked Lists:
1. **Efficient Implementation of Circular Structures**: Circular linked lists are useful for representing circular structures such as queues, where elements need to be continuously cycled. With a circular linked list, there's no need to traverse the entire list to find the end; the last node's next pointer points back to the first node.
   
2. **Memory Utilization**: Circular linked lists can be more memory efficient in certain scenarios compared to traditional linked lists, especially when dealing with situations where elements are continuously added and removed.

3. **Traversal Flexibility**: In a circular linked list, starting from any node, you can traverse the entire list without worrying about reaching the end, as the traversal will eventually loop back to the starting node.

#### Disadvantages of Circular Linked Lists:
1. **Complexity in Insertion and Deletion**: Insertion and deletion operations in circular linked lists can be slightly more complex compared to traditional linked lists, especially when dealing with corner cases such as inserting at the beginning or end of the list.

2. **Potential Infinite Loop**: Care must be taken to properly manage the circular structure to avoid infinite loops during traversal. If pointers are not properly updated, it can lead to an infinite loop situation where traversal never ends.

3. **No Explicit End**: Unlike traditional linked lists where the last node's next pointer is NULL, in a circular linked list, determining the end of the list can be slightly more complex since every node is technically part of the loop.


<br/>






