#Задача. Базовый синтаксис
import json
#1.Прочитать JSON-файл в словарь data
with open('data.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

#2.Итерировать по всем ключам верхнего уровня и вывести их
print("(2) Ключи верхнего уровня:")
for key in config.keys():
    print(key)

#3.Итерировать по всем значениям словаря departments
print("(3) Ключи по значениям словаря departments:")
for employees in config['departments'].values():
    print(employees)

#4.Итерировать по парам ключ-значение в departments
print("(4) Ключ-значение словаря departments:")
for key, value in config['departments'].items():
    print(f"{key}: {value}")

#5.Добавить нового сотрудника "David" в отдел "dev"
config['departments']['dev'].append('David')
print(config['departments'])

#6.Увеличить бюджет на 10%
config["budget"] =  int(config["budget"] * 1.1)
print(config["budget"])

#7.Записать изменённый словарь обратно в файл
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=4)

#Задача 1: Анализ конфигурации модели NLP
config = {
    "model_name": "bert-base-uncased",
    "batch_size": 32,
    "max_length": 128,
    "learning_rate": 2e-5,
    "epochs": 3,
    "labels": ["positive", "negative", "neutral"]
}

#Получите значение learning_rate двумя способами: через скобки и через get()
print("Способ 1 - через квадратные скобки:")
lr1 = config["learning_rate"]
print(f"learning_rate = {lr1}")

print("\nСпособ 2 - через метод get():")
lr2 = config.get("learning_rate")
print(f"learning_rate = {lr2}")

#Добавьте новый параметр "early_stopping": True
config["early_stopping"] = True
print(config)

#Измените batch_size на 64
config["batch_size"] = 64
print(config)

#Пройдитесь по всем параметрам конфигурации и выведите только те, значения которых - числа
for key, value in config.items():
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        print(f"{key}: {value}")

#Создайте копию конфигурации для тестирования с batch_size=8 и epochs=1
test_config = config.copy()
test_config["batch_size"] = 8
test_config["epochs"] = 1
print(test_config)
