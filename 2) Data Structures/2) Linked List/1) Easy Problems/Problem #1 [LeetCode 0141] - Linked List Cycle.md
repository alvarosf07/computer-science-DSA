# [LeetCode 141 - Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)


## Description

Given head, the `head` of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.


<p><strong class="example">Example 1:</strong></p>

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png" style="width: 450px; height: 169px;" />

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png"" />


```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

<br/>

<p><strong>Constraints:</strong></p>

<ul>
	<li> The number of nodes in the list is the range <code>[0, 10000]</code>.</li>
	<li><code>-10^5 <= Node.val <= 10^5</code></li>
  <li>`pos` is `-1` or a valid index in the linked-list.</li>
</ul>

<br/>

#### Follow up: 
Can you solve it using `O(1)` (i.e. constant) memory?


<p>&nbsp;</p>

## Solutions

### Solution 1
  * Time Complexity: O(n)
  * Space Complexity: O(1)

#### Python:
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast: return True
        
        return False
```

<!-- tabs:end -->

<!-- end -->
