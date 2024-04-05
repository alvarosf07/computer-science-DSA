
# 4. Tree Bottom View
The bottom view of a (Binary) Tree is a set of nodes visible when the tree is visited from the bottom.

<br/>

## 4.1. Graphical Representation
[Source](https://www.geeksforgeeks.org/properties-of-binary-tree/)

<img alt="" src="https://media.geeksforgeeks.org/wp-content/uploads/20230203074235/new-binary-tree.png" style="width: 370px;" />

The bottom view of the given tree would be:  "2 5 11 4 9"

<br/>

## 4.2. Algorithm
The problem can be solved in several ways:
* I) Using level order traversal
* II) Using DFS

<br/>

## 4.3. Code
### I) Level Order Traversal
> The idea is to store tree nodes in a queue for the level order traversal. Start with the horizontal distance hd as 0 of the root node, Using a Map which stores key-value pairs sorted by key and keep on adding a left child to the queue along with the horizontal distance as hd-1 and the right child as hd+1.

> Every time a new horizontal distance or an existing horizontal distance is encountered put the node data for the horizontal distance as the key. For the first time it will add it to the map, next time it will replace the value. This will make sure that the bottom-most element for that horizontal distance is present on the map and if you see the tree from beneath that you will see that element. At last traverse the keys of map and print their respective values.

#### Python code:
```python
# Python3 program to print Bottom
# View of Binary Tree

# deque supports efficient pish and pop on both ends
from collections import deque

# Tree node class
class Node:
	
	def __init__(self, key):
		
		self.data = key
		self.hd = float('inf')
		self.left = None
		self.right = None

# Method that prints the bottom view.
def bottomView(root):

	if (root == None):
		return
	
	# Initialize a variable 'hd' with 0
	# for the root element.
	hd = 0
	
	# Store minimum and maximum horizontal distance
	# so that we do not have to sort keys at the end
	min_hd, max_hd = 0, 0
	
	hd_dict = dict()

	# Queue to store tree nodes in level
	# order traversal
	q = deque()

	# Assign initialized horizontal distance
	# value to root node and add it to the queue.
	root.hd = hd
	q.append(root) 

	# Loop until the queue is empty (standard
	# level order loop)
	while q:
		curr_node = q.popleft()
		
		# Extract the horizontal distance value
		# from the dequeued tree node.
		hd = curr_node.hd
		
		# Update the minimum and maximum hd
		min_hd = min(min_hd, hd)
		max_hd = max(max_hd, hd)

		# Put the dequeued tree node to dictionary
		# having key as horizontal distance. Every
		# time we find a node having same horizontal
		# distance we need to update the value in
		# the map.
		hd_dict[hd] = curr_node.data

		# If the dequeued node has a left child, add
		# it to the queue with a horizontal distance hd-1.
		if curr_node.left:
			curr_node.left.hd = hd - 1
			q.append(curr_node.left)

		# If the dequeued node has a right child, add
		# it to the queue with a horizontal distance
		# hd+1.
		if curr_node.right:
			curr_node.right.hd = hd + 1
			q.append(curr_node.right)

	# Traverse the map from least horizontal distance to
	# most horizontal distance.
	for i in range(min_hd, max_hd+1):
		print(hd_dict[i], end = ' ')
		
# Driver Code
if __name__=='__main__':
	
	root = Node(20)
	root.left = Node(8)
	root.right = Node(22)
	root.left.left = Node(5)
	root.left.right = Node(3)
	root.right.left = Node(4)
	root.right.right = Node(25)
	root.left.right.left = Node(10)
	root.left.right.right = Node(14)
	
	print("Bottom view of the given binary tree :") # 5 10 4 14 25 
	
	bottomView(root)

# source: https://www.geeksforgeeks.org/bottom-view-binary-tree/

```
<br/>

### II) DFS
> Create a map where the key is the horizontal distance and the value is a pair(a, b) where a is the value of the node and b is the height of the node. Perform a pre-order traversal of the tree. If the current node at a horizontal distance of h is the first we’ve seen, insert it into the map. Otherwise, compare the node with the existing one in map and if the height of the new node is greater, update the Map.

#### Python code:
```python
# Python3 program to print Bottom
# View of Binary Tree 
class Node:
	
	def __init__(self, key = None, 
					left = None, 
					right = None):
						
		self.data = key
		self.left = left
		self.right = right
		
def printBottomView(root):
	
	# Create a dictionary where
	# key -> relative horizontal distance
	# of the node from root node and
	# value -> pair containing node's 
	# value and its level
	d = dict()
	
	printBottomViewUtil(root, d, 0, 0)
	
	# Traverse the dictionary in sorted 
	# order of their keys and print
	# the bottom view
	for i in sorted(d.keys()):
		print(d[i][0], end = " ")

def printBottomViewUtil(root, d, hd, level):
	
	# Base case
	if root is None:
		return
	
	# If current level is more than or equal 
	# to maximum level seen so far for the 
	# same horizontal distance or horizontal
	# distance is seen for the first time, 
	# update the dictionary
	if hd in d:
		if level >= d[hd][1]:
			d[hd] = [root.data, level]
	else:
		d[hd] = [root.data, level]
		
	# recur for left subtree by decreasing
	# horizontal distance and increasing
	# level by 1
	printBottomViewUtil(root.left, d, hd - 1, level + 1)
	
	# recur for right subtree by increasing
	# horizontal distance and increasing 
	# level by 1
	printBottomViewUtil(root.right, d, hd + 1, level + 1)

# Driver Code 
if __name__ == '__main__':
	
	root = Node(20)
	root.left = Node(8)
	root.right = Node(22) 
	root.left.left = Node(5) 
	root.left.right = Node(3) 
	root.right.left = Node(4) 
	root.right.right = Node(25) 
	root.left.right.left = Node(10) 
	root.left.right.right = Node(14) 
	
	print("Bottom view of the given binary tree :") # 5 10 4 14 25 
	
	printBottomView(root)


# source: https://www.geeksforgeeks.org/bottom-view-binary-tree/

```
<br/>
