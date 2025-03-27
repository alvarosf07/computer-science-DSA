
# Solution #1 - Implementing Queue in Python
class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self,val):
    self.queue.append(val)

  def dequeue(self,val):
    if self.queue:
      self.queue.pop(0)
    raise IndexError("Dequeue from an empty queue")

  def size(self):
    return len(self.queue)
    

# Solution #2 - Implementing Queue in Python using deque library
from collections import deque
class Queue:
  def __init__(self):
    self.queue = deque()

  def enqueue(self,val):
    self.queue.append(val)

  def dequeue(self,val):
    if self.queue:
      self.queue.popleft() # deque library allows efficient pops from the beginning of the queue
    raise IndexError("Dequeue from an empty queue")

  def size(self):
    return len(self.queue)
