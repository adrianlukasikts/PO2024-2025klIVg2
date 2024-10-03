from book import Book
from user import User


class UserAlreadyExistsException(Exception):
    pass


class BookAlreadyExistsException(Exception):
    pass


class Library:
    def __init__(self):
        self.books: dict[str, list[Book]] = {}
        self.borrowed_books: dict[int, list[int]] = {}
        self.users: list[User] = []

    def add_book(self, book: Book):
        if not self.books.get(book.title):
            self.books[book.title] = [book]
        else:
            if book in self.books[book.title]:
                raise BookAlreadyExistsException()
            self.books[book.title].append(book)

    def add_user(self, user: User):
        if user in self.users:
            raise UserAlreadyExistsException()

        self.users.append(user)

    def print_books(self):
        print(*self.books.keys())


library = Library()
book_one = Book(0, "Hobbit", "Tolkien", 2222, "przygoda")
book_two = Book(1, "Władca pierścieni", "Tolkien", 2222, "przygoda")
book_three = Book(2, "Lord of the rings", "Tolkien", 2222, "przygoda")
library.add_book(book_one)
library.add_book(book_two)
library.add_book(book_three)

library.print_books()
