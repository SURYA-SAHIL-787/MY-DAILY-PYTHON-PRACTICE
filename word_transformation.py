import heapq


def shortest_transformation(words, start, target):
    """
    Each word is treated as a node.
    Two words are connected when they differ by exactly one character.
    Edge cost = ASCII difference between the changed characters.
    """

    if start not in words or target not in words:
        return -1

    graph = {word: [] for word in words}

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = words[i]
            word2 = words[j]

            if len(word1) != len(word2):
                continue

            differences = []

            for k in range(len(word1)):
                if word1[k] != word2[k]:
                    differences.append(k)

            if len(differences) == 1:
                index = differences[0]
                cost = abs(ord(word1[index]) - ord(word2[index]))

                graph[word1].append((word2, cost))
                graph[word2].append((word1, cost))

    distances = {word: float("inf") for word in words}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_word = heapq.heappop(priority_queue)

        if current_distance > distances[current_word]:
            continue

        if current_word == target:
            return current_distance

        for neighbour, cost in graph[current_word]:
            new_distance = current_distance + cost

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbour)
                )

    return -1


words = ["cat", "bat", "bet", "bed", "bad", "had"]
start_word = "cat"
target_word = "bed"

result = shortest_transformation(words, start_word, target_word)

if result == -1:
    print("No transformation path exists.")
else:
    print("Minimum transformation cost:", result)
