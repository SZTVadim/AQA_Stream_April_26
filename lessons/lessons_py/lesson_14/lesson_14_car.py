from lesson_14 import Vehicle

class Car(Vehicle):
    def __init__(self, name: str, plate_number: str, seats: int):
        super().__init__(name, plate_number)
        self.seats = seats

        #    - реализуйте метод `move()` — возвращает строку вида:
    #  `"{info} едет по дороге"`
    def move(self):
        return f"{self.info()} едет по дороге"

