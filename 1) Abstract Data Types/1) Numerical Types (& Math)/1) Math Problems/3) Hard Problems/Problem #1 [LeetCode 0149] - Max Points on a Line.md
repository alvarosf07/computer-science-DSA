# [LeetCode 149 - Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line)      ${\textsf{\color{WildStrawberry} [Hard] }}$



## Description

<p>Given an array of <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a point on the <strong>X-Y</strong> plane, return <em>the maximum number of points that lie on the same straight line</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://spcdn.pages.dev/leetcode/problems/0149.Max%20Points%20on%20a%20Line/images/plane1.jpg" style="width: 300px; height: 294px;" />
<pre>
<strong>Input:</strong> points = [[1,1],[2,2],[3,3]]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://spcdn.pages.dev/leetcode/problems/0149.Max%20Points%20on%20a%20Line/images/plane2.jpg" style="width: 300px; height: 294px;" />
<pre>
<strong>Input:</strong> points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 300</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li>All the <code>points</code> are <strong>unique</strong>.</li>
</ul>

<br/>

## Solution 1

<!-- tabs:start -->
#### Python:
```python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 1
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                cnt = 2
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    a = (y2 - y1) * (x3 - x1)
                    b = (y3 - y1) * (x2 - x1)
                    cnt += a == b
                ans = max(ans, cnt)
        return ans
```
#### JAVA:
```java
class Solution {
    public int maxPoints(int[][] points) {
        int n = points.length;
        int ans = 1;
        for (int i = 0; i < n; ++i) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = i + 1; j < n; ++j) {
                int x2 = points[j][0], y2 = points[j][1];
                int cnt = 2;
                for (int k = j + 1; k < n; ++k) {
                    int x3 = points[k][0], y3 = points[k][1];
                    int a = (y2 - y1) * (x3 - x1);
                    int b = (y3 - y1) * (x2 - x1);
                    if (a == b) {
                        ++cnt;
                    }
                }
                ans = Math.max(ans, cnt);
            }
        }
        return ans;
    }
}
```
#### C++:
```cpp
class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int n = points.size();
        int ans = 1;
        for (int i = 0; i < n; ++i) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = i + 1; j < n; ++j) {
                int x2 = points[j][0], y2 = points[j][1];
                int cnt = 2;
                for (int k = j + 1; k < n; ++k) {
                    int x3 = points[k][0], y3 = points[k][1];
                    int a = (y2 - y1) * (x3 - x1);
                    int b = (y3 - y1) * (x2 - x1);
                    cnt += a == b;
                }
                ans = max(ans, cnt);
            }
        }
        return ans;
    }
};
```
<!-- tabs:end -->

<br/>

### Solution 2

<!-- tabs:start -->

#### Python:
```python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        n = len(points)
        ans = 1
        for i in range(n):
            x1, y1 = points[i]
            cnt = Counter()
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                g = gcd(dx, dy)
                k = (dx // g, dy // g)
                cnt[k] += 1
                ans = max(ans, cnt[k] + 1)
        return ans
```

#### JAVA:
```java
class Solution {
    public int maxPoints(int[][] points) {
        int n = points.length;
        int ans = 1;
        for (int i = 0; i < n; ++i) {
            int x1 = points[i][0], y1 = points[i][1];
            Map<String, Integer> cnt = new HashMap<>();
            for (int j = i + 1; j < n; ++j) {
                int x2 = points[j][0], y2 = points[j][1];
                int dx = x2 - x1, dy = y2 - y1;
                int g = gcd(dx, dy);
                String k = (dx / g) + "." + (dy / g);
                cnt.put(k, cnt.getOrDefault(k, 0) + 1);
                ans = Math.max(ans, cnt.get(k) + 1);
            }
        }
        return ans;
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
```

#### C++:
```cpp
class Solution {
public:
    int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
    int maxPoints(vector<vector<int>>& points) {
        int n = points.size();
        int ans = 1;
        for (int i = 0; i < n; ++i) {
            int x1 = points[i][0], y1 = points[i][1];
            unordered_map<string, int> cnt;
            for (int j = i + 1; j < n; ++j) {
                int x2 = points[j][0], y2 = points[j][1];
                int dx = x2 - x1, dy = y2 - y1;
                int g = gcd(dx, dy);
                string k = to_string(dx / g) + "." + to_string(dy / g);
                cnt[k]++;
                ans = max(ans, cnt[k] + 1);
            }
        }
        return ans;
    }
};
```

<!-- tabs:end -->

<!-- end -->
