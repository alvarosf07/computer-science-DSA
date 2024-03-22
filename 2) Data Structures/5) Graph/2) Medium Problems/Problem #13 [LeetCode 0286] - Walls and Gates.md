# [LeetCode 286 - Walls and Gates](https://leetcode.com/problems/walls-and-gates)


## Description

<p>You are given an <code>m x n</code> grid <code>rooms</code>&nbsp;initialized with these three possible values.</p>

<ul>
	<li><code>-1</code>&nbsp;A wall or an obstacle.</li>
	<li><code>0</code> A gate.</li>
	<li><code>INF</code> Infinity means an empty room. We use the value <code>2<sup>31</sup> - 1 = 2147483647</code> to represent <code>INF</code> as you may assume that the distance to a gate is less than <code>2147483647</code>.</li>
</ul>

<p>Fill each empty room with the distance to <em>its nearest gate</em>. If it is impossible to reach a gate, it should be filled with <code>INF</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://spcdn.pages.dev/leetcode/problems/0286.Walls%20and%20Gates/images/grid.jpg" style="width: 500px; height: 223px;" />
<pre>
<strong>Input:</strong> rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
<strong>Output:</strong> [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> rooms = [[-1]]
<strong>Output:</strong> [[-1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == rooms.length</code></li>
	<li><code>n == rooms[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 250</code></li>
	<li><code>rooms[i][j]</code> is <code>-1</code>, <code>0</code>, or <code>2<sup>31</sup> - 1</code>.</li>
</ul>

<br/>

## [Solution 1](https://leetcode.ca/2016-09-11-286-Walls-and-Gates/)
This solution code is a solution for the problem where you are given a 2D grid rooms initialized with three possible values:

* -1: A wall or an obstacle.
* 0: A gate.
* INF (represented by 2**31 - 1): An empty room. The goal is to fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should remain INF.

#### Methodology:
  1. Initialization:
     * The dimensions of the grid are stored in m and n.
     * A very large value (inf = 2**31 - 1) is used to represent INF, the initial state for empty rooms.
     * A queue q is initialized with the positions of all gates in the grid. This queue will be used for a Breadth-First Search (BFS).
  3. Breadth-First Search (BFS):
     * The BFS starts from all gates simultaneously. This parallel start is crucial because it ensures that the search radiates uniformly from all gates, efficiently calculating the minimum distance to each gate for all rooms.
     * With each iteration (d += 1), the distance from the gates increases by 1. This distance d is used to update the rooms that are reached in this iteration.
     * For each position (i, j) dequeued from q, the algorithm checks its four adjacent positions. If an adjacent position (x, y) is within bounds and its value is inf (indicating an unvisited empty room), the room’s value is updated to d (the current distance from a gate), and (x, y) is added to the queue for further exploration in the next iteration.
  5. Updating Rooms:
     * The grid rooms is updated in-place, with each empty room getting the distance to its nearest gate. This is achieved by setting the value of rooms[x][y] to d when it is first reached in the BFS. Since the BFS ensures that the shortest path is found first (due to the queue processing elements in order of their insertion and distances increasing uniformly), each room is guaranteed to be assigned the shortest distance to a gate.
  7. Termination:
     * The BFS terminates when there are no more rooms to process (i.e., the queue q becomes empty). At this point, all reachable rooms have been assigned the shortest distance to a nearest gate.
    
#### Key Points:
  * The use of BFS from gates (as opposed to starting the search from each empty room and looking for a gate) is efficient and ensures the shortest paths are found without redundant calculations.
  * This solution modifies the rooms grid in-place, effectively turning it into the result without needing additional space (apart from the space for the queue, which is relatively small).
  * The choice of inf as 2**31 - 1 is arbitrary but effectively represents a very large distance, assuming the grid sizes are reasonable and won’t exceed this distance.
<!-- tabs:start -->

#### Python:
```python
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        inf = 2**31 - 1
        q = deque([(i, j) for i in range(m) for j in range(n) if rooms[i][j] == 0])
        d = 0
        while q:
            d += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    x, y = i + a, j + b
                    if 0 <= x < m and 0 <= y < n and rooms[x][y] == inf:
                        rooms[x][y] = d
                        q.append((x, y))
```

#### JAVA:
```java
class Solution {
    public void wallsAndGates(int[][] rooms) {
        int m = rooms.length;
        int n = rooms[0].length;
        Deque<int[]> q = new LinkedList<>();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (rooms[i][j] == 0) {
                    q.offer(new int[] {i, j});
                }
            }
        }
        int d = 0;
        int[] dirs = {-1, 0, 1, 0, -1};
        while (!q.isEmpty()) {
            ++d;
            for (int i = q.size(); i > 0; --i) {
                int[] p = q.poll();
                for (int j = 0; j < 4; ++j) {
                    int x = p[0] + dirs[j];
                    int y = p[1] + dirs[j + 1];
                    if (x >= 0 && x < m && y >= 0 && y < n && rooms[x][y] == Integer.MAX_VALUE) {
                        rooms[x][y] = d;
                        q.offer(new int[] {x, y});
                    }
                }
            }
        }
    }
}
```
#### C++:
```cpp
class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        int m = rooms.size();
        int n = rooms[0].size();
        queue<pair<int, int>> q;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (rooms[i][j] == 0)
                    q.emplace(i, j);
        int d = 0;
        vector<int> dirs = {-1, 0, 1, 0, -1};
        while (!q.empty()) {
            ++d;
            for (int i = q.size(); i > 0; --i) {
                auto p = q.front();
                q.pop();
                for (int j = 0; j < 4; ++j) {
                    int x = p.first + dirs[j];
                    int y = p.second + dirs[j + 1];
                    if (x >= 0 && x < m && y >= 0 && y < n && rooms[x][y] == INT_MAX) {
                        rooms[x][y] = d;
                        q.emplace(x, y);
                    }
                }
            }
        }
    }
};
```

<!-- tabs:end -->

<!-- end -->
