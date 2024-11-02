# DEF: The queue module implements multi-producer, 
# multi-consumer queues.
# It is especially useful in threaded 
# programming when information must be 
# exchanged safely
# between multiple threads.

# The module implements three types of queue, which differ only in the order in which 
# the entries are retrieved.
# In a FIFO queue, the first tasks added are the f
# irst retrieved.
# In a LIFO queue, the most recently added 
# entry is the first retrieved (operating like a stack)

# To important operatio of Queue
# enque --> Adding element to queue
# deque --> Removing elemnet from queue

# We can perform this using both end in queue
# usinge list
# enqueue, deque in left end

from queue import Queue
from collections import deque
# l1 = []
# l1.append('Hello')
# l1.append('World')
# l1.append('Hey')
# print(l1)

# print(l1.pop(0))
# print(l1.pop(0))
# print(l1)

# enqueue, deque in right end

l2 = []
# l2.insert(0, 10)
# # print(l2)
# l2.insert(0, 20)
# # print(l2)
# l2.insert(0, 30)
# print(l2)

# print(l2.pop())
# print(l2.pop())
# print(l2)
# -------------------------------------------------------------------------------------------------------
d1 = deque()

# enqueue, deque in left end

# d1.append('Hello')
# d1.append('siri')
# print(d1)

# d1.popleft()
# print(d1)

# enqueue, deque in right end

# d1.appendleft(1)
# d1.appendleft(2)
# d1.appendleft(3)
# d1.appendleft(4)
# d1.appendleft(5)
# # print(d1)

# d1.pop()
# d1.pop()
# print(d1)
# -------------------------------------------------------------------------------------------------------

# q1 = Queue(maxsize=2)
# q1.put('Hello')
# q1.put(10, block=True, timeout=0.1)
# # print(q1)
# q1.put(30, block=True, timeout=0.1)
# q1.put(20, block=True, timeout=0.1)

# print(q1.get())
# print(q1.get())
# print(q1.get())

# # length of queue
# print(q1.qsize())

# # to check empty
# print(q1.empty())
# print(q1)
