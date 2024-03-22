# [LeetCode 694 - Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands)


## Description

<p>You are given an <code>m x n</code> binary matrix <code>grid</code>. An island is a group of <code>1</code>&#39;s (representing land) connected <strong>4-directionally</strong> (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.</p>

<p>An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.</p>

<p>Return <em>the number of <b>distinct</b> islands</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://spcdn.pages.dev/leetcode/problems/0694.Number%20of%20Distinct%20Islands/images/distinctisland1-1-grid.jpg" style="width: 413px; height: 334px;" />
<pre>
<strong>Input:</strong> grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://spcdn.pages.dev/leetcode/problems/0694.Number%20of%20Distinct%20Islands/images/distinctisland1-2-grid.jpg" style="width: 413px; height: 334px;" />
<pre>
<strong>Input:</strong> grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

<br/>

## Solution 1

<!-- tabs:start -->
#### Python:
```python
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, k: int):
            grid[i][j] = 0
            path.append(str(k))
            dirs = (-1, 0, 1, 0, -1)
            for h in range(1, 5):
                x, y = i + dirs[h - 1], j + dirs[h]
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    dfs(x, y, h)
            path.append(str(-k))

        paths = set()
        path = []
        m, n = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    dfs(i, j, 0)
                    paths.add("".join(path))
                    path.clear()
        return len(paths)
```
#### JAVA:
```java
class Solution {
    private int m;
    private int n;
    private int[][] grid;
    private StringBuilder path = new StringBuilder();

    public int numDistinctIslands(int[][] grid) {
        m = grid.length;
        n = grid[0].length;
        this.grid = grid;
        Set<String> paths = new HashSet<>();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    dfs(i, j, 0);
                    paths.add(path.toString());
                    path.setLength(0);
                }
            }
        }
        return paths.size();
    }

    private void dfs(int i, int j, int k) {
        grid[i][j] = 0;
        path.append(k);
        int[] dirs = {-1, 0, 1, 0, -1};
        for (int h = 1; h < 5; ++h) {
            int x = i + dirs[h - 1];
            int y = j + dirs[h];
            if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == 1) {
                dfs(x, y, h);
            }
        }
        path.append(k);
    }
}
```
#### C++:
```cpp
class Solution {
public:
    int numDistinctIslands(vector<vector<int>>& grid) {
        unordered_set<string> paths;
        string path;
        int m = grid.size(), n = grid[0].size();
        int dirs[5] = {-1, 0, 1, 0, -1};

        function<void(int, int, int)> dfs = [&](int i, int j, int k) {
            grid[i][j] = 0;
            path += to_string(k);
            for (int h = 1; h < 5; ++h) {
                int x = i + dirs[h - 1], y = j + dirs[h];
                if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y]) {
                    dfs(x, y, h);
                }
            }
            path += to_string(k);
        };

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j]) {
                    dfs(i, j, 0);
                    paths.insert(path);
                    path.clear();
                }
            }
        }
        return paths.size();
    }
};
```

<!-- tabs:end -->

<!-- end -->
