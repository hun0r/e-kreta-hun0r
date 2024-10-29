from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime
from .. import alias
from . import Group, ValueDescriptor, SubjectDescriptor

class Evaluation(BaseModel):
    creatingTime  : datetime          = alias("KeszitesDatuma")
    form          : str               = alias("Jelleg")
    formType      : ValueDescriptor   = alias("ErtekFajta")
    group         : Group             = alias("OsztalyCsoport")
    mode          : ValueDescriptor   = alias("Mod")
    numberValue   : int               = alias("SzamErtek")
    recordDate    : datetime          = alias("RogzitesDatuma")
    seenByTutelary: datetime          = alias("LattamozasDatuma")
    shortValue    : str               = alias("SzovegesErtekelesRovidNev")
    sortIndex     : int               = alias("SortIndex")
    subject       : SubjectDescriptor = alias("Tantargy")
    teacher       : str               = alias("ErtekeloTanarNeve")
    theme         : str               = alias("Tema")
    type          : ValueDescriptor   = alias("Tipus")
    uid           : str               = alias("Uid")
    value         : str               = alias("SzovegesErtek")
    weight        : str               = alias("SulySzazalekErteke")