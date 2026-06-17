nums = list(map(int, input("Enter numbers: ").split()))

result = []

def backtrack(current, used):
    if len(current) == len(nums):
        result.append(current.copy())
        return

    for i in range(len(nums)):
        if used[i] == False:
            used[i] = True
            current.append(nums[i])

            backtrack(current, used)

            current.pop()
            used[i] = False

used = [False] * len(nums)

backtrack([], used)

print("All permutations:")

for p in result:
    print(p)
