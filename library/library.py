from math import trunc

from book import Book
from user import User


class UserAlreadyExistsException(Exception):
    pass


class BookAlreadyExistsException(Exception):
    pass

class BookDoesNotExistException(Exception):
    pass

class UserDoesNotExistException(Exception):
    pass

class BookAlreadyRentedException(Exception):
    pass

class Library:
    def __init__(self):
        self.books: dict[str, list[Book]] = {}
        self.rented_books: dict[int, list[int]] = {}
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

    def print_users(self):
        print(*self.users)

    def can_book_be_rented(self, book: Book, user_id: int):
        if not self.books.get(book.title) or book.id not in map(lambda b: b.id, self.books[book.title]):
            raise BookDoesNotExistException()
        if user_id not in map(lambda user: user.id, self.users):
            raise  UserDoesNotExistException()
        for value in self.rented_books.values():
            if book.id in value:
                raise BookAlreadyRentedException()

        return True

    def rent_book(self, book:Book, user_id: int):
        try:
            if self.can_book_be_rented(book,user_id):
                if user_id not in self.rented_books:
                    self.rented_books[user_id] = [book.id]
                else:
                    self.rented_books[user_id].append(book.id)
        except BookDoesNotExistException:
            print("Book not exists")
        except BookAlreadyRentedException:
            print("Book is already rented")
        except UserDoesNotExistException:
            print("User not exists")

    def return_book(self, book_id:int):
        for user_id, book_ids in self.rented_books.items():
            if book_id in book_ids:
                book_ids.remove(book_id)
                if not book_ids:
                    self.rented_books.pop(user_id)
                return
            # TODO raise exception







library = Library()
book_one = Book("Hobbit", "Tolkien", 2222, "przygoda")
book_two = Book("Władca pierścieni", "Tolkien", 2222, "przygoda")
book_three = Book("Lord of the rings", "Tolkien", 2222, "przygoda")
library.add_book(book_one)
library.add_book(book_two)
library.add_book(book_three)
library.add_user(User("janek", "kicia", "400200300"))
library.add_user(User("bogdan", "piesek", "400200301"))
library.add_user(User("milosz", "dzbanek", "400200302"))
library.print_users()

library.print_books()
library.rent_book(book_one,0)