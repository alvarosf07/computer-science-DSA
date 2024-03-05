# Insertion Sort Algorithm

Insertion sort is a simple sorting algorithm that builds the final sorted list one element at a time. It repeatedly takes the next element from the unsorted portion of the list and inserts it into its correct position in the sorted portion.

<br/>

## Steps of Insertion Sort Algorithm

* Step 1:
  - Start with the second element of the list.

* Step 2:
  - Compare the current element with the elements before it, moving them one position to the right until finding the correct position for insertion.

* Step 3:
  - Insert the current element into its correct position.

* Step 4:
  - Repeat steps 2 and 3 until the entire list is sorted.

<br/>

## Visual Explanation

Insertion sort inserts elements into their correct positions in the sorted portion of the list:

![Insertion Sort Visualization](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

<br/>

## Time Complexity

The time complexity of Insertion sort is `O(n^2)`, where n is the number of elements in the list. This is because, in the worst-case scenario, each element must be compared and shifted to its correct position.

<br/>

## Code Implementation

Here's a simple implementation of Insertion sort in Python:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
arr = [64, 25, 12, 22, 11]
insertion_sort(arr)
print("Sorted array:", arr)
```
