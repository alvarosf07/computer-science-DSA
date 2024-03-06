# Data Structures I - Array

Arrays are fundamental data structures that allow storing and accessing a collection of elements of the same data type in contiguous memory locations. 
Arrays are among the oldest and most important data structures; they offer a convenient way to organize and manipulate data efficiently and are used by almost every program.

<br/>

> An array is a linear data structure consisting of a collection of elements (pre)allocated in contiguous spaces in the computer memory address.
> Each element in an array occupies the same amount of space in memory and can be identified by at least one index or key.

<br/>

## Understanding

Arrays can be visualized as a sequential arrangement of elements, where each element has a unique index. Imagine a row of boxes in which you can store items. Each box has its own number, indicating its position in the row. Here's an illustration to help visualize:

![Array Visualization](/Resources/Images/array_visualization.png)

<br/>

## Characteristics

| Characteristic                      | Time Complexity | Description                                                |
|-------------------------------------|-----------------|------------------------------------------------------------|
| Memory Address - Time of Allocation | O(1)            | Compiled at initialization (arrays require pre-allocating a big chunk of sequential memory to store data) |
| Memory Address - Spatial Allocation | -               | Contiguous memory allocation                               |
| Memory Address - Space              | -               | Fixed-size (determined at initialization)                    |
| Memory Address - Data Types         | -               | Homogeneous data types                                     |
| Memory Address - Data Reference     | -               | Elements are accessed using their index or position in the array |
| Element Access                      | O(1)            | Direct access using index                                  |
| Element Modification                | O(1)            | Direct modification using index                            |
| Element Insertion                   | O(n)            | Requires shifting elements                                 |
| Element Deletion                    | O(n)            | Requires shifting elements                                 |

<br/>

## Array Advantages

Arrays offer several advantages over other data structures:
- **Efficient Memory Spatial Allocation**: Arrays use contiguous memory allocation, reducing overhead.
- **Efficient Element Access and Modification**: Elements can be accessed directly using their index, with constant time complexity.
- **Simple Implementation**: Arrays are straightforward to implement and use.
  
Disadvantages:
- **Fixed Size**: Most arrays have a fixed size, limiting flexibility.
- **Homogeneous Data**: Arrays typically store elements of the same data type, restricting versatility.
- **Inefficient Insertion and Deletion**: Insertion and deletion operations may require shifting elements, leading to inefficiency, with linear time complexity.


Arrays are best used when:
- Random access to elements is required.
- Memory usage needs to be optimized.
- The size of the data collection is known and fixed.
