class Book:
    def __init__(self, title, author, is_read=False) -> None:
        self.title = title
        self.author = author
        self.is_read = is_read

    def status(self) -> bool:
        return self.is_read

    def mark_as_read(self):
        self.is_read = True

books: list[Book] = [
    Book("book01", "author01"),
    Book("book02", "author01", True),
    Book("book03", "author03"),
    Book("book04", "author05", True),
    Book("book05", "author03"),
]

books[0].mark_as_read()
books[1].mark_as_read()

for book in books:
    if book.status():
        print(book.title)