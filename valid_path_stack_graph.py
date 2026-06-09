def valid_path(n, edges, source, destination):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    stack = [source]
    visited = set()

    while stack:
        node = stack.pop()

        if node == destination:
            return True

        if node not in visited:
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    stack.append(nei)

    return False


print(valid_path(3, [[0, 1], [1, 2]], 0, 2))
