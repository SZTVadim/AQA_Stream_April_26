a = [1, 2, 3]
print(id(a))
b = a
print(id(b))
b.append(4)
print(a)
print(b)

# Проверка типа данных
c = 1
e = 1.1
d = ""

print(type(d))
print(type(c))
print(type(e))
print(type(a))
print(type(b))

# Арифметические операторы:
int_1 = 2
int_2 = 10
int_3 = 3
int_4 = 3

print(int_1 ** int_2)
print(int_2 // int_3)
print(int_2 % int_3)
print(int_2 % int_1)

#  операторы сравнения:
print(int_1 >= int_2)
print(int_1 <= int_2)
print(int_1 == int_2)
print(int_3 == int_4)
print(int_3 != int_4)

# Операторы присваивания
int_1 += 10  # эквивалентно int_1 = int_1 + 10
print(int_1)
int_1 -= 10  # эквивалентно int_1 = int_1 - 10
print(int_1)

# Логические операторы
# and
if 1 and 2 in a:
    print(True)
else:
    print(False)

if 1 and 4 in a:
    print(True)
else:
    print(False)
# or
if 1 or 4 in a:
    print(True)
else:
    print(False)

if "a" and 4 in a:
    print(True)
else:
    print(False)

text = "apple"
print("=" * 30)
print("ap" in text)
print("appp" in text)
print("appp" not in text)

# Тождественные операторы
c = [1, 2, 3]
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(a is c)


# длинная строка длинная строкадлинная строкадлинная строкадлинная строкадлинная строкадлинная строкадлинная строка.

def my_funt():
    """Это
    пример
    многострочного
    комментария"""
    pass
