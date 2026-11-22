def priority_pairing(nums, k):
    if k <= 0:
        raise ValueError("k must be positive")

    counts = [0] * k

    for num in nums:
        counts[num % k] += 1

    pairs = counts[0] // 2

    for r in range(1, (k + 1) // 2):
        pairs += min(counts[r], counts[k - r])

    if k % 2 == 0:
        pairs += counts[k // 2] // 2

    return pairs


print(priority_pairing([2, 3, 5, 7, 8, 10], 5))
# Output: 3
