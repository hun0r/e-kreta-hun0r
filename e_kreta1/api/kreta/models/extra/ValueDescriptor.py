from __future__ import annotations
from pydantic import BaseModel
from .. import alias

class ValueDescriptor(BaseModel):
    description: str = alias("Leiras")
    name       : str = alias("Nev")
    uid        : str = alias("Uid")
