from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime
from .. import alias
from . import Group, ValueDescriptor, SubjectDescriptor, Attachment

class Lesson(BaseModel):
    announcedTestUid               : str               = alias("BejelentettSzamonkeresUid")
    attachments                    : list[Attachment]  = alias("Csatolmanyok")
    classGroup                     : Group             = alias("OsztalyCsoport")
    classScheduleNumber            : int               = alias("Oraszam")
    classroom                      : str               = alias("TeremNeve")
    classworkGroupId               : str               = alias("FeladatGroupUid")
    digitalInstrumentType          : str               = alias("DigitalisEszkozTipus")
    digitalPlatformType            : str               = alias("DigitalisPlatformTipus")
    endTime                        : datetime          = alias("VegIdopont")
    homeWorkUid                    : str               = alias("HaziFeladatUid")
    homeworkEditedByStudentEnabled : bool              = alias("IsTanuloHaziFeladatEnabled")
    isDigitalLesson                : bool              = alias("IsDigitalisOra")
    languageTaskGroupId            : str               = alias("NyelviFeladatGroupUid")
    lessonNumber                   : int               = alias("OraEvesSorszama")
    name                           : str               = alias("Nev")
    presence                       : ValueDescriptor   = alias("TanuloJelenlet")
    startTime                      : datetime          = alias("KezdetIdopont")
    state                          : ValueDescriptor   = alias("Allapot")
    subject                        : SubjectDescriptor = alias("Tantargy")
    supplyTeacher                  : str               = alias("HelyettesTanarNeve")
    supportedDigitalInstrumentTypes: list[str]         = alias("DigitalisTamogatoEszkozTipusList")
    teacher                        : str               = alias("TanarNeve")
    topic                          : str               = alias("Tema")
    type                           : ValueDescriptor   = alias("Tipus")
    uid                            : str               = alias("Uid")
