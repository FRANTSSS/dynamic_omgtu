from typing import List
from .models import Vacancy

__all__ = [
    "HHService"
]


class HHService:
    def search_by_searchform_with_city(self, search_line: str, area: str) -> List[Vacancy]:
        raise NotImplementedError
