arr = [3, 5, 2, 7, 11, 4]
k = 2

count = 0

for i in range(len(arr)):
    prime_count = 0

    for j in range(i, len(arr)):
        num = arr[j]
        is_prime = num > 1

        for x in range(2, int(num ** 0.5) + 1):
            if num % x == 0:
                is_prime = False
                break

        if is_prime:
            prime_count += 1

        if prime_count == k:
            count += 1
        elif prime_count > k:
            break

print(count)
