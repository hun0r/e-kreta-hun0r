from __future__ import annotations
from datetime import datetime, timedelta
from pydantic import BaseModel, field_validator
from .. import alias
from . import Group, ValueDescriptor, Lesson, SubjectDescriptor

class Omission(BaseModel):
    creatingTime      : datetime          = alias("KeszitesDatuma")
    date              : datetime          = alias("Datum")
    delayTime         : timedelta         = alias("KesesPercben")
    @field_validator("delayTime")
    def dur_as_mins(cls, v: int):
        return timedelta(minutes=v)
    group             : Group             = alias("OsztalyCsoport")
    justificationState: str               = alias("IgazolasAllapota")
    justificationType : ValueDescriptor   = alias("IgazolasTipusa")
    lesson            : Lesson            = alias("Ora")
    mode              : ValueDescriptor   = alias("Mod")
    subject           : SubjectDescriptor = alias("Tantargy")
    teacher           : str               = alias("RogzitoTanarNeve")
    type              : ValueDescriptor   = alias("Tipus")
    uid               : str               = alias("Uid")
