def has_cycle(n, edges):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    for start in range(n):
        if start in visited:
            continue

        stack = [(start, -1)]

        while stack:
            node, parent = stack.pop()

            if node in visited:
                return True

            visited.add(node)

            for nei in graph[node]:
                if nei != parent:
                    stack.append((nei, node))

    return False


print(has_cycle(3, [[0, 1], [1, 2], [2, 0]]))
