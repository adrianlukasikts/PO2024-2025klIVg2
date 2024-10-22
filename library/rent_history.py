from datetime import date


class RentHistory:
    def __init__(self, user_id: int, rental_date: date):
        self.user_id = user_id
        self.rental_date = rental_date
        self.return_date = date.today()

    def get_fee(self):
        difference = (self.return_date - self.rental_date).days
        return max(0, difference - 30)


