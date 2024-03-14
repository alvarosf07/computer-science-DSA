# [LeetCode 206 - Reverse a Linked List](https://leetcode.com/problems/reverse-linked-list/description/)


## Description

Given the `head` of a singly linked list, reverse the list, and return the reversed list.


<p><strong class="example">Example 1:</strong></p>

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg" style="width: 450px; height: 169px;" />

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

<p><strong class="example">Example 2:</strong></p>

```
Input: head = [1,2]
Output: [2,1]
```

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li> The number of nodes in the list is the range <code>[0, 5000]</code>.</li>
	<li><code>-5000 <= Node.val <= 5000</code></li>
</ul>



<p>&nbsp;</p>

## Solutions

### Solution 1
Use 3 pointers in order to change the links between nodes.

#### Python:
```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        pre = ListNode(-1)
        pre.next = head
        cur = pre.next
        nex = cur.next
        
        while nex:
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = cur.next
        
        return pre.next
```

<!-- tabs:end -->

<!-- end -->
