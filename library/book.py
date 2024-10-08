class Book:
    counter_id = 0

    def __init__(self, title: str, author: str, year: int, genre: str):
        self.id = Book.counter_id
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        Book.counter_id +=1

    def __repr__(self):
        return f"id: {self.id}, title: {self.title}, author: {self.author}, release year: {self.year}, genre: {self.genre}"

