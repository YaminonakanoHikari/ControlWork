# Инкапсуляция.Задание №1
class Persоn:
    def __init__(self, age=0):
        self.set_age(age)  # Проверка через метод

    def set_age(self, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        self.__age = age

    def get_age(self):
        return self.__age


# Пример использования
try:
    p = Persоn()
    p.set_age(25)
    print(p.get_age())  # Вывод: 25

    p.set_age(-5)  # Попытка установить отрицательный возраст
except ValueError as e:
    print("Ошибка:", e)

print(p.get_age())  # 25, значение не изменилось


#Наследование.Задание №2
class Animаl:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal" # Хотела написать я животное и разговаривать не умею, но рисковать не хочется


class Dog(Animаl):
    def speak(self):
        return "Woof"


class Сat(Animаl):
    def speak(self):
        return "Meow"


# Пример использования
dog = Dog("Buddy")
cat = Сat("Kitty")

print(dog.name, dog.speak())  # Buddy Woof
print(cat.name, cat.speak())  # Kitty Meow

#Полиморфизм.Задание №3
class Vehiclе:
    def move(self):
        return "Vehicle is moving"

class Car(Vehiclе):
    def move(self):
        return "Car is driving"

class Bicyclе(Vehiclе):
    def move(self):
        return "Bicycle is pedaling"

# Функция полиморфизма
def move(vehicle):
    # Проверяем, есть ли у объекта метод move
    if hasattr(vehicle, "move"):
        return vehicle.move()
    else:
        return "This object cannot move"


# Пример использования
car = Car()
bike = Bicyclе()

print(move(car))  # Car is driving
print(move(bike)) # Bicycle is pedaling

# Абстракция.Задание №4
from abc import ABC, abstractmethod
import math

class Shаpe(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Rectаngle(Shаpe):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Прямоугольник площадью {self.area()}"


class Сircle(Shаpe):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2)

    def __str__(self):
        return f"Круг площадью {self.area()}"


# Пример использования
rect = Rectаngle(10, 5)
circle = Сircle(7)

print(rect)   # Прямоугольник площадью 50
print(circle) # Круг площадью 154

