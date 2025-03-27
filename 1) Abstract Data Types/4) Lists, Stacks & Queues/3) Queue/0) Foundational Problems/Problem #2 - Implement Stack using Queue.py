# https://leetcode.com/problems/implement-stack-using-queues/

# Solution #1 - Implement Stack Using 2 Queues (python lists)
class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        if self.queue1:
            self.queue2.append(self.queue1.pop())
        self.queue1.append(x)

    def pop(self) -> int:
        if self.queue1:
            val = self.queue1.pop()
        if self.queue2:
            self.queue1.append(self.queue2.pop())
        return val

    def top(self) -> int:
        if self.queue1:
            return self.queue1[0]
        else:
            return null

    def empty(self) -> bool:
        if self.queue1:
            return False
        else:
            return True




# Solution #2 - Implement Stack Using collections.deque() Queue
class MyStack:

    def __init__(self):
        self._deque = collections.deque()

    def push(self, x: int) -> None:
        self._deque.append(x)
        for _ in range(len(self._deque)-1):
            self._deque.append(self._deque.popleft())

    def pop(self) -> int:
        return self._deque.popleft()

    def top(self) -> int:
        return self._deque[0]

    def empty(self) -> bool:
        return len(self._deque) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
