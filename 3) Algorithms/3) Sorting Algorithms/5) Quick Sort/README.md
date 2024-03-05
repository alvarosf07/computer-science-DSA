# Quick Sort Algorithm

Quick sort is a divide-and-conquer algorithm that selects a 'pivot' element from the list and partitions the other elements into two sublists according to whether they are less than or greater than the pivot. It then recursively sorts the sublists.

<br/>

## Steps of Quick Sort Algorithm

* Step 1:
  - Choose a pivot element from the list.

* Step 2:
  - Partition the list into two sublists: elements less than the pivot and elements greater than the pivot.

* Step 3:
  - Recursively apply Quick sort to the sublists.

<br/>

## Visual Explanation

Quick sort selects a pivot element, partitions the list, and recursively sorts the sublists until the entire list is sorted:

![Quick Sort Visualization](https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif)

<br/>

## Time Complexity

The time complexity of Quick sort is O(n log n) on average, but O(n^2) in the worst-case scenario (when the pivot is consistently the smallest or largest element). However, the worst-case scenario is rare in practice. Quick sort is an in-place sorting algorithm, meaning it does not require extra space proportional to the input size.

<br/>

## Code Implementation

Here's a simple implementation of Quick sort in Python:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
'''
