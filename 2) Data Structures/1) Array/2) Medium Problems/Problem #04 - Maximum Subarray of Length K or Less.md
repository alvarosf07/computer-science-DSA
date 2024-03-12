# Problem #04 - Maximum Subarray of Length K or Less

# Description
Given an array arr of integers (positive and negative), and an integer number k, return the maximum sum that can be obtained in any contiguous subarray with at most k elements.

Inputs:
  - array
  - k

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
Output : 5
Explanation: We get the maximum sum by adding only two elements (2 and 3).
```

<br/>

## Solutions

### Solution #1 - Naive Solution
A Simple Solution is to generate all subarrays of size k and less, compute their sums and finally return the maximum of all sums. The time complexity of this solution is `O(n*k*t)`.
#### Python:
```python
def getMaxProfit(pnl, k):
    max_pnl = pnl[0]
    curr_pnl = pnl[0]

    for length in range (1,k+1):
        for i in range(1,len(pnl)):
            if i<length:
                curr_pnl += pnl[i]
            if i>= length:
                curr_pnl = curr_pnl - pnl[i-length]+pnl[i]
            max_pnl = max(max_pnl, curr_pnl)
        curr_pnl = pnl[0]

    return max_pnl
```

<br/>

### Solution #2 - Efficient Solution
An Efficient Solution is derived from Kadane algorithm. The key for this problem is realizing that you can apply Kadane's algorithm if the length of the sliding window is less than k, and if not you can move the sliding window or reset it to 0 depending on whether the new sliding window [left+1,right] satisfies Kadane condition or not.

* Time Complexity: O(n)
* Auxiliary Space: O(k+n)
  
#### Python:
```python
def get_max_subarray_with_length_k_or_less(arr, k):
    max_sum = arr[0]
    cum_sum = 0
    left = 0

    for r in range(len(arr)):
        if r-left < k:
            if cum_sum+arr[r] >= 0:
                cum_sum += arr[r]
                max_sum = max(max_sum, cum_sum)

            else:
                if max_sum < 0:
                    max_sum = max(max_sum, arr[r])
                else:
                    max_sum = max(max_sum, cum_sum)
                cum_sum = 0
                left += 1

        else:
            if cum_sum-arr[left]+arr[r] >= 0:
                cum_sum = cum_sum-arr[left]+arr[r]
                max_sum = max(max_sum, cum_sum)
                left += 1

            else:
                max_sum = max(max_sum, cum_sum)
                cum_sum = 0
                left = r+1
        #print(r, max_sum, cum_sum, left)
    return max_sum
```


