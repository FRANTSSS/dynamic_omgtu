import asyncio
from typing import List

import pytest

from lab3.service.core.models import (
    Equation,
    EquationRoots
)
from service.test_design import quadratic_equation_roots


@pytest.fixture
def odds(quadratic_odds_roots) -> Equation:
    odds = Equation(
        a=quadratic_odds_roots.get("odds")[0],
        b=quadratic_odds_roots.get("odds")[1],
        c=quadratic_odds_roots.get("odds")[2]
    )
    return odds


@pytest.fixture
def roots(quadratic_odds_roots) -> List[EquationRoots]:
    roots = []
    for i in quadratic_odds_roots.get("roots"):
        roots.append(EquationRoots(
            value=i
        ))
    return roots


@pytest.fixture
def loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    yield loop

    loop.close()


def pytest_generate_tests(metafunc):
    metafunc.parametrize("quadratic_odds_roots", quadratic_equation_roots)
