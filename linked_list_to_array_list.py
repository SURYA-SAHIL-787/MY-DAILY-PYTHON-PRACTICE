# Question:
# Create a linked list.
# Insert 5 values manually.
# Convert linked list into Python list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)

head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

array_list = []

current = head

while current is not None:
    array_list.append(current.data)
    print("Added to list:", current.data)
    current = current.next

print("Final array list:")
print(array_list)
