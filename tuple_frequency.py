# Program to count frequency of elements inside a tuple using dictionary

numbers = (10, 20, 10, 30, 20, 10, 40, 30, 50, 20)

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Original Tuple:")
print(numbers)

print("\nFrequency of Elements:")
for key, value in frequency.items():
    print(key, "appears", value, "times")
