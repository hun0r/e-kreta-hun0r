from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel
from . import ValueDescriptor
from .. import alias

class TimeTableWeek(BaseModel):
    endDateAsString: datetime        = alias("VegNapDatuma")
    numberOfWeek   : int             = alias("HetSorszama")
    startDate      : datetime        = alias("KezdoNapDatuma")
    type           : ValueDescriptor = alias("Tipus")
    uid            : str             = alias("Uid")
