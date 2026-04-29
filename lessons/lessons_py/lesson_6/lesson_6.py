# Что такое словари (dictionaries)
my_list = [1, 2, 3, 4, 5]
print(my_list[0])

student = {
    "name": "Ivan",
    "age": 21,
    "is_teacher": False,
    "is_student": True,
    "address": {
        "city": "Saratov",
        "country": "Russia"
    }
}
print(student["name"])
print(student["is_teacher"])
print(student["address"]["city"])

for key in student:
    """Перебираем значения по ключам"""
    print(key)

address = student["address"]

for value in student.values():
    """Перебираем по values"""
    print(value)

print(student.values())
print(student.keys())
print(student.items())
for key, value in student.items():
    """Перебираем пары key, values"""
    print(value)

# Удаление элементов
student_new = {"имя": "Иван", "возраст": 20, "курс": 2}

del student_new["имя"]
print(student_new)
age = student_new.pop("возраст")
print(age)
print(student_new)

# Генераторы словарей (Dictionary Comprehensions)
# Создание словаря из списка:
squares_dict = {f"элемент_{x}": x ** 2 for x in range(1,4)}
print(squares_dict)

# Фильтрация элементов:
even_squares = {f"элемент_{x}": x ** 3 for x in range(2,6) if x % 2 == 0}
# even_squares = {f"элемент_{x}": x ** 3 for x in range(2,6)}
print(even_squares)

# Преобразование строкового ключа:
words = ["apple", "banana", "cherry"]
length_dict = {word: len(word) for word in words}
print(length_dict)

# Объединение словарей
dict1 = {'элемент_1': 1, 'элемент_2': 4, 'элемент_3': 9}
dict2 = {'элемент_2': 8, 'элемент_4': 64}
dict1.update(dict2)
print(dict1)


users = {[
    {
        "id": 1,
        "name": "Анна",
        "is_admin": None,
        "profile": {
            "city": "Москва",
            "skills": ["Python", "pytest"],
            "settings": [{
                "theme": "dark",
                "notifications": True,
            }],
        },
    },
    {
        "id": 2,
        "name": "Борис",
        "is_admin": True,
        "profile": {
            "city": ["Казань", "СПБ", "Москва"],
            "skills": ["Java", "Selenium"],
            "settings": {
                "theme": "light",
                "notifications": False,
            },
        },
    },
]}
# Имя первого пользователя
name_first_person = users[0]["name"]
print(name_first_person)
print(users[0]["profile"]["settings"][0]["theme"])
print(users[1]["profile"]["city"][1])
