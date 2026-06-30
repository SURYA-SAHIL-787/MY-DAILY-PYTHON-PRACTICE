class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_and_earn(head):
    points = {}

    curr = head
    while curr:
        points[curr.data] = points.get(curr.data, 0) + curr.data
        curr = curr.next

    nums = sorted(points.keys())

    take = 0
    skip = 0
    prev = None

    for num in nums:
        value = points[num]

        if prev is not None and num == prev + 1:
            new_take = skip + value
            new_skip = max(take, skip)
        else:
            new_take = max(take, skip) + value
            new_skip = max(take, skip)

        take = new_take
        skip = new_skip
        prev = num

    return max(take, skip)


head = Node(3)
head.next = Node(4)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(4)

print(delete_and_earn(head))
