from .helpers import (
    HHRequests,
    parse_vacancies_api
)

from .exceptions import HHSearchStrategyError

__all__ = [
    "HHSearchStrategy"
]


class HHSearchStrategy:
    def __init__(self, base_url: str, client_id: str = None) -> None:
        #
        # Logic with authorization and other settings
        #
        if client_id is None:
            self.headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                                          "(KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                            "content-type": "application/json; charset=utf-8"
                            }
        self.base_url = base_url
        self.requests = HHRequests(base_url, self.headers)

    def set_base_url(self, new_base_url: str) -> None:
        self.base_url = new_base_url
        self.requests = HHRequests(self.base_url, self.headers)

    def simple_search_by_searchform_with_city(self, search_line: str, area: str) -> list:
        query = "/vacancies"
        params = {'text': search_line, 'area': area, 'per_page': '100', 'page': 0}
        r = self.requests.get(query, params)
        if r.status_code != 200:
            raise HHSearchStrategyError(f"Status code response {str(r.status_code)} to "
                                        f"\n{query} {params} != 200,\n{r.text}")
        result = parse_vacancies_api(r.json())
        return result
