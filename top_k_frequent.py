def top_k_frequent(arr, k):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    buckets = [[] for _ in range(len(arr) + 1)]

    for num, count in freq.items():
        buckets[count].append(num)

    result = []

    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)

            if len(result) == k:
                return result

    return result


arr = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))

print("Top", k, "frequent elements:", top_k_frequent(arr, k))
