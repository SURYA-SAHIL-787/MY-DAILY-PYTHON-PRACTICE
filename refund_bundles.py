def count_refund_bundles(transactions: list[tuple[str, int]]) -> int:
    starts = {}
    balance = 0
    count = 0

    for merchant, amount in transactions:
        # Record this index as a possible start using the sum before it.
        start_key = (merchant, balance)
        starts[start_key] = starts.get(start_key, 0) + 1

        balance += amount

        # A matching start has the same merchant and prefix sum.
        count += starts.get((merchant, balance), 0)

    return count


if __name__ == "__main__":
    transactions = [("A", 5), ("B", -2), ("A", -3), ("B", 2), ("A", 1)]
    print(count_refund_bundles(transactions))  # 2
