# Функции и условные контрукции в Python
a = 1


def circle_area(radius):
    pi = 3.14
    result = pi * radius * radius
    return result
    result += result  # Эта строка не будет выполняться, так как она после return


my_text = ("ОПЕРАТОР RETURN ИСПОЛЬЗУЕТСЯ ДЛЯ ВОЗВРАТА РЕЗУЛЬТАТА ИЗ ФУНКЦИИ В ОСНОВНУЮ ПРОГРАММУ. ПОСЛЕ ВЫПОЛНЕНИЯ "
           "RETURN ФУНКЦИЯ ЗАВЕРШАЕТ СВОЮ РАБОТУ И ПЕРЕДАЁТ ЗНАЧЕНИЕ ВЫЗЫВАЮЩЕМУ КОДУ")


def lower_text(text):
    return text.lower()


# print(lower_text(my_text))

variable = circle_area(5)


# print(variable)


def greeting(age=None, city=None, name=None):
    if age is not None:
        print(f"мне {age} лет")
    if city:
        print(f"я из города {city}")
    if name:
        print(f"Hello, {name}!")


# greeting(name="Вася")
# greeting(25, "Omsk", "Petya")
# greeting()
x = None
if not x:
    print()

# Условия

# y = 19
# if y % 2 == 0:
#     print(f"{y} четное")
# else:
#     print(f"{y} не четное")

# if-elif-else
# b = 0
# if b > 0:
#     print("положительное")
# elif b < 0:
#     print("отрицательное")
# else:
#     print("ноль")

# Задача из собеса
my_list = list(range(1, 100))


# если кратно 3 то пишет fuzz
# если кратно 5 то пишет buzz
# если кратно 3 и 5 то пишет fuzzbuzz
# в противном случае просто выподим число
# list_result = []
#
# for num in my_list:
#     if num % 3 == 0 and num % 5 == 0:
#         list_result.append("FuzzBuzz")
#     elif num % 3 == 0:
#         list_result.append("Fuzz")
#     elif num % 5 == 0:
#         list_result.append("Buzz")
#     else:
#         list_result.append(num)

# print(list_result)

# Функция + условия
def check_temperature(temp):
    if temp < 0:
        return "Мороз"
    elif temp < 20:
        return "Прохаладно"
    elif temp < 30:
        return "Тепло"
    else:
        return "Жарко"


# print(check_temperature(-10))
# print(check_temperature(12))
# print(check_temperature(20))
# print(check_temperature(50))

# match / case
# command = "stopp"
# match command:
#     case "start":
#         print("Стартуем")
#     case "stop":
#         print("Останавливаем")
#     case "pause":
#         print("Пауза")
#     case _:
#         print("Неизвестная команда")


# Цикл while
# number = -11
# while number <5:
#     print(f"number= {number}")
#     number += 1

# while True:
#     number = int(input("Введите чсисло: "))
#     if number == 5:
#         print("Вы угадали")
#         break

# message = "Hello"
# for c in message:
#     print(c)
# else:
#     print(f"Последний символ: {c}. Цикл завершен")
# print("Работа программы завершена")

# Анонимные функции (lambda)
def square(num):
    return num ** 2


square_num = lambda x: x ** 2
print(square_num(5))
