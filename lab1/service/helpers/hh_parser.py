import json

__all__ = [
    "parse_vacancies_api"
]


def parse_vacancies_api(result_api: dict) -> list:
    dirty_vacancies = result_api.get("items")
    vacancies = list([["name", "employer", "area", "salary_from", "salary_to", "currency", "gross"]])
    for vacancy in dirty_vacancies:
        vacancy_item = list()
        vacancy_item.append(vacancy.get("name"))
        vacancy_item.append(vacancy.get("employer").get("name"))
        vacancy_item.append(vacancy.get("area").get("name"))
        if vacancy.get("salary") is None:
            vacancy_item.append("")
            vacancy_item.append("")
            vacancy_item.append("")
            vacancy_item.append("")
        else:
            vacancy_item.append(vacancy.get("salary").get("from"))
            vacancy_item.append(vacancy.get("salary").get("to"))
            vacancy_item.append(vacancy.get("salary").get("currency"))
            vacancy_item.append(str(vacancy.get("salary").get("gross")).lower())
        vacancy_item = ["" if i is None else i for i in vacancy_item]
        vacancies.append(vacancy_item)

    return vacancies
