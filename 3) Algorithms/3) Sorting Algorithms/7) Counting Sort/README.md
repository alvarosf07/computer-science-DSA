# Counting Sort Algorithm

Counting sort is an integer sorting algorithm that operates by counting the number of occurrences of each unique element in the input list and using this information to determine the position of each element in the sorted output list.

Counting sort is efficient if the range of input data is not significantly greater than the number of items to be sorted. It is often used as a subroutine in more complex sorting algorithms like radix sort.

<br/>

## Steps of Counting Sort Algorithm

* Step 1:
  - Find the maximum value in the input list to determine the size of the counting array.

* Step 2:
  - Initialize a counting array with a size equal to the maximum value + 1.

* Step 3:
  - Count the occurrences of each unique element in the input list and store them in the counting array.

* Step 4:
  - Calculate the cumulative sum of the counts in the counting array.

* Step 5:
  - Use the counting array to determine the position of each element in the sorted output list.

<br/>

## Visual Explanation

Counting sort counts the occurrences of each unique element in the input list and uses this information to determine the position of each element in the sorted output list.

![Counting Sort Visualization](https://example.com/counting_sort.gif)

<br/>

## Time Complexity

The time complexity of Counting sort is `O(n + k)`, where n is the number of elements in the input list and k is the range of input values. Counting sort is a non-comparison-based sorting algorithm, so it can achieve linear time complexity under certain conditions. The space complexity of Counting sort is O(n + k).

<br/>

## Code Implementation

Here's a simple implementation of Counting sort in Python:

```python
def counting_sort(arr):
    max_val = max(arr)
    counts = [0] * (max_val + 1)

    for num in arr:
        counts[num] += 1

    sorted_arr = []
    for i in range(len(counts)):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
```
