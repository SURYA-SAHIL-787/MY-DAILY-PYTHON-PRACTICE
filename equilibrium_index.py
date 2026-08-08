arr = [1, 3, 5, 2, 2]

total = sum(arr)
left_sum = 0

for i in range(len(arr)):
    total -= arr[i]

    if left_sum == total:
        print("Equilibrium Index:", i)
        break

    left_sum += arr[i]
else:
    print("No Equilibrium Index")
