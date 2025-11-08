"""
Задачи на логические операции
"""


"""
Задача 1: Система авторизации для NLP-платформы

Контекст: Вы разрабатываете систему доступа к AI-моделям. Нужно проверить, может ли пользователь использовать модель

Инструкция: Заполните пропуски, используя логические операторы
"""
# Данные пользователя
user_role = "admin"
has_api_key = True
model_available = True
request_count_today = 95
daily_limit = 100

# ЗАДАНИЕ: Напишите условие доступа
# Пользователь имеет доступ если:
# - он администратор ИЛИ у него есть API-ключ
# - И модель доступна
# - И не превышен дневной лимит запросов

print((user_role == "admin" or has_api_key == True) and model_available == True and request_count_today < daily_limit)

"""
Дополнение к материалу: Приоритет операторов
"""

# Приоритет: NOT -> AND -> OR
result1 = not True and False    # False and False = False
result2 = not (True and False)  # not False = True

# Используйте скобки для ясности!
#complex_condition = (a > b) and (c < d) or (e == f)


"""
Задача 2: Валидатор текста для обработки

Контекст: Перед отправкой текста в NLP-модель нужно проверить его качество

Инструкция: Реализуйте проверки текста
"""

text = "Привет! Как дела?"
banned_words = ["мат", "оскорбление", "спам", "реклама"]

# ЗАДАНИЕ: Соберите финальную проверку
# Текст валиден если:
# - длина от 1 до 1000 символов
# - И не содержит запрещенных слов
# - И НЕ состоит только из английских символов

# Проверки (проверка мата и англоязычного текста написана, нужно реализовать логику)
contains_banned_words = any(word in text.lower() for word in banned_words)
is_english_only = all(ord(c) < 128 for c in text if c != ' ')
is_length_1_1000 = 1 <= len(text) <= 1000
is_text_checks_out = not (all(ord(c) < 128 for c in text.lower() if c != ' ')) and not (any(word in text.lower() for word in banned_words)) and (1 <= len(text) <= 1000)

"""
Дополнение: Оператор in - проверка принадлежности

Оператор in проверяет, содержится ли элемент в последовательности
Возвращает True если содержится, False если нет

Использование ->
"""

# Со строками
text = "Hello World"
print(f"'Hello' in 'Hello World' -> {'Hello' in text}")  # True
print(f"'Python' in 'Hello World' -> {'Python' in text}")  # False
print(f"'world' in 'Hello World' -> {'world' in text}")  # False (регистр)
print(f"'o W' in 'Hello World' -> {'o W' in text}")  # True (подстрока)

# Списки
fruits = ["apple", "banana", "orange"]
print(f"'apple' in ['apple', 'banana', 'orange'] -> {'apple' in fruits}")  # True
print(f"'grape' in ['apple', 'banana', 'orange'] -> {'grape' in fruits}")  # False

# Словари (проверяет ключи)
user_data = {"name": "John", "age": 30, "city": "Moscow"}
print(f"'name' in {{'name': 'John'}} -> {'name' in user_data}")  # True
print(f"'John' in {{'name': 'John'}} -> {'John' in user_data}")  # False

# Множества
unique_numbers = {1, 2, 3, 4, 5}
print(f"3 in {{1, 2, 3, 4, 5}} -> {3 in unique_numbers}")  # True

"""
Задача 3: Система прав модератора

Контекст: Разрабатываем систему прав доступа для модерации контента

Инструкция: Определите права доступа
"""

# Данные пользователя и системы
user_permissions = ["read", "analyze", "moderate"]
content_categories = ["text", "image"]
current_content_type = "text"

# ЗАДАНИЕ: Определите возможности пользователя
# Может модерировать если:
# - есть права модератора И может обрабатывать текущий тип контента
can_moderate = ("moderate" in user_permissions) and (current_content_type in content_categories)
# Может анализировать если:
# - есть права на анализ И доступен любой контент
can_analyze = ("analyze" in user_permissions) and any(content in content_categories for content in content_categories)

"""
Дополнение: Функции min(), max() и sum()

min() возвращает наименьший элемент из:
- последовательности
- или из нескольких аргументов

max() делает то же для наибольшего

sum() считает сумму элементов
"""

numbers = [5, 2, 8, 1, 9]
print(f"min([5, 2, 8, 1, 9]) = {min(numbers)}")  # 1

print(f"max(5, 2, 8, 1, 9) = {max(5, 2, 8, 1, 9)}")  # 9

numbers = [1, 2, 3, 4, 5]
print(f"sum([1, 2, 3, 4, 5]) = {sum(numbers)}")  # 15

"""
Задача 4: Анализатор тональности отзывов

Контекст: Анализируем массив отзывов для выявления проблем

Инструкция: Проанализируйте тональность отзывов
"""

# Тональность отзывов от -1 (очень негативный) до +1 (очень позитивный)

reviews_sentiments = [0.8, 0.6, -0.3, 0.9, 0.7]

# ЗАДАНИЕ: Определите характеристики отзывов с помощью следующих проверок
# - Все отзывы позитивные: минимальное значение должно быть > 0
is_all_reviews_positive = min(reviews_sentiments) > 0
# - Есть хотя бы один негативный: минимальное значение должно быть < 0
is_any_negative_review = min(reviews_sentiments) < 0
# - Есть очень негативные отзывы: минимальное значение должно быть < -0.5
is_very_negative_review = min(reviews_sentiments) < -0.5
# - Большинство отзывов позитивные
# Здесь произведен расчет всех положительных отзывов
# Вам осталось произвести проверку: их сумма должна быть больше или равна 
# максимально возможной оценке, которую можно получить по всем отзывам
positive_count = sum(1 for _ in filter(lambda x: x > 0, reviews_sentiments)) 
is_very_positive_review = positive_count >= len(reviews_sentiments)*1
"""
Задача 5: Система подписок для NLP-сервиса

Контекст: Проверяем доступ к премиум-функциям AI-сервиса

Инструкция: Реализуйте проверку подписки
"""

# Данные пользователя и системы
user_tier = "premium"
subscription_active = True
available_models = ["gpt-3", "bert", "word2vec", "fasttext"]
premium_models = ["gpt-3", "bert", "gpt-4"]
user_quota = {"used": 45, "total": 100}

# ЗАДАНИЕ: Проверьте доступ к функциям
# Доступ к премиум-моделям если:
# - премиум-пользователь И активная подписка
# - И есть хотя бы одна премиум-модель
# - И не превышена квота
have_premium_access = (user_tier == "premium") and subscription_active and (any(model in available_models for model in premium_models)) and (user_quota["used"] < user_quota["total"])
# Доступ к базовым функциям если:
# - есть любые модели И не превышена квота
have_basic_access = (any(model in available_models for model in available_models)) and (user_quota["used"] < user_quota["total"])

# Эта проверка уже реализована. Напишите остальные и примените их
has_any_premium_model = any(model in available_models for model in premium_models)

print(can_analyze)