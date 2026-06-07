def generate_permutations(arr):
    result = []

    def backtrack(index):
        if index == len(arr):
            result.append(arr[:])
            return

        for i in range(index, len(arr)):
            arr[index], arr[i] = arr[i], arr[index]
            backtrack(index + 1)
            arr[index], arr[i] = arr[i], arr[index]

    backtrack(0)
    return result


arr = list(map(int, input("Enter numbers: ").split()))
permutations = generate_permutations(arr)

print("All permutations:")
for p in permutations:
    print(p)
