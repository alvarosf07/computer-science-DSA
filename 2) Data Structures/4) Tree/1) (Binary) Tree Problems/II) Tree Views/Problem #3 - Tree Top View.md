
# 3. Tree Left View
The top view of a (Binary) Tree is a set of nodes visible when the tree is visited from the top.

<br/>

## 3.1. Graphical Representation
[Source](https://www.geeksforgeeks.org/properties-of-binary-tree/)

<img alt="" src="https://media.geeksforgeeks.org/wp-content/uploads/20230203074235/new-binary-tree.png" style="width: 370px;" />

The left view of the given tree would be:  "2 7 2 5 9"

<br/>

## 3.2. Algorithm
The main approach to solve the top view problem is to follow a similar strategy to the vertical tree traversal, ordering the tree in vertical levels and selecting the uppermost node of every level.

<br/>

## 3.3. Code
> The idea is to do something similar to vertical Order Traversal. Like vertical Order Traversal, we need to put nodes of the same horizontal distance together. We do a level order traversal so that the topmost node at a horizontal node is visited before any other node of the same horizontal distance below it. Hashing is used to check if a node at a given horizontal distance is seen or not. 

#### Python code:
```python
# Python3 program to print top
# view of binary tree

# Binary Tree Node
class newNode:

	# Construct to create a newNode
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None
		self.hd = 0

# function should print the topView
# of the binary tree


def topview(root):

	if(root == None):
		return
	q = []
	m = dict()
	hd = 0
	root.hd = hd

	# push node and horizontal
	# distance to queue
	q.append(root)

	while(len(q)):
		root = q[0]
		hd = root.hd

		# count function returns 1 if the
		# container contains an element
		# whose key is equivalent to hd,
		# or returns zero otherwise.
		if hd not in m:
			m[hd] = root.data
		if(root.left):
			root.left.hd = hd - 1
			q.append(root.left)

		if(root.right):
			root.right.hd = hd + 1
			q.append(root.right)

		q.pop(0)
	for i in sorted(m):
		print(m[i], end=" ")


# Driver Code
if __name__ == '__main__':

	""" Create following Binary Tree
		 1
		/ \
               2   3
                \
                 4
                  \
                   5
                     \
                       6
	"""
	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.right = newNode(4)
	root.left.right.right = newNode(5)
	root.left.right.right.right = newNode(6)
	print("The top view of the tree is: ")  # Output: 2 1 3 6
	topview(root)


# source: https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/

```
<br/>
