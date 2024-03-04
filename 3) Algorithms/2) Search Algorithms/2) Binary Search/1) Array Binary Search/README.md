# 1. Binary Search (Array)

> Binary search is an efficient search algorithm that works by repeatedly dividing the search interval in half. It compares the target value with the middle element of the array and decides whether to continue searching in the left or right half of the array. This process is repeated until the target value is found or the search interval is empty.

<br/>


## 1.1. How Does Binary Search Work?

Binary search works on the principle of divide and conquer. It starts by examining the middle element of the array. If the target value is equal to the middle element, the search is complete. If the target value is less than the middle element, the search continues in the left half of the array. If the target value is greater than the middle element, the search continues in the right half of the array. This process is repeated until the target value is found or the search interval is empty.

<br/>


## 1.2. Key Features of Binary Search:

1. **Efficiency:** Binary search has a time complexity of O(log n), making it highly efficient for searching in large sorted arrays.

2. **Versatility:** Binary search can be applied to any sorted list or array, regardless of its size or the type of elements.

3. **Ease of Implementation:** While binary search is more complex than linear search, it is still relatively simple to implement and understand.

<br/>


## 1.3. Example of Binary Search:

Consider the problem of searching for a specific value (e.g., 42) in a sorted list of integers:

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
arr = [10, 20, 30, 40, 50]
target = 40
print("Index of target value:", binary_search(arr, target))
```
<br/>


## 1.4. When to Use Binary Search:
Binary search is most commonly used in scenarios where:

* The list is sorted in ascending order.
* The size of the list is relatively large.
* Efficient searching is required, and the overhead of sorting the list beforehand is acceptable.

<br/>

<br/>



# 2. Shifted Binary Search

> Shifted Binary Search is a variation of the traditional binary search algorithm that is used to search for a target element in a sorted array that has been rotated or shifted. This means the array is not strictly sorted in ascending or descending order, but it is still possible to apply binary search with slight modifications.

<br/>

## 2.1. How Does Shifted Binary Search Work?

Shifted Binary Search works similarly to the traditional binary search algorithm but with additional checks to handle the rotation or shift in the array. It divides the array into two halves and compares the target element with the middle element to determine which half to continue the search in. This process continues recursively until the target element is found or the search space is exhausted.

<br/>

## 2.2. Step-by-Step Guide of Shifted Binary Search:

1. **Identify Pivot Point:** Determine the index of the pivot point where the rotation or shift in the array occurs. This can be done using binary search or linear search in logarithmic or linear time, respectively.

2. **Determine Search Space:** Decide which half of the array to search in based on the target element and the elements at the boundaries of the array.

3. **Apply Binary Search:** Perform binary search within the selected search space, adjusting the indices and comparisons as necessary to account for the rotation or shift.

4. **Repeat or Terminate:** Continue the binary search recursively until the target element is found or the search space is exhausted. If the target element is not found, return a designated value or indicate that the element does not exist in the array.

<br/>

## 2.3. Algorithms to Solve Shifted Binary Search:

1. **Finding Pivot Point:**
   - Linear Search: Iterate through the array to find the index where the element is smaller than the previous element.
   - Binary Search: Use binary search to find the index where the element is smaller than the previous element and greater than the next element.

2. **Binary Search with Rotation:**
   - Once the pivot point is identified, apply binary search separately to the two halves of the array.

<br/>

## 2.4. Key Features of Shifted Binary Search:

1. **Efficiency:** Shifted Binary Search maintains the `O(n)` efficiency of traditional binary search algorithms, with slight modifications to handle rotation or shift in the array.

2. **Versatility:** Shifted Binary Search can be applied to sorted arrays that have been rotated or shifted, making it useful in scenarios where the array may not be strictly sorted.

<br/>

## 2.5. When to Use Shifted Binary Search:

Shifted Binary Search is most commonly used in scenarios where:

- The array is sorted but may have been rotated or shifted.
- Efficient searching of the target element is required, and traditional binary search may not be applicable.

<br/>

## 2.6. Example of Shifted Binary Search:


Consider the problem of finding the index of the target element in the following shifted array:
Applying Shifted Binary Search, we would first identify the pivot point (index 5) where the rotation occurs. Then, we would apply binary search separately to the two halves of the array to find the target element.

Original Array: [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]

```python
def find_pivot(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > arr[mid + 1]:
            return mid + 1
        elif arr[mid] < arr[left]:
            right = mid
        else:
            left = mid + 1
    
    return 0

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def shifted_binary_search(arr, target):
    pivot = find_pivot(arr)
    
    if pivot == 0:
        return binary_search(arr, target)
    
    if arr[0] <= target <= arr[pivot - 1]:
        return binary_search(arr[:pivot], target)
    else:
        result = binary_search(arr[pivot:], target)
        return result + pivot if result != -1 else -1

# Example usage:
arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
target = 3
index = shifted_binary_search(arr, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")

```

The overall time complexity of the Shifted Binary Search algorithm is dominated by the time complexity of finding the pivot point, as it is the most time-consuming step.
Therefore, the overall time complexity is O(log n), where n is the number of elements in the array.




