text = "   Python - отличный язык для начинающих! Python мощный.   "

# 1. Уберите лишние пробелы
clean_text = text.strip()
# 2. Подсчитайте общее количество символов
total_chars = len(text)
# 3. Подсчитайте сколько раз встречается слово "Python"
python_count = text.count("Python")
# 4. Проверьте, начинается ли текст с "Python"
starts_with_python = text.startswith("Python")
# 5. Переведите текст в нижний регистр
lower_text = text.lower()


print(f"Очищенный текст: '{clean_text}'")
print(f"Всего символов: {total_chars}")
print(f"Слов 'Python' найдено: {python_count}")
print(f"Начинается с 'Python': {starts_with_python}")
print(f"В нижнем регистре: {lower_text}")

########################################################################

user_data = "ivanov:Иван:Петров:25:Москва"

# 1. Разбейте строку по разделителю ":"
username, first_name,last_name, age, city =  user_data.split(':')
# 2. Извлеките отдельные данные

print(f"Логин: {username}")
print(f"Имя: {first_name}")
print(f"Фамилия: {last_name}")
print(f"Возраст: {age}")
print(f"Город: {city}")

########################################################################

email = "  USER@EXAMPLE.COM  "

# 1. Уберите пробелы и переведите в нижний регистр
clean_email = email.strip()
clean_email = clean_email.lower()
# 2. Проверьте, содержит ли email символ "@"
has_at = True
has_at = clean_email.count("@")
# 3. Проверьте, заканчивается ли на ".com" или ".ru"
ends_with_com = True
ends_with_com = clean_email.endswith(".com")

ends_with_ru = True
ends_with_ru = clean_email.endswith(".ru")

print(f"Очищенный email: {clean_email}")
print(f"Содержит @: {has_at}")
print(f"Заканчивается на .com: {ends_with_com}")
print(f"Заканчивается на .ru: {ends_with_ru}")


####### 20.10 ########

##Task 1
full_name = "иванов иван иванович"
# Ожидаемый вывод: "Иванов И.И."
