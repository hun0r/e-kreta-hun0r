from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime
from .. import alias

class GuardianEAdmin(BaseModel):
    classId               : int  = alias("tanuloOsztalyKretaAzonosito")
    emailAddress          : str  = alias("emailCim")
    guardianName          : str  = alias("gondviseloNev")
    isLegalRepresentative : bool = alias("isTorvenyesKepviselo")
    isSzmk                : bool = alias("isSZMK")
    isSzmkDeputy          : bool = alias("isSZMKHelyettes")
    kretaId               : int  = alias("kretaAzonosito")
    relationType          : str  = alias("rokonsagiFok")
    studentClass          : str  = alias("tanuloOsztaly")
    studentId             : str  = alias("tanuloOktatasiAzonosito")
    studentName           : str  = alias("tanuloNev")
    szmkClass             : str  = alias("SZMKOsztaly")
    szmkClassDeputy       : str  = alias("sZMKOsztalyHelyettes")
    szmkClassDeputyKretaId: int  = alias("sZMKOsztalyHelyettesKretaAzonosito")
    szmkClassKretaEmployee: int  = alias("sZMKOsztalyKretaAlkalmazott")
    szmkClassKretaId      : int  = alias("sZMKOsztalyKretaAzonosito") 

class Guardian4T(BaseModel):
    dateOfBirth     : datetime = alias("SzuletesiDatum")
    firstname       : str      = alias("Utonev")
    firstnameOfBirth: str      = alias("SzuletesiUtonev")
    mothersFirstname: str      = alias("AnyjaUtonev")
    mothersSurname  : str      = alias("AnyjaVezeteknev")
    namePrefix      : str      = alias("Elotag")
    placeOfBirth    : str      = alias("SzuletesiHely")
    surname         : str      = alias("Vezeteknev")
    surnameOfBirth  : str      = alias("SzuletesiVezeteknev")

class Guardian(BaseModel):
    email                : str  = alias("EmailCim")
    hasParentalRights    : bool = alias("IsNincsFelugyeletiJoga")
    isLegalRepresentative: bool = alias("IsTorvenyesKepviselo")
    name                 : str  = alias("Nev")
    phoneNumber          : str  = alias("Telefonszam")
    uid                  : str  = alias("Uid")
