
# 1. Tree Right View
The right view of a (Binary) Tree is a set of nodes visible when the tree is visited from the Right side.

<br/>

## 1.1. Graphical Representation
[Source](https://www.geeksforgeeks.org/properties-of-binary-tree/)

<img alt="" src="https://media.geeksforgeeks.org/wp-content/uploads/20230203074235/new-binary-tree.png" style="width: 370px;" />

The right view of the given tree would be:  "2 5 9 4"

<br/>

## 1.2. Algorithm
The right view of a tree can be obtained following several algorithms:
* Right view of a tree via recursion
* Right view of a tree via BFS 

<br/>

## 1.3. Code
### I) Tree Right View via Recursion
```
The idea is to use recursion and keep track of the maximum level also. And traverse the tree in a manner that the right subtree is visited before the left subtree.
```
#### Python code:
```python
# Python program to print right view of Binary Tree

# A binary tree node


class Node:
	# A constructor to create a new Binary tree Node
	def __init__(self, item):
		self.data = item
		self.left = None
		self.right = None

# Recursive function to print right view of Binary Tree
# used max_level as reference list ..only max_level[0]
# is helpful to us


def rightViewUtil(root, level, max_level):

	# Base Case
	if root is None:
		return

	# If this is the last node of its level
	if (max_level[0] < level):
		print "%d " % (root.data),
		max_level[0] = level

	# Recur for right subtree first, then left subtree
	rightViewUtil(root.right, level+1, max_level)
	rightViewUtil(root.left, level+1, max_level)


def rightView(root):
	max_level = [0]
	rightViewUtil(root, 1, max_level)


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

rightView(root)

# source: https://www.geeksforgeeks.org/print-right-view-binary-tree-2/

```
<br/>

### II) Tree Right View via BFS
```
The idea is to use Level Order Traversal as the last node every level gives the right view of the binary tree.
```
#### Python code:
```python
# Python3 program to print right
# view of Binary Tree
from collections import deque

# A binary tree node


class Node:

	# A constructor to create a new
	# Binary tree Node
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None

# Function to print Right view of
# binary tree


def rightView(root):

	if root is None:
		return

	q = deque()
	q.append(root)

	while q:

		# Get number of nodes for each level
		n = len(q)

		# Traverse all the nodes of the
		# current level

		while n > 0:
			n -= 1

			# Get the front node in the queue
			node = q.popleft()

			# Print the last node of each level
			if n == 0:
				print(node.data, end=" ")

			# If left child is not null push it
			# into the queue
			if node.left:
				q.append(node.left)

			# If right child is not null push
			# it into the queue
			if node.right:
				q.append(node.right)

# Driver code


# Let's construct the tree as
# shown in example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

rightView(root)

# source: https://www.geeksforgeeks.org/print-right-view-binary-tree-2/

````
