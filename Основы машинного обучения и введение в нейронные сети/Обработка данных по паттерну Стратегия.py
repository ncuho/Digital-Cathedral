from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def process_data(self, data):
        pass


class ListProcessingStrategy(Strategy):
    def process_data(self, data):
        return max(data)


class DictionaryProcessingStrategy(Strategy):
    def process_data(self, data):
        data = {key: value for key, value in data.items() if value['max_humidity'] > 85}
        return data


class DataProcessor:
    def __init__(self, strategy: Strategy):
        self.__strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.__strategy = strategy

    def process_data(self, data):
        return self.__strategy.process_data(data)


if __name__ == "__main__":
    array = [1, 4, 7, 2, 3, 5, 10, 8, 4, 9]
    cities = {
        'CityA': {
            'avarage_temperature': 21.308,
            'amount_weather': 106.53999999999999,
            'max_humidity': 88.66,
            'min_humidity': 59.02
        },
        'CityB': {
            'avarage_temperature': 20.764000000000003,
            'amount_weather': 103.82000000000001,
            'max_humidity': 89.55,
            'min_humidity': 73.01
        },
        'CityC': {
            'avarage_temperature': 24.500000000000004,
            'amount_weather': 122.50000000000001,
            'max_humidity': 83.67,
            'min_humidity': 52.18
        }
    }

    processor = DataProcessor(ListProcessingStrategy())
    print(processor.process_data(array))

    processor.set_strategy(DictionaryProcessingStrategy())
    print(processor.process_data(cities))