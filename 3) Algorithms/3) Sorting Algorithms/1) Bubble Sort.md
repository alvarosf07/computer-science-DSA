# Bubble Sort Algorithm

Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

<br/>

## Steps of Bubble Sort Algorithm

1. **Step 1:**
   - Start with the first element in the list.

2. **Step 2:**
   - Compare the current element with the next element.

3. **Step 3:**
   - If the current element is greater than the next element, swap them.

4. **Step 4:**
   - Move to the next pair of elements and repeat steps 2 and 3.

5. **Step 5:**
   - Continue this process until the entire list is sorted.

<br/>

## Visual Explanation

Bubble sort compares adjacent elements and swaps them if necessary, gradually sorting the list.

![Bubble Sort Visualization](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)



<br/>

## Code Implementation

Python:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)
