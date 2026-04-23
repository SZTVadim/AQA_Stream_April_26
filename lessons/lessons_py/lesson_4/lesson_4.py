# sum_first = 3 + "5" # получим ошибку TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(sum_first)

sum_second = 3 + int("5")
print(sum_second)

first_text = "Hello"
print(id(first_text))
first_text = "World"
print(id(first_text))

# Основные операции со строками - Преобразование регистра
any_text = " Какой-то тEкст, Для примера "
second_any_text = any_text.lower()
print(any_text)
print(second_any_text)
print(any_text.capitalize())
print(any_text.upper())
print(any_text.lower())
print(any_text.title())

# Основные операции со строками - Удаление пробелов
print(any_text)
print(any_text.strip())
print(any_text.lstrip())
print(any_text.rstrip())
clean_synbol = "%My text'"
print(clean_synbol.strip("'%"))
print(clean_synbol.lstrip("%"))
print(clean_synbol.rstrip("'"))

# Основные операции со строками - Разделение и объединение строк
text_for_list = "один:два:три:четыре или пять:шесть"
print(text_for_list)
list_from_string = text_for_list.split(":")
print(list_from_string)
new_text_from_list = " ".join(list_from_string)
print(new_text_from_list)

# Основные операции со строками - Замена подстрок

text_replace = "Я люблю Java. Java - это круто!"
new_text_replace = text_replace.replace("Java", "Python")
print(new_text_replace)

# Основные операции со строками - Поиск и подсчет

text_search = "Python программирование на Python"
print(text_search.find("Python"))
print(text_search.find("Java"))
print(text_search.count("Python"))
print(text_search.index("Python"))
print(text_search.index("Java"))  # Получим ошибку, так как ничего не найдено

# Основные операции со строками - Проверка типа символов
print("hello".isalpha())
print("hello1".isalpha())
print("123".isdigit())
print("Hello123".isalnum())
print("Hello123 ".isalnum())
print("   ".isspace())
print("".isspace())

# Основные операции со строками - Срезы строк
text_by_srez = "Инкапсуляция и полиморфизм"
print(text_by_srez[7:])
print(text_by_srez[:7])
print(text_by_srez[5:20])
print(text_by_srez[5:20:3])

# Переворот текста
print(text_by_srez[::-1])

# Основные операции со строками - Экранирование символов
text_screen = "\tPython \n\"программирование\" на Python"
print(text_screen)

# Основные операции со строками - Тройные кавычки(многострочный комментарй)
text = """Это
многострочный
текст"""
print(text)