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


def max_sum_increasing_subsequence(head):
    arr = linked_list_to_array(head)
    n = len(arr)

    if n == 0:
        return 0

    dp = arr[:]

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + arr[i])

    return max(dp)


head = Node(1)
head.next = Node(101)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(100)

print(max_sum_increasing_subsequence(head))
