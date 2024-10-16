import datetime


class RentedBook:
    def __init__(self, book_id: int):
        self.book_id = book_id
        self.rental_date = datetime.date.today()

    def __repr__(self):
        return f"Rented book({self.book_id}, {self.rental_date})"