# [LeetCode 0001 - Two Sum](https://leetcode.com/problems/two-sum)


## Description
<p> Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. </p>

<p>Given an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]

</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]


</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
  	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>

<br/>

## Solutions

### Solution 1: Hash Table (beats 100% in running time)

The key to solve this problem is realizing that for every number in the array, we don't need to check every other number looking for the one that adds up to the target. Instead, we simply iterate through each number `x` in the array and check if we have already seen a number which equals `target`-`x`. If so, we return the indexes of both; if not, we save the current number in a hash map (adding its index as value) and continue iterating.

<!-- tabs:start -->

#### Python:
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}

        for i in range(0,len(nums)):
            if (target-nums[i]) in ht: 
                return (ht[target-nums[i]],i)
            else:
                ht[nums[i]]=i
        
```
