# [Geeks for Geeks - Convert Binary Tree into BST](https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/)


## Description

Given a Binary Tree, convert it to a Binary Search Tree. The conversion must be done in such a way that keeps the original structure of Binary Tree.


### Example 1:
```
Input:
          10
         /  \
        2    7
       / \
      8   4
Output:
          8
         /  \
        4    10
       / \
      2   7
```

<br/>
 
## Solution 1 - Inorder traversal

1. Create a temp array arr[] that stores inorder traversal of the tree. This step takes O(n) time.
2. Sort the temp array arr[]. Time complexity of this step depends upon the sorting algorithm. In the following implementation, Quick Sort is used which takes (n^2) time. This can be done in O(nLogn) time using Heap Sort or Merge Sort.
3. Again do inorder traversal of tree and copy array elements to tree nodes one by one. This step takes O(n) time.
	  
```Python
# Program to convert binary tree to BST

# A binary tree node
class Node:
	
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right = None

# Helper function to store the inorder traversal of a tree
def storeInorder(root, inorder):
	
	# Base Case
	if root is None:
		return
	
	# First store the left subtree
	storeInorder(root.left, inorder)
	
	# Copy the root's data
	inorder.append(root.data)

	# Finally store the right subtree
	storeInorder(root.right, inorder)

# A helper function to count nodes in a binary tree
def countNodes(root):
	if root is None:
		return 0

	return countNodes(root.left) + countNodes(root.right) + 1

# Helper function that copies contents of sorted array 
# to Binary tree
def arrayToBST(arr, root):

	# Base Case
	if root is None:
		return
	
	# First update the left subtree
	arrayToBST(arr, root.left)

	# now update root's data delete the value from array
	root.data = arr[0]
	arr.pop(0)

	# Finally update the right subtree
	arrayToBST(arr, root.right)

# This function converts a given binary tree to BST
def binaryTreeToBST(root):
	
	# Base Case: Tree is empty
	if root is None:
		return
	
	# Count the number of nodes in Binary Tree so that 
	# we know the size of temporary array to be created
	n = countNodes(root)

	# Create the temp array and store the inorder traversal 
	# of tree 
	arr = []
	storeInorder(root, arr)
	
	# Sort the array
	arr.sort()

	# copy array elements back to binary tree
	arrayToBST(arr, root)

# Print the inorder traversal of the tree
def printInorder(root):
	if root is None:
		return
	printInorder(root.left)
	print (root.data,end=" ")
	printInorder(root.right)

# Driver program to test above function
root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right = Node(5)

# Convert binary tree to BST 
binaryTreeToBST(root)

print ("Following is the inorder traversal of the converted BST")
printInorder(root)

```

<br/>

## Solution 2 - Inorder traversal + Vector sorting

In this approach, we will first perform an inorder traversal of the binary tree and store the nodes in a vector. After that, we will sort the vector in ascending order, and then use the sorted vector to construct a binary search tree.

 * Define a struct for a binary tree node with a value, left and right pointers.
 * Implement an inorder traversal of the binary tree to store the nodes in a vector. In this implementation, a vector of TreeNode* is used to store the nodes in inorder traversal order. The function takes in a TreeNode* root and a reference to the vector of TreeNode* nodes.
 * Implement a function to construct a binary search tree from the sorted vector of TreeNode* nodes. The function takes in the vector of TreeNode* nodes, start index, and end index of the vector. It recursively constructs the binary search tree by taking the middle element of the vector as the root, and then constructing the left and right subtrees recursively.
 * Implement a function to convert a binary tree to a binary search tree. This function takes in the root of the binary tree and returns the root of the binary search tree. It first calls the inorder traversal function to store the nodes of the binary tree in a vector, then sorts the vector of TreeNode* based on the values of the nodes using a lambda function, and finally calls the function to construct the binary search tree.
 * Implement a function to print the inorder traversal of a binary tree. This function takes in the root of the binary tree and prints its inorder traversal.
 * In the driver code, create a binary tree with some nodes, print its inorder traversal, convert it to a binary search tree, print the inorder traversal of the binary search tree, and free the dynamically allocated memory for the nodes.
	  
```Python
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# Inorder traversal to store the nodes in a list
def inorder(root, nodes):
	if root is None:
		return
	inorder(root.left, nodes)
	nodes.append(root)
	inorder(root.right, nodes)

# Function to construct a binary search tree from a sorted list
def constructBST(nodes, start, end):
	if start > end:
		return None
	mid = (start + end) // 2
	root = nodes[mid]
	root.left = constructBST(nodes, start, mid - 1)
	root.right = constructBST(nodes, mid + 1, end)
	return root

# Function to convert a binary tree to a binary search tree
def convertToBST(root):
	nodes = []
	inorder(root, nodes)
	nodes.sort(key=lambda node: node.val)
	return constructBST(nodes, 0, len(nodes) - 1)

# Function to print the inorder traversal of a binary tree
def printInorder(root):
	if root is None:
		return
	printInorder(root.left)
	print(root.val, end=" ")
	printInorder(root.right)

# Driver code
if __name__ == "__main__":
	# Example binary tree
	root = TreeNode(10)
	root.left = TreeNode(30)
	root.right = TreeNode(15)
	root.left.left = TreeNode(20)
	root.left.right = TreeNode(5)

	# Convert binary tree to binary search tree
	bst = convertToBST(root)

	print("Following is Inorder Traversal of the converted BST:")
	printInorder(bst)
	print()
	
```
