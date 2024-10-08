class User:
    counter_id = 0

    def __init__(self, name: str, surname: str, phone: str):
        self.id = User.counter_id
        self.name = name
        self.surname = surname
        self.phone = phone
        User.counter_id +=1

    def __repr__(self):
        return f"id: {self.id} name: {self.name} surname: {self.surname} phone: {self.phone}"
