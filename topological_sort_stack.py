def topological_sort(n, edges):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)

    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)

        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)

        stack.append(node)

    for i in range(n):
        if i not in visited:
            dfs(i)

    return stack[::-1]


print(topological_sort(6, [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]))
