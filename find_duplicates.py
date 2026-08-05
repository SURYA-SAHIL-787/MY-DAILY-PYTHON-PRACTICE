def find_duplicates(arr):
    seen = set()
    duplicates = []
    added = set()

    for number in arr:
        if number in seen and number not in added:
            duplicates.append(number)
            added.add(number)
        else:
            seen.add(number)

    return duplicates


n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the array elements: ").split()))

if len(arr) != n:
    print("Error: Number of elements does not match n.")
else:
    result = find_duplicates(arr)

    if result:
        print("Duplicate elements:", result)
    else:
        print("No duplicate elements found.")
