import json
from config import config
from api_response import api_response
from pipeline_config import pipeline_config
from nlp_aggegation import models_stats

# Task 1
print("\nЗадача 1\n=============================================================")
# 1 Прочитать JSON-файл в словарь data
# 2 Итерировать по всем ключам верхнего уровня и вывести их
# 3 Итерировать по всем значениям словаря departments
# 4 Итерировать по парам ключ-значение в departments
# 5 Добавить нового сотрудника "David" в отдел "dev"
# 6 Увеличить бюджет на 10%
# 7 Записать изменённый словарь обратно в файл

# 1
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(f"Data.json до изменений:\n{data}")

# 2
print("\nКлючи верхнего уровня:")
for key in data.keys():
    print(key)

# 3
print("\nЗначения departments:")
for value in data["departments"].values():
    print(value)

# 4
print("\nОтделы и сотрудники:")
for department, employees in data["departments"].items():
    print(f"{department}: {employees}")

# 5
data["departments"]["dev"].append("David")
print(f"\nНовый сотрудник David добавлен\n{data["departments"]["dev"]}")

# 6
data["budget"] *= 1.10
print(f"\nОбновленный бюджет\n{data["budget"]}")

# 7
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

# Вывод обновленного файла
with open("data.json", "r", encoding="utf-8") as file:
    data_upd = json.load(file)
    print(f"\nОбновленный Data.json\n{data_upd}")
print("\nКонец задачи 1\n=============================================================")


# Task 1.2
print("\nЗадача 1.2\n=============================================================")
# 1 Получите значение learning_rate двумя способами: через скобки и через get()
# 2 Добавьте новый параметр "early_stopping": True
# 3 Измените batch_size на 64
# 4 Пройдитесь по всем параметрам конфигурации и выведите только те, значения которых - числа
# 5 Создайте копию конфигурации для тестирования с batch_size=8 и epochs=1

# 1
lr_1 = config["learning_rate"]
lr_2 = config.get("learning_rate")

print(lr_1)
print(lr_2)

# 2
config["early_stopping"] = True
print(f"\nДобавлен новый параметр early_stopping со значением True:\n{config}")

# 3
config["batch_size"] = 64
print(f"\nИзменен batch_size на 64:\n{config}")

# 4
print("\nЧисловые параметры:")
for key, value in config.items():
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        print(f"{key}: {value}")
# 5
test_config = config.copy()
test_config["batch_size"] = 8
test_config["epochs"] = 1

print(f"\nКонфигурация для тестирования: {test_config}")
print("\nКонец задачи 1.2\n=============================================================")

# Task 2
# print("\nЗадача 2\n=============================================================")
# 1 Получите оценку тональности (score)
# 2 Пройдитесь по всем сущностям (entities) и выведите только названия сущностей
# 3 Найдите сущность с максимальной уверенностью (confidence)
# 4 Добавьте в поле ответа "model_version": "2.1.0"
# 5 Отфильтруйте все поля, значения которых являются строками


# 1
sentiment_score = api_response["sentiment"]["score"]
print(f"Оценка тональности (score): {sentiment_score}")

# 2
print("\nСущности:")
for entity in api_response["entities"]:
    print(entity["entity"])

# 3
max_confidence_entity = max(api_response["entities"], key=lambda x: x["confidence"])
print(f"\nСущность с максимальной уверенностью: {max_confidence_entity['entity']} (confidence: {max_confidence_entity['confidence']})")

# 4
api_response["model_version"] = "2.1.0"
print(f"\nДобавленное поле 'model_version':\n{api_response}")

# 5
filtered_response = {key: value for key, value in api_response.items() if isinstance(value, str)}
print(f"\nФильтрация строковых значений:\n{filtered_response}")

print("\nКонец задачи 2\n=============================================================")

# Task 3
# print("\nЗадача 3\n=============================================================")
# 1 Включите stemming, установив "enabled": True
# 2 Добавьте "numbers" в custom_words для стоп-слов
# 3 Получите список всех включенных шагов пайплайна
# 4 Измените output_format на "vectors"
# 5 Создайте упрощенную конфигурацию только с включенными шагами

# 1
pipeline_config["steps"]["stemming"]["enabled"] = True
print(f"\nВключен stemming: {pipeline_config['steps']['stemming']}")

# 2
pipeline_config["steps"]["stopwords"]["custom_words"].append("numbers")
print(f"\nДобавлено 'numbers' в custom_words для стоп-слов: {pipeline_config['steps']['stopwords']['custom_words']}")

# 3
enabled_steps = [step for step, config in pipeline_config["steps"].items() if config["enabled"]]
print(f"\nВключенные шаги пайплайна: {enabled_steps}")

# 4
pipeline_config["output_format"] = "vectors"
print(f"\nИзменен output_format на 'vectors':\n{pipeline_config}")

# 5
simplified_config = {step: config for step, config in pipeline_config["steps"].items() if config["enabled"]}
print(f"\nУпрощенная конфигурация с включенными шагами:\n{simplified_config}")

print("\nКонец задачи 3\n=============================================================")

# Task 4
print("\nЗадача 4\n=============================================================")
# 1 Найдите модель с максимальной точностью (accuracy)
# 2 Рассчитайте среднее время инференса по всем моделям
# 3 Создайте новый словарь только с метриками accuracy и f1_score для каждой модели
# 4 Добавьте новую модель "albert-base" с данными: accuracy=0.87, f1_score=0.86, inference_time=55, size_mb=180
# 5 Отфильтруйте модели, размер которых меньше 500 МБ

# 1
max_accuracy_model = max(models_stats, key=lambda model: models_stats[model]["accuracy"])
max_accuracy_value = models_stats[max_accuracy_model]["accuracy"]
print(f"\nМодель с максимальной точностью: {max_accuracy_model} (accuracy: {max_accuracy_value})")

# 2
total_inference_time = sum(model["inference_time"] for model in models_stats.values())
average_inference_time = total_inference_time / len(models_stats)
print(f"\nСреднее время инференса: {average_inference_time:.2f} секунд")

# 3
metrics_dict = {model: {"accuracy": stats["accuracy"], "f1_score": stats["f1_score"]}
                for model, stats in models_stats.items()}
print(f"\nСловарь с метриками accuracy и f1_score:\n{metrics_dict}")

# 4
models_stats["albert-base"] = {
    "accuracy": 0.87,
    "f1_score": 0.86,
    "inference_time": 55,
    "size_mb": 180
}
print(f"\nОбновленный список моделей с добавленной моделью 'albert-base':\n{models_stats}")

# 5
filtered_models = {model: stats for model, stats in models_stats.items() if stats["size_mb"] < 500}
print(f"\nМодели, размер которых меньше 500 МБ:\n{filtered_models}")

print("\nКонец задачи 4\n=============================================================")

# Task 5
print("\nЗадача 5\n=============================================================")
# 1 Загрузите конфигурацию из JSON-файла
# 2 Добавьте новую модель для "summarization" с соответствующими параметрами
# 3 Увеличьте rate_limit на 50%
# 4 Добавьте русский язык ("ru") в поддерживаемые языки для модели sentiment
# 5 Создайте отдельный словарь только с настройками сервера
# 6 Сохраните обновленную конфигурацию в новый файл nlp_service_config_updated.json

# 1
with open("nlp_service_config.json", "r", encoding="utf-8") as file:
    nlp_service_config = json.load(file)
    print(f"Данные из nlp_service_config.json:\n{nlp_service_config}")

# 2
nlp_service_config["models"]["summarization"] = {
    "path": "/models/bert-summarization",
    "max_input_length": 1024,
    "supported_languages": ["en", "es", "fr", "de"]
}
print(f"\nДобавлена новая модель для 'summarization': {nlp_service_config['models']['summarization']}")

# 3
nlp_service_config["rate_limit"] *= 1.5
print(f"\nОбновленный rate_limit: {nlp_service_config['rate_limit']}")

# 4
nlp_service_config["models"]["sentiment"]["supported_languages"].append("ru")
print(f"\nОбновленные поддерживаемые языки для sentiment: {nlp_service_config['models']['sentiment']['supported_languages']}")

# 5
server_config = nlp_service_config["server"]
print(f"\nНастройки сервера: {server_config}")

# 6
with open("nlp_service_config_updated.json", "w", encoding="utf-8") as file:
    json.dump(nlp_service_config, file, indent=4, ensure_ascii=False)

print("\nОбновленная конфигурация сохранена в 'nlp_service_config_updated.json'")
with open("nlp_service_config_updated.json", "r", encoding="utf-8") as file:
    data_upd = json.load(file)
    print(f"\nСодержимое nlp_service_config_updated.json\n{data_upd}")

print("\nКонец задачи 5\n=============================================================")