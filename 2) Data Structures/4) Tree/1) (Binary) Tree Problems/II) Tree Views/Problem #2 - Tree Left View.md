
# 2. Tree Left View
The left view of a (Binary) Tree is a set of nodes visible when the tree is visited from the Left side.

<br/>

## 2.1. Graphical Representation
[Source](https://www.geeksforgeeks.org/properties-of-binary-tree/)

<img alt="" src="https://media.geeksforgeeks.org/wp-content/uploads/20230203074235/new-binary-tree.png" style="width: 370px;" />

The left view of the given tree would be:  "2 7 2 5"

<br/>

## 2.2. Algorithm
The left view of a tree can be obtained following several algorithms:
* Right view of a tree via recursion
* Right view of a tree via BFS 

<br/>

## 2.3. Code
### I) Tree Left View via Recursion
> Keep track of the level of a node by passing the level as a parameter to all recursive calls and also keep track of the maximum level. Whenever, we see a node whose level is more than maximum level so far, we print the node because this is the first node in its level 

#### Python code:
```python
# Python program to print left view of Binary Tree

# A binary tree node
class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


# Recursive function print left view of a binary tree
def leftViewUtil(root, level, max_level):

	# Base Case
	if root is None:
		return

	# If this is the first node of its level
	if (max_level[0] < level):
		print (root.data, end = " ")
		max_level[0] = level

	# Recur for left and right subtree
	leftViewUtil(root.left, level + 1, max_level)
	leftViewUtil(root.right, level + 1, max_level)


# A wrapper over leftViewUtil()
def leftView(root):
	max_level = [0]
	leftViewUtil(root, 1, max_level)


# Driver program to test above function
if __name__ == '__main__':
	root = Node(10)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(7)
	root.left.right = Node(8)
	root.right.right = Node(15)
	root.right.left = Node(12)
	root.right.right.left = Node(14)
	
	leftView(root)

# source: https://www.geeksforgeeks.org/print-left-view-binary-tree/

```
<br/>

### II) Tree Right View via BFS
> The left view contains all nodes that are the first nodes in their levels. A simple solution is to do level order traversal and print the first node in every level. 

#### Python code:
```python
# Python3 program to print left view of
# Binary Tree

# Binary Tree Node
""" utility that allocates a newNode 
with the given key """


class newNode:

	# Construct to create a newNode
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None
		self.hd = 0

# function to print left view of
# binary tree


def printLeftView(root):

	if (not root):
		return

	q = []
	q.append(root)

	while (len(q)):

		# number of nodes at current level
		n = len(q)

		# Traverse all nodes of current level
		for i in range(1, n + 1):
			temp = q[0]
			q.pop(0)

			# Print the left most element
			# at the level
			if (i == 1):
				print(temp.data, end=" ")

			# Add left node to queue
			if (temp.left != None):
				q.append(temp.left)

			# Add right node to queue
			if (temp.right != None):
				q.append(temp.right)


# Driver Code
if __name__ == '__main__':

	root = newNode(10)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.left = newNode(7)
	root.left.right = newNode(8)
	root.right.right = newNode(15)
	root.right.left = newNode(12)
	root.right.right.left = newNode(14)
	printLeftView(root)

# source: https://www.geeksforgeeks.org/print-left-view-binary-tree/

````
