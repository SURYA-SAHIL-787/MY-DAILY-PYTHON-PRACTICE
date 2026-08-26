class Cinema:
    def __init__(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats = [["O" for _ in range(seats_per_row)] for _ in range(rows)]

    def display_seats(self):
        print("\nCinema Seating")
        for i in range(self.rows):
            print(f"Row {i + 1}:", *self.seats[i])

    def book_seat(self, row, seat):
        if row < 1 or row > self.rows or seat < 1 or seat > self.seats_per_row:
            print("Invalid seat number.")
            return

        if self.seats[row - 1][seat - 1] == "O":
            self.seats[row - 1][seat - 1] = "X"
            print(f"Seat {row}-{seat} booked successfully.")
        else:
            print("Seat is already booked.")


cinema = Cinema(4, 5)

cinema.display_seats()

cinema.book_seat(2, 3)
cinema.book_seat(3, 4)
cinema.book_seat(2, 3)

cinema.display_seats()
