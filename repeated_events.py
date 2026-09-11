events = [
    "100m",
    "Swimming",
    "100m",
    "Long Jump",
    "Swimming",
    "Boxing",
    "100m",
    "Boxing"
]

event_count = {}

for event in events:
    event_count[event] = event_count.get(event, 0) + 1

print("Repeated Events:")

for event, count in event_count.items():
    if count > 1:
        print(event, ":", count)
