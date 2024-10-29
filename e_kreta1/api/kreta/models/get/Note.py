from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime
from .. import alias
from . import Group, ValueDescriptor

class Note(BaseModel):
    content         : str             = alias("Tartalom")
    contentFormatted: str             = alias("TartalomFormazott")
    creatingTime    : datetime        = alias("KeszitesDatuma")
    date            : datetime        = alias("Datum")
    group           : Group           = alias("OsztalyCsoport")
    seenByTutelary  : datetime        = alias("LattamozasDatuma")
    teacher         : str             = alias("KeszitoTanarNeve")
    title           : str             = alias("Cim")
    type            : ValueDescriptor = alias("Tipus")
    uid             : str             = alias("Uid")

    
  
  
      



           
      
        


        
                 
                     
             
      
                       
        
      
     
    