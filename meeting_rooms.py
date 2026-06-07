import heapq


def min_meeting_rooms(meetings):
    if not meetings:
        return 0

    meetings.sort()
    heap = []

    for start, end in meetings:
        if heap and heap[0] <= start:
            heapq.heappop(heap)

        heapq.heappush(heap, end)

    return len(heap)


n = int(input("Enter number of meetings: "))
meetings = []

for _ in range(n):
    start, end = map(int, input("Enter start and end time: ").split())
    meetings.append((start, end))

print("Minimum rooms required:", min_meeting_rooms(meetings))
