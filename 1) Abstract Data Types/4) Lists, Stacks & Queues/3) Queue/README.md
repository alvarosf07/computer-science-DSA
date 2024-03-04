# Queue
## Queue Definition

> A Queue is a type of (list) abstract data structure, in which elements are added and deleted following the "FIFO" principle:  "First In, First Out".

## Queue Implementation
### <code>list.pop(0)</code> vs <code>deque.popleft()</code>

* <code>list.pop(0)</code>
  * <code>pop(0)</code> removes the first item from the list and it requires to
  * It shifts left <code>len(list) - 1</code> items to fill the gap.

* <code>q = collections.deque()</code>
  * <code>deque()</code> implementation uses a doubly linked list.
  * No matter how large the deque, <code>deque.popleft()</code> requires a constant (limited above) number of operations.

The time complexity of <code>deque.popleft()</code> is <code>O(1)</code>, while the time complexity of <code>list.pop(0)</code> is <code>O(k)</code>, as index 0 is considered an intermediate index.
