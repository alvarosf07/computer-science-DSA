
# [LeetCode 61 - Rotate List](https://leetcode.com/problems/rotate-list/description/)


## Description

Given the `head` of a singly linked list, rotate the list to the right by `k` places.

If there are two middle nodes, return the second middle node.


#### Example 1:

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg" style="width: 370px;" />

```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```

#### Example 2:

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg" style="width: 250px;" />

```
Input: head = [0,1,2], k = 4
Output: [2,0,1]
```

<br/>

#### Constraints:
  * The number of nodes in the list is the range `[0, 500]`.
  * `-100 <= Node.val <= 100`
  * `0 <= k <= 2 * 109`

<br/>


<br/>

## Solution 1
Two-pointer approach: 
  * Go to the (length - K)th node
  * Then disconnect right part and connect it to the front head.
  * Return the new head (ie. node where we disconnected) 

#### Complexity:
  * Time: O(N)
  * Space: O(1)

#### ➤ Python:
```python
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k: return head
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        
        k = k % count
        
        fast = head
        slow = head
        while fast:
            if k >= 0:
                fast = fast.next
                k -= 1
            else:
                fast = fast.next
                slow = slow.next
        
        end = slow.next
        slow.next = None
        cur = end
        while cur and cur.next:
            cur = cur.next
        if not end: return head
        cur.next = head
        return end
```

<br/>

## Solution 2
``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return None
        
        lastElement = head
        length = 1
        # get the length of the list and the last node in the list
        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1

        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        k = k % length
            
        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        lastElement.next = head
        
        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)
        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next
        
        # Get the next node from the tempNode and then set the tempNode.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = tempNode.next
        tempNode.next = None
        
        return answer

```
[Source](https://leetcode.com/problems/rotate-list/solutions/348197/96-faster-simple-python-solution-with-explanation)
<!-- end -->
