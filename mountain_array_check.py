arr = [1, 3, 5, 4, 2]

peak = 0

for i in range(1, len(arr)):
    if arr[i] > arr[peak]:
        peak = i

valid = True

for i in range(peak):
    if arr[i] >= arr[i + 1]:
        valid = False

for i in range(peak, len(arr) - 1):
    if arr[i] <= arr[i + 1]:
        valid = False

if peak == 0 or peak == len(arr) - 1:
    valid = False

print(valid)
