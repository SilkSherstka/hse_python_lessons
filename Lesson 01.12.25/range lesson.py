# Вывести "Hello" 5 раз
for i in range(5):
    print("Hello")
######################################################

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

######################################################

students = ["Анна", "Борис", "Виктория", "Григорий"]
grades = [85, 92, 78, 96]

print("Результаты экзамена:")
for i in range(len(students)):
    print(f"{students[i]}: {grades[i]} баллов")

######################################################

products = ["Ноутбук", "Мышь", "Клавиатура", "Монитор"]
prices = [50000, 2500, 4000, 30000]
quantities = [10, 50, 30, 15]
total_revenue = 0

for i in range(len(products)):
    total_value = prices[i] * quantities[i]
    total_revenue += total_value
    print(f"{products[i]}: {total_value} руб.")

print(f"\nОбщая выручка: {total_revenue} руб.")

######################################################

cities = ["Москва", "Санкт-Петербург", "Новосибирск"]
temperatures = [15, 12, 8]
updates = [2, -1, 3]  # Изменения температуры
for i in range(len(cities)):
    old_temp = temperatures[i]
    new_temp = old_temp + updates[i]
    print(f"{cities[i]}: {old_temp}°C → {new_temp}°C")

#Создайте списки с помощью list(range()):

#Числа от 0 до 9
print(list(range(10)))
#Четные числа от 2 до 20
print(list(range(2,21,2)))
#Числа от 10 до 1 в обратном порядке
print(list(range(10,0,-1)))

#Дан список слов. Найдите все слова, содержащие букву 'а', и замените их на "FOUND"

words = ["apple", "banana", "cherry", "date", "fig", "grape"]

for i in range(len(words)):
    print(f"{words[i].replace('a', 'FOUND')}")


#У вас есть данные о продажах: товары, цены и количество проданных единиц
products = ["Ноутбук", "Мышь", "Клавиатура", "Монитор"]
prices = [50000, 2500, 4000, 30000]
quantities = [8, 45, 25, 12]
#Рассчитайте общую выручку по каждому товару 
total_revenue_by_product = [0,0,0,0]

for i in range(len(total_revenue_by_product)):
    total_revenue_by_product[i] = prices[i] * quantities[i]
    print(f"{products[i]}: {total_revenue_by_product[i]} руб.")
# и найдите товар с максимальной выручкой
print(f"Товар с максимальной выручкой: {max(total_revenue_by_product)} руб.")

######################################################
products = ["Телефон", "Планшет", "Ноутбук", "Наушники"]
prices = [30000, 45000, 80000, 15000]
stock = [15, 8, 5, 20]
discounts = [10, 15, 20, 5]  # Скидки в процентах
#В интернет-магазине нужно применить 
# скидки к товарам, 
cost_after_discount = [0,0,0,0]

for i in range(len(cost_after_discount)):
    cost_after_discount[i] = prices[i] - prices[i]*discounts[i]/100
    print(f"{products[i]}: {cost_after_discount[i]} руб.")
# обновить цены и пересчитать остатки (просто вывести значение stock по индексу)
for i in range(len(stock)):
    print(f"{products[i]}: {stock[i]} шт.")

############## enumerate ##############
students = ["Анна", "Борис", "Виктория", "Григорий"]

print("Список студентов:")
for number, student in enumerate(students, start=1):
    print(f"{number}. {student}")

############################
fruits = ["apple", "banana", "cherry"]
print("Фрукты в корзине:")
# выведите 1. apple и т.д.
for number, fruits in enumerate(fruits, start=1):
    print(f"{number}. {fruits}")

############## list comprehension ##############
fruits = ["apple", "banana", "cherry"]
print("Фрукты в корзине:")
# выведите 1. apple и т.д.
for number, fruits in enumerate(fruits, start=1):
    print(f"{number}. {fruits}")

#for word in words:
#    lower_words.append(word.lower())

words = [word.lower() for word in words]
print(words)

"""
Пример 1
"""
example = []

for x in range(5):
    x = x**2
    example.append(x)

#example = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
print(example)

"""
Пример 2
"""
another_example = []

for x in range(10):
    if x % 2 == 0:
        another_example.append(x)

#another_example = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
print(another_example)

"""
Пример 3
"""
words_example = []

for word in ["hello", "world"]:
    words_example.append(word.upper())

#words_example = [word.upper() for word in ["hello", "world"]]  # ['HELLO', 'WORLD']
print(words_example)


############################ expression for item in iterable if condition]

############################
#Создайте список четных чисел от 0 до 20 двумя способами

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

nums = [x for x in range(21) if x % 2 == 0]
print(nums)

#Создайте список слов длиннее 4 символов с list comprehension

words = ["cat", "elephant", "dog", "butterfly", "ox"]
long_words = [word for word in words if len(word) > 4]

print(long_words)
