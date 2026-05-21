# Question:
# Take 5 names in a list.
# Insert them into a queue.
# Remove and print them in FIFO order.

names = ["Amit", "Ravi", "Sita", "Neha", "Kiran"]

queue = []

print("Original list:")
print(names)

for name in names:
    queue.append(name)
    print("Inserted into queue:", name)

print("Queue after insertion:")
print(queue)

print("Removing from queue:")

while len(queue) > 0:
    removed = queue.pop(0)
    print("Removed from queue:", removed)

print("Queue is empty now")
