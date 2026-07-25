class LinkedNode:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency = [None] * vertices

    def add_edge(self, source, destination):
        new_node = LinkedNode(destination)
        new_node.next = self.adjacency[source]
        self.adjacency[source] = new_node

        new_node = LinkedNode(source)
        new_node.next = self.adjacency[destination]
        self.adjacency[destination] = new_node

    def find_component(self, starting_vertex, visited):
        stack = [starting_vertex]
        visited[starting_vertex] = True
        component = []

        while stack:
            vertex = stack.pop()
            component.append(vertex)

            current = self.adjacency[vertex]

            while current is not None:
                if not visited[current.vertex]:
                    visited[current.vertex] = True
                    stack.append(current.vertex)

                current = current.next

        return component

    def connected_components(self):
        visited = [False] * self.vertices
        components = []

        for vertex in range(self.vertices):
            if not visited[vertex]:
                component = self.find_component(vertex, visited)
                insertion_sort_numbers(component)
                components.append(component)

        insertion_sort_components(components)
        return components


def insertion_sort_numbers(values):
    for index in range(1, len(values)):
        current_value = values[index]
        position = index - 1

        while position >= 0 and values[position] > current_value:
            values[position + 1] = values[position]
            position -= 1

        values[position + 1] = current_value


def insertion_sort_components(components):
    for index in range(1, len(components)):
        current_component = components[index]
        position = index - 1

        while position >= 0:
            previous_component = components[position]

            should_move = (
                len(previous_component) < len(current_component)
                or (
                    len(previous_component) == len(current_component)
                    and previous_component[0] > current_component[0]
                )
            )

            if not should_move:
                break

            components[position + 1] = components[position]
            position -= 1

        components[position + 1] = current_component


def main():
    vertices, edges = map(int, input().split())
    graph = Graph(vertices)

    for _ in range(edges):
        source, destination = map(int, input().split())
        graph.add_edge(source, destination)

    components = graph.connected_components()

    print("Connected components sorted by size:")

    for index, component in enumerate(components, start=1):
        print(
            f"Component {index}:",
            " ".join(map(str, component))
        )


if __name__ == "__main__":
    main()
