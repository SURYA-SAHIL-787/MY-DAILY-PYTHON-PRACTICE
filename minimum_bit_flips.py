def min_bit_flips(start, goal):
    difference = start ^ goal
    count = 0

    while difference:
        difference &= difference - 1
        count += 1

    return count


print(min_bit_flips(10, 7))  # 3
