from src.functions import user_menu, load_vacancies_from_file


def main():
    """Функция MAIN"""
    vac_data = load_vacancies_from_file()
    user_menu(vac_data)


if __name__ == "__main__":
    main()