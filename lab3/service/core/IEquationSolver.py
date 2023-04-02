from typing import List

from .models import *

__all__ = [
    "IEquationSolver"
]


class IEquationSolver:
    async def get_equation_roots(self, eq: Equation) -> List[EquationRoots]:
        raise NotImplementedError()
