from ioc_container import ioc
from service import (
    EquationSolver,
    IEquationSolver
)

__all__ = [
    "bootstrap"
]


def bootstrap() -> None:
    ioc.set_instance(IEquationSolver, EquationSolver())


bootstrap()
