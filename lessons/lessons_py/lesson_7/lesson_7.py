# Множества - коллекции уникальных элементов

# numbers = {"apple", "mango", "cherry", "banana"}
# numbers = {1, 22, 333, 341, 434, 4, 5}
# print(numbers)

# Добавление элементов
# fruits = {"яблоко", "банан"}
# fruits.add("апельсин")
# print(fruits)
#
# fruits.update(["груша", "виноград"])
# print(fruits)

# Удаление элементов
# fruits = {"яблоко", "банан", "апельсин"}
# fruits.discard("банан")
# fruits.discard(",fyfy")
# print(fruits)

# my_set = {"1", "2", "3", "4", "5"}
# my_set.remove("1")
# print(my_set)
# my_set.remove(6)  # Ошибка KyeError
# removed = my_set.pop()
# print(removed)

# Кортежи
# my_tuple = 1, 2, 3
# my_tuple_1 = (1, 2, 3)
# mixed_tuple = (1, "hello", 3.14, True)
# print(my_tuple)
# print(my_tuple_1)
# print(mixed_tuple)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_tuplle = tuple(my_list)
# print(type(my_tuplle))
# print(my_tuplle)

# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[-1])
# print(my_tuple[1:3])
# print(3 in my_tuple)
# print(33 in my_tuple)
# print(len(my_tuple))

# поиск и подсчет
# my_tuple = (1, 2, 3, 2, 1, 2)
# print(my_tuple.index(2))
# print(my_tuple.index(4))  # ValueError: tuple.index(x): x not in tuple
# print(my_tuple.count(2))
# print(my_tuple.count(4))

# объединение кортежей
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5)
# combined = tuple1 + tuple2
# print(combined)
# repeated = tuple2 * 4
# print(repeated)

# Распаковка кортежей
# point = (10, 20)
# x, y = point
# print(x)
# print(y)

# data = (1, 2, 3, 4, 5)
# first, *middle, last = data
# one, two, *_ = data
# print(first)
# print(middle)
# print(last)
# print(one)
# print(two)

# Генераторы кортежей (Tuple Comprehensions)

# my_generator = (x for x in range(5))
# my_tupple = tuple((x for x in range(5)))
# print(my_generator)
# print(my_tupple)
# print(next(my_generator))

# Кортежи из одного элемента
# not_tupple = (5)
# print(type(not_tupple))
#
# my_tupple = (5,)
# print(my_tupple)
# print(type(my_tupple))
#
# my_any_tupple = 5,
# print(my_any_tupple)
# print(type(my_any_tupple))
