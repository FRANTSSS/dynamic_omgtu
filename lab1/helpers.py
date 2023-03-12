import xlsxwriter

__all__ = [
    "write_result_to_xlsx"
]


def write_result_to_xlsx(file_path: str, data: list) -> None:
    book = xlsxwriter.Workbook(file_path)
    sheet = book.add_worksheet()

    for i in range(len(data)):
        for j in range(len(data[0])):
            sheet.write(i, j, data[i][j])

    book.close()
