from collections import deque


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None

        return self.items.pop()


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return None

        return self.items.popleft()


names = ["Arun", "Meena", "Rahul", "Priya", "Kiran"]

stack = Stack()
queue = Queue()

for name in names:
    stack.push(name)
    queue.enqueue(name)

stack_order = []
queue_order = []

while not stack.is_empty():
    stack_order.append(stack.pop())

while not queue.is_empty():
    queue_order.append(queue.dequeue())

print("Original Array:", names)

print("Stack Processing Order:")
print(stack_order)

print("Queue Processing Order:")
print(queue_order)
