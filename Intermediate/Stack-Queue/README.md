# Stack and Queue

In Python, you can use lists to implement both stacks and queues, but for efficient queue operations (enqueue and dequeue), you can use the `collections.deque` class from the built-in `collections` module.

Let's see how you can use lists as stacks and queues:

1. **Stack using Python List**:
A stack is a Last-In-First-Out (LIFO) data structure where elements are added and removed from the top. Python lists are well-suited for implementing stacks because they support both append (push) and pop operations efficiently.

```python
# Stack using Python List
stack = []

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

print("Stack:", stack)  # Output: Stack: [1, 2, 3]

# Pop elements from the stack
print("Popped:", stack.pop())  # Output: Popped: 3
print("Popped:", stack.pop())  # Output: Popped: 2

print("Stack after pops:", stack)  # Output: Stack after pops: [1]
```

2. **Queue using `collections.deque`**:
A queue is a First-In-First-Out (FIFO) data structure where elements are added at the rear and removed from the front. While you can use lists to implement queues, using `collections.deque` provides more efficient enqueue and dequeue operations.

```python
from collections import deque

# Queue using collections.deque
queue = deque()

# Enqueue elements into the queue
queue.append(1)
queue.append(2)
queue.append(3)

print("Queue:", queue)  # Output: Queue: deque([1, 2, 3])

# Dequeue elements from the queue
print("Dequeued:", queue.popleft())  # Output: Dequeued: 1
print("Dequeued:", queue.popleft())  # Output: Dequeued: 2

print("Queue after dequeues:", queue)  # Output: Queue after dequeues: deque([3])
```

Using `collections.deque` ensures that both enqueue (`append`) and dequeue (`popleft`) operations have O(1) time complexity, making it efficient for implementing queues.

These examples demonstrate how you can leverage Python lists and `collections.deque` to implement stack and queue data structures efficiently.