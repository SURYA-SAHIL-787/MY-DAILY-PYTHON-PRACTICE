class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.title} borrowed successfully.")
        else:
            print(f"{self.title} is not available.")

    def return_book(self):
        self.is_available = True
        print(f"{self.title} returned successfully.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_available_books(self):
        print("Available books:")

        for book in self.books:
            if book.is_available:
                print(f"{book.title} by {book.author}")


library = Library()

book1 = Book("Python Basics", "Ravi")
book2 = Book("Data Structures", "Ananya")
book3 = Book("Object-Oriented Python", "Kiran")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

book1.borrow_book()

library.display_available_books()

book1.return_book()
