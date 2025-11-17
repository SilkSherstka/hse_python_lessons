#Напишите цикл while, который выводит числа от 1 до 5
i = 1
while i < 6:
    print(i)
    i=i+1

#Напишите цикл, который принимает на вход любое слово и делит его на буквы 
# (и выводит список букв на экран), цикл остановится, если пользователь ввёл “стоп”

while True:
    word = input()

    if word == "stop":
        break

    print(list(word))

#Задача: Реализуйте механизм входа с 3 попытками

correct_password = "secret123"
logged_in = False
attempts = 0
max_attempts = 3

while logged_in == False and attempts < max_attempts:
    user_input = input("Введите пароль:")
    attempts = attempts + 1
    if user_input == correct_password:
        logged_in = True
        attempts = 0
        print("You are in")
    else:
        print("incorrect password")
    if attempts == max_attempts:
        print("too many attempts")


