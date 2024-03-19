
# [LeetCode 21 - Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)


## Description

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


#### Example 1:

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" style="width: 370px;" />

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

#### Example 2:

```
Input: list1 = [], list2 = []
Output: []
```

#### Example 3:

```
Input: list1 = [], list2 = [0]
Output: [0]
```

<br/>

#### Constraints:
  * The number of nodes in the list is the range `[0, 50]`.
  * `-100 <= Node.val <= 100`
  * Both `list1`and `list2` are sorted in non-decreasing order.

<br/>


<br/>

## Solution 1
 1. We create a dummy node to which we attach nodes from lists.
 2. We iterate over lists using two-pointers and build up a resulting list so that values are monotonically increased.

#### Complexity:
  * Time: `O(n)`
  * Space: `O(1)`

#### ➤ [Python](https://leetcode.com/problems/merge-two-sorted-lists/solutions/1826693/python3-merging-explained):
```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next
```

<br/>

<!-- end -->
