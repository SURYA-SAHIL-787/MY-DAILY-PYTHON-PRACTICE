def max_meetings(start, end):
    meetings = []

    for i in range(len(start)):
        meetings.append((end[i], start[i]))

    meetings.sort()

    count = 0
    last_end_time = -1

    for end_time, start_time in meetings:
        if start_time > last_end_time:
            count += 1
            last_end_time = end_time

    return count
