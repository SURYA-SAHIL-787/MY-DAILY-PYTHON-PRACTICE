from collections import Counter

def top_k_frequent(nums, k):
    frequency = Counter(nums)

    most_common = frequency.most_common(k)

    result = []

    for num, count in most_common:
        result.append(num)

    return result
