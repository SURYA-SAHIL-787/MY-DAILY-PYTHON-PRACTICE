def longest_subarray(arr, k):
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


arr = list(map(int, input("Enter positive numbers: ").split()))
k = int(input("Enter k: "))

print("Longest subarray length:", longest_subarray(arr, k))
