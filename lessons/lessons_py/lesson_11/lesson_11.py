# Классы в Python
variable = "test"


def my_func():
    return 1


class MyClassTest:
    test_text = "test_1"

    def my_func(self):
        self.test_text = "что-то другое"
        return self.test_text


test_class = MyClassTest()

print(test_class.test_text)
print(test_class.my_func())
print(test_class.test_text)


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self, age):
        print(f"я {self.name}, мне {age} лет")


person1 = Person("John")
print(person1.name)

person2 = Person("Kate")
print(person2.name)
person2.greeting(22)
