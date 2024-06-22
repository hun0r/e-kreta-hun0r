import jwt
import requests
import warnings
from .idp_api import IdpApiV1
from ..config import AUTH_HEADER, URL
from ..utils import RequestsHandler

class Session:
    def __init__(self, access_token, refresh_token, auto_revoke, *_, **__) -> None:
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.headers = AUTH_HEADER.copy()
        self.headers["Authorization"] = self.headers["Authorization"].format(self.access_token)
        self.auto_revoke = auto_revoke

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()

    def __del__(self):
        if self.auto_revoke:
            self.close()
            warnings.warn(
                "Your token got automatically revoked. If u want to save the token set the 'auto_revoke' to False",
            )

    def close(self) -> None:
        try:
            IdpApiV1.revokeRefreshToken(self.refresh_token)
            self.refresh_token = None
            self.access_token = None
            self.headers = AUTH_HEADER.copy()
        except: pass

    @classmethod
    def login(cls, userName: str|int, password: str|int , klik: str|int, *, auto_revoke: bool = True, bypass_format: False) -> "Session":
        if not bypass_format:
            try:
                _userName = "".join(filter(str.isdigit, str(userName)))
                _password = "{}{}{}{}-{}{}-{}{}".format(filter(str.isdigit, str(password)))
                _klik = f"klik{"".join(filter(str.isdigit, str(klik)))}"
            except: 
                warnings.warn("invalid format: please consider enabeling bypass_format. (some times the format is not followed)")
                _userName = userName
                _password = password
                _klik = klik
        nonce = IdpApiV1.getNonce()
        login_info = IdpApiV1.login(_userName, _password, _klik, nonce)
        return cls(**login_info, auto_revoke = auto_revoke)
    
    def get_klik(self) -> str:
        return jwt.decode(
            self.access_token, 
            options={"verify_signature": False}, 
            algorithms=["RS256"]
        )["kreta:institute_code"]
    
    def get_url(self) -> str:
        return URL.format(klik=self.get_klik())
    
    def refresh(self) -> None:
        klik = self.get_klik()
        r = IdpApiV1.extendToken(self.refresh_token, klik)
        self.access_token, self.refresh_token = r["access_token"], r["refresh_token"]
        self.headers = AUTH_HEADER.copy()
        self.headers["Authorization"] = self.headers["Authorization"].format(self.access_token)

    def deleteBankAccountNumber(self) -> requests.Response:
        try:
            return RequestsHandler.delete(f'{self.get_url()}/sajat/Bankszamla', headers=self.headers).text
        except:
            self.refresh()
            return RequestsHandler.delete(f'{self.get_url()}/sajat/Bankszamla', headers=self.headers).text

    def deleteReservation(self, uid: str) -> requests.Response:
        try:
            return RequestsHandler.delete(f'{self.get_url()}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
        except:
            self.refresh()
            return RequestsHandler.delete(f'{self.get_url()}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
    
    def downloadAttachment(self, uid: str) -> str:
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/Csatolmany/{uid}', headers=self.headers).text
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/Csatolmany/{uid}', headers=self.headers).text
    
    def getAnnouncedTestsByUids(self, Uids: str = None) -> list:
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/BejelentettSzamonkeresek', headers=self.headers, params={'Uids': Uids}).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/BejelentettSzamonkeresek', headers=self.headers, params={'Uids': Uids}).json()
    
    def getAnnouncedTestsByDate(self, datumTol: str = None, datumIg: str = None) -> list:
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/BejelentettSzamonkeresek', headers=self.headers, params={'datumTol': datumTol, 'datumIg': datumIg}).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/BejelentettSzamonkeresek', headers=self.headers, params={'datumTol': datumTol, 'datumIg': datumIg}).json()
    
    def getClassAverage(self, oktatasiNevelesiFeladatUid: str, tantargyUid: str = None):
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/Ertekelesek/Atlagok/OsztalyAtlagok', headers=self.headers, params={
                'oktatasiNevelesiFeladatUid': oktatasiNevelesiFeladatUid,
                'tantargyUid': tantargyUid
            }).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/Ertekelesek/Atlagok/OsztalyAtlagok', headers=self.headers, params={
                'oktatasiNevelesiFeladatUid': oktatasiNevelesiFeladatUid,
                'tantargyUid': tantargyUid
            }).json()
    
    def getClassMaster(self, Uids: str):
        try:
            return RequestsHandler.get(f'{self.get_url()}/felhasznalok/Alkalmazottak/Tanarok/Osztalyfonokok', headers=self.headers, params={'Uids': Uids}).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/felhasznalok/Alkalmazottak/Tanarok/Osztalyfonokok', headers=self.headers, params={'Uids': Uids}).json()
    
    def getConsultingHour(self, uid: str):
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/Fogadoorak/{uid}', headers=self.headers).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/Fogadoorak/{uid}', headers=self.headers).json()
    
    def getConsultingHours(self, datumTol: str = None, datumIg: str = None) -> list:
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/Fogadoorak', headers=self.headers, params={'datumTol': datumTol, 'datumIg': datumIg}).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/Fogadoorak', headers=self.headers, params={'datumTol': datumTol, 'datumIg': datumIg}).json()
    
    def getDeviceGivenState(self) -> bool | None:
        try:
            return bool(RequestsHandler.get(f'{self.get_url()}/TargyiEszkoz/IsEszkozKiosztva', headers=self.headers).text)
        except:
            self.refresh()
            return bool(RequestsHandler.get(f'{self.get_url()}/TargyiEszkoz/IsEszkozKiosztva', headers=self.headers).text)
    
    def getEvaluations(self) -> list:
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/Ertekelesek', headers=self.headers).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/Ertekelesek', headers=self.headers).json()
    
    def getGroups(self) -> list:
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/OsztalyCsoportok', headers=self.headers).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/OsztalyCsoportok', headers=self.headers).json()
    
    def getGuardian4T(self):
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/GondviseloAdatlap', headers=self.headers).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/GondviseloAdatlap', headers=self.headers).json()
    
    def getHomework(self, id: str):
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/HaziFeladatok/{id}', headers=self.headers).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/HaziFeladatok/{id}', headers=self.headers).json()
    
    def getHomeworks(self, datumTol: str = None, datumIg: str = None):
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/HaziFeladatok', headers=self.headers, params={'datumTol': datumTol, 'datumIg': datumIg}).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/HaziFeladatok', headers=self.headers, params={'datumTol': datumTol, 'datumIg': datumIg}).json()
    
    def getLEPEvents(self):
        try:
            return RequestsHandler.get(f'{self.get_url()}/Lep/Eloadasok', headers=self.headers).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/Lep/Eloadasok', headers=self.headers).json()
    
    def getLesson(self, orarendElemUid: str = None):
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/OrarendElem', headers=self.headers, params={'orarendElemUid': orarendElemUid}).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/OrarendElem', headers=self.headers, params={'orarendElemUid': orarendElemUid}).json()
    
    def getLessons(self, datumTol: str = None, datumIg: str = None):
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/OrarendElemek', headers=self.headers, params={'datumTol': datumTol, 'datumIg': datumIg}).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/OrarendElemek', headers=self.headers, params={'datumTol': datumTol, 'datumIg': datumIg}).json()
    
    def getNotes(self, datumTol: str = None, datumIg: str = None):
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/Feljegyzesek', headers=self.headers, params={'datumTol': datumTol, 'datumIg': datumIg}).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/Feljegyzesek', headers=self.headers, params={'datumTol': datumTol, 'datumIg': datumIg}).json()
    
    def getNoticeBoardItems(self):
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/FaliujsagElemek', headers=self.headers).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/FaliujsagElemek', headers=self.headers).json()
    
    def getOmissions(self, datumTol: str = None, datumIg: str = None) -> list:
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/Mulasztasok', headers=self.headers, params={'datumTol': datumTol, 'datumIg': datumIg}).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/Mulasztasok', headers=self.headers, params={'datumTol': datumTol, 'datumIg': datumIg}).json()
    
    def getRegistrationState(self) -> str:
        """probably a str bool i didnt test it yet"""
        try:
            return RequestsHandler.get(f'{self.get_url()}/TargyiEszkoz/IsRegisztralt', headers=self.headers).text
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/TargyiEszkoz/IsRegisztralt', headers=self.headers).text
    
    def getSchoolYearCalendar(self):
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/Intezmenyek/TanevRendjeElemek', headers=self.headers).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/Intezmenyek/TanevRendjeElemek', headers=self.headers).json()
    
    def getStudent(self):
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/TanuloAdatlap', headers=self.headers).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/TanuloAdatlap', headers=self.headers).json()
            
    def getSubjectAverage(self, oktatasiNevelesiFeladatUid: str):
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/Ertekelesek/Atlagok/TantargyiAtlagok', headers=self.headers, params={'oktatasiNevelesiFeladatUid': oktatasiNevelesiFeladatUid}).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/Ertekelesek/Atlagok/TantargyiAtlagok', headers=self.headers, params={'oktatasiNevelesiFeladatUid': oktatasiNevelesiFeladatUid}).json()
    
    def getTimeTableWeeks(self):
        try:
            return RequestsHandler.get(f'{self.get_url()}/sajat/Intezmenyek/Hetirendek/Orarendi', headers=self.headers).json()
        except:
            self.refresh()
            return RequestsHandler.get(f'{self.get_url()}/sajat/Intezmenyek/Hetirendek/Orarendi', headers=self.headers).json()
    
    def postBankAccountNumber(self, BankszamlaSzam: str, BankszamlaTulajdonosNeve: str, BankszamlaTulajdonosTipusId: str, SzamlavezetoBank: str):
        try:
            return RequestsHandler.post(f'{self.get_url()}/sajat/Bankszamla', headers=self.headers, data=f'BankAccountNumberPostDto(bankAccountNumber={BankszamlaSzam}, bankAccountOwnerType={BankszamlaTulajdonosTipusId}, bankAccountOwnerName={BankszamlaTulajdonosNeve}, bankName={SzamlavezetoBank})').text
        except:
            self.refresh()
            return RequestsHandler.post(f'{self.get_url()}/sajat/Bankszamla', headers=self.headers, data=f'BankAccountNumberPostDto(bankAccountNumber={BankszamlaSzam}, bankAccountOwnerType={BankszamlaTulajdonosTipusId}, bankAccountOwnerName={BankszamlaTulajdonosNeve}, bankName={SzamlavezetoBank})').text
    
    def postContact(self, email, telefonszam):
        try:
            return RequestsHandler.post(f'{self.get_url()}/sajat/Elerhetoseg', headers=self.headers, data={'email': email, 'telefonszam': telefonszam}).text
        except:
            self.refresh()
            return RequestsHandler.post(f'{self.get_url()}/sajat/Elerhetoseg', headers=self.headers, data={'email': email, 'telefonszam': telefonszam}).text
    
    def postCovidForm(self):
        try:
            return RequestsHandler.post(f'{self.get_url()}/Bejelentes/Covid', headers=self.headers).text
        except:
            self.refresh()
            return RequestsHandler.post(f'{self.get_url()}/Bejelentes/Covid', headers=self.headers).text
    
    def postReservation(self, uid: str):
        try:
            return RequestsHandler.post(f'{self.get_url()}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
        except:
            self.refresh()
            return RequestsHandler.post(f'{self.get_url()}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
    
    def updateLepEventPermission(self, EloadasId: str, Dontes: bool):
        try:
            return RequestsHandler.post(f'{self.get_url()}/Lep/Eloadasok/GondviseloEngedelyezes', headers=self.headers, data=f'LepEventGuardianPermissionPostDto(eventId={EloadasId}, isPermitted={str(Dontes)})').text
        except:
            self.refresh()
            return RequestsHandler.post(f'{self.get_url()}/Lep/Eloadasok/GondviseloEngedelyezes', headers=self.headers, data=f'LepEventGuardianPermissionPostDto(eventId={EloadasId}, isPermitted={str(Dontes)})').text
