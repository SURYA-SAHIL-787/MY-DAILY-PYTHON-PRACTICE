class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def house_robber(head):
    include = 0
    exclude = 0

    curr = head
    while curr:
        new_include = exclude + curr.data
        new_exclude = max(include, exclude)

        include = new_include
        exclude = new_exclude

        curr = curr.next

    return max(include, exclude)


head = Node(2)
head.next = Node(7)
head.next.next = Node(9)
head.next.next.next = Node(3)
head.next.next.next.next = Node(1)

print(house_robber(head))
