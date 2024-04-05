# [Geeks for Geeks - Check if Binary Tree is BST](https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/)
https://leetcode.com/problems/validate-binary-search-tree/


## Description

A Binary Search Tree (BST) is a node-based binary tree data structure that has the following properties:

* The left subtree of a node contains only nodes with keys less than the node’s key.
* The right subtree of a node contains only nodes with keys greater than the node’s key.
* Both the left and right subtrees must also be binary search trees.
* Each node (item in the tree) has a distinct key.

Given a Binary Tree, return `True` if it's a Binary Search Tree or `False` if it's not.

<br/>

 ## Solution 1 - Naive Approach
 
 The idea is to for each node, check if max value in left subtree is smaller than the node and min value in right subtree greater than the node. 
 
<!-- tabs:start -->

#### Python:
```python
# Python program to check if a binary tree is bst or not
# A binary tree node has data, pointer to left child
# and a pointer to right child
class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def maxValue(node):
	if node is None:
		return 0;
	
	leftMax = maxValue(node.left)
	rightMax = maxValue(node.right)
	
	value = 0;
	if leftMax > rightMax:
		value = leftMax
	else:
		value = rightMax
	
	if value < node.data:
		value = node.data
	
	return value
	
def minValue(node):
	if node is None:
		return 1000000000
	
	leftMax = minValue(node.left)
	rightMax = minValue(node.right)
	
	value = 0
	if leftMax < rightMax:
		value = leftMax
	else:
		value = rightMax
	
	if value > node.data:
		value = node.data
	
	return value

# Returns true if a binary tree is a binary search tree
def isBST(node):
	if node is None:
		return True
	
	# false if the max of the left is > than us
	if(node.left is not None and maxValue(node.left) > node.data):
		return False
	
	# false if the min of the right is <= than us
	if(node.right is not None and minValue(node.right) < node.data):
		return False
	
	#false if, recursively, the left or right is not a BST
	if(isBST(node.left) is False or isBST(node.right) is False):
		return False
	
	# passing all that, it's a BST
	return True

# Driver code
if __name__ == "__main__":
root = Node(4)
root.left = Node(2)
root.right = Node(5)
# root.right.left = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)

# Function call
if isBST(root) is True:
	print("Is BST")
else:
	print("Not a BST")

```

<br/>

## Solution 2 - BSF (Inorder traversal)
 
 > The idea is to use Inorder traversal of a binary search tree generates output, sorted in ascending order. So generate inorder traversal of the given binary tree and check if the values are sorted or not

#### Python:
```python
# Python program to check if a binary tree is bst or not

import math

# A binary tree node has data,
# pointer to left child and
# a pointer to right child
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def isBSTUtil(root, prev):

	# traverse the tree in inorder fashion
	# and keep track of prev node
	if (root != None):
		if (isBSTUtil(root.left, prev) == False):
			return False

		# Allows only distinct valued nodes
		if (prev != None and
				root.data <= prev.data):
			return False

		prev = root
		return isBSTUtil(root.right, prev)

	return True


def isBST(root):
	prev = None
	return isBSTUtil(root, prev)


# Driver Code
if __name__ == '__main__':
	root = Node(3)
	root.left = Node(2)
	root.right = Node(5)
	root.right.left = Node(1)
	root.right.right = Node(4)

	# Function call
	if (isBST(root) == None):
		print("Is BST")
	else:
		print("Not a BST")

```
