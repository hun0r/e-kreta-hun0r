from __future__ import annotations
from pydantic import BaseModel
from .. import alias

class HomeworkStatePost(BaseModel):
    isDone            : bool = alias("IsMegoldva")
    teacherHomeworkUid: str  = alias("TanarHaziFeladatUid")
