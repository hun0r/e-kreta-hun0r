from __future__ import annotations
from pydantic import BaseModel
from .. import alias

class Contact(BaseModel):
    email          : str  = alias("Email")
    id             : str  = alias("Id")
    isEmailVerified: bool = alias("IsEmailMegerositve")
    phoneNumber    : str  = alias("Telefonszam")
