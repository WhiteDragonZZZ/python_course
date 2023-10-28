first_number = input("Введите первое число ")
second_number = input("Введите второе число ")
third_number = input("Введите третье число ")

if first_number > second_number:
    first_number, second_number = second_number, first_number
if second_number > third_number:
    second_number, third_number = third_number, second_number
if first_number > second_number:
    first_number, second_number = second_number, first_number
print(first_number, second_number, third_number)