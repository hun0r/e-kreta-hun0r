from __future__ import annotations
from pydantic import BaseModel
from .. import alias
from . import ValueDescriptor

class SubjectDescriptor(BaseModel):
    name           : str             = alias("Nev")
    subjectCategory: ValueDescriptor = alias("Kategoria")
    uid            : str             = alias("Uid")
