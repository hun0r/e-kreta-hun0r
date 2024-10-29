from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime
from .. import alias
from . import SubjectDescriptor

class SubjectAverage(BaseModel):
    averageNumber           : float                 = alias("Atlag")                        
    averagesInTime          : list[AverageWithTime] = alias("AtlagAlakulasaIdoFuggvenyeben")
    sortIndex               : int                   = alias("SortIndex")                    
    subject                 : SubjectDescriptor     = alias("Tantargy")                     
    sumOfWeightedEvaluations: float                 = alias("SulyozottOsztalyzatOsszege")   
    sumOfWeights            : float                 = alias("SulyozottOsztalyzatSzama")     
    uid                     : str                   = alias("Uid")                          

class AverageWithTime(BaseModel):
    average: float    = alias("Atlag")
    date   : datetime = alias("Datum")
