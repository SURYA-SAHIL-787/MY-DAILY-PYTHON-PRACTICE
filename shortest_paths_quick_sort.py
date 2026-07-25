import heapq


class AdjacentNode:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
        self.next = None


class WeightedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency = [None] * vertices

    def add_edge(self, source, destination, weight):
        new_node = AdjacentNode(destination, weight)
        new_node.next = self.adjacency[source]
        self.adjacency[source] = new_node

        new_node = AdjacentNode(source, weight)
        new_node.next = self.adjacency[destination]
        self.adjacency[destination] = new_node

    def dijkstra(self, source):
        distances = [float("inf")] * self.vertices
        distances[source] = 0

        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(
                priority_queue
            )

            if current_distance > distances[current_vertex]:
                continue

            current = self.adjacency[current_vertex]

            while current is not None:
                new_distance = current_distance + current.weight

                if new_distance < distances[current.vertex]:
                    distances[current.vertex] = new_distance

                    heapq.heappush(
                        priority_queue,
                        (new_distance, current.vertex)
                    )

                current = current.next

        return distances


def partition(values, low, high):
    pivot = values[high][1]
    smaller_index = low - 1

    for index in range(low, high):
        if (
            values[index][1] < pivot
            or (
                values[index][1] == pivot
                and values[index][0] < values[high][0]
            )
        ):
            smaller_index += 1
            values[smaller_index], values[index] = (
                values[index],
                values[smaller_index],
            )

    values[smaller_index + 1], values[high] = (
        values[high],
        values[smaller_index + 1],
    )

    return smaller_index + 1


def quick_sort(values, low, high):
    if low < high:
        pivot_index = partition(values, low, high)

        quick_sort(values, low, pivot_index - 1)
        quick_sort(values, pivot_index + 1, high)


def main():
    vertices, edges = map(int, input().split())
    graph = WeightedGraph(vertices)

    for _ in range(edges):
        source, destination, weight = map(int, input().split())
        graph.add_edge(source, destination, weight)

    source_vertex = int(input())

    distances = graph.dijkstra(source_vertex)

    result = [
        (vertex, distances[vertex])
        for vertex in range(vertices)
    ]

    quick_sort(result, 0, len(result) - 1)

    print("Vertices sorted by shortest distance:")

    for vertex, distance in result:
        if distance == float("inf"):
            print(f"Vertex {vertex}: Unreachable")
        else:
            print(f"Vertex {vertex}: Distance {distance}")


if __name__ == "__main__":
    main()
