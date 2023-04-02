from typing import (
    Optional,
    List
)

from pydantic import BaseModel
from service import EquationRoots

__all__ = [
    "Entity"
]


class Entity(BaseModel):
    success: bool
    data: List[EquationRoots]
    message: Optional[str]
