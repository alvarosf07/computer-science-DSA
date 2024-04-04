
# 4. Tree Preorder Traversal

<br/>

## 4.1. Algorithm
The main idea of level order traversal is to traverse all the nodes of a lower level before moving to any of the nodes of a higher level. This can be done in any of the following ways: 

* The naive one (finding the height of the tree and traversing each level and printing the nodes of that level)
* Efficiently using a queue.


<br/>

## 4.2. Graphic Representation

[Source](https://builtin.com/software-engineering-perspectives/tree-traversal)

<img alt="" src="https://builtin.com/sites/www.builtin.com/files/inline-images/5_tree-traversal.gif" style="width: 370px;" />


<br/>

## 4.3. Code

#### I) Naive Approach:
Find the height of the tree and traverse each level printing the nodes of that level

```python
# Recursive Python program for level
# order traversal of Binary Tree


# A node structure
class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None


# Function to print level order traversal of tree
def printLevelOrder(root):
	h = height(root)
	for i in range(1, h+1):
		printCurrentLevel(root, i)


# Print nodes at a current level
def printCurrentLevel(root, level):
	if root is None:
		return
	if level == 1:
		print(root.data, end=" ")
	elif level > 1:
		printCurrentLevel(root.left, level-1)
		printCurrentLevel(root.right, level-1)


# Compute the height of a tree--the number of nodes
# along the longest path from the root node down to
# the farthest leaf node
def height(node):
	if node is None:
		return 0
	else:

		# Compute the height of each subtree
		lheight = height(node.left)
		rheight = height(node.right)

		# Use the larger one
		if lheight > rheight:
			return lheight+1
		else:
			return rheight+1


# Driver program to test above function
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	print("Level order traversal of binary tree is -")
	printLevelOrder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


# source: https://www.geeksforgeeks.org/level-order-tree-traversal/

```
<br/>

#### II) Efficient Approach:
For each node, first, the node is visited and then it’s child nodes are put in a FIFO queue. Then again the first node is popped out and then it’s child nodes are put in a FIFO queue and repeat until queue becomes empty.

```python
# Python program to print level
# order traversal using Queue


# A node structure
class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None


# Iterative Method to print the
# height of a binary tree
def printLevelOrder(root):

	# Base Case
	if root is None:
		return

	# Create an empty queue
	# for level order traversal
	queue = []

	# Enqueue Root and initialize height
	queue.append(root)

	while(len(queue) > 0):

		# Print front of queue and
		# remove it from queue
		print(queue[0].data, end=" ")
		node = queue.pop(0)

		# Enqueue left child
		if node.left is not None:
			queue.append(node.left)

		# Enqueue right child
		if node.right is not None:
			queue.append(node.right)


# Driver Program to test above function
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	print("Level Order Traversal of binary tree is -")
	printLevelOrder(root)


# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


# source: https://www.geeksforgeeks.org/level-order-tree-traversal/

```
