from collections import deque


class Train:
    def __init__(self, train_number, seats):
        self.train_number = train_number
        self.available_seats = seats
        self.waitlist = deque()
        self.tickets = {}
        self.next_ticket_id = 1

    def book_ticket(self, passenger_name):
        ticket_id = self.next_ticket_id
        self.next_ticket_id += 1

        if self.available_seats > 0:
            self.available_seats -= 1
            status = "Confirmed"
        else:
            self.waitlist.append(ticket_id)
            status = "Waitlisted"

        self.tickets[ticket_id] = {
            "passenger": passenger_name,
            "status": status,
        }
        return ticket_id, status

    def cancel_ticket(self, ticket_id):
        ticket = self.tickets.get(ticket_id)

        if ticket is None or ticket["status"] == "Cancelled":
            return "Ticket not found or already cancelled"

        if ticket["status"] == "Confirmed":
            ticket["status"] = "Cancelled"

            if self.waitlist:
                next_id = self.waitlist.popleft()
                self.tickets[next_id]["status"] = "Confirmed"
            else:
                self.available_seats += 1
        else:
            ticket["status"] = "Cancelled"
            self.waitlist.remove(ticket_id)

        return "Ticket cancelled"


train = Train("T101", seats=1)

ticket1, status1 = train.book_ticket("Asha")
ticket2, status2 = train.book_ticket("Ravi")

print(ticket1, status1)
print(ticket2, status2)

train.cancel_ticket(ticket1)
print("Ravi's status:", train.tickets[ticket2]["status"])
