print("Добро пожаловать,вы заполняете анкету")
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
birthday_date = input("Введите ваш год рождения: ")
status_course = input("Нравится ли вам курс? ")
course_future = input("Что вы ожидаете в дальнейших занятиях? ")
print("Вы заполнили такие данные:")

full_age = 2023-int(birthday_date)

print(f"Ваще зовут {name} {surname}")
print(f"Вам {full_age} лет")
print(f"Вам ответ к первому вопросу: {status_course}")
print(f"Ваш ответ к второму вопросу: {course_future}")

