import sys
input = sys.stdin.readline


class RollbackDSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.components = n
        self.history = []

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            self.history.append((-1, -1, -1))
            return

        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.history.append((rb, ra, self.size[ra]))
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1

    def snapshot(self):
        return len(self.history)

    def rollback(self, snap):
        while len(self.history) > snap:
            rb, ra, old_size_ra = self.history.pop()

            if rb == -1:
                continue

            self.parent[rb] = rb
            self.size[ra] = old_size_ra
            self.components += 1


def normalize_edge(u, v):
    if u > v:
        u, v = v, u
    return (u, v)


def add_interval(seg, node, left, right, ql, qr, edge):
    if qr < left or right < ql:
        return

    if ql <= left and right <= qr:
        seg[node].append(edge)
        return

    mid = (left + right) // 2
    add_interval(seg, node * 2, left, mid, ql, qr, edge)
    add_interval(seg, node * 2 + 1, mid + 1, right, ql, qr, edge)


def solve_segment_tree(seg, dsu, answers, query_type, node, left, right):
    snap = dsu.snapshot()

    for u, v in seg[node]:
        dsu.union(u, v)

    if left == right:
        if query_type[left] == "qry":
            answers[left] = dsu.components
    else:
        mid = (left + right) // 2
        solve_segment_tree(seg, dsu, answers, query_type, node * 2, left, mid)
        solve_segment_tree(seg, dsu, answers, query_type, node * 2 + 1, mid + 1, right)

    dsu.rollback(snap)


def main():
    n, q = map(int, input().split())

    operations = [None] * (q + 1)
    query_type = [""] * (q + 1)

    active = {}
    intervals = []

    for time in range(1, q + 1):
        parts = input().split()
        op = parts[0]
        query_type[time] = op

        if op == "add":
            u, v = map(int, parts[1:])
            edge = normalize_edge(u, v)
            active[edge] = time
            operations[time] = (op, edge)

        elif op == "rem":
            u, v = map(int, parts[1:])
            edge = normalize_edge(u, v)

            start = active.pop(edge)
            intervals.append((start, time - 1, edge))
            operations[time] = (op, edge)

        else:
            operations[time] = (op, None)

    for edge, start in active.items():
        intervals.append((start, q, edge))

    seg = [[] for _ in range(4 * (q + 5))]

    for start, end, edge in intervals:
        if start <= end:
            add_interval(seg, 1, 1, q, start, end, edge)

    dsu = RollbackDSU(n)
    answers = [None] * (q + 1)

    solve_segment_tree(seg, dsu, answers, query_type, 1, 1, q)

    output = []
    for time in range(1, q + 1):
        if query_type[time] == "qry":
            output.append(str(answers[time]))

    print("\n".join(output))


if __name__ == "__main__":
    main()
