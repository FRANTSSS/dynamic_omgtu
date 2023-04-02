from pydantic import BaseModel
from typing import Union

__all__ = [
    "EquationRoots"
]


class EquationRoots(BaseModel):
    name: str = None
    value: Union[int, float] = None
