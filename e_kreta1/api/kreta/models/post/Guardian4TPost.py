from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime
from .. import alias

class Guardian4TPost(BaseModel):
    dateOfBirth     : datetime = alias("SzuletesiDatum")
    firstname       : str      = alias("Utonev")
    firstnameOfBirth: str      = alias("SzuletesiUtonev")
    isAszfAccepted  : bool     = alias("IsElfogadottAszf")
    mothersFirstname: str      = alias("AnyjaUtonev")
    mothersSurname  : str      = alias("AnyjaVezeteknev")
    namePrefix      : str      = alias("Elotag")
    placeOfBirth    : str      = alias("SzuletesiHely")
    surname         : str      = alias("Vezeteknev")
    surnameOfBirth  : str      = alias("SzuletesiVezeteknev")
    