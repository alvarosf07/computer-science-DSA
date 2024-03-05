# Heap Sort Algorithm

Heap sort is a comparison-based sorting algorithm that builds a heap from the input list and then repeatedly extracts the maximum (for a max-heap) or minimum (for a min-heap) element from the heap and places it at the end of the sorted list.

<br/>

## Steps of Heap Sort Algorithm

* Step 1:
  - Build a max-heap from the input list.

* Step 2:
  - Repeatedly extract the maximum element from the heap and place it at the end of the sorted list.

* Step 3:
  - Reduce the size of the heap by one and heapify the remaining elements.

<br/>

## Visual Explanation

Heap sort builds a max-heap from the input list and then repeatedly extracts the maximum element from the heap, placing it at the end of the sorted list.

![Heap Sort Visualization](https://upload.wikimedia.org/wikipedia/commons/4/4d/Heapsort-example.gif)

<br/>

## Time Complexity

The time complexity of Heap sort is `O(n log n)`, where n is the number of elements in the list. This is because building the heap takes O(n) time, and each of the n extraction operations takes O(log n) time. Heap sort is an in-place sorting algorithm, meaning it does not require extra space proportional to the input size.

<br/>

## Code Implementation

Python:

```python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Example usage
arr = [64, 25, 12, 22, 11]
heap_sort(arr)
print("Sorted array:", arr)
