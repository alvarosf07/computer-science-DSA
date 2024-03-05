# Radix Sort Algorithm

Radix sort is a non-comparison-based sorting algorithm that sorts elements by first grouping the individual digits of the same place value and sorting them according to their increasing/decreasing order.

Radix sort works by sorting elements based on their digits from the least significant digit (LSD) to the most significant digit (MSD) or vice versa. It is often used to sort numbers represented in decimal, binary, or hexadecimal notation.

<br/>

## Steps of Radix Sort Algorithm

* Step 1:
  - Identify the maximum number of digits among all elements in the input list.

* Step 2:
  - Starting from the least significant digit (LSD) to the most significant digit (MSD) or vice versa, perform a stable sort on each digit using a counting sort or another stable sorting algorithm.

* Step 3:
  - Repeat Step 2 for each digit position until all digits have been processed.

<br/>

## Visual Explanation

Radix sort sorts numbers by processing each digit position from the least significant digit (LSD) to the most significant digit (MSD) using counting sort as the stable sorting algorithm.

![Radix Sort Visualization](https://upload.wikimedia.org/wikipedia/commons/b/b9/Radix_sort_example.gif)

<br/>

## Time Complexity

The time complexity of Radix sort is `O(d * (n + b))`, where n is the number of elements in the input list, d is the maximum number of digits in any element, and b is the base of the number system (e.g., 10 for decimal, 2 for binary). Radix sort is a linear-time sorting algorithm when d is a constant. The space complexity of Radix sort is O(n + b).

<br/>

## Code Implementation

Here's a simple implementation of Radix sort in Python:

```python
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sorted array:", arr)
```
