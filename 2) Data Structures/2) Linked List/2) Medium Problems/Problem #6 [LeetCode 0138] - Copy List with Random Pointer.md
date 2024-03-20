
# [LeetCode 138 - Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/description/)


## Description

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a [deep copy](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) of the list. The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:

 * `val`: an integer representing `Node.val`
 * `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.
 
Your code will only be given the head of the original linked list.


#### Example 1:

<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/e1.png" style="width: 750px;" />

```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

#### Example 2:

<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/e2.png" style="width: 750px;" />

```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

<br/>

#### Example 3:

<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/e3.png" style="width: 750px;" />

```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

<br/>

#### Constraints:
  * `0 <= n <= 1000`
  * `-10^4 <= Node.val <= 10^4`
  * `Node.random`is `null`or is pointing to some node in the linked list.
  

<br/>


<br/>

## Solution 1 - Hash Map Method
The basic idea is to traverse the list twice. In the first pass, we create a new node for each node in the original list and store the mapping in a hash map. In the second pass, we set the `next` and `random` pointers for each new node based on the hash map.
 1. Create an empty hash map, `old_to_new`, to store the mapping from old nodes to new nodes.
 2. First Pass - Node Creation:
    * Traverse the original list and for each node, create a corresponding new node.
    * Store the mapping in `old_to_new`.
 4. Second Pass - Setting Pointers:
    * Traverse the original list again.
    * For each node, set its corresponding new node's `next` and `random` pointers based on the hash map.

#### Complexity:
  * Time: `O(2n)`
  * Space: `O(1)`

#### ➤ [Python](https://leetcode.com/problems/copy-list-with-random-pointer/solutions/4003262/97-92-hash-table-linked-list):
```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}
        
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
            
        return old_to_new[head]
```

<br/>

## Solution 2 - Interweaving Nodes Method
The crux of this method is to interweave the nodes of the original and copied lists. This interweaving allows us to set the `random` pointers for the new nodes without needing additional memory for mapping.
 1. Initialization and Interweaving:
    * Traverse the original list.
    * For each node, create a corresponding new node and place it between the current node and the current node's `next`.
 3. Setting Random Pointers:
    * Traverse the interweaved list.
    * For each old node, set its corresponding new node's `random`pointer.
 4. Separating Lists:
    * Traverse the interweaved list again to separate the old and new lists.

#### Complexity:
  * Time: `O(n)`
  * Space: `O(1)`

#### ➤ [Python](https://leetcode.com/problems/copy-list-with-random-pointer/solutions/4003262/97-92-hash-table-linked-list)

``` python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
            
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        old_head = head
        new_head = head.next
        curr_old = old_head
        curr_new = new_head
        
        while curr_old:
            curr_old.next = curr_old.next.next
            curr_new.next = curr_new.next.next if curr_new.next else None
            curr_old = curr_old.next
            curr_new = curr_new.next
            
        return new_head

```
<!-- end -->
