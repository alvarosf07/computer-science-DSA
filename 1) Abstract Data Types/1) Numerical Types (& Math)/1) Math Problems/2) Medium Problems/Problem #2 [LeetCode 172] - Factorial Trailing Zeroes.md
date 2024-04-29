# [LeetCode 172 - Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes)


## Description

<p>Given an integer <code>n</code>, return <em>the number of trailing zeroes in </em><code>n!</code>.</p>

<p>Note that <code>n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> 3! = 6, no trailing zero.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 1
<strong>Explanation:</strong> 5! = 120, one trailing zero.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you write a solution that works in logarithmic time complexity?</p>

<br/>

## Solution 1

The number of 0s in the factorial will be equal to the number of 2s and 5s in the prime decomposition of n. Each time that we have a 2 and a 5 in the prime factorial decomposition of n, we will have one trailing 0 in n!. 
We can observe that the number of 2s in prime factors is always more than or equal to the number of 5s. So, if we count 5s in prime factors, we are done. We just need to count the number of 5s (restrictive factor) in the factorial decomposition of n in order to calculate the number of 0s (when n<5 we will have zero trailing 0s, when n<10 we will have 1 trailing 0s, when n<15 we will have 2 trailing 0s...). 

<!-- tabs:start -->

#### Python:
```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans
```

#### JAVA:
```java
class Solution {
    public int trailingZeroes(int n) {
        int ans = 0;
        while (n > 0) {
            n /= 5;
            ans += n;
        }
        return ans;
    }
}
```

#### C++:
```cpp
class Solution {
public:
    int trailingZeroes(int n) {
        int ans = 0;
        while (n) {
            n /= 5;
            ans += n;
        }
        return ans;
    }
};
```

<!-- tabs:end -->

<!-- end -->
