class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def maximum_non_adjacent_sum(head):
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


head = Node(5)
head.next = Node(5)
head.next.next = Node(10)
head.next.next.next = Node(100)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(5)

print(maximum_non_adjacent_sum(head))
