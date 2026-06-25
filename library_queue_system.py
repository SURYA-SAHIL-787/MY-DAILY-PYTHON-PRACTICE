from collections import deque


class Book:
    def __init__(self, title, copies):
        self.title = title
        self.copies = copies
        self.waiting_queue = deque()

    def borrow_book(self, student):
        if self.copies > 0:
            self.copies -= 1
            print(f"{student.name} borrowed '{self.title}'")
        else:
            self.waiting_queue.append(student)
            print(f"No copies left. {student.name} added to waiting queue.")

    def return_book(self):
        if self.waiting_queue:
            next_student = self.waiting_queue.popleft()
            print(f"Book returned. '{self.title}' assigned to {next_student.name}")
        else:
            self.copies += 1
            print(f"Book returned. Available copies: {self.copies}")

    def show_queue(self):
        if not self.waiting_queue:
            print("Waiting queue is empty.")
        else:
            print("Waiting queue:", [student.name for student in self.waiting_queue])


class Student:
    def __init__(self, name):
        self.name = name


def main():
    book = Book("Python DSA", 2)

    s1 = Student("Amit")
    s2 = Student("Neha")
    s3 = Student("Ravi")
    s4 = Student("Sara")

    book.borrow_book(s1)
    book.borrow_book(s2)
    book.borrow_book(s3)
    book.borrow_book(s4)

    book.show_queue()

    book.return_book()
    book.show_queue()


if __name__ == "__main__":
    main()
