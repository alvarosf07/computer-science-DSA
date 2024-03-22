# [LeetCode 207 - Course Schedule](https://leetcode.com/problems/course-schedule)


## Description

<p>There are a total of <code>numCourses</code> courses you have to take, labeled from <code>0</code> to <code>numCourses - 1</code>. You are given an array <code>prerequisites</code> where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you <strong>must</strong> take course <code>b<sub>i</sub></code> first if you want to take course <code>a<sub>i</sub></code>.</p>

<ul>
	<li>For example, the pair <code>[0, 1]</code>, indicates that to take course <code>0</code> you have to first take course <code>1</code>.</li>
</ul>

<p>Return <code>true</code> if you can finish all courses. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]]
<strong>Output:</strong> true
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0],[0,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numCourses &lt;= 2000</code></li>
	<li><code>0 &lt;= prerequisites.length &lt;= 5000</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; numCourses</code></li>
	<li>All the pairs prerequisites[i] are <strong>unique</strong>.</li>
</ul>

<br/>

## Solution 1: Topological Sorting

For this problem, we can consider the courses as nodes in a graph, and prerequisites as edges in the graph. Thus, we can transform this problem into determining whether there is a cycle in the directed graph.

Specifically, we can use the idea of topological sorting. For each node with an in-degree of $0$, we reduce the in-degree of its out-degree nodes by $1$, until all nodes have been traversed.

If all nodes have been traversed, it means there is no cycle in the graph, and we can complete all courses; otherwise, we cannot complete all courses.

The time complexity is $O(n + m)$, and the space complexity is $O(n + m)$. Here, $n$ and $m$ are the number of courses and prerequisites respectively.

<!-- tabs:start -->

#### Python:
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        indeg = [0] * numCourses
        for a, b in prerequisites:
            g[b].append(a)
            indeg[a] += 1
        cnt = 0
        q = deque(i for i, x in enumerate(indeg) if x == 0)
        while q:
            i = q.popleft()
            cnt += 1
            for j in g[i]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)
        return cnt == numCourses
```
#### JAVA:
```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] g = new List[numCourses];
        Arrays.setAll(g, k -> new ArrayList<>());
        int[] indeg = new int[numCourses];
        for (var p : prerequisites) {
            int a = p[0], b = p[1];
            g[b].add(a);
            ++indeg[a];
        }
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < numCourses; ++i) {
            if (indeg[i] == 0) {
                q.offer(i);
            }
        }
        int cnt = 0;
        while (!q.isEmpty()) {
            int i = q.poll();
            ++cnt;
            for (int j : g[i]) {
                if (--indeg[j] == 0) {
                    q.offer(j);
                }
            }
        }
        return cnt == numCourses;
    }
}
```
#### C++:
```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> g(numCourses);
        vector<int> indeg(numCourses);
        for (auto& p : prerequisites) {
            int a = p[0], b = p[1];
            g[b].push_back(a);
            ++indeg[a];
        }
        queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (indeg[i] == 0) {
                q.push(i);
            }
        }
        int cnt = 0;
        while (!q.empty()) {
            int i = q.front();
            q.pop();
            ++cnt;
            for (int j : g[i]) {
                if (--indeg[j] == 0) {
                    q.push(j);
                }
            }
        }
        return cnt == numCourses;
    }
};
```
<!-- tabs:end -->

<br/>

## Solution 2 - BFS with Kahn's Algorithm for Topological Sorting

This solution is usually seen in problems where we need to answer two questions:
 * Is it possible to have a topological order?
 * If yes, then print out one of all the orders.

#### ➤ [Python](https://leetcode.com/problems/course-schedule/solutions/441722/python-99-time-and-100-space-collection-of-solutions-with-explanation):
```python
    class Solution:
        def buildAdjacencyList(self, n, edgesList):
    				...
    
        def topoBFS(self, numNodes, edgesList):
            # Note: for consistency with other solutions above, we keep building
            # an adjacency list here. We can also merge this step with the next step.
            adjList = self.buildAdjacencyList(numNodes, edgesList)
    
            # 1. A list stores No. of incoming edges of each vertex
            inDegrees = [0] * numNodes
            for v1, v2 in edgesList:
                # v2v1 form a directed edge
                inDegrees[v1] += 1
    
            # 2. a queue of all vertices with no incoming edge
            # at least one such node must exist in a non-empty acyclic graph
            # vertices in this queue have the same order as the eventual topological
            # sort
            queue = []
            for v in range(numNodes):
                if inDegrees[v] == 0:
                    queue.append(v)
    
            # initialize count of visited vertices
            count = 0
            # an empty list that will contain the final topological order
            topoOrder = []
    
            while queue:
                # a. pop a vertex from front of queue
                # depending on the order that vertices are removed from queue,
                # a different solution is created
                v = queue.pop(0)
                # b. append it to topoOrder
                topoOrder.append(v)
    
                # increase count by 1
                count += 1
    
                # for each descendant of current vertex, reduce its in-degree by 1
                for des in adjList[v]:
                    inDegrees[des] -= 1
                    # if in-degree becomes 0, add it to queue
                    if inDegrees[des] == 0:
                        queue.append(des)
    
            if count != numNodes:
                return None  # graph has at least one cycle
            else:
                return topoOrder
    
        def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            return True if self.topoBFS(numCourses, prerequisites) else False
```


<br/>

## Solution 3 - DFS with an array storing 3 different states of a vertex

This solution is from "Introduction to Algorithms" book where it uses 3 different colours instead of 3 states.

It's also similar to this article Python DFS + Memoization where we use an array for Memoization

#### ➤ [Python](https://leetcode.com/problems/course-schedule/solutions/441722/python-99-time-and-100-space-collection-of-solutions-with-explanation):
```python
    class Solution:
    	def buildAdjacencyList(self, n, edgesList):
    		...
    		
        def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            # build Adjacency list from Edges list
            adjList = self.buildAdjacencyList(numCourses, prerequisites)
    
            # Each vertex can have 3 different states:
            # state 0   : vertex is not visited. It's a default state.
            # state -1  : vertex is being processed. Either all of its descendants
            #             are not processed or it's still in the function call stack.
            # state 1   : vertex and all its descendants are processed.
            state = [0] * numCourses
    
            def hasCycle(v):
                if state[v] == 1:
                    # This vertex is processed so we pass.
                    return False
                if state[v] == -1:
                    # This vertex is being processed and it means we have a cycle.
                    return True
    
                # Set state to -1
                state[v] = -1
    
                for i in adjList[v]:
                    if hasCycle(i):
                        return True
    
                state[v] = 1
                return False
    
            # we traverse each vertex using DFS, if we find a cycle, stop and return
            for v in range(numCourses):
                if hasCycle(v):
                    return False
    
            return True
```
<br/>

## Solution 4 - DFS with a stack storing all decendants being processed

Same idea as Solution 3, this time we use a stack to store all vertices being processed. While visiting a descendant of a vertex, if we found it in the stack it means a cycle appears.

This technique is also used to find a Topological order from the graph.

#### ➤ [Python](https://leetcode.com/problems/course-schedule/solutions/441722/python-99-time-and-100-space-collection-of-solutions-with-explanation):
```python
        class Solution:
        def buildAdjacencyList(self, n, edgesList):
            ...
    
        def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            # build Adjacency list from Edges list
            adjList = self.buildAdjacencyList(numCourses, prerequisites)
            visited = set()
    
            def hasCycle(v, stack):
                if v in visited:
                    if v in stack:
                        # This vertex is being processed and it means we have a cycle.
                        return True
                    # This vertex is processed so we pass
                    return False
    
                # mark this vertex as visited
                visited.add(v)
                # add it to the current stack
                stack.append(v)
    
                for i in adjList[v]:
                    if hasCycle(i, stack):
                        return True
    
                # once processed, we pop it out of the stack
                stack.pop()
                return False
    
            # we traverse each vertex using DFS, if we find a cycle, stop and return
            for v in range(numCourses):
                if hasCycle(v, []):
                    return False
    
            return True
```
<!-- end -->
