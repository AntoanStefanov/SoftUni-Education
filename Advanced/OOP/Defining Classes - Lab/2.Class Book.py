class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book = Book('My Book', 'Me', 200)
book2 = Book('Another', 'You', 100)
print(book.name)
print(book2.name)