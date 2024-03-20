
# [LeetCode 141 - Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)


## Description

Given the `head` of a singly linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. 
Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.


#### Example 1:

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png" style="width: 370px;" />

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

#### Example 2:

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png" style="width: 200px;" />

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

#### Example 3:

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png" style="width: 50px;" />

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

<br/>

#### Constraints:
  * The number of nodes in the list is the range <code>[0, 10000]</code>.
  * <code>-100000 <= Node.val <= 100000 </code>
  * `pos` is `-1` or a valid index in the linked-list.

<br/>


<br/>

## Solution 1 - Hash Table Method
This approach involves storing visited nodes in a hash table. During traversal, if a node is encountered that already exists in the hash table, a cycle is confirmed.

#### Complexity:
  * Time: O(n)
  * Space: O(n)

#### ➤ Python:
[Source](https://leetcode.com/problems/linked-list-cycle/solutions/3999014/99-68-two-pointer-hash-table)
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        current_node = head
        while current_node:
            if current_node in visited_nodes:
                return True
            visited_nodes.add(current_node)
            current_node = current_node.next
        return False         
```
<br/>

 
<!-- end -->

## Solution 2 - Two-Pointers Method (Floyd's Cycle-Finding Algorithm)
Also known as the "hare and tortoise" algorithm, this method employs two pointers that move at different speeds. 
If there is a cycle, the fast pointer will eventually catch up to the slow pointer, confirming the cycle's existence.

#### Complexity:
  * Time: O(n)
  * Space: O(1)

#### ➤ Python:
[Source](https://leetcode.com/problems/linked-list-cycle/solutions/3999014/99-68-two-pointer-hash-table)
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False
```
<br/>
