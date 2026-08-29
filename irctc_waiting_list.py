from collections import deque


class WaitingList:
    def __init__(self):
        self.queue = deque()

    def add_passenger(self, name):
        self.queue.append(name)
        print(name, "added to waiting list.")

    def confirm_ticket(self):
        if self.queue:
            passenger = self.queue.popleft()
            print("Ticket confirmed for", passenger)
        else:
            print("Waiting list is empty.")


waiting = WaitingList()

waiting.add_passenger("Arun")
waiting.add_passenger("Meena")
waiting.add_passenger("Kiran")

waiting.confirm_ticket()
waiting.confirm_ticket()
