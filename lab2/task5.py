first_number = input("Введите первое число ")
second_number = input("Введите второе число ")
third_number = input("Введите третье число ")

if first_number==second_number and first_number==third_number:
    print(3)
elif first_number==second_number or second_number==third_number or third_number==first_number:
    print(2)
else:
    print(0)