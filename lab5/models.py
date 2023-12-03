class Person:
    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age = age

    def __str__(self):
        return f"{self.fullname}"


class Driver(Person):
    def __init__(self, fullname, age, experience):
        Person.__init__(self, fullname=fullname, age=age)
        self.experience = experience

    def __str__(self):
        return f"{self.fullname}+{self.experience}"


class Engine:
    def __init__(self, power, company):
        self.power = power
        self.company = company

    def __str__(self):
        return f"{self.power} {self.company}"


class Car(Driver, Engine):

    def __init__(self, carClass, marka, fullname, age, experience, power, company):
        Driver.__init__(self, fullname=fullname, age=age, experience=experience)
        Engine.__init__(self, power=power, company=company)
        self.carClass = carClass
        self.marka = marka

    def start(self):
        return "Поехали"

    def stop(self):
        return "Остановитесь!"

    def turn_right(self):
        return "Направоо"

    def turn_left(self):
        return "Налевоо"

    def __str__(self):
        return f"Марка:{self.marka}  Класс:{self.carClass} Вес:{self.power} Водитель:{self.fullname} Стаж:{self.experience} Производитель: {self.company}"


class Lorry(Car):
    def __init__(self, carClass, marka, fullname, age, experience, power, company, carrying):
        Car.__init__(self, carClass=carClass, marka=marka, fullname=fullname, age=age, experience=experience,
                     power=power, company=company)
        self.carrying = carrying

    def __str__(self):
        return f"{super().__str__()} Грузоподъемность:{self.carrying}"


class SportCar(Car):
    def __init__(self, carClass, marka, fullname, age, experience, power, company, speed):
        Car.__init__(self, carClass=carClass, marka=marka, fullname=fullname, age=age, experience=experience,
                     power=power, company=company)
        self.speed = speed

    def __str__(self):
        return f"{super().__str__()} Скорость{self.speed}"
