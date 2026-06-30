class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length_of_list(head):
    count = 0
    curr = head

    while curr:
        count += 1
        curr = curr.next

    return count


def climbing_ways(head):
    n = length_of_list(head)

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev2 = 1
    prev1 = 2

    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print(climbing_ways(head))
