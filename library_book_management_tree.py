class BookNode:
    def __init__(self, title):
        self.title = title
        self.left = None
        self.right = None


class LibraryBST:
    def insert(self, root, title):
        if root is None:
            return BookNode(title)

        if title.lower() < root.title.lower():
            root.left = self.insert(root.left, title)

        elif title.lower() > root.title.lower():
            root.right = self.insert(root.right, title)

        return root

    def display_books(self, root):
        if root:
            self.display_books(root.left)
            print(root.title)
            self.display_books(root.right)

    def count_keyword(self, root, keyword):
        if root is None:
            return 0

        count = 0

        if keyword.lower() in root.title.lower():
            count = 1

        return (
            count
            + self.count_keyword(root.left, keyword)
            + self.count_keyword(root.right, keyword)
        )

    def longest_title(self, root):
        if root is None:
            return ""

        left_title = self.longest_title(root.left)
        right_title = self.longest_title(root.right)

        longest = root.title

        if len(left_title) > len(longest):
            longest = left_title

        if len(right_title) > len(longest):
            longest = right_title

        return longest


library = LibraryBST()
root = None

books = [
    "Python Programming",
    "Data Structures",
    "Artificial Intelligence",
    "Computer Networks",
    "Machine Learning",
    "Database Management"
]

for book in books:
    root = library.insert(root, book)

print("Books in alphabetical order:")

library.display_books(root)

keyword = input("\nEnter a word to search in book titles: ")

matching_books = library.count_keyword(root, keyword)
longest_book = library.longest_title(root)

print(
    "Number of book titles containing",
    keyword + ":",
    matching_books
)

print("Longest book title:", longest_book)
