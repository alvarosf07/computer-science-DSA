# Binary Tree Search (BTS)

> Binary Tree Search (BTS), also known as binary search tree (BST) traversal, is a method used to search for a specific value in a binary tree data structure. It utilizes the properties of binary trees to efficiently locate the desired value.

<br/>

## How Does Binary Tree Search Work?

Binary Tree Search works by traversing the binary tree in a specific order (in-order, pre-order, or post-order) and comparing the target value with each node encountered during the traversal. Based on the comparison, the algorithm decides whether to continue searching in the left subtree, right subtree, or terminate the search if the target value is found.

<br/>

## Step-by-Step Guide of Binary Tree Search:

1. **Start at the Root Node:** Begin the search at the root node of the binary tree.

2. **Compare with Current Node:** Compare the target value with the value of the current node.

3. **Go Left or Right:** Based on the comparison result:
   - If the target value is less than the value of the current node, move to the left subtree.
   - If the target value is greater than the value of the current node, move to the right subtree.

4. **Repeat:** Continue steps 2-3 recursively until the target value is found or all nodes have been traversed.

5. **Termination:** Terminate the search if the target value is found, otherwise, return a message indicating that the value is not present in the binary tree.

For a visual demonstration of Binary Tree Search, you can watch this [video](https://www.youtube.com/watch?v=5cPbNCrdotA) tutorial.

<br/>

## Key Features of Binary Tree Search:

1. **Efficiency:** Binary Tree Search has an average time complexity of O(log n) for balanced binary trees, making it highly efficient for searching large datasets.

2. **Versatility:** Binary Tree Search can be applied to various types of binary trees, including binary search trees (BSTs) and balanced binary trees (AVL trees).

3. **Space Efficiency:** Binary Tree Search requires minimal additional memory overhead, as it only requires storage for the current node being examined during the search.

<br/>

## When to Use Binary Tree Search:

Binary Tree Search is most commonly used in scenarios where:

- The data is organized in a hierarchical structure represented by a binary tree.
- Efficient searching, insertion, and deletion operations are required.
- The data is sorted or can be organized in a way that facilitates binary tree traversal.

<br/>

## Example of Binary Tree Search:

Consider the problem of searching for the value 7 in the following binary search tree:

```markdown
    5
   / \
  3   8
 / \   \
1   4   10
       /
      7
```

Applying Binary Tree Search, we would start at the root (5), compare with 7, then move to the right subtree since 7 is greater than 5. Continuing this process, we would eventually find the target value 7 in the binary tree.

