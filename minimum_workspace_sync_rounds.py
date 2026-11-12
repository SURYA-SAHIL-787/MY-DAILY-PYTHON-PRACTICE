"""
A workspace has n files. Each dependency a b means file a must finish
syncing before file b can start. Each file takes one round to sync,
and any number of ready files can sync in parallel.

Input: Enter n and m, followed by m lines containing a and b.
Files are numbered from 1 to n.
Output: The minimum number of rounds, or -1 if dependencies form a cycle.

Example input:
5 4
1 3
2 3
3 4
2 5

Example output:
3
"""

from collections import deque
import sys


def minimum_sync_rounds(n, dependencies):
    dependents = [[] for _ in range(n + 1)]
    remaining = [0] * (n + 1)

    for prerequisite, file in dependencies:
        dependents[prerequisite].append(file)
        remaining[file] += 1

    ready = deque(file for file in range(1, n + 1) if remaining[file] == 0)
    rounds = synced = 0

    while ready:
        rounds += 1
        # Files unlocked during this round can sync in the next round.
        for _ in range(len(ready)):
            file = ready.popleft()
            synced += 1

            for dependent in dependents[file]:
                remaining[dependent] -= 1
                if remaining[dependent] == 0:
                    ready.append(dependent)

    return rounds if synced == n else -1


if __name__ == "__main__":
    values = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(values), next(values)
    dependencies = ((next(values), next(values)) for _ in range(m))
    print(minimum_sync_rounds(n, dependencies))
