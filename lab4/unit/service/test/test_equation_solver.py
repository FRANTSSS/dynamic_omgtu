from typing import List

import pytest
from pytest_check import check

from lab3.service.core.models import (
    Equation,
    EquationRoots
)
from lab3.service.exceptions import *
from lab3.service.impl.EquationSolver import EquationSolver


@pytest.mark.asyncio
async def test_equation_solver_difficult_roots(loop, odds: Equation, roots: List[EquationRoots]):
    eq = EquationSolver()
    try:
        eq_roots = await eq.get_equation_roots(odds)
        with check:
            for i in range(len(eq_roots)):
                assert roots[i].value in [i.value for i in eq_roots]
    except EquationRootsNotFoundError:
        assert True
