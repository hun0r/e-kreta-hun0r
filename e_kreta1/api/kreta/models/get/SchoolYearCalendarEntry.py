from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel
from .. import alias
from . import Group, ValueDescriptor

class SchoolYearCalendarEntry(BaseModel):
    date            : datetime        = alias("Datum")
    dayType         : ValueDescriptor = alias("Naptipus")
    group           : Group           = alias("OsztalyCsoport")
    irregularDay    : ValueDescriptor = alias("ElteroOrarendSzerintiTanitasiNap")
    uid             : str             = alias("Uid")
    weekTypeSchedule: ValueDescriptor = alias("OrarendiNapHetirendje")
