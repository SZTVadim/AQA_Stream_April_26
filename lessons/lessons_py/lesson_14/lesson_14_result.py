#  "Toyota Camry", "A123BC", 5
# "Tesla Model 3", "E777EE", 4
# "Yamaha", "M001MM", True
# "Главная парковка", capacity=2
from lesson_14_bike import Bike
from lesson_14_car import Car
from lesson_14_parking import Parking

car1 = Car("Toyota Camry", "A123BC", 5)
car2 = Car("Tesla Model 3", "E777EE", 4)

bike1 = Bike("Yamaha", "M001MM", True)
parking1 = Parking("Главная парковка", 2)

parking1.park(car1)
parking1.park(car2)
print(parking1.park(bike1))
print(f"Всего припарковано: {parking1.get_parket_count()}")
print([car.__dict__ for car in parking1.get_vehicles()])
parking1.leave(car1)
print(f"Всего припарковано: {parking1.get_parket_count()}")
