class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def linked_list_to_array(head):
    arr = []
    curr = head

    while curr:
        arr.append(curr.data)
        curr = curr.next

    return arr


def minimum_cost(head):
    cost = linked_list_to_array(head)
    n = len(cost)

    if n == 0:
        return 0
    if n == 1:
        return cost[0]

    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    return dp[n - 1]


head = Node(1)
head.next = Node(100)
head.next.next = Node(1)
head.next.next.next = Node(1)

print(minimum_cost(head))
