shopping_list = ["хлеб", "молоко"]

# Добавление
shopping_list.append("сыр")        # в конец
shopping_list.insert(1, "яблоки")  # на позицию

# Удаление
shopping_list.remove("молоко")     # по значению
shopping_list.pop(0)               # по индексу


stack = []

# Добавляем элементы (push)
stack.append("тарелка1")  # низ стека
stack.append("тарелка2")
stack.append("тарелка3")  # верх стека
print(stack)  # ['тарелка1', 'тарелка2', 'тарелка3']

# Удаляем элементы (pop) - всегда с КОНЦА!
last_item = stack.pop()
print(last_item)  # 'тарелка3'
print(stack)      # ['тарелка1', 'тарелка2']

######task 1
numbers = [10, 20, 30]
# 1. Добавьте число 40 в конец
numbers.append(40)
print(numbers)
# 2. Удалите число 20
numbers.remove(20)
print(numbers)
# 3. Вставьте число 5 на начало списка
numbers.insert(0,5)
# Выведите результат
print(numbers)

#######кортеж 

# Создание
person = ("Анна", 25, "инженер")

# Чтение - можно
name = person[0]        # "Анна"
age = person[1]         # 25
print(person)
print(name)
print(age)
#person[1] = 26        # ОШИБКА!



#######множество 

students_math = {"Аня", "Боря", "Вова"}
students_physics = {"Боря", "Галя", "Дима"}

# Объединение
all_students = students_math | students_physics
# {"Аня", "Боря", "Вова", "Галя", "Дима"}

# Пересечение
both_subjects = students_math & students_physics
# {"Боря"}

# Добавление
students_math.add("Зоя")

#task 2
# Дано:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Найдите:
# 1. Общие элементы (пересечение)
print(set1 & set2)

# 2. Все уникальные элементы (объединение)
print(set1 | set2)

# 3. Элементы, которые есть в set1, но нет в set2
print(set1 - set2)


######Очень часто приходится...
##data_structures = dataset.load()

#for structure in data_structures:
#    if isinstance(structure, list):
#        print("Это список!")
#    elif isinstance(structure, tuple):
#        print("Это кортеж!")
#    elif isinstance(structure, set):
#        print("Это множество!")


#Task 3
#Создайте программу, которая раскидывает элементы по типам в разные списки, 
# т.е. создает отдельные списки для: int, str, list, tuple
#Целые числа: [1, 42, 0]
#Строки: ['hello', 'world']
#Списки: [[1, 2]]
#Кортежи: [(5, 6)]
#Дробные числа: [3.14]
mixed_data = [
    1, 
    "hello", 
    3.14, 
    [1, 2], 
    42, 
    "world", 
    0, 
    (5, 6),
    {"name": "John"},
    True,
    {7, 8, 9}
]
int_data = []
str_data = []
list_data = []
turple_data = []
float_data = []
set_data = []
bool_data = []

for data in mixed_data:
    if isinstance(data, list):
        list_data.append(data)
    elif isinstance(data, bool):
        bool_data.append(data)    
    elif isinstance(data, tuple):
        turple_data.append(data)
    elif isinstance(data, set):
        set_data.append(data)
    elif isinstance(data, float):
        float_data.append(data)
    elif isinstance(data, str):
        str_data.append(data)
    elif isinstance(data, int):
        int_data.append(data)
    

print(f"Целые числа:{int_data}")
print(f"Строки::{str_data}")
print(f"Списки:{list_data}")
print(f"Кортежи:{turple_data}")
print(f"Дробные числа:{float_data}")


    





