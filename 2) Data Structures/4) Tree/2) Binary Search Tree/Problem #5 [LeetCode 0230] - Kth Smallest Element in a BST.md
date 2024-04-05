# [LeetCode 230 - Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst)

## Description

<p>Given the <code>root</code> of a binary search tree, and an integer <code>k</code>, return <em>the</em> <code>k<sup>th</sup></code> <em>smallest value (<strong>1-indexed</strong>) of all the values of the nodes in the tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://spcdn.pages.dev/leetcode/problems/0230.Kth%20Smallest%20Element%20in%20a%20BST/images/kthtree1.jpg" style="width: 212px; height: 301px;" />
<pre>
<strong>Input:</strong> root = [3,1,4,null,2], k = 1
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://spcdn.pages.dev/leetcode/problems/0230.Kth%20Smallest%20Element%20in%20a%20BST/images/kthtree2.jpg" style="width: 382px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,null,1], k = 3
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is <code>n</code>.</li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?</p>

#### Follow-up: can you find the Kth largest element in a BST

<br/>

## Solution 1 - Naive Approach (Inorder traversal + sorting)

We can do traversal of the given tree using any traversal technique and store the node values in an array/vector. Then we can sort the array in ascending order such that the 1st smallest element comes at 0th index, 2nd smallest element at 1st index ... kth samllest element at k-1th index.

#### Complexity:
* Time complexity:
  * O(n)O(n)O(n) + O(nlogn)O(nlogn)O(nlogn) -> O(nlogn)O(nlogn)O(nlogn)
    * O(n) for traversing the Tree and O(nlogn) for sorting the vector of size n.
* Space complexity:
  * O(n)O(n)O(n) + recursive stack space

#### Python:
```python

```

#### C++:
```cpp
class Solution {
public:
    void preOrderTraversal(TreeNode* root, vector<int> &v){
        if(root == NULL)    return;
        
        //root, left, right 
        v.push_back(root->val);
        preOrderTraversal(root->left, v);
        preOrderTraversal(root->right, v);      
    }
    int kthSmallest(TreeNode* root, int k) {
        vector<int> v; 
        preOrderTraversal(root, v);
        sort(v.begin(), v.end());
        return v[k-1];
    }
};
```

<!-- tabs:end -->

<br/>

## Solution 2 - Improved Approach (Inorder traversal + improved sorting)

In the above approach we are using an extra O(nlogn) for sorting the vector. We need to remove it somehow so that our time complexity boils down to O(n).

The naive approach of O(nlogn) can also be converted to O(nlogk) using priority queue as we do in the following array question.
https://leetcode.com/problems/kth-largest-element-in-an-array/

But, here I will be discussing only the O(n) one.



We know that the tree given to us is a Binary Search Tree, therefore, all the nodes at the left subtree of a given node will be less than the current node value and it will be less then all the nodes at the right subtree of that node.
i.e.
```
           N
          / \
         L   R
    
         L<N<R in case of BST
```
So, we can take advantage of this and do an INORDER TRAVERSAL. The inorder traversal will always result in a sorted array and the extra NlogN that we were using for sorting will be omitted.

#### Complexity:
* Time complexity:
  * O(n) for traversing the Tree consisting of n nodes.
* Space complexity:
  * O(n)O(n)O(n) + recursive stack space

#### Python:
```python

```

#### C++:
```cpp
class Solution {
public:
    void inOrderTraversal(TreeNode* root, vector<int> &v){
        if(root == NULL)    return;
        
        //left, root, right 
        inOrderTraversal(root->left, v);
        v.push_back(root->val);
        inOrderTraversal(root->right, v);      
    }
    int kthSmallest(TreeNode* root, int k) {
        vector<int> v; 
        inOrderTraversal(root, v);
        return v[k-1];
    }
};

```



<br/>

## Solution 3 - Optimal Approach: Inorder traversal stopping at kth element (O(n) time and O(1) space)

Approach 2 is fine, but there we are still creating an extra vector to store the node values. We can avoid it so that our space complexity further boils down to O(1).

We need the kth smallest element. And, we know that our inorder traversal will first give the 1st smallest element, then 2nd smallest element ... and so on.
So, instead of storing the node values inside a vector, we can maintain a 'cnt' variable to keep track if we have reached kth smallest value or not in the inorder traversal. And then, we can return the value once cnt reaches k value.

#### Complexity:
* Time complexity:
  * O(n) for traversing the Tree consisting of n nodes.
* Space complexity:
  * O(1)O(1)O(1) + recursive stack space

#### Python:
```python
def findNode(node, res):
            if len(res) > 1:
                return

            if node.left:
                findNode(node.left, res)

            res[0] -= 1
            if res[0] == 0:
                res.append(node.val)
                return
            
            if node.right:
                findNode(node.right, res)
                
        res = [k]
        findNode(root, res)
        return res[1]
```

#### C++:
```cpp
class Solution {
public:
    void solve(TreeNode* root, int &cnt, int &ans, int k){
        if(root == NULL)    return;
        //left, root, right 
        solve(root->left, cnt, ans, k);
        cnt++;
        if(cnt == k){
            ans = root->val;
            return;
        }
        solve(root->right, cnt, ans, k);
    }
    int kthSmallest(TreeNode* root, int k) {
        
        int cnt = 0;        
        int ans;
        solve(root, cnt, ans, k);
        return ans;
    }
};

```

Source of solutions: [LeetCode Answer](https://leetcode.com/problems/kth-smallest-element-in-a-bst/solutions/3469071/i-bet-you-will-understand-brute-better-optimal-beginner-friendly-c/)
