# 2. Tree Preorder Traversal

<br/>

## 2.1. Algorithm
1. Visit the root.
2. Traverse the left subtree, i.e., call Preorder(left->subtree)
3. Traverse the right subtree, i.e., call Preorder(right->subtree) 

<br/>

## 2.2. Graphic Representation

[Source](https://builtin.com/software-engineering-perspectives/tree-traversal)

<img alt="" src="https://builtin.com/sites/www.builtin.com/files/inline-images/3_tree-traversal.gif" style="width: 370px;" />


<br/>

## 2.3. Code
```python
# Python3 program to for tree traversals
 
 
# A class that represents an individual node
# in a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
# A function to do preorder tree traversal
def printPreorder(root):
 
    if root:
 
        # First print the data of node
        print(root.val, end=" "),
 
        # Then recur on left child
        printPreorder(root.left)
 
        # Finally recur on right child
        printPreorder(root.right)
 
 
# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    # Function call
    print("Preorder traversal of binary tree is")
    printPreorder(root)


# source: https://www.geeksforgeeks.org/vertical-order-traversal-of-binary-tree-using-map/

```
