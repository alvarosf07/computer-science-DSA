# [LeetCode 322 - Coin Change](https://leetcode.com/problems/coin-change)


## Description

<p>You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.</p>

<p>Return <em>the fewest number of coins that you need to make up that amount</em>. If that amount of money cannot be made up by any combination of the coins, return <code>-1</code>.</p>

<p>You may assume that you have an infinite number of each kind of coin.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> coins = [1,2,5], amount = 11
<strong>Output:</strong> 3
<strong>Explanation:</strong> 11 = 5 + 5 + 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> coins = [2], amount = 3
<strong>Output:</strong> -1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> coins = [1], amount = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= coins.length &lt;= 12</code></li>
	<li><code>1 &lt;= coins[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>0 &lt;= amount &lt;= 10<sup>4</sup></code></li>
</ul>



<br/> 
 
## Solution 1

<!-- tabs:start -->

#### Python: 
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m, n = len(coins), amount
        f = [[inf] * (n + 1) for _ in range(m + 1)]
        f[0][0] = 0
        for i, x in enumerate(coins, 1):
            for j in range(n + 1):
                f[i][j] = f[i - 1][j]
                if j >= x:
                    f[i][j] = min(f[i][j], f[i][j - x] + 1)
        return -1 if f[m][n] >= inf else f[m][n]
```

#### JAVA: 
```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        final int inf = 1 << 30;
        int m = coins.length;
        int n = amount;
        int[][] f = new int[m + 1][n + 1];
        for (var g : f) {
            Arrays.fill(g, inf);
        }
        f[0][0] = 0;
        for (int i = 1; i <= m; ++i) {
            for (int j = 0; j <= n; ++j) {
                f[i][j] = f[i - 1][j];
                if (j >= coins[i - 1]) {
                    f[i][j] = Math.min(f[i][j], f[i][j - coins[i - 1]] + 1);
                }
            }
        }
        return f[m][n] >= inf ? -1 : f[m][n];
    }
}
```

#### C++: 
```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int m = coins.size(), n = amount;
        int f[m + 1][n + 1];
        memset(f, 0x3f, sizeof(f));
        f[0][0] = 0;
        for (int i = 1; i <= m; ++i) {
            for (int j = 0; j <= n; ++j) {
                f[i][j] = f[i - 1][j];
                if (j >= coins[i - 1]) {
                    f[i][j] = min(f[i][j], f[i][j - coins[i - 1]] + 1);
                }
            }
        }
        return f[m][n] > n ? -1 : f[m][n];
    }
};
```

<!-- tabs:end -->

<br/> 
 
## Solution 2

<!-- tabs:start -->

#### Python: 
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        f = [0] + [inf] * n
        for x in coins:
            for j in range(x, n + 1):
                f[j] = min(f[j], f[j - x] + 1)
        return -1 if f[n] >= inf else f[n]
```

#### JAVA: 
```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        final int inf = 1 << 30;
        int n = amount;
        int[] f = new int[n + 1];
        Arrays.fill(f, inf);
        f[0] = 0;
        for (int x : coins) {
            for (int j = x; j <= n; ++j) {
                f[j] = Math.min(f[j], f[j - x] + 1);
            }
        }
        return f[n] >= inf ? -1 : f[n];
    }
}
```

#### C++: 
```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = amount;
        int f[n + 1];
        memset(f, 0x3f, sizeof(f));
        f[0] = 0;
        for (int x : coins) {
            for (int j = x; j <= n; ++j) {
                f[j] = min(f[j], f[j - x] + 1);
            }
        }
        return f[n] > n ? -1 : f[n];
    }
};
```

<!-- tabs:end -->

<!-- end -->
