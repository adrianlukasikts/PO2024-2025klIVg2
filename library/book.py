class Book:
    def __init__(self, id: int, title: str, author: str, year: int, genre: str):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __repr__(self):
        return f"id: {self.id}, title: {self.title}, author: {self.author}, release year: {self.year}, genre: {self.genre}"

