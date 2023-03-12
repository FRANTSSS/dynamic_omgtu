import os

from dotenv import load_dotenv
from service import HHService
from helpers import write_result_to_xlsx


if __name__ == "__main__":
    load_dotenv()
    base_url = os.environ.get("BASE_URL")
    output = os.environ.get("OUTPUT")
    hh = HHService(base_url)
    result = hh.get_vacancies_by_python_omsk()
    write_result_to_xlsx(output, result)
