# Распаковка
# распаковка словарей
def my_func(name, age, size_jacket):
    print(f'{name} is {age} years old, and size: {size_jacket}')


def data_person():
    return {"name": "Vasya", "age": 30, "size_jacket": 50}


my_func(**data_person())


# *args и **kwargs

def summ_data(*args):
    return sum(args)


my_list = list(range(1, 101))
print(summ_data(*my_list))


# Позиционые аргументы
def args_func(one: int, two: str, three):
    return f"one: {one} + two: {two} + three: {three}"


one = 1
two = "2"
three = 3
print(args_func("2", 3, 1))
print(args_func(two=two, three=three, one=one))
print(args_func(two=two, three=three, one=one))


def process_data(*args, **kwargs):
    print("Позиционные аргументы:", args)
    print("Именованные аргументы:", kwargs)
    print(f"Всего позиционных: {len(args)}")
    print(f"Всего именованных: {len(kwargs)}")


process_data(1, 2, 3, name="Иван", age=20, city="Москва")
