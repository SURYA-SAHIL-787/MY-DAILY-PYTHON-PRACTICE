class TrainSearch:
    def __init__(self, trains):
        self.trains = sorted(trains)

    def search(self, train_name):
        low = 0
        high = len(self.trains) - 1

        while low <= high:
            mid = (low + high) // 2

            if self.trains[mid] == train_name:
                return mid

            elif self.trains[mid] < train_name:
                low = mid + 1

            else:
                high = mid - 1

        return -1


trains = [
    "Chennai Express",
    "Duronto Express",
    "Rajdhani Express",
    "Shatabdi Express"
]

search = TrainSearch(trains)

result = search.search("Rajdhani Express")

if result != -1:
    print("Train found.")
else:
    print("Train not found.")
