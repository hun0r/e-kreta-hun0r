from __future__ import annotations
from pydantic import BaseModel
from .. import alias

class LepEventGuardianPermissionPost(BaseModel):
    eventId    : str  = alias("EloadasId")
    IsPermitted: bool = alias("Dontes")
