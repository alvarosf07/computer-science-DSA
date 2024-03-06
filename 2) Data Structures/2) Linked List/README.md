# Data Structures II - Linked List

<br/>

> A linked list is a collection of elements stored in a chain of nodes that don't need to be at sequential memory addresses. 
> Each node can take as much memory as needed, and will contain two pieces of data: its value, and a pointer to the next node. 
A cell with an empty pointer marks the end of the chain.
<br/>

## Understanding

Imagine a chain of interconnected nodes, where each node holds a piece of data and a pointer to the next node. 
Visualizing a linked list as a train of data compartments can help understand the concept:

![Linked List Visualization](/Resources/Images/linkedlist_visualization.png)

<br/>

## Characteristics

| Characteristic                | Time Complexity | Description                                                |
|-------------------------------|-----------------|------------------------------------------------------------|
| Memory Time Allocation| -               | Compiled at runtime (memory is not pre-allocated)                    |
| Memory Spatial Allocation | Dispersed      | Nodes are not necessarily stored in contiguous memory      |
| Memory Address - Space          | Limited by system memory | Dynamically allocated, theoretically infinite       |
| Memory Address - Types | -             | Typically allows any data type                             |
| Memory Address - Reference | Pointer          | Nodes reference the next node using pointers                |
| Element Access                | O(n)            | Sequential traversal required for access                   |
| Element Modification          | O(n)            | Requires traversal to find and modify specific element     |
| Element Insertion             | O(1)            | Insertion at the beginning (if head is known), otherwise O(n)|
| Element Deletion              | O(1)            | Deletion at the beginning (if head is known), otherwise O(n)|

<br/>

## Linked List Advantages & Disadvantages

#### Advantages:
- **Dynamic Size**: Linked lists can grow and shrink in size dynamically, unlike arrays with fixed size.
- **Efficient Insertion and Deletion**: Insertion and deletion operations can be performed efficiently, especially at the beginning of the list.
- **Versatility**: Linked lists can accommodate elements of different data types and sizes.

#### Disadvantages:
- **Memory Overhead**: Additional memory is required to store pointers for each node, leading to higher overhead compared to arrays.
- **Sequential Access**: Accessing elements requires sequential traversal, which can be inefficient for large lists.
- **Pointer Complexity**: Managing pointers can introduce complexity and potential errors.

#### Linked lists are best used when:
- The size of the data collection is unknown or varies.
- Frequent insertion and deletion operations are expected.
- Random access to elements is not a primary requirement.





