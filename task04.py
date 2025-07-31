class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

movie1 = Movie("Inception", "fantastika", 148, 8.8)
print(movie1.title, movie1.genre, movie1.duration, movie1.rating)