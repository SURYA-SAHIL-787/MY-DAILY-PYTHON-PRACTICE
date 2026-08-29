class Ticket:
    def __init__(self, passenger, train):
        self.passenger = passenger
        self.train = train


class BookingSystem:
    def __init__(self):
        self.bookings = []

    def book_ticket(self, ticket):
        self.bookings.append(ticket)
        print("Ticket booked for", ticket.passenger)

    def show_bookings(self):
        print("\nBooked Tickets:")
        for ticket in self.bookings:
            print(ticket.passenger, "-", ticket.train)


system = BookingSystem()

system.book_ticket(Ticket("Rahul", "Chennai Express"))
system.book_ticket(Ticket("Priya", "Shatabdi Express"))

system.show_bookings()
