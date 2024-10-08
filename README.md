# Курсовая работа 4
## Описание проекта

Этот проект представляет собой инструмент для работы с вакансиями на платформе hh.ru. Он позволяет получать информацию о вакансиях, сохранять её в файл, а также работать с этим файлом и фильтровать его.
## Требования к реализации

- **API для работы с hh.ru**: Реализован абстрактный класс `APIVacancies` и конкретный класс `HeadHunterRuAPI`, который подключается к API hh.ru и получает вакансии согласно заданным параметрам.
- **Класс Vacancy**: Определяет атрибуты вакансии, включая название, ссылку, зарплату, описание и требования. Поддерживает методы сравнения вакансий по зарплате и валидацию данных.
- **JSON хранилище вакансий**: Абстрактный класс `Saver` определяет интерфейс для работы с вакансиями, а класс `JSONSaver` реализует этот интерфейс для работы с JSON файлом, обеспечивая сохранение, чтение и удаление вакансий.

## Интерфейс пользователя

Программа предоставляет функционал для взаимодействия с пользователем через консоль:

- Ввод поискового запроса для получения вакансий из hh.ru.
- Получение топ N вакансий по зарплате.

## Использование

Для использования программы необходимо установить `poetry` и выполнить следующие шаги:

1. Клонирование репозитория
```bash
https://github.com/Ivan-Anokhin/Course_4
```
2. Установление зависимостей
```bash
poetry install
```
3. Запуск проекта
```text
python main.py
```