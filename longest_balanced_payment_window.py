"""
Find the longest contiguous window where total payments equal total refunds
and the window contains the same number of payments and refunds.

Input: First enter n, then n signed, nonzero amounts separated by whitespace.
Positive amounts are payments. Negative amounts are refunds.
Output: The maximum window length, or 0 if no window qualifies.
"""

import sys


def longest_balanced_window(amounts):
    first_seen = {(0, 0): 0}
    net_amount = 0
    net_count = 0
    longest = 0

    for index, amount in enumerate(amounts, start=1):
        net_amount += amount
        net_count += 1 if amount > 0 else -1
        state = (net_amount, net_count)

        # A repeated state means both balances stayed unchanged over the window.
        start = first_seen.setdefault(state, index)
        longest = max(longest, index - start)

    return longest


if __name__ == "__main__":
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    print(longest_balanced_window(next(data) for _ in range(n)))
