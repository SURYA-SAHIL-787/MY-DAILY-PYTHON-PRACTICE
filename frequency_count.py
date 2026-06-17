nums = list(map(int, input("Enter numbers: ").split()))

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency of elements:")

for key in freq:
    print(key, "appears", freq[key], "times")
