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


def minimum_partition_difference(head):
    arr = linked_list_to_array(head)
    total_sum = sum(arr)

    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in arr:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    for s in range(target, -1, -1):
        if dp[s]:
            return total_sum - 2 * s

    return total_sum


head = Node(1)
head.next = Node(6)
head.next.next = Node(11)
head.next.next.next = Node(5)

print(minimum_partition_difference(head))
