from ..core import (
    IEquationSolver,
    Equation,
    EquationRoots,
)
from typing import (
    Union,
    List
)
from ..exceptions import *
from math import sqrt


__all__ = [
    "EquationSolver"
]


class EquationSolver(IEquationSolver):
    def __init__(self):
        pass

    async def __get_discriminant(self, eq: Equation) -> Union[int, float]:
        d = (eq.b*eq.b) - (4*eq.a*eq.c)
        return d

    async def get_equation_roots(self, eq: Equation) -> List[EquationRoots]:
        discriminant = await self.__get_discriminant(eq)
        if discriminant < 0:
            raise EquationRootsNotFoundError
        if discriminant == 0:
            try:
                x = (-eq.b) / (2*eq.a)
            except ZeroDivisionError:
                raise EquationZeroDivisionError
            return [EquationRoots(name="x1", value=x)]
        else:
            try:
                x1 = (-eq.b + (sqrt(discriminant))) / (2*eq.a)
                x2 = (-eq.b - (sqrt(discriminant))) / (2*eq.a)
            except ZeroDivisionError:
                raise EquationZeroDivisionError
            return [EquationRoots(name="x1", value=x1), EquationRoots(name="x2", value=x2)]
