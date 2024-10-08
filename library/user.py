class User:
    counter_id = 0

    def __init__(self, name: str, surname: str, phone: str):
        self.id = User.counter_id
        self.name = name
        self.surname = surname
        self.phone = phone
        User.counter_id +=1
