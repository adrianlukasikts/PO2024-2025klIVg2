from functools import reduce

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


class BookIsNotRentedException(Exception):
    pass

class GenreDoesNotExist(Exception):
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
            raise UserDoesNotExistException()
        for value in self.rented_books.values():
            if book.id in value:
                raise BookAlreadyRentedException()

        return True

    def rent_book(self, book: Book, user_id: int):
        try:
            if self.can_book_be_rented(book, user_id):
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

    def return_book(self, book_id: int):
        for user_id, book_ids in self.rented_books.items():
            if book_id in book_ids:
                book_ids.remove(book_id)
                if not book_ids:
                    self.rented_books.pop(user_id)
                return
        raise BookIsNotRentedException()

    def add_books(self, *args: Book):
        for book in args:
            self.add_book(book)

    def add_users(self, *args: User):
        for user in args:
            self.add_user(user)

    def print_title_by_gen(self, genre:str):
        count_title = 0
        for title, books in self.books.items():
            if genre in map(lambda book: book.genre, books):
                print(title)
                count_title += 1
        if count_title == 0:
            raise GenreDoesNotExist()

    def print_gen_by_autor(self, autor:str):
        books = self.books.values()
        books = reduce(list.__add__, books)
        books = filter(lambda book: book.author == autor, books)
        books = map(lambda book: book.genre, books)
        genres = set(books)
        if genres:
            print(genres)
        else:
            raise GenreDoesNotExist()




library = Library()
book_one = Book("Hobbit", "Tolkien", 2222, "przygoda")
book_two = Book("Władca pierścieni", "Tolkien", 2222, "przygoda")
book_three = Book("Lord of the rings", "Tolkien", 2222, "przygoda")
book_four = Book("Lord of dead", "Tolkien", 2222, "Akcja")
book_five = Book("NieHobbit", "NieTolkien", 2024, "przygoda")
# library.add_book(book_one)
# library.add_book(book_two)
# library.add_book(book_three)
library.add_books(book_one, book_two, book_three)
library.add_books(book_four)
library.add_books(book_five)
library.add_user(User("janek", "kicia", "400200300"))
# library.add_user(User("bogdan", "piesek", "400200301"))
# library.add_user(User("milosz", "dzbanek", "400200302"))
library.add_users(User("milosz", "dzbanek", "400200302"), User("bogdan", "piesek", "400200301"))
library.print_users()

library.print_books()
library.rent_book(book_one, 0)
try:
    library.return_book(123456789)
except BookIsNotRentedException:
    print("Kisionszka nie byla wyporzyczona")

try:
    library.print_title_by_gen("niegatunek")
except GenreDoesNotExist:
    print("Gatunek nie występuje")

try:
    library.print_gen_by_autor("NieTolkien1")
except GenreDoesNotExist:
    print("Gatunek nie wystepuje")
# library.print_title_by_gen("Akcja")