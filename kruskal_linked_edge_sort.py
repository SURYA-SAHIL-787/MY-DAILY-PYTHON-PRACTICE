class EdgeNode:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight
        self.next = None


class EdgeLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, source, destination, weight):
        new_edge = EdgeNode(source, destination, weight)

        if self.head is None:
            self.head = new_edge
            self.tail = new_edge
        else:
            self.tail.next = new_edge
            self.tail = new_edge

    def to_list(self):
        edges = []
        current = self.head

        while current is not None:
            edges.append(
                (
                    current.source,
                    current.destination,
                    current.weight,
                )
            )
            current = current.next

        return edges


class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(
                self.parent[vertex]
            )

        return self.parent[vertex]

    def union(self, first, second):
        first_root = self.find(first)
        second_root = self.find(second)

        if first_root == second_root:
            return False

        if self.rank[first_root] < self.rank[second_root]:
            self.parent[first_root] = second_root

        elif self.rank[first_root] > self.rank[second_root]:
            self.parent[second_root] = first_root

        else:
            self.parent[second_root] = first_root
            self.rank[first_root] += 1

        return True


def partition(edges, low, high):
    pivot_weight = edges[high][2]
    smaller_index = low - 1

    for index in range(low, high):
        if edges[index][2] <= pivot_weight:
            smaller_index += 1

            edges[smaller_index], edges[index] = (
                edges[index],
                edges[smaller_index],
            )

    edges[smaller_index + 1], edges[high] = (
        edges[high],
        edges[smaller_index + 1],
    )

    return smaller_index + 1


def quick_sort_edges(edges, low, high):
    if low < high:
        pivot_index = partition(edges, low, high)

        quick_sort_edges(edges, low, pivot_index - 1)
        quick_sort_edges(edges, pivot_index + 1, high)


def kruskal(vertices, edges):
    quick_sort_edges(edges, 0, len(edges) - 1)

    disjoint_set = DisjointSet(vertices)
    minimum_spanning_tree = []
    total_weight = 0

    for source, destination, weight in edges:
        if disjoint_set.union(source, destination):
            minimum_spanning_tree.append(
                (source, destination, weight)
            )
            total_weight += weight

            if len(minimum_spanning_tree) == vertices - 1:
                break

    if len(minimum_spanning_tree) != vertices - 1:
        return None, 0

    return minimum_spanning_tree, total_weight


def main():
    vertices, edge_count = map(int, input().split())

    edge_linked_list = EdgeLinkedList()

    for _ in range(edge_count):
        source, destination, weight = map(int, input().split())

        edge_linked_list.append(
            source,
            destination,
            weight
        )

    edges = edge_linked_list.to_list()

    minimum_spanning_tree, total_weight = kruskal(
        vertices,
        edges
    )

    if minimum_spanning_tree is None:
        print("Minimum spanning tree is not possible.")
    else:
        print("Minimum Spanning Tree:")

        for source, destination, weight in minimum_spanning_tree:
            print(f"{source} - {destination}: {weight}")

        print(f"Total weight: {total_weight}")


if __name__ == "__main__":
    main()
