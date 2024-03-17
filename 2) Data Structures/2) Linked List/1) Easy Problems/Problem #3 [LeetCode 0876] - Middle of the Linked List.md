

# [LeetCode 0876 - Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/description/)


## Description

Given the `head` of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.


#### Example 1:

<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg" style="width: 370px;" />

```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
```

#### Example 2:

<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg" style="width: 450px;" />

```
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
```

<br/>

#### Constraints:
  * The number of nodes in the list is the range <code>[0, 100]</code>.
  * <code>-10^5 <= Node.val <= 100</code>

<br/>


<br/>

## Solutions

### Solution 1
  * Time: O(N)
  * Space: O(1)

#### ➤ Python:
```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
```

<!-- end -->
