# [LeetCode 2291 - Maximum Profit From Trading Stocks](https://leetcode.com/problems/maximum-profit-from-trading-stocks)


## Description

<p>You are given two <strong>0-indexed</strong> integer arrays of the same length <code>present</code> and <code>future</code> where <code>present[i]</code> is the current price of the <code>i<sup>th</sup></code> stock and <code>future[i]</code> is the price of the <code>i<sup>th</sup></code> stock a year in the future. You may buy each stock at most <strong>once</strong>. You are also given an integer <code>budget</code> representing the amount of money you currently have.</p>

<p>Return <em>the maximum amount of profit you can make.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> present = [5,4,6,2,3], future = [8,5,4,3,5], budget = 10
<strong>Output:</strong> 6
<strong>Explanation:</strong> One possible way to maximize your profit is to:
Buy the 0<sup>th</sup>, 3<sup>rd</sup>, and 4<sup>th</sup> stocks for a total of 5 + 2 + 3 = 10.
Next year, sell all three stocks for a total of 8 + 3 + 5 = 16.
The profit you made is 16 - 10 = 6.
It can be shown that the maximum profit you can make is 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> present = [2,2,5], future = [3,4,10], budget = 6
<strong>Output:</strong> 5
<strong>Explanation:</strong> The only possible way to maximize your profit is to:
Buy the 2<sup>nd</sup> stock, and make a profit of 10 - 5 = 5.
It can be shown that the maximum profit you can make is 5.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> present = [3,3,12], future = [0,3,15], budget = 10
<strong>Output:</strong> 0
<strong>Explanation:</strong> One possible way to maximize your profit is to:
Buy the 1<sup>st</sup> stock, and make a profit of 3 - 3 = 0.
It can be shown that the maximum profit you can make is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == present.length == future.length</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= present[i], future[i] &lt;= 100</code></li>
	<li><code>0 &lt;= budget &lt;= 1000</code></li>
</ul>

<br/>

## Solutions

### Solution 0 (Naive Solution)
The force brute approach simply aims to generate all possible combinations of portfolios (`portfolios`), and select the one with the hightest profit. We only add to `portfolios` those `new_portfolio` which are within the budget limit, to eliminate useless combinations.

<!-- tabs:start -->

#### Python:
```python
class Solution:
    def max_profit (present, future, budget):
	portfolios = [[]]
	max_profit = 0
	
	for i in range(len(present)):
		for j in range(len(portfolios)):
		    new_portfolio = portfolios[j]+[i]
		    cost_portfolio = 0
		    profit_portfolio = 0
		    for e in new_portfolio:
			cost_portfolio += present[e]
			profit_portfolio += future[e] - present[e]
		    if cost_portfolio <= budget:
			max_profit = max(max_profit, profit_portfolio)
			portfolios += [new_portfolio]
	return max_profit
```

<br/>

### Solution 1

<!-- tabs:start -->

#### Python:
```python
class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        f = [[0] * (budget + 1) for _ in range(len(present) + 1)]
        for i, w in enumerate(present, 1):
            for j in range(budget + 1):
                f[i][j] = f[i - 1][j]
                if j >= w and future[i - 1] > w:
                    f[i][j] = max(f[i][j], f[i - 1][j - w] + future[i - 1] - w)
        return f[-1][-1]
```

#### JAVA:
```java
class Solution {
    public int maximumProfit(int[] present, int[] future, int budget) {
        int n = present.length;
        int[][] f = new int[n + 1][budget + 1];
        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j <= budget; ++j) {
                f[i][j] = f[i - 1][j];
                if (j >= present[i - 1]) {
                    f[i][j] = Math.max(
                        f[i][j], f[i - 1][j - present[i - 1]] + future[i - 1] - present[i - 1]);
                }
            }
        }
        return f[n][budget];
    }
}
```

#### C++:
```cpp
class Solution {
public:
    int maximumProfit(vector<int>& present, vector<int>& future, int budget) {
        int n = present.size();
        int f[n + 1][budget + 1];
        memset(f, 0, sizeof f);
        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j <= budget; ++j) {
                f[i][j] = f[i - 1][j];
                if (j >= present[i - 1]) {
                    f[i][j] = max(f[i][j], f[i - 1][j - present[i - 1]] + future[i - 1] - present[i - 1]);
                }
            }
        }
        return f[n][budget];
    }
};
```

<!-- tabs:end -->

<br/>

### Solution 2

<!-- tabs:start -->

```python
class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        f = [0] * (budget + 1)
        for a, b in zip(present, future):
            for j in range(budget, a - 1, -1):
                f[j] = max(f[j], f[j - a] + b - a)
        return f[-1]
```

<!-- end -->
