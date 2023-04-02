from fastapi import APIRouter
from fastapi.responses import FileResponse

from ioc_container import ioc
from models import Entity
from service import (
    IEquationSolver,
    Equation,
    EquationZeroDivisionError,
    EquationRootsNotFoundError
)

__all__ = [
    "route"
]

eq_solver = ioc.get_instance(IEquationSolver)
route = APIRouter()


@route.get("/")
async def root():
    return FileResponse("static/index.html")


@route.get("/style.css")
async def style():
    return FileResponse("static/style.css")


@route.get("/app.js")
async def js():
    return FileResponse("static/app.js")


@route.post("/equation/roots")
async def get_eq_roots(eq: Equation):
    try:
        roots = await eq_solver.get_equation_roots(eq)
        return Entity(success=True, data=roots)
    except EquationRootsNotFoundError:
        return Entity(success=True, data=[], message="Not Found")
    except EquationZeroDivisionError:
        return Entity(success=True, data=[], message="When calculating the roots, there was an attempt to divide by 0")
