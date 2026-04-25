# Списки

# В списках можем хранить различные типы данных
# list_int = [1, 2, 3]
# list_str = ["улица 1", "улица 2", "улица 3"]
# list_bool = [False, True]
# list_list = [[1, 2, 4], ["a", "b", "c"]]
# list_obj = [{"age":25}, {"city":"SPB"}]


# Добавление элементов
# fruits = ["яблоко"]
# fruits.append("банан")
# print(fruits)
#
# fruits.extend(["груша", "апельсин"])
# print(fruits)
#
# fruits.insert(1, "виноград")
# print(fruits)

# Удаление элементов
# fruits = ["яблоко", "банан", "апельсин", "банан"]
# fruits.remove("банан")
# print(fruits)
# delete_fruit = fruits.pop()
# print(delete_fruit)
# print(fruits)

# Поиск элементов
# fruits = ["яблоко", "банан", "апельсин", "банан"]
# print(fruits.index("банан"))
# print(fruits.index("дыня"))  # Вызовет ошибку, так как нет данного элемента
# print(fruits.count("банан"))
#
# if "яблоко" in fruits:
#     print("Яблоко найдено")

# Сортировка и реверс
# numbers = [3, 1, 4, 1, 5, 9, 2]
# new_numbers = sorted(numbers, reverse=True)  # не изменяет исходный список
# print(numbers)
# print(new_numbers)
# numbers.sort()  # по возрастанию
# print(numbers)
# numbers.sort(reverse=True)  # по убыванию
# print(numbers)

# Минимум и максимум
# numbers = [3, 1, 4, 1, 5, 9, 2]
# print(min(numbers))  # 1
# print(max(numbers))  # 9
#
# words = ["яблоко", "банан", "апельсин", "аапельсин"]
# print(min(words))  # "апельсин" (по алфавиту)
# print(max(words))  # "яблоко"

# new_word = ["banana", "банан", "apple", "яблоко", "аапельсин"]
# print(min(new_word))
# print(max(new_word))

# Копирование списков
# original = [1, 2, 3]
# copy_1 = original.copy()
# copy_2 = original[:]
# original.append(4)
# print(original)
# print(id(original))
# print(copy_1)
# print(id(copy_1))
# print(copy_2)
# print(id(copy_2))
# print(copy_1 == copy_2)

# Сумма элементов списка
# numbers = [1, 2, 3, 4, 5.99]
# invalid_numbers = [1, 2, 3, "4", 5.99]
# print(sum(numbers))
# print(sum(invalid_numbers))  # вызовет ошибку, так как нельзя складывать число и строку

# Генераторы списков (List Comprehensions)
# squares = [x ** 2 for x in range(5)]
# print(squares)

# words = ["helLLo", "WORLDD", "Apple"]
# lower_words = [x.lower() for x in words]
# print(words)
# print(lower_words)

# text = "Привет!"
# print(len(text))
# print(type(len(text)))
# print(len(numbers))

# words = ["cat", "dog", "elephant", "ant", "tiger"]
# long_words = [word for word in words if len(word)>5]
# print(long_words)


# words_id_loop = []
# for x in words:
#     if len(x) > 5:
#         words_id_loop.append(x.lower())
#         print(words_id_loop)

# numbers = [-2, -1, 0, 1, 2]
# result = [x**2 if x > 0 else 0 for x in numbers]
# print(result)
