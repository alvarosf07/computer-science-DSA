# [Geeks for Geeks - Mirror Tree](https://practice.geeksforgeeks.org/problems/mirror-tree/1#)


## Description

<p>Given a binary tree, convert it into its mirror.</p>

<p>The <strong>diameter</strong> of a binary tree is the <strong>length</strong> of the longest path between any two nodes in a tree. This path may or may not pass through the <code>root</code>.</p>

<p>The <strong>length</strong> of a path between two nodes is represented by the number of edges between them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://contribute.geeksforgeeks.org/wp-content/uploads/mirrortrees.jpg" style="width: 492px;" />
<pre>
<strong>Input:</strong> Input:
      1
    /  \
   2    3
<strong>Output:</strong> 3 1 2
<strong>Explanation:</strong> The tree is:
   1    (mirror)  1
 /  \    =>      /  \
2    3          3    2
The inorder of mirror is 3 1 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>


<br/>

## Solution 1

<!-- tabs:start -->

#### Python:
```python
class Solution:
    def mirror(self,root):
        
        def solve(root):
            if not root: return
            solve(root.left)
            solve(root.right)
            l = root.left
            r = root.right
            root.left = r
            root.right = l
            
        solve(root)
        return root

# Time: O(N)
# Space: O(1)
```
