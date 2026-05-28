# 1) Создайте абстрактный класс `Vehicle`, 
# который должен принимать аргументы name, plate_number

#   - добавьте абстрактный метод `move()`, который должен описывать,
#     как транспортное средство перемещается;
from abc import abstractmethod

class Vehicle:
    def __init__(self, name: str, plate_number: str):
        self.name = name
        self.plate_number = plate_number

    @abstractmethod   
    def move(self):
        """Транспортное средство едет прямо по главной дороге"""
        pass

#    - добавьте обычный метод `info()`, который возвращает строку
#  с названием транспорта и его номером (госномер).

    def info(self):
        return f'{self.name}, {self.plate_number}' 
    

