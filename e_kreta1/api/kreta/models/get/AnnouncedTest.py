from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime
from .. import alias
from . import Group, ValueDescriptor, SubjectDescriptor

class AnnouncedTest(BaseModel):
    subjectName        : str               = alias("TantargyNeve")
    announcedAt        : datetime          = alias("BejelentesDatuma")
    classScheduleNumber: int               = alias("OrarendiOraOraszama")
    date               : datetime          = alias("Datum")
    group              : Group             = alias("OsztalyCsoport")
    mode               : ValueDescriptor   = alias("Modja")
    subject            : SubjectDescriptor = alias("Tantargy")
    teacher            : str               = alias("RogzitoTanarNeve")
    theme              : str               = alias("Temaja")
    uid                : str               = alias("Uid")

                
                        
                        
                 
          
         
            
            
          
        










