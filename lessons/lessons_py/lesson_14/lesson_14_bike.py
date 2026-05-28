from lesson_14 import Vehicle

class Bike(Vehicle):
    def __init__(self, name: str, plate_number: str, has_engine: bool):
        super().__init__(name, plate_number)
        self.has_engine = has_engine

        #    - реализуйте метод `move()` — возвращает строку вида:
    #  `"{info} едет по велодорожке"`
    def move(self):
        return f"{self.info()} едет по велодорожке"