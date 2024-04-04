
# 6. Tree Diagonal Traversal

<br/>

## 6.1. Algorithm
In the Diagonal Traversal of a Tree, all the nodes in a single diagonal will be printed one by one.


<br/>

## 6.2. Graphic Representation

[Source](https://www.geeksforgeeks.org/diagonal-traversal-of-binary-tree/)

<img alt="" src="https://media.geeksforgeeks.org/wp-content/uploads/d1-1.png" style="width: 370px;" />

For example, boundary traversal of the following tree is “8 10 14 3 6 7 13 1 4”

<br/>

## 6.3. Code

```python
# Python program for diagonal 
# traversal of Binary Tree

# A binary tree node
class Node:

	# Constructor to create a 
	# new binary tree node
	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right = None


""" root - root of the binary tree
d - distance of current line from rightmost
		-topmost slope.
diagonalPrint - multimap to store Diagonal
				elements (Passed by Reference) """
def diagonalPrintUtil(root, d, diagonalPrintMap):
	
	# Base Case 
	if root is None:
		return

	# Store all nodes of same line 
	# together as a vector
	try :
		diagonalPrintMap[d].append(root.data)
	except KeyError:
		diagonalPrintMap[d] = [root.data]

	# Increase the vertical distance 
	# if left child
	diagonalPrintUtil(root.left, d+1, diagonalPrintMap)
	
	# Vertical distance remains 
	# same for right child
	diagonalPrintUtil(root.right, d, diagonalPrintMap)



# Print diagonal traversal of given binary tree
def diagonalPrint(root):

	# Create a dict to store diagonal elements 
	diagonalPrintMap = dict()
	
	# Find the diagonal traversal
	diagonalPrintUtil(root, 0, diagonalPrintMap)

	print ("Diagonal Traversal of binary tree : ")
	for i in diagonalPrintMap:
		for j in diagonalPrintMap[i]:
			print (j,end=" ")
		print()


# Driver Program 
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)

diagonalPrint(root)

# Source: https://www.geeksforgeeks.org/diagonal-traversal-of-binary-tree/
```
