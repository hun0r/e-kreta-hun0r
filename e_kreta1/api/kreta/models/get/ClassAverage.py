from __future__ import annotations
from pydantic import BaseModel
from .. import alias
from . import SubjectDescriptor

class ClassAverage(BaseModel):
    average                   : float             = alias("TanuloAtlag")
    classAverageNumber        : float             = alias("OsztalyCsoportAtlag")
    differenceFromClassAverage: float             = alias("OsztalyCsoportAtlagtolValoElteres")
    subject                   : SubjectDescriptor = alias("Tantargy")
    uid                       : str               = alias("Uid")
