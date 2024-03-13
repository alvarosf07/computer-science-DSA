# [LeetCode 33 - Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Description
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer target, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

 

#### Example 1:
```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

#### Example 2:
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

#### Example 3:
```
Input: nums = [1], target = 0
Output: -1
```

#### Constraints:

* `1 <= nums.length <= 5000`
* `-10^4 <= nums[i] <= 10^4`
* All values of `nums` are unique.
* `nums` is an ascending array that is possibly rotated.
* `-10^4 <= target <= 10^4`

<br/>

## Solutions
### Solution 1
#### Python:
* Time: `O(log(N))`
* Space: `O(1)`

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0; r = len(nums)-1
        
        while l <= r:
            mid = (l+r) // 2
            
            if nums[mid] == target: return mid
            
            elif nums[l] <= nums[mid]:  # Left subarray of mid is sorted
                if nums[l] <= target < nums[mid]: # target present at Left subarray of mid 
                    r = mid-1
                else: # target at right subarray of mid
                    l = mid+1
            else:  # right subarray of mid is sorted
                if nums[mid] < target <= nums[r]:  # target is present at right subarray of mid
                    l = mid+1
                else:  # target at left subarray of mid
                    r = mid - 1
        
        return -1
```
    
