lessonNumber = int(input("Введите номер урока "))

hour = lessonNumber * 45 + ((lessonNumber + 1) // 2 - 1 + (lessonNumber + 1) % 2) * 5 + (
            lessonNumber // 2 - 1 + lessonNumber % 2) * 15
minutes = hour % 60

print('%d %d' % (hour // 60 + 9, minutes % 60))
