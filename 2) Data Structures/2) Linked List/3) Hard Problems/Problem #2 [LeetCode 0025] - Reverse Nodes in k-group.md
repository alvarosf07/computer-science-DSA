
# [LeetCode 25 - Reverse Nodes in k-Group](https://leetcode.com/problems/rotate-list/description/)


## Description

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


#### Example 1:

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg" style="width: 370px;" />

```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

#### Example 2:

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg" style="width: 450px;" />

```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

<br/>

#### Constraints:
  * The number of nodes in the list is the range `n`.
  * `1 <= k <= n <= 5000`
  * `0 <= Node.val <= 1000`

<br/>

#### Follow-up: 
Can you solve the problem in O(1) extra memory space?

<br/>

## Solution 1 - Recursive Approach

#### ➤ [Python](https://leetcode.com/problems/reverse-nodes-in-k-group/solutions/3521559/python3-iterative-recursive-solutions):
```python
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        start = end = head
        # find the k-th node (the end node for the current group)
        for _ in range(k):
            if not end: return head # not enough items (< k) => remain the order
            end = end.next
        # reverse the current group with k nodes
        newHead = self.reverse(start, end)
        # after reverse start is the end for the group, link it with the next reversed group
        start.next = self.reverseKGroup(end, k)

        return newHead

    # reverse diapason [start:end), end not inclusive
    def reverse(self, start, end):
        prev = None
        while start != end:
            start.next, start, prev = prev, start.next, start
        return prev # return head node of the reversed group
```

<br/>

## Solution 2 - Iterative Approach
#### ➤ [Python](https://leetcode.com/problems/reverse-nodes-in-k-group/solutions/3521559/python3-iterative-recursive-solutions):
``` python
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getGroupEnd(cur, k):
            while k > 1 and cur.next:
                cur = cur.next 
                k-=1
            return cur if k == 1 else None

        def reverseGroup(start, end):
            prev, cur, new_group_start = None, start, end.next
            while cur != new_group_start:
                cur.next, cur, prev = prev, cur.next, cur  

        dummy = ListNode()
        prev_group = dummy
        while head:
            group_start = head
            group_end = getGroupEnd(head, k)
            if not group_end: break # not enough todes to make a new group
            next_group_start = group_end.next # save link to the next group start
            reverseGroup(group_start, group_end) # reverse the current group
            prev_group.next = group_end # group_end is the start of the reversed group
            prev_group = group_start # group_start is the end of the reversed group
            group_start.next = next_group_start # link current reversed group with the next group
            head = next_group_start # move current point to the start of the next group

        return dummy.next        

```
<!-- end -->
