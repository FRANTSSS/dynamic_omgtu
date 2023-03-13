from pydantic import BaseModel
from typing import Optional

__all__ = [
    "Vacancy"
]


class Vacancy(BaseModel):
    name: str
    employer: str
    area: str
    salary_from: Optional[str] = None
    salary_to: Optional[str] = None
    currency: Optional[str] = None
    gross: Optional[str] = None
