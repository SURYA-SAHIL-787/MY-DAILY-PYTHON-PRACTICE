import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline


class LazySegmentTree:
    def __init__(self, arr):
        self.n = len(arr) - 1
        self.tree = [0] * (4 * self.n + 5)
        self.lazy = [0] * (4 * self.n + 5)
        self.build(arr, 1, 1, self.n)

    def build(self, arr, node, left, right):
        if left == right:
            self.tree[node] = arr[left]
            return

        mid = (left + right) // 2
        self.build(arr, node * 2, left, mid)
        self.build(arr, node * 2 + 1, mid + 1, right)
        self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def push(self, node):
        if self.lazy[node] != 0:
            value = self.lazy[node]

            left_child = node * 2
            right_child = node * 2 + 1

            self.tree[left_child] += value
            self.lazy[left_child] += value

            self.tree[right_child] += value
            self.lazy[right_child] += value

            self.lazy[node] = 0

    def range_add(self, node, left, right, ql, qr, value):
        if qr < left or right < ql:
            return

        if ql <= left and right <= qr:
            self.tree[node] += value
            self.lazy[node] += value
            return

        self.push(node)

        mid = (left + right) // 2
        self.range_add(node * 2, left, mid, ql, qr, value)
        self.range_add(node * 2 + 1, mid + 1, right, ql, qr, value)

        self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def range_max(self, node, left, right, ql, qr):
        if qr < left or right < ql:
            return -10**30

        if ql <= left and right <= qr:
            return self.tree[node]

        self.push(node)

        mid = (left + right) // 2
        left_answer = self.range_max(node * 2, left, mid, ql, qr)
        right_answer = self.range_max(node * 2 + 1, mid + 1, right, ql, qr)

        return max(left_answer, right_answer)


def dfs_size(u, p, graph, parent, depth, subtree_size, heavy):
    parent[u] = p
    subtree_size[u] = 1
    max_child_size = 0

    for v in graph[u]:
        if v == p:
            continue

        depth[v] = depth[u] + 1
        dfs_size(v, u, graph, parent, depth, subtree_size, heavy)
        subtree_size[u] += subtree_size[v]

        if subtree_size[v] > max_child_size:
            max_child_size = subtree_size[v]
            heavy[u] = v


def dfs_decompose(u, head_node, graph, parent, heavy, head, pos, reverse_pos, current_pos):
    head[u] = head_node
    pos[u] = current_pos[0]
    reverse_pos[current_pos[0]] = u
    current_pos[0] += 1

    if heavy[u] != -1:
        dfs_decompose(
            heavy[u],
            head_node,
            graph,
            parent,
            heavy,
            head,
            pos,
            reverse_pos,
            current_pos
        )

    for v in graph[u]:
        if v != parent[u] and v != heavy[u]:
            dfs_decompose(
                v,
                v,
                graph,
                parent,
                heavy,
                head,
                pos,
                reverse_pos,
                current_pos
            )


def path_add(u, v, value, parent, depth, head, pos, seg):
    while head[u] != head[v]:
        if depth[head[u]] < depth[head[v]]:
            u, v = v, u

        seg.range_add(1, 1, seg.n, pos[head[u]], pos[u], value)
        u = parent[head[u]]

    if depth[u] > depth[v]:
        u, v = v, u

    seg.range_add(1, 1, seg.n, pos[u], pos[v], value)


def path_max(u, v, parent, depth, head, pos, seg):
    answer = -10**30

    while head[u] != head[v]:
        if depth[head[u]] < depth[head[v]]:
            u, v = v, u

        answer = max(answer, seg.range_max(1, 1, seg.n, pos[head[u]], pos[u]))
        u = parent[head[u]]

    if depth[u] > depth[v]:
        u, v = v, u

    answer = max(answer, seg.range_max(1, 1, seg.n, pos[u], pos[v]))

    return answer


def main():
    n, q = map(int, input().split())
    values = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    subtree_size = [0] * (n + 1)
    heavy = [-1] * (n + 1)

    dfs_size(1, 0, graph, parent, depth, subtree_size, heavy)

    head = [0] * (n + 1)
    pos = [0] * (n + 1)
    reverse_pos = [0] * (n + 1)
    current_pos = [1]

    dfs_decompose(1, 1, graph, parent, heavy, head, pos, reverse_pos, current_pos)

    base_array = [0] * (n + 1)
    for node in range(1, n + 1):
        base_array[pos[node]] = values[node]

    seg = LazySegmentTree(base_array)

    output = []

    for _ in range(q):
        parts = input().split()

        if parts[0] == "add":
            u = int(parts[1])
            v = int(parts[2])
            x = int(parts[3])
            path_add(u, v, x, parent, depth, head, pos, seg)

        else:
            u = int(parts[1])
            v = int(parts[2])
            output.append(str(path_max(u, v, parent, depth, head, pos, seg)))

    print("\n".join(output))


if __name__ == "__main__":
    main()
