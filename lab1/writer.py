import xlsxwriter
from service import Vacancy
from typing import List

__all__ = [
    "write_result_to_xlsx"
]


def write_result_to_xlsx(file_path: str, data: List[Vacancy]) -> None:
    book = xlsxwriter.Workbook(file_path)
    sheet = book.add_worksheet()

    data.insert(0, Vacancy(
        name="name",
        employer_name="employer_name",
        area_name="area_name",
        salary_from="salary_from",
        salary_to="salary_to",
        currency="currency",
        gross="gross"
    ))
    for i in range(len(data)):
        for j in range(len(data[0].dict())):
            sheet.write(i, j, list(data[i].dict().values())[j])

    book.close()
