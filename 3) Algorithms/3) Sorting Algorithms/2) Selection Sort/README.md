# Selection Sort Algorithm

Selection sort is a simple sorting algorithm that repeatedly selects the smallest (or largest) element from the unsorted portion of the list and moves it to its correct position in the sorted portion. This process is repeated until the entire list is sorted.

<br/>

## Steps of Selection Sort Algorithm

* **Step 1** - Find the minimum element in the unsorted portion of the list.

* **Step 2** - Swap the minimum element with the first element in the unsorted portion.

* **Step 3** - Move the boundary of the unsorted portion to the right, excluding the first element which is now sorted.

* **Step 4** - Repeat steps 1 to 3 until the entire list is sorted.

<br/>

## Visual Explanation

Selection sort repeatedly selects the smallest element from the unsorted portion and moves it to its correct position in the sorted portion.

![Selection Sort Visualization](https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif)

<br/>

## Time Complexity

The time complexity of Selection sort is `O(n^2)` in all cases, where n is the number of elements in the list. This is because the algorithm involves nested loops, with each loop iterating over the entire list.

<br/>

## Code Implementation

Python:

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
```
