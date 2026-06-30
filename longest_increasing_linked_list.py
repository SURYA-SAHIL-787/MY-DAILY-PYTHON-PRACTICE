class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def longest_increasing(head):
    if head is None:
        return 0

    max_len = 1
    curr_len = 1
    curr = head

    while curr.next:
        if curr.next.data > curr.data:
            curr_len += 1
        else:
            curr_len = 1

        max_len = max(max_len, curr_len)
        curr = curr.next

    return max_len


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print(longest_increasing(head))
