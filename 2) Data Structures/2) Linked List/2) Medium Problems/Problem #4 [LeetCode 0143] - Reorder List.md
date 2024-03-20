

# [LeetCode 143 - Reorder List](https://leetcode.com/problems/reorder-list/description/)


## Description

You are given the head of a singly linked-list. The list can be represented as:

```
L0 → L1 → … → Ln - 1 → Ln
```

Reorder the list to be on the following form:

```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
```


#### Example 1:

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg" style="width: 370px;" />

```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

#### Example 2:

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg" style="width: 450px;" />

```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

<br/>

#### Constraints:
  * The number of nodes in the list is the range <code>[0, 50000]</code>.
  * <code>1 <= Node.val <= 1000 </code>

<br/>


<br/>

## Solution 1 - Two-pointer approach 
1. Find the middle node of the linked list using slow and fast pointer approach.
2. Reverse the second half of the linked list.
3. Merge the first half and the reversed second half of the linked list alternatively.

#### Complexity:
  * Time: `O(N)`
  * Space: `O(1)`

#### ➤ [Python](https://leetcode.com/problems/reorder-list/solutions/3205828/143-solution-with-step-by-step-explanation):
```python
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        curr, prev = slow.next, None
        slow.next = None # set the next of the slow to None to break the link
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_half = prev
        
        # Step 3: Merge the first half and the reversed second half of the linked list
        first_half = head
        while first_half and second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half, second_half = temp1, temp2
```

<!-- end -->
