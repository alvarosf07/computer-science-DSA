
# [Problem #04 - Find Kth Max Number in Array](https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/)

## Solution 1 - Sort list and select kth position
  * Time complexity: `O(N * log(N))`
  * Auxiliary Space: `O(1)`
```python
def kLargest(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]
 
 
# Driver code
arr = [1, 23, 12, 9, 30, 2, 50]
k = 3
kLargest(arr, k) #Output: 23
```
<br/>

## Solution 2 - Quicksort Partitioning Algorithm
> This is an optimization over method 1, if QuickSort is used as a sorting algorithm in first step. In QuickSort, pick a pivot element, then move the pivot element to its correct position and partition the surrounding array. The idea is, not to do complete quicksort, but stop at the point where pivot itself is k’th largest element. Also, not to recur for both left and right sides of pivot, but recur for one of them according to the position of pivot.

These are the steps to implement the Quicksort partitioning algorithm:
1. Choose a pivot element from the array.
2. Partition the array into two subarrays: one with elements less than the pivot and another with elements greater than the pivot.
3. Recur on the subarray that contains the kth largest element.
4. Repeat the process until the pivot element is the kth largest element.

#### Complexity:
  * Time complexity: `O(N^2)` in worst case (`O(N)` on average)
  * Auxiliary Space: `O(n)`

```python
def partition(arr, l, r):
	x = arr[r] # Choose the last element as the pivot
	i = l

	# Iterate through the array and move elements smaller than the pivot to the left
	for j in range(l, r):
		if arr[j] <= x:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1

	# Swap the pivot element with the element at index 'i'
	arr[i], arr[r] = arr[r], arr[i]
	return i

def kthLargest(arr, l, r, k, N):
	# Partition the array around the pivot
	pos = partition(arr, l, r)

	# If the position is the same as 'k', we have found the kth largest element
	if pos - l == k - 1:
		return

	# If the position is less than 'k', recurse for the right subarray
	elif pos - l < k - 1:
		kthLargest(arr, pos + 1, r, k - pos + l - 1, N)

	# Otherwise, recurse for the left subarray
	else:
		kthLargest(arr, l, pos - 1, k, N)

if __name__ == "__main__":
	arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
	N = len(arr)
	k = 3

	# Find the kth largest elements
	kthLargest(arr, 0, N - 1, k, N)

	# Print K Largest numbers
	print(f"{k} largest elements are:", end=" ")
	for i in range(N - 1, N - k - 1, -1):
		print(arr[i], end=" ")

	print()

```
Note: It would be possible to improve the standard quicksort algorithm by using the random() function. Instead of using the pivot element as the last element, we can randomly choose the pivot element randomly.

<br/>


## Solution 3 - Using Priority Queue (Min-Heap)
> The intuition behind this approach is to maintain a minheap (priority queue) of size K while iterating through the array. Doing this ensures that the min heap always contains the K largest elements encountered so far. If the size of the min heap exceeds K, remove the smallest element this step ensures that the heap maintains the K largest elements encountered so far. In the end, the min heap contains the K largest elements of the array.

These are the steps to implement the Quicksort partitioning algorithm:
1. Initialize a min heap (priority queue) pq.
2. For each element in the array:
    * Push the element onto the max heap.
    * If the size of the max heap exceeds K, pop (remove) the smallest element from the min heap. This step ensures that the min heap maintains the K largest elements encountered so far.
3. After processing all elements, the min heap will contain the K largest elements of the array.

#### Complexity:
  * Time complexity: `O(N * log(K))`
  * Auxiliary Space: `O(k)`

```python
# Python code for k largest elements in an array
import heapq

# Function to find k largest array element

def kLargest(v, N, K):

	# Implementation using
	# a Priority Queue
	pq = []
	heapq.heapify(pq)

	for i in range(N):

		# Insert elements into
		# the priority queue
		heapq.heappush(pq, v[i])

		# If size of the priority
		# queue exceeds k
		if (len(pq) > K):
			heapq.heappop(pq)

	# Print the k largest element
	while(len(pq) != 0):
		print(heapq.heappop(pq), end=' ')
	print()


# driver program

# Given array
arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
# Size of array
n = len(arr)
k = 3
print(k, " largest elements are : ", end='')
kLargest(arr, n, k)

```
