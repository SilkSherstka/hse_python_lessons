numbers = [2, 4, 6, 8, 10]
i = 0

for num in numbers:
    i += num

print(i)
print(sum([2, 4, 6, 8, 10]))

#########################################
words = ["apple", "banana", "cherry"]
for word in words:
    print(len(word))

#########################################
#Дана строка text = "Python". Выведите каждый символ строки и его порядковый номер (начиная с 1) # Символ 1: P
text = "Python"
i = 0

for letter in text:
    print(f"Символ {i+1}: {text[i]}")
    i=i+1

#########################################
#Дан список чисел [3, 7, 2, 9, 5]. Умножьте каждый элемент на 2 и выведите результат
numsers = [3, 7, 2, 9, 5]
for num in numsers:
    print(num*2)

#########################################
#Дан список ["cat", "elephant", "dog", "butterfly"]. Выведите на экран слова, длина которых больше 3 букв
animals = ["cat", "elephant", "dog", "butterfly"]
for word in animals:
    if len(word)>3:
        print(word)


#########################################
#Дан кортеж ("Иванов", "Иван", "Иванович"). Приведите к нижнему регистру каждое слово и выведите на экран
name = ("Иванов", "Иван", "Иванович")
for word in name:
    print(word.lower())
