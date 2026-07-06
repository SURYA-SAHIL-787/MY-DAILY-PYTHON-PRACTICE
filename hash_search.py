# hash_search.py
# Search using hashing (dictionary)

def hash_search(arr, key):
    hash_map = {val: i for i, val in enumerate(arr)}
    return hash_map.get(key, -1)

# Example usage
if __name__ == "__main__":
    arr = [15, 8, 23, 42, 4, 16]
    key = 42
    result = hash_search(arr, key)
    print("Element found at index:", result)
