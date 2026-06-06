# Простой декоратор
import time
from dataclasses import dataclass


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Создаем тестового пользователя")
        func(*args, **kwargs)
        print("Удаляем тестового пользователя")

    return wrapper


@my_decorator
def my_test_func():
    print("Выполняем тесты")


# my_test_func()

# Декоратор с параметрами
def repeat(num: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(num=13)
def sum_int(*args):
    print(sum(args))


# sum_int(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,)
# Декораторы методов внутри класса

class Car:
    __car_count = 0  # Атрибут класса – общее количество машин

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.__car_count += 1

    @classmethod
    def from_string(cls, car_sting):
        brand, model = car_sting.split("-")
        return cls(brand, model)

    @property  # используется для методов которые просто что-то отдают (геттеры)
    def get_car_count(self):
        return self.__car_count

    @staticmethod
    def get_time():
        return datetime.datetime.now().strftime("%H:%M:%S")

    def __repr__(self):
        return f"Car(brand='{self.brand}', model='{self.model}')"

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return self.brand == other.brand and self.model == other.model


# Toyota-Corolla
car1 = Car("Toyota", "Corolla")
car2 = Car.from_string("Toyota-Corolla")
# print(Car.__car_count)
# print(car1.get_car_count) # проперти выхываются без круглых скобок

print(Car.get_time())
my_time = car1.get_time()  # Обращение к статичному методу
# print(my_time)

# Контекстный менеджер
with open("example.txt",
          "w") as my_file:  # Открываем файл и закрываем его после выхода из блока with ("w" это права для записи и чтения)
    my_file.write("Записали какие-то строки в наш тестовый файл")
# Если файла нет то он будет создан и запишет необходимые строки, а есои файл есть, то он перезапишет содержимое на нашу строку


print(car1)


# Датакласс
@dataclass
class CarNew:
    brand: str
    model: str


car_mew = CarNew("Toyota", "Corolla")
car_mew1 = CarNew("Toyota", "Corolla")
print(car_mew)
print(car_mew1 == car_mew)
