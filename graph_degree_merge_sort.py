class ListNode:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency = [None] * vertices

    def add_edge(self, source, destination):
        new_node = ListNode(destination)
        new_node.next = self.adjacency[source]
        self.adjacency[source] = new_node

        new_node = ListNode(source)
        new_node.next = self.adjacency[destination]
        self.adjacency[destination] = new_node

    def get_degree(self, vertex):
        degree = 0
        current = self.adjacency[vertex]

        while current is not None:
            degree += 1
            current = current.next

        return degree


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        left_vertex, left_degree = left[i]
        right_vertex, right_degree = right[j]

        if (
            left_degree > right_degree
            or (
                left_degree == right_degree
                and left_vertex < right_vertex
            )
        ):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(values):
    if len(values) <= 1:
        return values

    middle = len(values) // 2

    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    return merge(left, right)


def main():
    vertices, edges = map(int, input().split())
    graph = Graph(vertices)

    for _ in range(edges):
        source, destination = map(int, input().split())
        graph.add_edge(source, destination)

    vertex_degrees = []

    for vertex in range(vertices):
        degree = graph.get_degree(vertex)
        vertex_degrees.append((vertex, degree))

    sorted_vertices = merge_sort(vertex_degrees)

    print("Vertices sorted by degree:")

    for vertex, degree in sorted_vertices:
        print(f"Vertex {vertex}: Degree {degree}")


if __name__ == "__main__":
    main()
