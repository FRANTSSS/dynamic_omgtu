from pydantic import BaseModel
from typing import Mapping

__all__ = [
    "EnvDTO"
]


class EnvDTO(BaseModel):
    memory: Mapping
    bot: Mapping
