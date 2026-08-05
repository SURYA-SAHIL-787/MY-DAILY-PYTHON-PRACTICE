from collections import deque


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

    def display(self):
        print(list(self.items))


numbers = [12, 7, 18, 5, 24, 11, 30, 9]

even_queue = Queue()
odd_queue = Queue()

for number in numbers:
    if number % 2 == 0:
        even_queue.enqueue(number)
    else:
        odd_queue.enqueue(number)

print("Original Array:", numbers)

print("Even Number Queue:")
even_queue.display()

print("Odd Number Queue:")
odd_queue.display()

print("\nRemoving Even Numbers:")

while not even_queue.is_empty():
    print(even_queue.dequeue(), end=" ")

print("\n\nRemoving Odd Numbers:")

while not odd_queue.is_empty():
    print(odd_queue.dequeue(), end=" ")
