

class User:

    def __init__(self, name: str, surname: str, age: int, address: str, username: str, password: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.username = username
        self.password = password

    def __str__(self):
        return  f"{self.name}, {self.surname}, {self.age}, {self.address},{self.username},{self.password}"




