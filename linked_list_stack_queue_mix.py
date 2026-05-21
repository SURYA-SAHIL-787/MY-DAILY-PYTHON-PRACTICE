# Question:
# Create a linked list.
# Store linked list values into a stack.
# Move stack values into a queue.
# Print final queue.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)

head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

stack = []

queue = []

current = head

while current is not None:
    stack.append(current.data)
    print("Pushed into stack:", current.data)
    current = current.next

while len(stack) > 0:
    value = stack.pop()
    queue.append(value)
    print("Moved to queue:", value)

print("Final queue:")
print(queue)
