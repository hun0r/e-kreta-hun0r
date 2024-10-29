from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime
from .. import alias
from . import Teacher

class ConsultingHourList(BaseModel):
    consultingHours   : list[ConsultingHour] = alias("Fogadoorak")
    teacherDescriptior: Teacher              = alias("Tantargy")

class ConsultingHour(BaseModel):
    classroomDescriptor    : UidNameStructure             = alias("Terem")
    consultingHourTimeSlots: list[ConsultingHourTimeSlot] = alias("Idopontok")
    deadline               : datetime                     = alias("JelentkezesHatarido")
    endTime                : datetime                     = alias("VegIdopont")
    isReservationEnabled   : bool                         = alias("IsJelentkezesFeatureEnabled")
    startTime              : datetime                     = alias("KezdoIdopont")
    uid                    : str                          = alias("Uid")

class ConsultingHourTimeSlot(BaseModel):
    endTimeAsString  : datetime = alias("VegIdopont")
    isReservedByMe   : bool     = alias("IsJelentkeztem")
    startTimeAsString: datetime = alias("KezdoIdopont")
    uid              : str      = alias("Uid")

class UidNameStructure(BaseModel):
    name: str = alias("Nev")
    uid : str = alias("Uid")