n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array: ").split()))

fenwick = [0] * (n + 1)

def update(index, value):
    while index <= n:
        fenwick[index] += value
        index += index & -index

def prefix_sum(index):
    total = 0
    while index > 0:
        total += fenwick[index]
        index -= index & -index
    return total

def range_sum(left, right):
    return prefix_sum(right) - prefix_sum(left - 1)

for i in range(n):
    update(i + 1, arr[i])

q = int(input("Enter number of queries: "))

for _ in range(q):
    query = list(map(int, input("Enter query: ").split()))

    if query[0] == 1:
        index = query[1]
        value = query[2]
        update(index, value)

    elif query[0] == 2:
        left = query[1]
        right = query[2]
        print("Range sum:", range_sum(left, right))
