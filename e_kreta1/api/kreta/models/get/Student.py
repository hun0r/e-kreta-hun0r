from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime
from .. import alias
from . import Guardian

class Student(BaseModel):
    addressDataList: list[str]   = alias("Cimek")
    bankAccount    : BankAccount    = alias("Bankszamla")
    dayOfBirth     : int            = alias("SzuletesiNap")
    emailAddress   : str            = alias("EmailCim")
    guardianList   : list[Guardian] = alias("Gondviselok")
    instituteCode  : str            = alias("IntezmenyAzonosito")
    instituteName  : str            = alias("IntezmenyNev")
    institution    : Institution    = alias("Intezmeny")
    monthOfBirth   : int            = alias("SzuletesiHonap")
    mothersName    : str            = alias("AnyjaNeve")
    name           : str            = alias("Nev")
    nameOfBirth    : str            = alias("SzuletesiNev")
    phoneNumber    : str            = alias("Telefonszam")
    placeOfBirth   : str            = alias("SzuletesiHely")
    schoolYearUID  : int            = alias("TanevUid")
    uid            : str            = alias("Uid")
    yearOfBirth    : int            = alias("SzuletesiEv")
    @property
    def birthDate(self) -> datetime:
        return datetime(self.yearOfBirth, self.monthOfBirth, self.dayOfBirth)

class BankAccount(BaseModel):
    accountNumber: str  = alias("BankszamlaSzam")
    isReadOnly   : bool = alias("IsReadOnly")
    ownerName    : str  = alias("BankszamlaTulajdonosNeve")
    ownerType    : int  = alias("BankszamlaTulajdonosTipusId")

class Institution(BaseModel):
    customizationSettings: CustomizationSettings = alias("TestreszabasBeallitasok")
    shortName            : str                   = alias("RovidNev")
    systemModuleList     : list[SystemModule]    = alias("Rendszermodulok")
    uid                  : str                   = alias("Uid")

class CustomizationSettings(BaseModel):
    delayOfNotifications : int      = alias("ErtekelesekMegjelenitesenekKesleltetesenekMerteke") # TODO: minutes, hours or days?
    """minutes hours or days?"""
    isClassAverageVisible: bool     = alias("IsOsztalyAtlagMegjeleniteseEllenorzoben")
    isContactDataEditable: bool     = alias("IsElerhetosegSzerkesztheto")
    isLessonsThemeVisible: bool     = alias("IsTanorakTemajaMegtekinthetoEllenorzoben")
    nextServerDeploy     : datetime = alias("KovetkezoTelepitesDatuma")

class SystemModule(BaseModel):
    isActive: bool = alias("IsAktiv")
    type    : str  = alias("Tipus")
    url     : str  = alias("Url")
