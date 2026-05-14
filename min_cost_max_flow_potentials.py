import sys
import heapq
input = sys.stdin.readline


class Edge:
    def __init__(self, to, rev, capacity, cost):
        self.to = to
        self.rev = rev
        self.capacity = capacity
        self.cost = cost


class MinCostMaxFlow:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]

    def add_edge(self, u, v, capacity, cost):
        forward = Edge(v, len(self.graph[v]), capacity, cost)
        backward = Edge(u, len(self.graph[u]), 0, -cost)

        self.graph[u].append(forward)
        self.graph[v].append(backward)

    def min_cost_max_flow(self, source, sink):
        n = self.n
        potential = [0] * (n + 1)

        total_flow = 0
        total_cost = 0

        while True:
            dist = [10**30] * (n + 1)
            parent_node = [-1] * (n + 1)
            parent_edge = [-1] * (n + 1)

            dist[source] = 0
            heap = [(0, source)]

            while heap:
                current_dist, u = heapq.heappop(heap)

                if current_dist != dist[u]:
                    continue

                for index, edge in enumerate(self.graph[u]):
                    if edge.capacity <= 0:
                        continue

                    next_dist = current_dist + edge.cost + potential[u] - potential[edge.to]

                    if next_dist < dist[edge.to]:
                        dist[edge.to] = next_dist
                        parent_node[edge.to] = u
                        parent_edge[edge.to] = index
                        heapq.heappush(heap, (next_dist, edge.to))

            if dist[sink] == 10**30:
                break

            for node in range(1, n + 1):
                if dist[node] < 10**30:
                    potential[node] += dist[node]

            pushed_flow = 10**30
            current = sink

            while current != source:
                previous = parent_node[current]
                edge_index = parent_edge[current]
                pushed_flow = min(pushed_flow, self.graph[previous][edge_index].capacity)
                current = previous

            current = sink

            while current != source:
                previous = parent_node[current]
                edge_index = parent_edge[current]

                edge = self.graph[previous][edge_index]
                reverse_edge = self.graph[current][edge.rev]

                edge.capacity -= pushed_flow
                reverse_edge.capacity += pushed_flow

                total_cost += pushed_flow * edge.cost
                current = previous

            total_flow += pushed_flow

        return total_flow, total_cost


def main():
    n, m, source, sink = map(int, input().split())

    solver = MinCostMaxFlow(n)

    for _ in range(m):
        u, v, capacity, cost = map(int, input().split())
        solver.add_edge(u, v, capacity, cost)

    max_flow, min_cost = solver.min_cost_max_flow(source, sink)

    print(max_flow, min_cost)


if __name__ == "__main__":
    main()
