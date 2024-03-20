
# [LeetCode 82 - Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/)


## Description

Given the `head` of a singly linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Return the linked list sorted as well.


#### Example 1:

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg" style="width: 370px;" />

```
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
```

#### Example 2:

<img alt="" src="[https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg](https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg)" style="width: 250px;" />

```
Input: head = [1,1,1,2,3]
Output: [2,3]
```

<br/>

#### Constraints:
  * The number of nodes in the list is the range `[0, 300]`.
  * `-100 <= Node.val <= 100`
  * The list is guaranteed to be sorted in ascending order.

<br/>


<br/>

## Solution 1 - Two Pointers Approach
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. 
Return the linked list sorted as well.

#### ➤ [Python](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/solutions/2419088/very-easy-100-fully-explained-java-c-python-js-c-python3):
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode(-1)
        fake.next = head
        # We use prev (for node just before duplications begins), curr (for the last node of the duplication group)...
        curr, prev = head, fake
        while curr:
            # while we have curr.next and its value is equal to curr...
            # It means, that we have one more duplicate...
            while curr.next and curr.val == curr.next.val:
                # So move curr pointer to the right...
                curr = curr.next
            # If it happens, that prev.next equal to curr...
            # It means, that we have only 1 element in the group of duplicated elements...
            if prev.next == curr:
                # Don't need to delete it, we move both pointers to right...
                prev = prev.next
                curr = curr.next
            # Otherwise, we need to skip a group of duplicated elements...
            # set prev.next = curr.next, and curr = prev.next...
            else:
                prev.next = curr.next
                curr = prev.next
        # Return the linked list...
        return fake.next
```

<br/>

<!-- end -->
