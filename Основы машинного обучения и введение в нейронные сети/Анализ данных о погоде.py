import random
from datetime import datetime, timedelta

def generate_dates(start_date, end_date):
    """
    Генерирует список дат между указанными начальной и конечной датами.

    Параметры
    ----------
    start_date : str
        Начальная дата в формате ГГГГ-ММ-ДД.
    end_date : str
        Конечная дата в формате ГГГГ-ММ-ДД.

    Возвращает
    -------
    list
        Список дат (в виде строк в формате ГГГГ-ММ-ДД) между начальной и конечной датами.
    """

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    date_list = [(start + timedelta(days=x)).strftime("%Y-%m-%d") for x in range((end - start).days + 1)]
    return date_list

def choose_city(cities):
    """
    Случайно выбирает город из списка городов.

    Параметры
    ----------
    cities : list
        Список названий городов.

    Возвращает
    -------
    str
        Случайно выбранный город из списка.
    """
    return random.choice(cities)

def generate_weather_data(temp_range, humidity_range, precipitation_range):
    """
    Генерирует случайные данные о погоде, включая температуру, влажность и осадки.

    Параметры
    ----------
    temp_range : tuple
        Кортеж (минимальная температура, максимальная температура), задающий диапазон температур.
    humidity_range : tuple
        Кортеж (минимальная влажность, максимальная влажность), задающий диапазон влажности.
    precipitation_range : tuple
        Кортеж (минимальное количество осадков, максимальное количество осадков), задающий диапазон осадков.

    Возвращает
    -------
    tuple
        Кортеж, содержащий случайно сгенерированные значения температуры, влажности и осадков.
    """
    temperature = random.uniform(*temp_range)
    humidity = random.uniform(*humidity_range)
    precipitation = random.uniform(*precipitation_range)
    return temperature, humidity, precipitation

def create_weather_data(start_date, end_date, cities, temp_range, humidity_range, precipitation_range):
    """
    Создает список словарей с данными о погоде для различных дат и городов.

    Параметры
    ----------
    start_date : str
        Начальная дата в формате ГГГГ-ММ-ДД.
    end_date : str
        Конечная дата в формате ГГГГ-ММ-ДД.
    cities : list
        Список названий городов.
    temp_range : tuple
        Кортеж (минимальная температура, максимальная температура), задающий диапазон температур.
    humidity_range : tuple
        Кортеж (минимальная влажность, максимальная влажность), задающий диапазон влажности.
    precipitation_range : tuple
        Кортеж (минимальное количество осадков, максимальное количество осадков), задающий диапазон осадков.

    Возвращает
    -------
    list
        Список словарей, каждый из которых представляет данные о погоде для конкретной даты и города.
    """
    weather_data = []
    for date in generate_dates(start_date, end_date):
        for city in cities:
            temperature, humidity, precipitation = generate_weather_data(temp_range, humidity_range, precipitation_range)
            weather_data.append({
                "date": date,
                "city": city,
                "temperature": round(temperature, 2),
                "humidity": round(humidity, 2),
                "precipitation": round(precipitation, 2)
            })
    return weather_data

# Пример использования
cities = ["CityA", "CityB", "CityC"]
temp_range = (10, 30)
humidity_range = (50, 90)
precipitation_range = (0, 10)

weather_data = create_weather_data("2023-11-01", "2023-11-05", cities, temp_range, humidity_range, precipitation_range)




'''
Создаем словарь с информацией о погоде по каждому городу вида (город : {топик : информация, ...})
Проходимся по каждому элементу из массива городов и к ключу нового или уже имеющегося города
добавляем среднее значение температуры по этому городу:
суммируем все температуры по одному городу и делим на количество записей по этому городу
'''
cities_temperature = {}
for i in range(len(cities)):
    cities_temperature[cities[i]] = {"avarage_temperature":
                                     sum(map(lambda weather: weather['temperature'] if cities[i] == weather['city'] else 0, weather_data)) /
                                     sum(map(lambda weather: cities[i] == weather['city'], weather_data))}




from functools import reduce
'''
Проходимся по каждому элементу из массива городов и к ключу нового или уже имеющегося города
добавляем сумму температур по этому городу:
суммируем все температуры по одному городу при помощи reduce
'''
for i in range(len(cities)):
    cities_temperature[cities[i]]['amount_weather'] = reduce(
        lambda x, y: x + y['temperature'] if cities[i] == y['city'] else x + 0, weather_data, 0)



'''
Создаем переменную с границей по которой будем фильровать данные
И фильтруем данные по влажности и записываем в новый массив
'''
threshold = 80.0
filter_data = list(filter(lambda x: x['humidity'] > threshold, weather_data))


print(cities_temperature)
print(filter_data)