from abc import ABC, abstractmethod
from config import path_operations
import json
import os


class Saver(ABC):
    """ Абстрактный класс для записи в файл """

    @abstractmethod
    def add_data(self, vacancy):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def del_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

class JSONSaver(Saver):
    """ Класс для записи в json-файл по пути data/vacancies.json (файл config)"""

    def __init__(self, filepath: str = path_operations, mode='w', encoding='utf-8'):
        self.__filepath = filepath
        self._mode = mode
        self._encoding = encoding

    def add_data(self, vacancy):
        """Добавить вакансии с ресурса"""

        if os.stat(path_operations).st_size != 0:
            existing_vacancies = self.get_data()
        else:
            existing_vacancies = []
        # Добавляем новые вакансии к существующим
        count = 0
        for i in vacancy:
            if i in existing_vacancies:
                continue
            else:
                count +=1
                existing_vacancies.append(i)

        self.save_data(existing_vacancies, count)
        return existing_vacancies

    def save_data(self, existing_vacancies, count: int):
        """Запись данных json в файл"""

        with open(self.__filepath, self._mode, encoding=self._encoding) as file:
            json.dump(existing_vacancies, file, ensure_ascii=False, indent=4)
        print(f'\nЯ нашел {count} подходящих вакансий и сохранил в файл {self.__filepath}\n\n'
              f'В файле записано {len(existing_vacancies)} вакансий\n\n')

    def get_data(self):
        """ Получение данных json из файла"""

        if os.stat(path_operations).st_size != 0:
            with open(self.__filepath, encoding=self._encoding) as file:
                return json.loads(file.read())
        return f'Нет данных'

    def del_data(self):
        """ Удаление данных из файла """

        with open(self.__filepath, 'w'):
            pass

