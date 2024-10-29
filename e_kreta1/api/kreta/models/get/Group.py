from __future__ import annotations
from pydantic import BaseModel
from .. import alias
from . import ValueDescriptor, ClassMaster

class Group(BaseModel):
    category            : ValueDescriptor = alias("OktatasNevelesiKategoria")
    classMaster         : ClassMaster     = alias("OsztalyFonok")
    classMasterAssistant: ClassMaster     = alias("OsztalyFonokHelyettes")
    educationType       : ValueDescriptor = alias("OktatasNevelesiFeladat")
    isActive            : bool            = alias("IsAktiv")
    name                : str             = alias("Nev")
    sortIndex           : int             = alias("OktatasNevelesiFeladatSortIndex")
    type                : str             = alias("Tipus")
    uid                 : str             = alias("Uid")
