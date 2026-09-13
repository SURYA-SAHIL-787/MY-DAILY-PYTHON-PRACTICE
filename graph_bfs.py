def bfs(graph, start):

    visited = set()
    queue = [start]

    visited.add(start)

    while queue:

        node = queue.pop(0)

        print(node, end=" ")

        for neighbour in graph[node]:

            if neighbour not in visited:

                visited.add(neighbour)
                queue.append(neighbour)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}


print("BFS Traversal:")

bfs(graph, 'A')
