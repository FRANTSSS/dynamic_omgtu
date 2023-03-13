from .helpers import (
    HHRequests,
    parse_vacancies_api
)

from ..core import HHService

from .exceptions import HHSearchStrategyError

__all__ = [
    "HHServiceImpl"
]


class HHServiceImpl(HHService):
    def __init__(self, base_url: str, client_id: str = None) -> None:
        #
        # Logic with authorization and other settings
        #
        if client_id is None:
            self.headers = {
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                              "(KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                "content-type": "application/json; charset=utf-8"
            }
        self.base_url = base_url

    def search_by_searchform_with_city(self, search_line: str, area: str) -> list:
        requests = HHRequests(self.base_url, self.headers)
        query = "/vacancies"
        params = {'text': search_line, 'area': area, 'per_page': '100', 'page': 0}
        r = requests.get(query, params)
        if r.status_code != 200:
            raise HHSearchStrategyError(f"Status code response {str(r.status_code)} to "
                                        f"\n{query} {params} != 200,\n{r.text}")
        result = parse_vacancies_api(r.json())
        return result
