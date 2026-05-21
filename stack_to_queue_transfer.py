# Question:
# Push 5 numbers into a stack.
# Pop each number from stack.
# Insert popped values into queue.
# Print final queue.

stack = []

queue = []

stack.append(100)
stack.append(200)
stack.append(300)
stack.append(400)
stack.append(500)

print("Initial stack:")
print(stack)

while len(stack) > 0:
    removed = stack.pop()
    queue.append(removed)
    print("Moved from stack to queue:", removed)

print("Final stack:")
print(stack)

print("Final queue:")
print(queue)
