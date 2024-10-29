from __future__ import annotations
from pydantic import BaseModel
from .. import alias

class BankAccountNumberPost(BaseModel):
    bankAccountNumber   : str = alias("BankszamlaSzam")
    bankAccountOwnerName: str = alias("BankszamlaTulajdonosNeve")
    bankAccountOwnerType: int = alias("BankszamlaTulajdonosTipusId")
    bankName            : str = alias("SzamlavezetoBank")
    