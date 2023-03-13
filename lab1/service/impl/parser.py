import json
from ..core import Vacancy
from typing import List

__all__ = [
    "parse_vacancies_api"
]


def parse_vacancies_api(result_api: dict) -> List[Vacancy]:
    dirty_vacancies = result_api.get("items")
    vacancies = list()
    for vacancy in dirty_vacancies:
        vacancy_item = Vacancy(
            name=vacancy.get("name"),
            employer_name=vacancy.get("employer").get("name"),
            area_name=vacancy.get("area").get("name")
        )
        if vacancy.get("salary") is not None:
            vacancy_item.salary_from = vacancy.get("salary").get("from")
            vacancy_item.salary_to = vacancy.get("salary").get("to")
            vacancy_item.currency = vacancy.get("salary").get("currency")
            vacancy_item.gross = str(vacancy.get("salary").get("gross")).lower()
        vacancies.append(vacancy_item)

    return vacancies
