from __future__ import annotations
from pydantic import BaseModel
from .. import alias

class Attachment(BaseModel):
    name: str = alias("Nev")
    type: str = alias("Tipus")
    uid : str = alias("Uid")
