import os

from dotenv import load_dotenv
from service import HHServiceImpl
from writer import write_result_to_xlsx


def main():
    load_dotenv()
    base_url = os.environ.get("BASE_URL")
    output = os.environ.get("OUTPUT")
    hh = HHServiceImpl(base_url)
    result = hh.search_by_searchform_with_city(search_line="python", area="68")
    write_result_to_xlsx(output, result)


if __name__ == "__main__":
    main()
