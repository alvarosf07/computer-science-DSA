
# [LeetCode 83 - Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)


## Description

Given the `head` of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


#### Example 1:

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/list1.jpg" />

```
Input: head = [1,1,2]
Output: [1,2]
```

#### Example 2:
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/list2.jpg" style="width: 370px;" />

```
Input: head = [1,1,2,3,3]
Output: [1,2,3]
```

<br/>

#### Constraints:
  * The number of nodes in the list is the range `[0, 300]`.
  * `-100 <= Node.val <= 100`
  * The list is guaranteed to be sorted in ascending order.

<br/>


<br/>

## Solution 1

#### Complexity:
  * Time: `O(n)`
  * Space: `O(1)`

#### ➤ Python:
```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur=head
        while cur:
            while cur.next and cur.next.val==cur.val:
                cur.next=cur.next.next
            cur=cur.next
        return head
        
```

<br/>

## Solution 2

#### ➤ Python:
```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur=head
        while cur:
            if cur.next and cur.next.val==cur.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return head
        
```

<br/>


<!-- end -->
