arr = [2, -3, 4, -2, 5]

max_product = arr[0]

for i in range(len(arr)):
    product = 1

    for j in range(i, len(arr)):
        product *= arr[j]

        if product > max_product:
            max_product = product

print(max_product)
