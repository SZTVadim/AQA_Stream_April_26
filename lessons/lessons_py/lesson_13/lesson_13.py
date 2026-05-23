from abc import ABC, abstractmethod


# Наследование
class Car(ABC):

    def __init__(self, model, brand, speed=0):
        self.model = model
        self.brand = brand
        self.speed = speed

    @abstractmethod
    def start_engine(self):
        """
        Абстрактный метод для запуска двигателя.
        Должен быть переопределён в подклассах.
        """
        return print("Что то тут происходит")

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
    def __init__(self, model, brand, battery_level, speed=0):
        super().__init__(model, brand, speed)
        self.battery_level = battery_level

    def start_engine(self):
        print("Электродвигатель запущен. Тихий старт!")

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Батарея заряжена до {self.battery_level}%")

    def display_info(self):
        print(f"Электромобиль: {self.brand} {self.model}, Скорость: {self.speed} км/ч, Заряд: {self.battery_level}%")


electric_car = ElectricCar("BMW", "X6", 100, 250)
print(electric_car.brand)
print(electric_car.model)
print(electric_car.speed)
electric_car.display_info()
print(electric_car.stop_engine())

# Полиморфизм
# Разные классы с одинаковым методом
class Собака:
    def звук(self):
        return "Гав-гав!"

class Кошка:
    def звук(self):
        return "Мяу!"

class Корова:
    def звук(self):
        return "Мууу!"