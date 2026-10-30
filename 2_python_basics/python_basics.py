import keyword
import random

a = "змінна з текстом"
a1 = "a"
b = 1
b1 = 1.1
c = ["a", 1, 1.25, "Слово", a]
d = {"a": "Слово", "b": 1, a: b}
e = ("a", a)
f = {"ss", a + str(b)}

print("Типи даних:")
print("str:", a, type(a).__name__)
print("int:", b, type(b).__name__)
print("float:", b1, type(b1).__name__)
print("list:", c)
print("dict:", d)
print("tuple:", e)
print("set:", f)

print("\nКонстанти Python:")
print("True:", True)
print("None:", None)
print("NotImplemented:", NotImplemented)

print("\nЗарезервовані слова:")
print(", ".join(keyword.kwlist[:15]) + ", ...")

print("\nВбудовані функції:")
print(abs(-12.5), abs(-12.5) == abs(12.5))
print("len(c) =", len(c))
print("repr(a) =", repr(a))

print("\nЦикл for:")
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(f"На позиції {index} знаходиться буква {letter}")

print("\nЦикл while:")
counter = 3
while counter > 0:
    print("Зворотній відлік:", counter)
    counter -= 1

print("\nРозгалуження:")
random_value = random.randint(0, 1)
if random_value == 1:
    print("Випало 1: умова виконана.")
else:
    print(f"Випало {random_value}: умова не виконана.")

print("\ntry / except / finally:")
try:
    result = 10 / 0
except ZeroDivisionError as error:
    print("Перехоплена помилка:", error)
finally:
    print("Блок finally завжди виконується.")

print("\nКонтекстний менеджер with:")
with open("python_basics.py", "r", encoding="utf-8") as source_file:
    first_line = source_file.readline().strip()
    print("Перша строка файла:", first_line)

print("\nЛямбда-функція:")
square = lambda value: value ** 2
numbers = [1, 2, 3, 4]
squared_numbers = list(map(square, numbers))
print("Квадрати чисел:", squared_numbers)
