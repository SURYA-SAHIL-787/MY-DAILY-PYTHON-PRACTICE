nums = list(map(int, input("Enter numbers: ").split()))

result = []

def backtrack(index, current):
    if index == len(nums):
        result.append(current.copy())
        return

    # Do not include current number
    backtrack(index + 1, current)

    # Include current number
    current.append(nums[index])
    backtrack(index + 1, current)

    # Remove last number
    current.pop()

backtrack(0, [])

print("All subsets:")

for subset in result:
    print(subset)
