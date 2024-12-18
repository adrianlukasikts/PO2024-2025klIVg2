from datetime import date
from functools import reduce

from book import Book
from rent_history import RentHistory
from rented_book import RentedBook
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


class NoFeeToPayException(Exception):
    pass


class PaymentHasToMoreThanZeroException(Exception):
    pass


class TooMuchMoneyException(Exception):
    pass


class Library:
    def __init__(self):
        self.books: dict[str, list[Book]] = {}
        self.rented_books: dict[int, list[RentedBook]] = {}
        self.users: list[User] = []
        self.rented_history: dict[int, list[RentHistory]] = {}
        self.users_fee: dict[int, int] = {}

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
        if self.rented_books.values():
            books_rented = list(reduce(list.__add__, self.rented_books.values()))
            if book.id in map(lambda rented_book: rented_book.book_id, books_rented):
                raise BookAlreadyRentedException()

        return True

    def rent_book(self, book: Book, user_id: int):
        try:
            if self.can_book_be_rented(book, user_id):
                if user_id not in self.rented_books:
                    self.rented_books[user_id] = [RentedBook(book.id)]
                else:
                    self.rented_books[user_id].append(RentedBook(book.id))
        except BookDoesNotExistException:
            print("Book not exists")
        except BookAlreadyRentedException:
            print("Book is already rented")
        except UserDoesNotExistException:
            print("User not exists")

    def return_book(self, book_id: int, return_date: date = date.today()):
        for user_id, rented_books in self.rented_books.items():
            if book_id in map(lambda rented_book: rented_book.book_id, rented_books):
                rented_one_book: RentedBook = \
                    list(filter(lambda rented_book: rented_book.book_id == book_id, rented_books))[0]
                rent_history = RentHistory(user_id, rented_one_book.rental_date, return_date)
                fee = rent_history.get_fee()
                if fee > 0:
                    if self.users_fee.get(user_id):
                        self.users_fee[user_id] += fee
                    else:
                        self.users_fee[user_id] = fee
                if self.rented_history.get(book_id):
                    self.rented_history[book_id].append(rent_history)
                else:
                    self.rented_history[book_id] = [rent_history]
                rented_books = list(filter(lambda rented_book: rented_book.book_id != book_id, rented_books))
                if not rented_books:
                    self.rented_books.pop(user_id)
                else:
                    self.rented_books[user_id] = rented_books
                return
        raise BookIsNotRentedException()

    def pay_fee(self, user_id: int, payment: int):
        if user_id not in map(lambda user: user.id, self.users):
            raise UserDoesNotExistException()
        if not self.users_fee.get(user_id):
            raise NoFeeToPayException()
        if payment <= 0:
            raise PaymentHasToMoreThanZeroException()
        if payment > self.users_fee[user_id]:
            raise TooMuchMoneyException()
        self.users_fee[user_id] -= payment
        if self.users_fee[user_id] == 0:
            self.users_fee.pop(user_id)

    def add_books(self, *args: Book):
        for book in args:
            self.add_book(book)

    def add_users(self, *args: User):
        for user in args:
            self.add_user(user)

    def print_title_by_gen(self, genre: str):
        count_title = 0
        for title, books in self.books.items():
            if genre in map(lambda book: book.genre, books):
                print(title)
                count_title += 1
        if count_title == 0:
            raise GenreDoesNotExist()

    def print_gen_by_autor(self, autor: str):
        books = self.books.values()
        books = reduce(list.__add__, books)
        books = filter(lambda book: book.author == autor, books)
        books = map(lambda book: book.genre, books)
        genres = set(books)
        if genres:
            print(genres)
        else:
            raise GenreDoesNotExist()
    def get_book(self, book_id: int) -> Book:
        books = reduce(list.__add__,self.books.values())
        filtered_books = list(filter(lambda book: book.id == book_id, books))
        if not filtered_books:
            raise BookDoesNotExistException()
        else:
            return filtered_books[0]



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
    library.print_gen_by_autor("NieTolkien")
except GenreDoesNotExist:
    print("Gatunek nie wystepuje")
# library.print_title_by_gen("Akcja")


library.return_book(book_one.id)

library.rent_book(book_one, 0)
# print(library.rented_books)
library.rent_book(book_two, 0)
print(library.rented_books)

library.return_book(book_one.id)
library.return_book(book_two.id, date(2024, 11, 25))


print(library.rented_history.get(0)[0].get_fee())
print(library.users_fee)

while True:
    print("1. Dodaj użytkownika")
    print("2. Dodaj ksiązke")
    print("3. Wyświetl wypożyczone książki użytkownika")
    print("4. Wypożycz książkę")
    print("5. Zwróć książkę")
    print("6. Wyświetl zadłużenie użytkownika")
    print("7. Pay up time aka spłacanie długów")
    print("@ Exit")

    option = input("Podaj numer akcji: ")
    match option:
        case "1":
            name = input("Podaj imię:")
            surname = input("Podaj nazwisko:")
            library.add_user(User(name, surname))
        case "2":
            book_name = input("Podaj nazwe ksiązki:")
            book_author = input("Podaj autora książki:")
            year_of_book = int(input("Podaj rok wydania książki:"))
            book_category = input("Podaj kategorię książki:")
            library.add_book(Book(book_name, book_author, year_of_book, book_category))
        case "3":
            user_id = int(input("Podaj indetyfikator użytkownika:"))
            rented_books_by_user = library.rented_books.get(user_id)
            if not rented_books_by_user:
                print([])
            else:
                print(list(map(lambda rented_book: rented_book.book_id, rented_books_by_user)))
        case "4":
            book_id = int(input("Podaj ID książki: "))
            user_id = int(input("Podaj ID użytkownika: "))
            library.rent_book(library.get_book(book_id), user_id)
        case "5":
            book_id = int(input("Podaj ID Ksiazki"))
            library.return_book(book_id)
        case "6":
            user_id = int(input("podaj id uzytkownika"))
            fee = library.users_fee.get(user_id)
            if fee: print(fee)
            else: print('0')
        case "7":
            pass
        case "@":
            break
        case _:
            print("ni poprawne data &")
