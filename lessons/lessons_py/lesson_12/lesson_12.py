# ООП
# Абстракция
from abc import ABC, abstractmethod

var = 1


class Car(ABC):
    def __init__(self, model, year):
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self):
        """
        Абстрактный метод для запуска двигателя.
        Должен быть переопределён в подклассах.
        """
        pass

    def stop_engine(self):
        """
        Обычный метод (не абстрактный) — его можно переопределить,
        но не обязательно. По умолчанию двигатель просто останавливается.
        """
        return "Двигатель остановлен."


class GasolineCar(Car):
    def start_engine(self):
        return "Бензиновый двигатель запущен. Громкий рёв!"


# gas_car = GasolineCar()
# print(gas_car.start_engine())
# print(gas_car.stop_engine())


class ElectricCar(Car):
    def __init__(self, model, year, battery_level):
        super().__init__(model, year)
        self.battery_level = battery_level

    def start_engine(self):
        print("Электродвигатель запущен. Тихий старт!")

electric_car = ElectricCar("BMW", 4, 100)
print(electric_car.year)
print(electric_car.model)

# Инкапсуляция
class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            "Недостаточно денег"

    def check_balance(self):
        return self.__balance


# vasya = Bank(100)
# print(vasya.check_balance())
# vasya.withdraw(55)
# print(vasya.check_balance())
