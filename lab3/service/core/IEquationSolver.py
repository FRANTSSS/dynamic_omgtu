from .models import *
from typing import (
    Union,
    List
)


__all__ = [
    "IEquationSolver"
]


class IEquationSolver:
    async def __get_discriminant(self, eq: Equation) -> Union[int, float]:
        raise NotImplementedError

    async def get_equation_roots(self, eq: Equation) -> List[EquationRoots]:
        raise NotImplementedError
