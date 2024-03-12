# [Problem #03 - Maximum Subarray of Length K](https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/)

## Description
Given an array of integers and a number k, find the maximum sum of a subarray of size k.

### Example 1
```cpp
Input  : arr[] = {100, 200, 300, 400},  k = 2
Output : 700
```

### Example 2
```cpp
Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4 
Output : 39
Explanation: We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.
```

### Example 3
```cpp
Input  : arr[] = {2, 3}, k = 3
Output : Invalid
Explanation: There is no subarray of size 3 as size of whole array is 2. 
```

<br/>

## Solutions

### Solution #1 - Naive Solution
A Simple Solution is to generate all subarrays of size k, compute their sums and finally return the maximum of all sums. The time complexity of this solution is `O(n*k)`.
#### Python:
```python
def max_sum_of_subarray(arr, n, k):
    max_sum = 0;
    for i in range(0, n-k+1):
        temp = 0;
        for j in range(i, i+k):
            temp += arr[j];
 
        if (temp > max_sum):
            max_sum = temp;
 
    return max_sum;
 
 
arr = [ 1, 4, 2, 10, 2, 3, 1, 0, 20 ];
k = 4;
n = len(arr);
max_sum=0;
 
 # brute force
max_sum = max_sum_of_subarray(arr, n, k);
print(max_sum);
```

<br/>

### Solution #2 - Efficient Solution
An Efficient Solution is based on the fact that sum of a subarray (or window) of size k can be obtained in O(1) time using the sum of the previous subarray (or window) of size k. Except for the first subarray of size k, for other subarrays, we compute the sum by removing the first element of the last window and adding the last element of the current window.
* Time Complexity: O(n)
* Auxiliary Space: O(1) 
#### Python:
```python
def maxSum(arr, n, k):
 
    # k must be smaller than n
    if (n < k):
     
        print("Invalid")
        return -1
     
    # Compute sum of first
    # window of size k
    res = 0
    for i in range(k):
        res += arr[i]
 
    # Compute sums of remaining windows by removing first element of previous window
    # and adding last element of current window.
    curr_sum = res
    for i in range(k, n):
     
        curr_sum += arr[i] - arr[i-k]
        res = max(res, curr_sum)
 
    return res
 
# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))
```

