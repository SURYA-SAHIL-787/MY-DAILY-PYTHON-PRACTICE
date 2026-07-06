# meta_binary_search.py
# Meta Binary Search (bitwise binary search)

def meta_binary_search(arr, key):
    n = len(arr)
    step = 1 << (n.bit_length() - 1)  # largest power of 2 <= n
    idx = -1

    while step > 0:
        if idx + step < n and arr[idx + step] <= key:
            idx += step
        step >>= 1

    if idx != -1 and arr[idx] == key:
        return idx
    return -1

# Example usage
if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10, 12, 14]
    key = 10
    result = meta_binary_search(arr, key)
    print("Element found at index:", result)
