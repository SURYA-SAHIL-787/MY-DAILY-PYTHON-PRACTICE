class AdjacentNode:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None


class DirectedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency = [None] * vertices

    def add_edge(self, source, destination):
        new_node = AdjacentNode(destination)
        new_node.next = self.adjacency[source]
        self.adjacency[source] = new_node

    def get_sorted_neighbours(self, vertex):
        neighbours = []
        current = self.adjacency[vertex]

        while current is not None:
            neighbours.append(current.vertex)
            current = current.next

        heap_sort(neighbours)
        return neighbours

    def topological_sort(self):
        state = [0] * self.vertices
        result = []

        for vertex in range(self.vertices):
            if state[vertex] == 0:
                if not self.depth_first_search(
                    vertex,
                    state,
                    result
                ):
                    return None

        result.reverse()
        return result

    def depth_first_search(self, vertex, state, result):
        state[vertex] = 1

        neighbours = self.get_sorted_neighbours(vertex)

        for neighbour in neighbours:
            if state[neighbour] == 1:
                return False

            if state[neighbour] == 0:
                if not self.depth_first_search(
                    neighbour,
                    state,
                    result
                ):
                    return False

        state[vertex] = 2
        result.append(vertex)
        return True


def heapify(values, size, root):
    largest = root
    left_child = 2 * root + 1
    right_child = 2 * root + 2

    if (
        left_child < size
        and values[left_child] > values[largest]
    ):
        largest = left_child

    if (
        right_child < size
        and values[right_child] > values[largest]
    ):
        largest = right_child

    if largest != root:
        values[root], values[largest] = (
            values[largest],
            values[root],
        )

        heapify(values, size, largest)


def heap_sort(values):
    size = len(values)

    for index in range(size // 2 - 1, -1, -1):
        heapify(values, size, index)

    for index in range(size - 1, 0, -1):
        values[0], values[index] = values[index], values[0]
        heapify(values, index, 0)


def main():
    vertices, edges = map(int, input().split())
    graph = DirectedGraph(vertices)

    for _ in range(edges):
        source, destination = map(int, input().split())
        graph.add_edge(source, destination)

    topological_order = graph.topological_sort()

    if topological_order is None:
        print("Topological sorting is not possible.")
        print("The graph contains a cycle.")
    else:
        print("Topological order:")
        print(" ".join(map(str, topological_order)))


if __name__ == "__main__":
    main()
