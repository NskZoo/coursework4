import json
from src.vacancy import Vacancy


def test_file_writer():
    vacancy = Vacancy("Билетный промоутер (удаленно)",
                      "Москва",
                      120000,
                      125000,
                      "Полная занятость",
                      "https://hh.ru/vacancy/90278470")

    with open('vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(vacancy.__dict__, file, indent=4, ensure_ascii=False)