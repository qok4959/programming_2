class Library:
    def __init__(self, books:dict[str, str]):
        self.books = books

    def find_book(self, isbn: str) -> str | None:
        return self.books.get(isbn)

obj = Library({'123': 'Harry Potter',
               '456': 'Lord of the Rings',
               '789': 'The Witcher',
               '101': 'The Hobbit'})

print(obj.find_book("789"))