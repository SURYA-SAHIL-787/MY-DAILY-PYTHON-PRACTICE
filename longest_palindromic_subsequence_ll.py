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


def longest_palindromic_subsequence(head):
    arr = linked_list_to_array(head)
    n = len(arr)

    if n == 0:
        return 0

    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if arr[i] == arr[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


head = Node("a")
head.next = Node("g")
head.next.next = Node("b")
head.next.next.next = Node("d")
head.next.next.next.next = Node("b")
head.next.next.next.next.next = Node("a")

print(longest_palindromic_subsequence(head))
