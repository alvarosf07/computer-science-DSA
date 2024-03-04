# Dutch National Flag Algorithm

> The Dutch National Flag algorithm, also known as the three-way partitioning algorithm, is a sorting algorithm designed to sort an array of elements with three distinct values into three partitions. It was originally devised by Edsger W. Dijkstra and is named after the Dutch national flag because of its resemblance to the tricolor flag of the Netherlands.

<br/>

## How Does the Dutch National Flag Algorithm Work?

The Dutch National Flag algorithm works by partitioning the array into three sections: elements less than a given pivot value, elements equal to the pivot value, and elements greater than the pivot value. It achieves this by maintaining three pointers to track the boundaries of each section and swapping elements as necessary to move them into the correct partition.

<br/>

## Step-by-Step Implementation of the Dutch National Flag Algorithm:

1. Initialize three pointers: `low` pointing to the start of the array, `mid` pointing to the start of the unprocessed region, and `high` pointing to the end of the array.
2. Iterate through the array while `mid` is less than or equal to `high`.
3. If the element at `mid` is less than the pivot value, swap it with the element at `low` and increment both `low` and `mid`.
4. If the element at `mid` is equal to the pivot value, leave it in place and increment `mid`.
5. If the element at `mid` is greater than the pivot value, swap it with the element at `high` and decrement `high`.
6. Continue this process until `mid` is greater than `high`, indicating that all elements have been processed.

<br/>

## Key Features of the Dutch National Flag Algorithm:

1. **Efficiency:** The algorithm has a time complexity of O(n), where n is the number of elements in the array, making it efficient for sorting arrays with three distinct values.
   
2. **In-place:** The Dutch National Flag algorithm sorts the array in-place without requiring additional memory, making it memory-efficient.

3. **Adaptability:** The algorithm can be easily modified to handle arrays with more than three distinct values or to sort elements based on different criteria.

<br/>

## When to Use the Dutch National Flag Algorithm:

The Dutch National Flag algorithm is most commonly used in scenarios where:

- The goal is to sort an array containing three distinct values into three partitions.
- The array contains elements that can be compared for order (e.g., integers, characters, or custom objects).
- Efficiency and in-place sorting are desired.

<br/>

## Example of the Dutch National Flag Algorithm:

Consider the problem of sorting an array containing red, white, and blue elements:

```python
def dutch_flag_sort(arr):
    low, mid, high = 0, 0, len(arr) - 1
    pivot = 1  # Pivot value for sorting red, white, and blue elements
    while mid <= high:
        if arr[mid] < pivot:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == pivot:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

# Example usage:
colors = ['blue', 'white', 'red', 'red', 'blue', 'white', 'blue']
dutch_flag_sort(colors)
print("Sorted colors:", colors)
