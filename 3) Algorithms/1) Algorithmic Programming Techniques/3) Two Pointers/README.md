# Two Pointers

> The two pointers technique is a simple and intuitive algorithmic approach that involves using two pointers to traverse a data structure (usually an array or a linked list) simultaneously. 
> These pointers are typically initialized to different positions in the data structure and are then manipulated to solve the problem efficiently.

<br/>


## How Does the Two Pointers Technique Work?

The two pointers technique works by manipulating the positions of two pointers within the data structure to meet certain conditions or constraints specified by the problem. By moving the pointers strategically, we can efficiently traverse the data structure and solve the problem in linear or near-linear time complexity.

<br/>

<img src="/Resources/Images/two_pointers.png" width="360">

<br/>



## Key Features of the Two Pointers Technique:

1. **Simple and Intuitive:** The two pointers technique is easy to understand and implement, making it accessible to programmers of all skill levels.

2. **Efficient:** By traversing the data structure in a single pass using two pointers, the two pointers technique often achieves optimal or near-optimal time complexity for a wide range of problems.

3. **Applicable to Various Problems:** The two pointers technique can be applied to a variety of problems, including array manipulation, searching, sorting, and more.

<br/>



## Example of Two Pointers Technique:

Consider the problem of finding a pair of elements in a sorted array that sum up to a given target value. 
In the following example, the two_sum function uses the two pointers technique to find a pair of elements in the sorted array nums that sum up to the target value:

```python
def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

# Example usage:
nums = [1, 2, 3, 4, 5]
target = 9
print("Indices of elements summing up to", target, ":", two_sum(nums, target))
```



<br/>



## When to use the Two Pointers Technique:

The two pointers technique is a versatile and efficient algorithmic approach that enables programmers to solve a variety of problems with optimal or near-optimal time complexity. 
By manipulating two pointers within a data structure, we can traverse the structure efficiently and solve the problem in a single pass. 
Whether you're manipulating arrays, linked lists, or other data structures, the two pointers technique is a valuable tool to have in your algorithmic toolkit.
