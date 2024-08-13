#from src.connector import Connector
from prettytable import PrettyTable


def start_user_menu(connector: Connector):
    while True:
        print(
            'Действия:\n',
            '1. Получить топ вакансий\n',
            '2.\n',
            '0. Выйти'
        )
        user_command = input()

        if user_command == '1':
            print_top_vacancies(connector)
        elif user_command == '0':
            return


def print_top_vacancies(connector: Connector):
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    vacancies = connector.get_vacancies()
    print('Ваши ваккансии:')
    t = PrettyTable(['№','Название', 'З/П, от', 'З/П, до', 'Описание:', 'Ссылка'])
    vac_num = 1
    for vac in sorted(vacancies, reverse=True)[:top_n]:
        if vac.description_vac:
            print_descr = str(vac.description_vac)[0:60] + '...'
        else:
            print_descr = None
        t.add_row([vac_num, vac.name[:50], vac.salary_from or '- ', vac.salary_to or '- ', print_descr or '-', vac.url])
        vac_num += 1
    print(t)