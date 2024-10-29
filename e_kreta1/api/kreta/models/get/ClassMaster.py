from __future__ import annotations
from pydantic import BaseModel
from .. import alias
from . import ValueDescriptor

class ClassMaster(BaseModel):
    listOfClass: list[SchoolClass] = alias("Osztalyai")
    teacher    : Teacher           = alias("Tanar")
    uid        : str               = alias("Uid")

class Teacher(BaseModel):
    employee: Employee = alias("Alkalmazott")
    uid     : str      = alias("Uid")

class Employee(BaseModel):
    email    : list[Email] = alias("Emailek")
    name     : str         = alias("Nev")
    phoneList: list[Phone] = alias("Telefonok")
    uid      : str         = alias("Uid")

class Email(BaseModel):
    email: str = alias("Email")
    uid  : str = alias("Uid")

class Phone(BaseModel):
    phone: str = alias("Telefonszam")
    uid  : str = alias("Uid")


class SchoolClass(BaseModel):
    category: ValueDescriptor = alias("OktatasNevelesiKategoria")
    name    : str             = alias("Nev")
    uid     : str             = alias("Uid")