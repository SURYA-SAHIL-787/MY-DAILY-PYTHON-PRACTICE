def can_finish(piles, speed, hours):
    total_hours = 0

    for pile in piles:
        total_hours += (pile + speed - 1) // speed

    return total_hours <= hours


def minimum_speed(piles, hours):
    low = 1
    high = max(piles)
    answer = high

    while low <= high:
        mid = (low + high) // 2

        if can_finish(piles, mid, hours):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


piles = list(map(int, input("Enter work piles: ").split()))
hours = int(input("Enter total hours: "))

print("Minimum speed required:", minimum_speed(piles, hours))
