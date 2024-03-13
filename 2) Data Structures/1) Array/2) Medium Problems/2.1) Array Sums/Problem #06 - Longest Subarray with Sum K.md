# [Problem #06 - Longest Subarray with Sum K](https://www.geeksforgeeks.org/longest-sub-array-sum-k/)

# Description
Given an array of integers and a number k, find the maximum sum of a subarray of size k.

## Example 1
```cpp
Input: arr[] = { 10, 5, 2, 7, 1, 9 }, k = 15
Output : 4
Explanation: The sub-array is {5, 2, 7, 1}.
```

## Example 2
```cpp
Input: arr[] = {-5, 8, -14, 2, 4, 12}, k = -5
Output : 5
```

<br/>

## Solutions

### Solution #1 - Naive Solution
Consider the sum of all the sub-arrays and return the length of the longest sub-array having the sum ‘k’. Time Complexity is of `O(n^2)`.
#### Python:
```python
def lenOfLongSubarr(arr, N, K):
   
    # Variable to store the answer
    maxlength = 0
 
    for i in range(0,N):
 
        # Variable to store sum of subarrays
        Sum = 0
 
        for j in range(i,N):
 
            # Storing sum of subarrays
            Sum += arr[j]
 
            # if Sum equals K
            if (Sum == K):
 
                # Update maxLength
                maxlength = max(maxlength, j - i + 1)
 
    # Return the maximum length
    return maxlength
 
# Driver Code
# Given input
arr = [ 10, 5, 2, 7, 1, 9 ]
n = len(arr)
k = 15
 
# Function Call
print("Length = " , lenOfLongSubarr(arr, n, k))
```

<br/>

### Solution #2 - Efficient Solution
Using hash table to keep track of the sliding window sum:
* Initialize sum = 0 and maxLen = 0.
* Create a hash table having (sum, index) tuples.
* For i = 0 to n-1, perform the following steps:
  * Accumulate arr[i] to sum.
  * If sum == k, update maxLen = i+1.
  * Check whether sum is present in the hash table or not. If not present, then add it to the hash table as (sum, i) pair.
  * Check if (sum-k) is present in the hash table or not. If present, then obtain index of (sum-k) from the hash table as index. Now check if maxLen < (i-index), then update maxLen = (i-index).
* Return maxLen.

#### Complexity:
* Time Complexity: O(n)
* Auxiliary Space: O(n) 
#### Python:
```python
def lenOfLongSubarr(arr, n, k):
 
    # dictionary mydict implemented
    # as hash map
    mydict = dict()
 
    # Initialize sum and maxLen with 0
    sum = 0
    maxLen = 0
 
    # traverse the given array
    for i in range(n):
 
        # accumulate the sum
        sum += arr[i]
 
        # when subArray starts from index '0'
        if (sum == k):
            maxLen = i + 1
 
        # check if 'sum-k' is present in
        # mydict or not
        elif (sum - k) in mydict:
            maxLen = max(maxLen, i - mydict[sum - k])
 
        # if sum is not present in dictionary
        # push it in the dictionary with its index
        if sum not in mydict:
            mydict[sum] = i
 
    return maxLen
 
# Driver Code
if __name__ == '__main__':
    arr = [10, 5, 2, 7, 1, 9]
    n = len(arr)
    k = 15
    print("Length =", lenOfLongSubarr(arr, n, k))
```


