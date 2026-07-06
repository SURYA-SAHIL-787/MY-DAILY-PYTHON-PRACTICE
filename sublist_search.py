# sublist_search.py
# Check if one list is a sublist of another

def is_sublist(main_list, sub_list):
    n, m = len(main_list), len(sub_list)
    for i in range(n - m + 1):
        if main_list[i:i+m] == sub_list:
            return True
    return False

# Example usage
if __name__ == "__main__":
    main = [1, 2, 3, 4, 5, 6]
    sub = [3, 4, 5]
    print("Sublist Found:", is_sublist(main, sub))
