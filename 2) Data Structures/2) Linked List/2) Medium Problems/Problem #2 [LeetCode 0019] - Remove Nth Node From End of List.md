


# [LeetCode 0019 - Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)


## Description

Given the `head` of a singly linked list, remove the nth node from the end of the list and return its head.

If there are two middle nodes, return the second middle node.


#### Example 1:

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 370px;" />

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

#### Example 2:

```
Input: head = [1], n = 1
Output: []
```

#### Example 3:
```
Input: head = [1,2], n = 1
Output: [1]
```

<br/>

#### Constraints:
  * The number of nodes in the list is the range <code>[0, 100]</code>.
  * <code>-10^5 <= Node.val <= 100</code>

<br/>


<br/>

## Solution 1
* Take a dummy node connect it with head (if we take a dummy node then it would be easy to delete the first node if target node is head ie. n = length of list).
* Take 2 pointers fast and slow. Increase the fast pointer by n steps.
* Then in next pass increase both slow and fast together by one step.
* Slow will stop before the target element then delete the link.

#### Complexity:
* Time: O(N)
* Space: O(1)

#### ➤ Python:
```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        fast = head
        slow = dummy
        
        for i in range(n):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        tmp = slow.next.next
        slow.next.next = None
        slow.next = tmp
        
        return dummy.next
```

<!-- end -->
