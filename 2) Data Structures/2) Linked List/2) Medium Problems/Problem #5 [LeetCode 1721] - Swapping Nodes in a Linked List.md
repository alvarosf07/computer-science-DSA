
# [LeetCode 1721 - Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/)


## Description

Given the `head` of a singly linked list, and an integer `k`.

Return the head of the linked list after swapping the values of the 
`kth` node from the beginning and the `kth` node from the end (the list is 1-indexed).


#### Example 1:

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/linked1.jpg" style="width: 310px;" />

```
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
```

#### Example 2:

```
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
```

<br/>

#### Constraints:
  * The number of nodes in the list is `n`.
  * `0 <= Node.val <= 100`
  * `1 <= k <= n <= 10^5`

<br/>

<br/>


## Solution 1 - Swapping Values
  1. Find the k-th node from the front.
  2. Find the k-th last element using two poiners method.
  3. Swap their values.
  4. Return the head of the Linked List

#### ➤ [Python](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/solutions/1054370/python-3-swapping-nodes-swapping-values-one-pass-fully-explained)
```python
def swapNodes(self, head: ListNode, k: int) -> ListNode:
	first = last = head
	for i in range(1, k):
		first = first.next
		
	null_checker = first 
	while null_checker.next:
		last = last.next
		null_checker = null_checker.next
	first.val, last.val = last.val, first.val
	return head
```

<br/>

## Solution 2 - Swapping Nodes
Here, the very first step will be to find the K-th first and K-th last nodes.
While doing so, we also need to store the addresses of previous nodes of the K-th first and K-th last nodes in two poiners.
See full explanation in the source.

#### ➤ [Python](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/solutions/1054370/python-3-swapping-nodes-swapping-values-one-pass-fully-explained)

``` python
def swapNodes(self, head: ListNode, k: int) -> ListNode:
    dummy = pre_right = pre_left = ListNode(next=head)
    right = left = head
    for i in range(k-1):
        pre_left = left
        left = left.next
    
    null_checker = left
    
    while null_checker.next:
        pre_right = right
        right = right.next
        null_checker = null_checker.next
        
    if left == right:
        return head
    
    pre_left.next, pre_right.next = right, left
    left.next, right.next = right.next, left.next
    return dummy.next

```
<!-- end -->
