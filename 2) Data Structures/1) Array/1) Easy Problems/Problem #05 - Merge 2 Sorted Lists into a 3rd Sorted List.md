# [Problem #05 - Merge 2 Sorted Lists into a 3rd Sorted List](https://www.geeksforgeeks.org/merge-two-sorted-arrays/)

## Solution #1 - Naive Approach: take each element of each array and sort the list
* Time Complexity : `O((m+n) log(m+n))` , the whole size of arr3 is m+n
* Auxiliary Space: `O(m+n)`, where m is the size of arr1 and n is the size of arr2.
```python
# Python program to merge two sorted arrays/
def mergeArrays(arr1, arr2, n1, n2, arr3):
	i = 0
	j = 0
	k = 0

	# traverse the arr1 and insert its element in arr3
	while(i < n1):
		arr3[k] = arr1[i]
		k += 1
		i += 1

	# now traverse arr2 and insert in arr3
	while(j < n2):
		arr3[k] = arr2[j]
		k += 1
		j += 1

	# sort the whole array arr3
	arr3.sort()


# Driver code
if __name__ == '__main__':
	arr1 = [1, 3, 5, 7]
	n1 = len(arr1)

	arr2 = [2, 4, 6, 8]
	n2 = len(arr2)

	arr3 = [0 for i in range(n1+n2)]
	mergeArrays(arr1, arr2, n1, n2, arr3)

	print("Array after merging")
	for i in range(n1 + n2):
		print(arr3[i], end=" ")

```

## Solution #2 - Use Merge function of MergeSort Algorithm
The idea is to always compare the first element of each sorted array, and add the bigger element to the final sorted array. Then eliminate the bigger element from the array it belonged to, and repeat the process until the end of both arrays.

Note that in this approach, eliminating the first element of each array (e.g. with method `pop()`is not very efficient (need to move all the other positions in the array). There's two possible solutions for this:
* Use Reversed Sorted Arrays, comparing the last elements of the array instead of the first ones
* Use two pointers to compare the highest element of each array, instead of popping elements from the arrays

#### Complexity:
* Time Complexity : `O(n1 + n2)`
* Auxiliary Space : `O(n1 + n2)`

```python

def mergeArrays(arr1, arr2, n1, n2):
	arr3 = [None] * (n1 + n2)
	i = 0
	j = 0
	k = 0

	# Traverse both array
	while i < n1 and j < n2:
		if arr1[i] < arr2[j]:
			arr3[k] = arr1[i]
			k = k + 1
			i = i + 1
		else:
			arr3[k] = arr2[j]
			k = k + 1
			j = j + 1
	

	# Store remaining elements of first array
	while i < n1:
		arr3[k] = arr1[i];
		k = k + 1
		i = i + 1

	# Store remaining elements of second array
	while j < n2:
		arr3[k] = arr2[j];
		k = k + 1
		j = j + 1
	print("Array after merging")
	for i in range(n1 + n2):
		print(str(arr3[i]), end = " ")

# Driver code
arr1 = [1, 3, 5, 7]
n1 = len(arr1)

arr2 = [2, 4, 6, 8]
n2 = len(arr2)
mergeArrays(arr1, arr2, n1, n2);

```



