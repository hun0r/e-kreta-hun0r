from __future__ import annotations
from pydantic import BaseModel
from .. import alias
from . import SubjectDescriptor, Group, Attachment

class Homework(BaseModel):
    subjectName             : str               = alias("TantargyNeve") 
    attachmentList          : list[Attachment]  = alias("Csatolmanyok") 
    createDateAsString      : str               = alias("RogzitesIdopontja") 
    deadlineDateAsString    : str               = alias("HataridoDatuma") 
    group                   : Group             = alias("OsztalyCsoport")
    isAllowToAttachFile     : bool              = alias("IsCsatolasEngedelyezes") 
    isDone                  : bool              = alias("IsMegoldva") 
    isStudentHomeworkEnabled: bool              = alias("IsTanuloHaziFeladatEnabled") 
    isTeacherRecorded       : bool              = alias("IsTanarRogzitette") 
    recordDateAsString      : str               = alias("FeladasDatuma") 
    recorderTeacherName     : str               = alias("RogzitoTanarNeve") 
    subject                 : SubjectDescriptor = alias("Tantargy") 
    submitable              : bool              = alias("IsBeadhato") 
    text                    : str               = alias("Szoveg") 
    uid                     : str               = alias("Uid")
