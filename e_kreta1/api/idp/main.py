from typing import Self
import requests
from datetime import datetime, timedelta
from . import login, extendToken, revokeRefreshToken
from e_kreta1.models.auth import (
    AccessToken
)
from e_kreta1.models import (
    delete,
    get,
    post
)


class Session:
    URL = "https://{institute_code}.e-kreta.hu/ellenorzo/V3/sajat"
    AUTH_HEADER = {
        "Authorization": "",
        "User-Agent": "hu.ekreta.tanulo/1.0.5/Android/0/0",
    }

    def __init__(self, token_type: str, access_token: str, refresh_token: str, id_token: str = None, expires_in: int = None, scope: str = None) -> None:
        self.access_token = AccessToken(token_type=token_type, access_token=access_token, expires_in=expires_in, scope=scope)
        self.refresh_token = refresh_token

    def __enter__(self) -> Self:
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass

    def __del__(self) -> None:
        self.close()

    def close(self) -> None:
        revokeRefreshToken(self.refresh_token)

    @classmethod
    def login(cls) -> Self:
        return cls(**login())

    @property
    def institute_code(self) -> str:
        return self.access_token.kreta_institute_code
    
    @property
    def url(self) -> str:
        return self.URL.format(institute_code=self.institute_code())
    
    @property
    def headers(self) -> dict:
        if self.access_token.isExpired():
            self.refresh()
        headers = self.AUTH_HEADER.copy()
        headers.update({"Authorization": f"{self.access_token}"})
        return headers
    
    def refresh(self) -> None:
        tokens = extendToken(self.refresh_token, self.institute_code())
        self.access_token, self.refresh_token = AccessToken(tokens["access_token"], tokens["token_type"]), tokens["refresh_token"]

    

#    def getClassMaster(self, Uids: str): ...
#    def getCounsultingHour(self, uid: str): ...
#    def getConsultingHoursByDate(self, from_date: str, to_date: str): ...
#    def getDeviceGivenState(self): ...
#    def getEvaluations(self): ...
#    def getGroups(self): ...
#    def getGuardian4T(self): ...
#    def getHomework(self, id: str): ...
#    def getHomeworksByDate(self, from_date: str, to_date: str): ...
#    def getLEPEvents(self): ...
#    def getLesson(self, id: str): ...
#    def getLessonsByDate(self, from_date: str, to_date: str): ...
#    def getNotesByDate(self, from_date: str, to_date: str): ...
#    def getNoticeBoardItems(self): ...
#    def getOmissionsByDate(self, from_date: str, to_date: str): ...
#    def getRegistrationState(self): ...
#    def getSchoolYearCalendar(self): ...
#    def getStudent(self): ...
#    def getSubjectAverage(self, EducationalTaskUid: str): ...
#    def getTimeTableWeeks(self): ...
#    def postBankAccountNumber(self, BancAccountNumber: str, BankAccountOwnerName: str, BankAccountOwnerTypeId: str, AccountManagerBank: str): ...
#    def postContact(self, email: str, phonenumber: str): ...
#    def postCovidForm(self): ...
#    def postReservation(self, uid: str): ...
#    def updateLepEventPermission(self, PresentationId: str, Decision: bool): ...
