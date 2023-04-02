from pydantic import BaseModel
from typing import Union

__all__ = [
    "Equation"
]


class Equation(BaseModel):
    a: Union[int, float]
    b: Union[int, float] = None
    c: Union[int, float] = None
