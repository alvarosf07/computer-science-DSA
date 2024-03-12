# [LeetCode 238 - Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)
## Description
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.


#### Example 1:
> Input: nums = [1,2,3,4]
> 
> Output: [24,12,8,6]

#### Example 2:
> Input: nums = [-1,1,0,-3,3]
> 
> Output: [0,0,9,0,0]
 

#### Constraints:

* `2 <= nums.length <= 105`

* `-30 <= nums[i] <= 30`

* The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#### Follow up: 
Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

<br/>

## Solutions
### Solution 1 - Brute Force Approach
Time Complexity: `O(n^2)`
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      output=[]
      prod = 1
  
      for i in range(len(nums)):
          for j in range(len(nums)): 
              if j != i: prod=prod*nums[j] 
          output[i] = prod
          prod = 1
  
      return output
```
<br/>

### Solution 2 - Improved Solution (with division)
Time Complexity: `O(2n)`
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      product = 1
      for e in nums:
          product = product*e
  
      return [product/e for e in nums]
```

<br/>

### Solution 3 - Better Solution: Left & Right Product Approach
* Time Complexity: `O(2n)`
* Space: `O(2n)`
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1]
        right = [1]

        for i in range(1,length):
            left.append(nums[i-1]*left[i-1])
        for i in range(length-2,-1,-1):
            right = [nums[i+1]*right[(i+1)-length]]+right

        return [a*b for a,b in zip(left,right)]
```
<br/>

### Follow up Solution - Optimal Solution: Left & Right Product Approach with O(1) space
* Time Complexity: `O(2n)`
* Space: `O(1)`
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1]*length

        for i in range(1,length):
            products[i] = products[i-1] * nums[i-1]

        for i in range(length-2,-1,-1):
            products[i] *= right
            right *= nums[i]

        return products
```



