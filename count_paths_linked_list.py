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


def count_ways(head):
    n = length_of_list(head)

    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(count_ways(head))
