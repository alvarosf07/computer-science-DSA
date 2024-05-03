# [LeetCode 215 - Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array)

## Description

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k<sup>th</sup></code> <em>largest element in the array</em>.</p>

<p>Note that it is the <code>k<sup>th</sup></code> largest element in the sorted order, not the <code>k<sup>th</sup></code> distinct element.</p>

<p>Can you solve it without sorting?</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,1,5,6,4], k = 2
<strong>Output:</strong> 5
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3,1,2,4,5,5,6], k = 4
<strong>Output:</strong> 4
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<br/>

## [Solution 1 - Sorting](https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/3906260/100-3-approaches-video-heap-quickselect-sorting/)
The most intuitive method, this approach involves sorting the entire array in descending order and then simply picking the kkk-th element. Though straightforward, it may not be the most efficient for very large arrays due to the sorting step.
The time complexity is $O(n \times \log n)$, where $n$ is the length of the array $nums$.

#### Python:
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]
```


<br/>

## [Solution 2 - Min-Heap](https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/3906260/100-3-approaches-video-heap-quickselect-sorting/)
Rather than sorting the entire array, this method utilizes a min-heap to maintain the kkk-th largest elements. The heap allows us to efficiently compare each new element with the smallest of the kkk-th largest elements seen so far. By the end of the iteration, the top of the heap will contain our desired kkk-th largest element.

#### Python:
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]
```

<br/>

## [Solution 3 - QuickSelect Algorithm](https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/3906260/100-3-approaches-video-heap-quickselect-sorting/)
Inspired by the QuickSort algorithm, QuickSelect is a divide-and-conquer technique. It partitions the array around a pivot and recursively searches for the kkk-th largest element in the appropriate partition. When the pivot is chosen randomly, the algorithm tends to have a linear average-case time complexity, making it faster than the sorting approach for large datasets.

#### Python:
```python
class Solution:
    def findKthLargest(self, nums, k):
        left, right = 0, len(nums) - 1
        while True:
            pivot_index = random.randint(left, right)
            new_pivot_index = self.partition(nums, left, right, pivot_index)
            if new_pivot_index == len(nums) - k:
                return nums[new_pivot_index]
            elif new_pivot_index > len(nums) - k:
                right = new_pivot_index - 1
            else:
                left = new_pivot_index + 1

    def partition(self, nums, left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        stored_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[stored_index] = nums[stored_index], nums[i]
                stored_index += 1
        nums[right], nums[stored_index] = nums[stored_index], nums[right]
        return stored_index
```


