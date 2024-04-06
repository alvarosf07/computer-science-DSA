# Data Structure IV - Tree
> A tree is a hierarchical data structure consisting of nodes connected by edges. Each node has a parent node and zero or more child nodes, forming a tree-like structure.
>
> Trees are widely used to represent hierarchical relationships and organize data efficiently.

<br/>

## 1.1. Definition
#### 📖 A slightly more technical definition of a Tree:
  A tree is a collection of elements stored in a non-linear structure of nodes that don't need to be at sequential memory addresses. 
  Each node can take as much memory as needed, and will contain two pieces of data: its value, and a pointers to other nodes in a hierarchical direction parent-to-child, where:
  +  No two references can link to the same node
  +  Root has no reference

#### 🆚 Tree vs Linked List
A tree is similar to a linked-list, with 2 main differences:
  + Is a Non-Sequential Collection of elements (don't need to be stored linearly in memory addresses)
  + Each node can have any number of links to other nodes, but these links MUST occur in a hierarchical direction parent-to-child, where:
    + Every node of the tree must have exactly one parent...
    + Except for the Root, which has no reference

<br/>

## 1.2. Understanding

Imagine a family tree, where each person is a node and relationships between family members are represented by edges. Visualizing a tree in this way can help understand the hierarchical structure:

<img src="/Resources/Images/tree_visualization.png" width="600">

<br/>

## 1.3. Characteristics

| Characteristic                | Time Complexity | Description                                                |
|-------------------------------|-----------------|------------------------------------------------------------|
| Memory Time Allocation        | -               | Dynamically allocated as nodes are added                    |
| Memory Spatial Allocation     | Hierarchical    | Nodes are organized hierarchically                           |
| Memory Address - Space        | Limited by system memory | Dynamically allocated, theoretically infinite       |
| Memory Address - Types        | -               | Typically allows any data type                             |
| Memory Address - Data Reference | Node or Edge    | Nodes reference their parent and child nodes through pointers|
| Element Access                | O(log n)        | Typically requires traversing the tree, O(log n) on average |
| Element Modification          | O(1)            | Direct modification of nodes and edges using pointers      |
| Element Insertion             | O(log n)        | Requires traversal to find insertion point, O(log n) on average|
| Element Deletion              | O(log n)        | Requires traversal to find deletion point, O(log n) on average|

<br/>

## 1.4. Tree Advantages, Disadvantages and Uses

#### Advantages:
- **Hierarchical Organization**: Provides a natural way to represent hierarchical relationships.
- **Element Modification and Access**: Searching for elements in a balanced tree can be done efficiently with O(log n) time complexity.
- **Relatively Fast Element Insertion and Deletion**: Balanced trees allow for efficient insertion and deletion operations.

#### Disadvantages:
- **Memory Overhead**: Requires additional memory for storing pointers, especially in large trees.
- **Complexity**: Implementing and maintaining tree structures can be complex.
- **Balancing**: Ensuring trees remain balanced (e.g., AVL trees) can be challenging.

#### Trees are best used when:
- Organizing data hierarchically, such as file systems or organizational charts.
- Implementing efficient search and retrieval operations.
- Maintaining sorted collections of data.

<br/>
<br/>

# 2. Types of Trees
There can be several types of trees, depending on different factors:

  * Trees by Number of Nodes:
    * Binary Tree
    * Generic Tree
  
  * Trees by Sorting Mechanism:
    * Binary Search Tree (BST) (horizontal sorting)
    * (Binary) Heap (vertical sorting)

<br/>

## 2.1. Binary Tree
Special type of tree where each parent node can have at most 2 children.

<br/>

## 2.2. Generic Tree 
Tree that is not a binary tree (at least one node has more than 2 children).

<br/>

## 2.3. (Binary) Search Tree (BST)
> Is a special type of binary tree which is horizontally sorted: all children to the left are lower than the parent, and all children to the right are higher than the parent.

<br/>

<img src="/Resources/Images/BST_visualization.png" width="500">

BSTs present 2 main advantages:
  * **Efficient Element Search/Access** - Element Access in `O(H)`, where H is the height of the tree. H is on average `Log2 N`.
  * **Efficient Element Insertion/Deletion** - Element Insertion/Deletion in `O(H)`, where H is the height of the tree. H is on average `Log2 N`.
  
  <br/>

  ### 2.3.1. Unbalanced BST
  There's one particular situation in Binary Search Trees (BST), where there are too many nodes that have only one child and are mainly located on one side of the Tree. 

  This is a common situation when we insert nodes lower/higher than the parent (they can only be placed to the left/right of the parent, all the time).

  The previous situation is not an ideal one, because the tree would be behaving more like a linked list. When the height of a tree is too high, operations become too inefficient.

  In this situation, the best solution is to rearrange the nodes in a tree, such that its height is reduced (and most nodes have 2 children). This is called "tree balancing".

  <img src="/Resources/Images/BST_unbalanced_visualization.png" width="550">
  
  <br/>

  ### 2.3.2. Balanced BST
  A perfectly balanced tree has the minimum possible height.
  
  Consider a Binary Search Tree with n nodes. Its maximum height is n, in which case it looks like a Linked List. The minimum height, with the tree perfectly balanced, is log2 n.

  The complexity of searching an item in a binary search tree is proportional to its height. In the worst case, the search must descend to the lowest level, reaching all the way to the tree’s leaves in order to find the item. 
  Searching in a balanced Binary Search Tree with n items is thus O(log2 n).

  That’s why balanced BSTs are often chosen for implementing Sets (which requires finding if items are already present) and Maps (which requires finding key-values).

  <br/>

  ### 2.3.3. Tree Balancing
  > The balancing process in a Binary Search Tree (BST) typically refers to maintaining the binary search property after insertions and deletions, ensuring that the height of the tree remains logarithmic with respect to the number of nodes.
  
  > BTS balancing typically consists on re-arranging the nodes of a tree which has more levels than its minimum possible height (as consequence of the causes explained above: parents with only one child and/or located on only one side of the tree).

  <br/>
  
  #### Tree Balancing Process
  
  * **Insertion:** When a new node is inserted into a BST, it is placed according to its key value while maintaining the binary search property. The new node is inserted as a leaf node.
  * **Rotation:** If the insertion causes the tree to become unbalanced, rotations may be performed to restore balance. The two primary rotation operations are:
    * Left Rotation: This operation is performed when a node becomes right-heavy due to insertion in its left subtree. It involves rotating the node to the left.
    * Right Rotation: This operation is performed when a node becomes left-heavy due to insertion in its right subtree. It involves rotating the node to the right.
  * **Recursive Balancing:** After a rotation, the balancing process may need to be applied recursively up the tree to ensure that all ancestors maintain the binary search property.
  * **Deletion:** When a node is deleted from a BST, its position is replaced by its successor (or predecessor) node to maintain the binary search property. If necessary, rotations are performed to rebalance the tree after deletion.
  * **Balanced Height:** The goal of the balancing process in a BST is to maintain a balanced height, ensuring that the height of the tree remains logarithmic with respect to the number of nodes. This ensures efficient search, insertion, and deletion operations with time complexity O(log n).

  <br/>
  
  #### Tree Balancing Drawback:
  As we've seen, balanced BTSs allow to capture all the full advantages of logarithmic_2 search within the tree.
  However, tree balancing is an expensive operation, as it requires sorting all nodes. Rebalancing a tree after each insertion or deletion can greatly slow down these operations. 
  Usually, trees undergo balancing after several insertions and deletions take place. But balancing the tree from time to time is only a reasonable strategy for trees that are rarely changed. 
  To efficiently handle binary trees that change a lot, self-balancing binary trees were invented.

  <br/>

  ### 2.3.4. Self-Balancing BSTs
  Self-balancing Trees are those whose procedures for inserting or removing items directly ensure the tree stays balanced:
  
  * **Red-Black Tree:**
    * **Quick Definition** - The Red-Black Tree is a famous example of a self-balancing tree, which colors nodes either “red” or “black” for its balancing strategy.
    * **Balancing Strategy** - They ensure that the tree remains balanced after insertion and deletion operations by applying specific rules to the structure of the tree and performing rotations when necessary.
        The balancing strategy of a red-black tree revolves around maintaining five properties:
        * Node Color: Each node is either red or black.
        * Root Property: The root node is black.
        * Red Property: Red nodes cannot have red children; every red node must have two black children.
        * Depth Property: All paths from a node to its descendant leaves must have the same number of black nodes. This property ensures that the tree remains balanced.
        * Leaf Nodes: Leaf nodes, often represented as NULL or sentinel nodes, are considered black.

      When inserting a new node into a red-black tree, the tree may become unbalanced. To maintain the properties of the red-black tree, the following strategies are applied:
        * Node Color Adjustment: When inserting a new node, it is initially colored red, violating the red property. However, this violation is resolved by recoloring nodes or performing rotations.
        * Rotation: Rotations are performed to restore the balance of the tree while preserving the properties of the red-black tree. There are two types of rotations:
          * Left Rotation: Moves a node down and to the left, promoting the right child of the node.
          * Right Rotation: Moves a node down and to the right, promoting the left child of the node.
      
      By applying these balancing strategies, red-black trees maintain a balanced structure, ensuring efficient search, insertion, and deletion operations with logarithmic time complexity.
    * **Uses** - Red-Black Trees are frequently used to implement Maps: the map can be heavily edited in an efficient way, and finding any given key in the map remains fast because of self-balancing.
  
  * **AVL Tree:**
    * **Quick Definition** - They require a bit more time to insert and delete items than Red-Black Trees, but tend to have better balancing. This means they’re faster than Red-Black Trees for retrieving items.
    * **Balancing Strategy** - The balancing strategy in AVL trees involves performing rotations to ensure that the tree remains balanced according to the AVL tree property. This property states that for every node in the tree, the heights of its left and right subtrees differ by at most one.
        To maintain this property after insertion or deletion operations, the tree may need to be rebalanced through one or more rotations.
    * **Uses** - AVL Trees are often used to optimize performance in read-intensive scenarios.
  
  * **B-Tree:**
    * **Quick Definition** - B-Trees are a generalization of Binary Trees. In B-trees, nodes may store more than one item and can have more than two children, making it efficient to operate with data in big chunks.
    * **Balancing Strategy** - The balancing strategy in B-trees involves maintaining a balance between height and the number of keys in each node. This is achieved by performing 4 types of operations:
      * **Insertion**: When a new key is inserted into a B-tree, it is first placed into the appropriate leaf node. If inserting the key causes the leaf node to exceed its maximum capacity, a split operation is performed.
      * **Split Operation**: When a leaf node is split due to insertion, approximately half of its keys are moved to a new node. The median key is then promoted to the parent node. If the parent node also exceeds its maximum capacity, the split operation is recursively applied to it.
      * **Rebalancing**: After a split operation, the parent node may also exceed its maximum capacity. In this case, the process is repeated recursively up the tree until a node is reached that does not exceed its maximum capacity.
      * **Merge Operation (Optional)**: During deletion, if a node falls below a minimum occupancy threshold, it may be merged with a neighboring node. This operation ensures that the B-tree remains balanced and efficient.
    * **Uses** - B-Trees are commonly used in database systems.


  <br/>

  ### 2.3.5. BSTs vs Hash Maps ([see source](https://www.geeksforgeeks.org/advantages-of-bst-over-hash-table/))
  Hash Table supports following operations in ?(1) time: 1) Search 2) Insert 3) Delete The time complexity of above operations in a self-balancing Binary Search Tree (BST) (like Red-Black Tree, AVL Tree, Splay Tree, etc) is O(Logn).  So Hash Table seems to beating BST in all common operations. When should we prefer BST over Hash Tables then? What are the advantages of BSTs vs Hash Maps?
  1. We can get all keys in sorted order by just doing Inorder Traversal of BST. This is not a natural operation in Hash Tables and requires extra efforts.
  2. Doing order statistics, finding closest lower and greater elements, doing range queries are easy to do with BSTs. Like sorting, these operations are not a natural operation with Hash Tables.
  3. BSTs are easy to implement compared to hashing, we can easily implement our own customized BST. To implement Hashing, we generally rely on libraries provided by programming languages.
  4. With Self-Balancing BSTs, all operations are guaranteed to work in O(Logn) time. But with Hashing, ?(1) is average time and some particular operations may be costly i.e, O(n2 ), especially when table resizing happens.
  5. Range searches can be done efficiently with BSTs, but hash tables can also support efficient range searches if implemented properly with techniques such as linear probing or chaining.
  6. BST are memory efficient but Hash table is not.
  7. BST does not require a load factor to be maintained as in Hash tables.
  8. BST can support multiple keys with the same value, whereas Hash tables use the key to identify unique elements and cannot have multiple keys with the same value.
  9. BST have a lower overhead in terms of memory and computational complexity, whereas Hash tables require additional memory to store hash values and handle collisions.
  10. BST performs well on small data sets with a small number of elements, whereas Hash tables are not highly suitable for small data sets with a few elements.
  11. BST allows for recursion, which can be used to solve problems more elegantly and efficiently. Hash tables do not allow for recursion.
  12. BST can be easily merged by using a different data structure such as a B+ tree, whereas Hash tables do not have a straightforward method for merging.
  
  
<br/>

## 2.4. (Binary) Heap
  > A Heap is a special type of binary tree which is vertically sorted: the parent nodes must always be greater (or lower) than both children nodes.

The main advantage of Heaps is their great efficiency **finding the highest or smallest item of the tree**. They can do it in constant time `O(1)`, because it's always the Root node of the tree.

However, accessing or inserting/deleting other nodes still costs `O(log n)`. 
  * Data is added by swapping nodes for parents until heap properties are satisfied.
  * Data is removed with queues (always shift target with last element in the queue, and then bubble up or down to satisfy heap rules).

<img src="/Resources/Images/heap_visualization.png" width="430">

<br/>

### 2.4.1. Types of Heaps
There are two main types of heaps:
* **Max Heap** -  It has the highest element at the root of the tree.
* **Min Heap** -  It has the lowest element at the root of the tree.

<img src="/Resources/Images/heapmin_visualization.png" width="380">

<br/>

### 2.4.2. Balanced Heap
If a Binary Heap has its minimum possible height, it is said to be balanced.

<br/>



