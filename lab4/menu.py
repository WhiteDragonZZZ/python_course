from lab4.models import User

# user = User(name="dds", surname="fkjdj", age=15, address="ssdjk", username="dsks", password="dkjskjsdk")
#
# name = str(input("Напишите имя"))
# surname = str(input("Напишите surname"))
# age = int(input("Напишите age"))
# address = str(input("Напишите address"))
# username = str(input("Напишите username"))
# password = str(input("Напишите password"))
#
# user2 = User(name=name, surname=surname, age=age, address=address, username=username, password=password)

users: list[User] = []

def create_user():
    name = str(input("Напишите имя:"))
    surname = str(input("Напишите surname:"))
    age = int(input("Напишите age:"))
    address = str(input("Напишите address:"))
    username = str(input("Напишите username:"))
    password = str(input("Напишите password:"))

    user = User(name=name, surname=surname, age=age, address=address, username=username, password=password)

    users.append(user)
    print("User is added")

def show_users():
    for user in users:
        print(user)

def delete_user(username: str):
    for user in users:
        if user.username ==username:
            users.remove(user)
# def delete_user():
#     user =
def authorization(email:str,password:str):
    for user in users:
        if user.surname==email and user.password==password:
            print("Connect!")
        elif user.surname==email and user.password!=password:
            print("Password error")
        elif user.surname!=email and user.password==password:
            print("email error")

print('''Выберите пункт меню :
1 - информация о всех пользователях ")
2 - добавить нового пользователя ")
3 - Авторизация
4 - Удаление пользователя
5 - Выход
''')

while True:
    menu = input('Введите пункт меню >>> ')
    if menu == '1':
        show_users()

    elif menu == '2':
        create_user()

    elif menu== '3':
        surname = str(input("Напишите surname:"))
        password = str(input("Напишите password:"))
        authorization(surname,password)

    elif menu=='4':
        username = str(input("Напишите username:"))
        delete_user(username)

    elif menu == '5':
        raise SystemExit

    else:
        print('Не существующий пункт')
