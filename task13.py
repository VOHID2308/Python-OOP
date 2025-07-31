class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False 

    def mark_as_read(self):
        self.is_read = True

    def status(self):
        if self.is_read:
            return f"{self.title} - read"
        else:
            return f"{self.title} - have not read"



book1 = Book("mock-dict", "herman melville")
book2 = Book("crime and punishment", "dostoevsky")
book3 = Book("1984", "George Orwell")
book4 = Book("pride and prejudice", "jane austen")

book1.mark_as_read()
book3.mark_as_read()

books = [book1, book2, book3, book4]
for book in books:
    print(book.status())