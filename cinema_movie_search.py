class Movie:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.title} - Rs.{self.price}"


class CinemaCatalogue:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def sort_movies(self):
        self.movies.sort(key=lambda movie: movie.title.lower())

    def binary_search(self, title):
        self.sort_movies()

        low = 0
        high = len(self.movies) - 1

        while low <= high:
            mid = (low + high) // 2
            current = self.movies[mid].title.lower()
            target = title.lower()

            if current == target:
                return self.movies[mid]

            if current < target:
                low = mid + 1
            else:
                high = mid - 1

        return None

    def display_movies(self):
        self.sort_movies()

        print("\nAvailable Movies:")
        for movie in self.movies:
            print(movie)


catalogue = CinemaCatalogue()

catalogue.add_movie(Movie("Avatar", 250))
catalogue.add_movie(Movie("Inception", 220))
catalogue.add_movie(Movie("Batman", 200))
catalogue.add_movie(Movie("Interstellar", 280))
catalogue.add_movie(Movie("Avengers", 240))

catalogue.display_movies()

search_title = "Interstellar"

result = catalogue.binary_search(search_title)

print("\nSearch Result:")

if result:
    print("Movie found:", result)
else:
    print("Movie not found.")
