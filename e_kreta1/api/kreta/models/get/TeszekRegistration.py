
from __future__ import annotations
from pydantic import BaseModel
from .. import alias

class TeszekRegistration(BaseModel):
    id                      : str = alias("Id")
    registrationDateAsString: str = alias("RegisztracioIdopontja")
