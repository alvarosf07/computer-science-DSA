# [136. Single Number](https://leetcode.com/problems/single-number)


## Description

<p>Given a <strong>non-empty</strong>&nbsp;array of integers <code>nums</code>, every element appears <em>twice</em> except for one. Find that single one.</p>

<p>You must&nbsp;implement a solution with a linear runtime complexity and use&nbsp;only constant&nbsp;extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,1]
<strong>Output:</strong> 1
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [4,1,2,1,2]
<strong>Output:</strong> 4
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code></li>
	<li>Each element in the array appears twice except for one element which appears only once.</li>
</ul>

## Solutions

### Solution 1: Bitwise Operation

The XOR operation has the following properties:

-   Any number XOR 0 is still the original number, i.e., $x \oplus 0 = x$;
-   Any number XOR itself is 0, i.e., $x \oplus x = 0$;

Performing XOR operation on all elements in the array will result in the number that only appears once.

The time complexity is $O(n)$, where $n$ is the length of the array. The space complexity is $O(1)$.

<!-- tabs:start -->

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)
```

```java
class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;
        for (int v : nums) {
            ans ^= v;
        }
        return ans;
    }
}
```

```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int v : nums) {
            ans ^= v;
        }
        return ans;
    }
};
```

```go
func singleNumber(nums []int) (ans int) {
	for _, v := range nums {
		ans ^= v
	}
	return
}
```

```ts
function singleNumber(nums: number[]): number {
    return nums.reduce((r, v) => r ^ v);
}
```

```rust
impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        nums.into_iter()
            .reduce(|r, v| r ^ v)
            .unwrap()
    }
}
```

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
    return nums.reduce((a, b) => a ^ b);
};
```

```cs
public class Solution {
    public int SingleNumber(int[] nums) {
        return nums.Aggregate(0, (a, b) => a ^ b);
    }
}
```

```c
int singleNumber(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        ans ^= nums[i];
    }
    return ans;
}
```

```swift
class Solution {
    func singleNumber(_ nums: [Int]) -> Int {
        return nums.reduce(0, ^)
    }
}
```

<!-- tabs:end -->

### Solution 2

<!-- tabs:start -->

```java
class Solution {
    public int singleNumber(int[] nums) {
        return Arrays.stream(nums).reduce(0, (a, b) -> a ^ b);
    }
}
```

<!-- tabs:end -->

<!-- end -->
