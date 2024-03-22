
# [LeetCode 133 - Clone Graph](https://leetcode.com/problems/clone-graph/description/)


## Description

Given a reference of a node in a [connected](https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph) undirected graph.

Return a [deep copy](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```
class Node {
    public int val;
    public List<Node> neighbors;
}
```

#### Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with `val == 1`, the second node with `val == 2`, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `val = 1`. You must return the copy of the given node as a reference to the cloned graph.



#### Example 1:

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png" style="width: 370px;" />

```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
```

#### Example 2:

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/07/graph.png" style="width: 100px;" />

```
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
```

#### Example 3:
```
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
```

<br/>

#### Constraints:
* The number of nodes in the graph is in the range `[0, 100]`.
* <code>1 <= Node.val <= 100</code>
* `Node.val` is unique for each node.
* There are no repeated edges and no self-loops in the graph.
* The Graph is connected and all nodes can be visited starting from the given node.

<br/>


<br/>

## Solution 1 - DFS
  1. Create deep copy for each node, and maintain the mapping relation

     <img alt="" src="https://assets.leetcode.com/users/images/38bb4d11-8e1f-458f-ad7a-777a986f6897_1603180412.259184.png" style="width: 500px;" />
    
  2. Rebuild node linkage by mapping relation
     
      <img alt="" src="https://assets.leetcode.com/users/images/d6bf4b24-ddc9-40c3-9ebd-446efad0db6d_1603180429.2965417.png" style="width: 500px;" />
      
  3. Rebuild neighbor list in DFS with mapping relation.

#### ➤ [Python](https://leetcode.com/problems/clone-graph/solutions/902692/python-by-dfs-w-diagram):
```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # key: memory id of original node
        # value: corresponding deep copy node
        mapping = {}
        
        # -----------------------------------------
        def helper( node: 'Node' ) -> 'Node':
            
            if not node:
    
                # empty node's deep copy is still empty node
                return node
            
            elif id(node) in mapping:
                
                # current node already has deep copy
                return mapping[ id(node) ]
            
            # create deep copy for current node
            mapping[ id(node) ] = Node( val=node.val, neighbors=[] )
            
            for original_neighbor in node.neighbors:
                # update neighbor list for current node
                mapping[ id(node) ].neighbors.append( helper(original_neighbor) )
            
            return  mapping[ id(node) ]
        
        # -----------------------------------------
        return helper( node )
```

<br/>

## Solution 2 - BFS
To solve this problem we need two things:
  * BFS to traverse the graph
  * A hash map to keep track of already visited and already cloned nodes

We push a node in the queue and make sure that the node is already cloned. Then we process neighbors. If a neighbor is already cloned and visited, we just append it to the current clone neighbors list, otherwise, we clone it first and append it to the queue to make sure that we can visit it in the next tick.

#### Complexity:
  * Time: `O(V + E)` (for BFS)
  * Space: `O(V)` (for hashmap)

#### ➤ [Python](https://leetcode.com/problems/clone-graph/solutions/1792858/python3-iterative-bfs-beats-98-explained):
``` python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft() 
            cur_clone = clones[cur.val]            

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                    
                cur_clone.neighbors.append(clones[ngbr.val])
                
        return clones[node.val]
```

<!-- end -->
