def dfs(graph, node, visited=None):

    if visited is None:
        visited = set()

    visited.add(node)

    print(node, end=" ")

    for neighbour in graph[node]:

        if neighbour not in visited:

            dfs(graph, neighbour, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}


print("DFS Traversal:")

dfs(graph, 'A')
