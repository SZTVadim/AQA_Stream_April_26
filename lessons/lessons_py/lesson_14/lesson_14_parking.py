#    - класс Parking и в `__init__` принимайте `name` (название парковки) и `capacity`
    #  (максимальное количество машин);
from lesson_14 import Vehicle

class Parking:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.__slots: list = []

#    - создайте метод `park(vehicle)`, который:
    #    * добавляет транспорт на парковку, если есть свободные места;
    #    * возвращает `True`, если машина успешно припаркована,
        #  иначе `False`;

    def park(self, vehicle: Vehicle):
        if  len(self.__slots) < self.capacity:
            self.__slots.append(vehicle)
            return True
        else:
            return False
        
    #    - создайте метод `leave(vehicle)`, который удаляет транспорт
    #  с парковки, если он там был;
    def leave(self, vehicle: Vehicle):
        if vehicle in self.__slots:
            self.__slots.remove(vehicle)
        
    #    - создайте метод `get_parked_count()` — возвращает количество
    #  припаркованных машин.
    def get_parket_count(self):
        return len(self.__slots)
    
    def get_vehicles(self):
        return tuple(self.__slots)
                