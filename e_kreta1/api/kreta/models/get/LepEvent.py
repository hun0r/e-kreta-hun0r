from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime
from .. import alias

class LepEvent(BaseModel):
    address              : str      = alias("Helyszin")
    creationDate         : datetime = alias("Datum")
    eventEndTime         : datetime = alias("EloadasVege")
    eventStartTime       : datetime = alias("EloadasKezdete")
    eventTitle           : str      = alias("EloadasNev")
    hasGuardianPermission: bool     = alias("GondviseloElfogadas")
    hasStudentAppeared   : bool     = alias("Megjelent")
    organizationName     : str      = alias("SzervezetNev")
    uid                  : str      = alias("Uid")
