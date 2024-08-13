from src.vacancy import Vacancy
from prettytable import PrettyTable
from src.vacancy_json import JSONSaver
from src.API_HH import HeadHunterRuAPI
import os
import json
from config import data_json, path_operations


def load_vacancies_from_file():
    """Загружает вакансии из локального файла"""

    if os.stat(path_operations).st_size != 0:
        with open(data_json, encoding='utf-8') as file:
            vac_data = json.loads(file.read())
    else:
        vac_data = []
    return vac_data


def user_menu(vac_data):
    """Реализует меню для работы пользователя"""

    while True:
        vac_len = len(vac_data)
        print(f'В настоящий момент в локальной базе есть {vac_len} вакансий\n')
        print(
            'Что будем делать?:\n',
            '1. Добавить вакансии с сервера\n',
            '2. Вывести на экран топ вакансии (по зарплате) в указанном количестве \n',
            '3. Удалить вакансии\n',
            '0. Завершить поиск вакансий'
        )
        user_command = input()

        if user_command == '1':
            a = HeadHunterRuAPI()
            user_text = input("Введите ключевые слова для поиска вакансии (может быть несколько слов):\n")
            vacancies = a.getting_vacancies(user_text)
            valid_vacancies = a.validate_data(vacancies)
            vacancies_json = JSONSaver()
            vacancies_json.add_data(valid_vacancies)
            user_vacancies = JSONSaver()
            vac_data = Vacancy.cast_to_object_list(user_vacancies.get_data())

        if user_command == '2':
            top_n = int(input("Введите количество вакансий для вывода на экран: "))
            print('Ваши ваккансии:')
            t = PrettyTable(['№', 'Название', 'З/П, от', 'З/П, до', 'Валюта', 'Описание:', 'Ссылка'])
            vac_num = 1
            all_vac = sorted(vac_data, reverse=True)[:top_n]
            for vac in all_vac:
                t.add_row([vac_num, vac.name[:40], vac.salary_from or '- ', vac.salary_to or '- ', vac.currency,
                           vac.responsibility[:50] or '-', vac.url])
                vac_num += 1
            print(t)

        if user_command == '3':
            with open(data_json, 'w'):
                pass
                vac_data = []
                print(f'Из базы были стёрты все вакансии.\n')

        elif user_command == '0':
            print('Выходим из программы, спасибо за работу!)')
            break
