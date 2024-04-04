# 3. Tree Preorder Traversal

<br/>

## 3.1. Algorithm
1. Traverse the left subtree, i.e., call Preorder(left->subtree)
2. Traverse the right subtree, i.e., call Preorder(right->subtree)
3. Visit the root


<br/>

## 3.2. Graphic Representation

[Source](https://builtin.com/software-engineering-perspectives/tree-traversal)

<img alt="" src="https://builtin.com/sites/www.builtin.com/files/inline-images/4_tree-traversal.gif" style="width: 370px;" />


<br/>

## 3.3. Code
```python


# Python3 program to for tree traversals
 
 
# A class that represents an individual node
# in a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
# A function to do postorder tree traversal
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # The recur on right child
        printPostorder(root.right)
 
        # Now print the data of node
        print(root.val, end=" "),
 
 
# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    # Function call
    print("Postorder traversal of binary tree is")
    printPostorder(root)


# source: https://www.geeksforgeeks.org/vertical-order-traversal-of-binary-tree-using-map/

```
