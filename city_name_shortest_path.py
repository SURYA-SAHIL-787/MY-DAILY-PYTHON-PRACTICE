import heapq


def calculate_string_cost(city_name):
    """
    Cost is calculated using the number of vowels
    and the length of the city name.
    """

    vowels = "aeiouAEIOU"
    vowel_count = 0

    for character in city_name:
        if character in vowels:
            vowel_count += 1

    return len(city_name) + vowel_count


def dijkstra(graph, start):
    distances = {city: float("inf") for city in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)

        if current_distance > distances[current_city]:
            continue

        for neighbour in graph[current_city]:
            travel_cost = calculate_string_cost(neighbour)
            new_distance = current_distance + travel_cost

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbour)
                )

    return distances


graph = {
    "Delhi": ["Mumbai", "Agra"],
    "Mumbai": ["Delhi", "Pune", "Chennai"],
    "Agra": ["Delhi", "Pune"],
    "Pune": ["Mumbai", "Agra", "Chennai"],
    "Chennai": ["Mumbai", "Pune"]
}

start_city = input("Enter the starting city: ").strip().title()

if start_city not in graph:
    print("City not found.")
else:
    shortest_distances = dijkstra(graph, start_city)

    print(f"\nShortest costs from {start_city}:")

    for city, distance in shortest_distances.items():
        print(f"{start_city} to {city}: {distance}")
