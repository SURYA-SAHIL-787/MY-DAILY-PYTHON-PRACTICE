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

for i in range(n):
    update(i + 1, arr[i])

q = int(input("Enter number of queries: "))

for _ in range(q):
    k = int(input("Enter prefix index: "))
    print("Prefix sum:", prefix_sum(k))
