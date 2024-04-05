# [LeetCode 1932 - Merge BSTs to Create Single BST](https://leetcode.com/problems/merge-bsts-to-create-single-bst)    [HARD]


## Description

<p>You are given <code>n</code> <strong>BST (binary search tree) root nodes</strong> for <code>n</code> separate BSTs stored in an array <code>trees</code> (<strong>0-indexed</strong>). Each BST in <code>trees</code> has <strong>at most 3 nodes</strong>, and no two roots have the same value. In one operation, you can:</p>

<ul>
	<li>Select two <strong>distinct</strong> indices <code>i</code> and <code>j</code> such that the value stored at one of the <strong>leaves </strong>of <code>trees[i]</code> is equal to the <strong>root value</strong> of <code>trees[j]</code>.</li>
	<li>Replace the leaf node in <code>trees[i]</code> with <code>trees[j]</code>.</li>
	<li>Remove <code>trees[j]</code> from <code>trees</code>.</li>
</ul>

<p>Return<em> the <strong>root</strong> of the resulting BST if it is possible to form a valid BST after performing </em><code>n - 1</code><em> operations, or</em><em> </em><code>null</code> <i>if it is impossible to create a valid BST</i>.</p>

<p>A BST (binary search tree) is a binary tree where each node satisfies the following property:</p>

<ul>
	<li>Every node in the node&#39;s left subtree has a value&nbsp;<strong>strictly less</strong>&nbsp;than the node&#39;s value.</li>
	<li>Every node in the node&#39;s right subtree has a value&nbsp;<strong>strictly greater</strong>&nbsp;than the node&#39;s value.</li>
</ul>

<p>A leaf is a node that has no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://spcdn.pages.dev/leetcode/problems/1932.Merge%20BSTs%20to%20Create%20Single%20BST/images/d1.png" style="width: 450px; height: 163px;" />
<pre>
<strong>Input:</strong> trees = [[2,1],[3,2,5],[5,4]]
<strong>Output:</strong> [3,2,5,1,null,4]
<strong>Explanation:</strong>
In the first operation, pick i=1 and j=0, and merge trees[0] into trees[1].
Delete trees[0], so trees = [[3,2,5,1],[5,4]].
<img alt="" src="https://spcdn.pages.dev/leetcode/problems/1932.Merge%20BSTs%20to%20Create%20Single%20BST/images/diagram.png" style="width: 450px; height: 181px;" />
In the second operation, pick i=0 and j=1, and merge trees[1] into trees[0].
Delete trees[1], so trees = [[3,2,5,1,null,4]].
<img alt="" src="https://spcdn.pages.dev/leetcode/problems/1932.Merge%20BSTs%20to%20Create%20Single%20BST/images/diagram-2.png" style="width: 220px; height: 165px;" />
The resulting tree, shown above, is a valid BST, so return its root.</pre>

<br/>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://spcdn.pages.dev/leetcode/problems/1932.Merge%20BSTs%20to%20Create%20Single%20BST/images/d2.png" style="width: 450px; height: 171px;" />
<pre>
<strong>Input:</strong> trees = [[5,3,8],[3,2,6]]
<strong>Output:</strong> []
<strong>Explanation:</strong>
Pick i=0 and j=1 and merge trees[1] into trees[0].
Delete trees[1], so trees = [[5,3,8,2,6]].
<img alt="" src="https://spcdn.pages.dev/leetcode/problems/1932.Merge%20BSTs%20to%20Create%20Single%20BST/images/diagram-3.png" style="width: 240px; height: 196px;" />
The resulting tree is shown above. This is the only valid operation that can be performed, but the resulting tree is not a valid BST, so return null.
</pre>

<br/>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://spcdn.pages.dev/leetcode/problems/1932.Merge%20BSTs%20to%20Create%20Single%20BST/images/d3.png" style="width: 430px; height: 168px;" />
<pre>
<strong>Input:</strong> trees = [[5,4],[3]]
<strong>Output:</strong> []
<strong>Explanation:</strong> It is impossible to perform any operations.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == trees.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li>The number of nodes in each tree is in the range <code>[1, 3]</code>.</li>
	<li>Each node in the input may have children but no grandchildren.</li>
	<li>No two roots of <code>trees</code> have the same value.</li>
	<li>All the trees in the input are <strong>valid BSTs</strong>.</li>
	<li><code>1 &lt;= TreeNode.val &lt;= 5 * 10<sup>4</sup></code>.</li>
</ul>

<br/>

## Solution 1

When asked to validate BST, we naturally think about in-order traversal (98. Validate Binary Search Tree). The question is how to do in-order traversal when we are given many separate trees.

First of all, we want to find a root node to start the traversal from, and we can do so by finding the node without any incoming edge (indeg = 0). If there's zero or more than one roots, we cannot create a single BST.

To traverse through nodes, we need to go from one BST to another. We achieve this with the help of a value-to-node map (nodes).

There are also two edges cases we need to check:

There is no cycle
We traverse through all nodes
Please see code below for more details =)


#### Complexity:

* Time complexity: O(N)
* Space complexity: O(N)

#### Python:
```python
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        nodes = {}
        indeg = collections.defaultdict(int)
        for t in trees:
            if t.val not in indeg:
                indeg[t.val] = 0
            if t.left:
                indeg[t.left.val] += 1
                if t.left.val not in nodes: nodes[t.left.val] = t.left
            if t.right:
                indeg[t.right.val] += 1
                if t.right.val not in nodes: nodes[t.right.val] = t.right
            nodes[t.val] = t
            
        # check single root
        sources = [k for k, v in indeg.items() if v == 0]
        if len(sources) != 1: return None
        
        self.cur = float('-inf')
        self.is_invalid = False
        seen = set()
        def inorder(val):
            # check cycle
            if val in seen:
                self.is_invalid = True
                return
            seen.add(val)
            node = nodes[val]
            if node.left: node.left = inorder(node.left.val)
            # check inorder increasing
            if val <= self.cur:
                self.is_invalid = True
                return
            self.cur = val
            if node.right: node.right = inorder(node.right.val)
            return node
        
        root = inorder(sources[0])
        # check full traversal
        if len(seen) != len(nodes) or self.is_invalid:
            return None
        return root
```

<!-- end -->
