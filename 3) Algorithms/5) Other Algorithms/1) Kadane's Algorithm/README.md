# Kadane's Algorithm

> Kadane's algorithm, is a dynamic programming algorithm used to find the maximum sum subarray within a given array of integers. It efficiently solves the maximum subarray problem, which is to find the contiguous subarray within an array that has the largest sum.

<br/>

## How Does the Kadane's Algorithm Work?

The Kardane algorithm works by iterating through the array and maintaining two variables: `max_ending_here` and `max_so_far`. At each iteration, it updates these variables to keep track of the `maximum sum` subarray ending at the current index and the `maximum sum` subarray found so far. By updating these variables dynamically, the algorithm efficiently finds the maximum sum subarray.

<br/>

## Key Features of Kadane's Algorithm:

1. **Efficiency:** The Kardane algorithm has a time complexity of O(n), where n is the size of the input array. This makes it highly efficient for finding the maximum sum subarray in large arrays.

2. **Simplicity:** The algorithm is relatively simple and easy to implement, making it accessible for programmers of all levels.

3. **Applications:** The Kardane algorithm has applications in various fields, including data analysis, image processing, and financial analysis, where finding the maximum sum subarray is a common problem.

<br/>

## When to Use Kadane's Algorithm:

The Kardane algorithm is most commonly used in scenarios where:

- The goal is to find the contiguous subarray within an array that has the largest sum.
- The input array contains integer values, and the problem can be represented as finding the maximum sum subarray.

<br/>

## Example of the Kadane's Algorithm:

Consider the problem of finding the maximum sum subarray within the array [−2, 1, −3, 4, −1, 2, 1, −5, 4]. One approach is to use Kadane's algorithm:

```python
def kardane_algorithm(nums):
    max_ending_here = max_so_far = nums[0]
    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum_subarray = kardane_algorithm(nums)
print("Maximum sum subarray:", max_sum_subarray)
```
