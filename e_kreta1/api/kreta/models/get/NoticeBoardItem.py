from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime
from .. import alias

class NoticeBoardItem(BaseModel):
    content        : str      = alias("Tartalom")
    expireEndTime  : datetime = alias("ErvenyessegVege")
    expireStartTime: datetime = alias("ErvenyessegKezdete")
    madeBy         : str      = alias("RogzitoNeve")
    title          : str      = alias("Cim")
    uid            : str      = alias("Uid")
