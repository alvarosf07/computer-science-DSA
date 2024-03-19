
# [LeetCode 61 - Rotate List](https://leetcode.com/problems/rotate-list/description/)


## Description

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


#### Example 1:

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

#### Example 2:

```
Input: lists = []
Output: []
```

#### Example 3:

```
Input: lists = [[]]
Output: []
```

<br/>

#### Constraints:
  * `k == lists.length`
  * `0 <= k <= 10^4`
  * `0 <= lists[i].length <= 500`
  * `-10^4 <= lists[i][j] <= 10^4`
  * `lists[i]` is sorted in ascending order.
  * The sum of `lists[i].length` will not exceed `10^4`.

<br/>


<br/>

## Solution 1 - Brute Force
We merge two sorted list among lists each round, until there is only one list.

#### ➤ Python:
```python
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0)
            return null;
        ListNode merged = null;
        for (ListNode head : lists) {
            merged = mergeTwoLists(merged, head);
        }
        return merged;
    }
    
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null)
            return l2;
        if (l2 == null)
            return l1;
        if (l1.val < l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        }
        else {
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        }
    }
}
```

<br/>

## Solution 2 - Merge Sort
#### ➤ Python:
``` python
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0)
            return null;
        return mergeKLists(lists, 0, lists.length - 1);
    }
    
    private ListNode mergeKLists(ListNode[] lists, int start, int end) {
        if (end < start)
            return null;
        if (start == end)
            return lists[start];
        if (start + 1 == end)
            return mergeTwoLists(lists[start], lists[end]);
        
        int mid = start + ((end - start) >> 1);
        ListNode lower = mergeKLists(lists, start, mid);
        ListNode upper = mergeKLists(lists, mid + 1, end);
        
        return mergeTwoLists(lower, upper);
    }
    
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null)
            return l2;
        if (l2 == null)
            return l1;
        if (l1.val < l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        }
        else {
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        }
    }
}

```

<br/>

## Solution 3 - Heap (Priority Queue)
#### ➤ Python:
``` python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        def push_node(heap, node):
            if node:
                heapq.heappush(heap, (node.val, id(node), node))

        for l in lists:
            push_node(heap, l)
        
        dummy = ListNode()
        current = dummy
        
        while heap:
            _, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, id(node.next), node.next))

        return dummy.next
```
<!-- end -->
