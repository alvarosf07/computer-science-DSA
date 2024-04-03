# Tree Inorder Traversal
## Algorithm

1. Traverse the left subtree, i.e., call Inorder(left->subtree)
1. Visit the root.
1. Traverse the right subtree, i.e., call Inorder(right->subtree)

<br/>

## Graphic Representation
<img alt="" src="https://builtin.com/sites/www.builtin.com/files/inline-images/2_tree-traversal.gif" style="width: 370px;" />

[Source](https://builtin.com/software-engineering-perspectives/tree-traversal)

<br/>

## Code
```python
# Python3 program to for tree traversals


# A class that represents an individual node in a
# Binary Tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do inorder tree traversal
def printInorder(root):

	if root:

		# First recur on left child
		printInorder(root.left)

		# Then print the data of node
		print(root.val, end=" "),

		# Now recur on right child
		printInorder(root.right)


# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	# Function call
	print("Inorder traversal of binary tree is")
	printInorder(root)


# source: https://www.geeksforgeeks.org/vertical-order-traversal-of-binary-tree-using-map/

```
