def rhythm_reset(nums, k):
    if not nums:
        return 0

    longest = 1
    current = 1

    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i - 1]) <= k:
            current += 1
        else:
            current = 1

        longest = max(longest, current)

    return longest


print(rhythm_reset([4, 6, 5, 12, 13, 14, 20], 2))
# Output: 3
