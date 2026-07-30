import heapq


def shortest_message_route(graph, source, destination):
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        if current_node == destination:
            break

        for neighbour, cost in graph[current_node]:
            new_distance = current_distance + cost

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                previous[neighbour] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbour)
                )

    if distances[destination] == float("inf"):
        return -1, []

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return distances[destination], path


graph = {
    "Home": [("School", 4), ("Library", 2)],
    "School": [("Home", 4), ("Mall", 5)],
    "Library": [("Home", 2), ("Mall", 1), ("Park", 7)],
    "Mall": [("School", 5), ("Library", 1), ("Park", 3)],
    "Park": [("Library", 7), ("Mall", 3)]
}

source = input("Enter the source location: ").strip().title()
destination = input("Enter the destination location: ").strip().title()

if source not in graph or destination not in graph:
    print("Invalid location name.")
else:
    distance, route = shortest_message_route(
        graph,
        source,
        destination
    )

    if distance == -1:
        print("No route exists.")
    else:
        route_string = " -> ".join(route)

        print("Shortest route:", route_string)
        print("Minimum cost:", distance)
        print("Route as one string:", route_string.replace(" -> ", "-"))
