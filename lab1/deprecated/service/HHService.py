from .exceptions import HHServiceError
from strategy import (
    HHSearchStrategy,
    HHSearchStrategyError
)

__all__ = [
    "HHService"
]


class HHService:
    def __init__(self, base_url: str) -> None:
        #
        # Logic with other service
        #
        self.search_strategy = HHSearchStrategy(base_url=base_url)
        self.base_url = base_url

    def get_vacancies_by_python_omsk(self) -> list:
        self.search_strategy.set_base_url(self.base_url.replace("//", "//api."))
        try:
            result = self.search_strategy.simple_search_by_searchform_with_city(search_line="python", area="68")
        except HHSearchStrategyError as e:
            raise HHServiceError(f"Get python vacancies by {self.search_strategy.base_url} failed! {e}")

        self.search_strategy.set_base_url(self.base_url)

        return result
