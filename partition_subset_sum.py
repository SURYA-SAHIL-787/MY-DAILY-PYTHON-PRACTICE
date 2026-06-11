nums = list(map(int, input().split()))
total = sum(nums)

if total % 2 != 0:
    print(False)
else:
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]

    print(dp[target])
