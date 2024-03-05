# Merge Sort Algorithm

Merge sort is a divide-and-conquer algorithm that divides the input list into two halves, sorts each half separately, and then merges the sorted halves to produce the final sorted list.

<br/>

## Steps of Merge Sort Algorithm

* Step 1:
  - Divide the input list into two halves.

* Step 2:
  - Recursively sort each half.

* Step 3:
  - Merge the sorted halves to produce the final sorted list.

<br/>

## Visual Explanation

Merge sort recursively divides the input list into smaller halves, sorts them individually, and then merges them back together to form the final sorted list:

![Merge Sort Visualization](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

<br/>

## Time Complexity

The time complexity of Merge sort is `O(n log n)`, where n is the number of elements in the list. This is because the algorithm recursively divides the input list into halves until reaching single-element lists, and then merges them together in sorted order.

<br/>

## Code Implementation

Here's a simple implementation of Merge sort with recursion in Python:

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Example usage
arr = [64, 25, 12, 22, 11]
merge_sort(arr)
print("Sorted array:", arr)
