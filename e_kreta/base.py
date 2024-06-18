import base, dc
import jwt, requests, hashlib, base64, hmac

# set default headers
HEADERS = {"User-Agent": "hu.ekreta.student/3.0.4/7.1.2/25"}
AUTH_HEADER = {
            "Authorization": "Bearer {}",
            "User-Agent": "hu.ekreta.tanulo/1.0.5/Android/0/0",
        }

# url format
URL = "https://{klik}.e-kreta.hu/ellenorzo/V3"
# global comunicator
proxies: dict = None


class session:
    def __init__(self, access_token, refresh_token, *_, **__) -> None:
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.headers = AUTH_HEADER.copy()
        self.headers["Authorization"] = self.headers["Authorization"].format(self.access_token)

    def __del__(self) -> None:
        IdpApiV1.revokeRefreshToken(self.refresh_token)

    def close(self) -> None:
        IdpApiV1.revokeRefreshToken(self.refresh_token)

    @classmethod
    def login(cls, userName: str|int, password: str|int , klik: str|int) -> "session":
        nonce = IdpApiV1.getNonce()
        login_info = IdpApiV1.login(userName, password, klik, nonce)
        
        return cls(**login_info)
    
    def get_klik(self) -> str:
        return jwt.decode(
            self.access_token, 
            options={"verify_signature": False}, 
            algorithms=["RS256"]
        )["kreta:institute_code"]
    
    def get_url(self) -> str:
        return URL.format(klik=self.get_klik())
    
    def refresh(self)->None:
        klik=self.get_klik
        r=IdpApiV1.extendToken(self.refresh_token,klik)
        self.access_token,self.refresh_token=r["access_token"],r["refresh_token"]
        self.headers = AUTH_HEADER.copy()
        self.headers["Authorization"] = self.headers["Authorization"].format(self.access_token)
    
    def deleteBankAccountNumber(self) -> requests.Response:
        try: return requests.delete(f'{self.get_url()}/sajat/Bankszamla', headers=self.headers).text
        except:
            self.refresh()
            return requests.delete(f'{self.get_url()}/sajat/Bankszamla', headers=self.headers).text
    
    def deleteReservation(self, uid: str) -> requests.Response:
        try: return requests.delete(f'{self.get_url()}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
        except:
            self.refresh()
            return requests.delete(f'{self.get_url()}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
    
    def downloadAttachment(self, uid: str) -> str:
        try: return requests.get(f'{self.get_url()}/sajat/Csatolmany/{uid}', headers=self.headers).text
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/Csatolmany/{uid}', headers=self.headers).text
    
    def getAnnouncedTests(self, Uids: str = None) -> list:
        try: return requests.get(f'{self.get_url()}/sajat/BejelentettSzamonkeresek', params={
                'Uids': Uids
                }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/BejelentettSzamonkeresek', params={
                'Uids': Uids
            }, headers=self.headers).json()
    
    def getAnnouncedTests(self, datumTol: str = None, datumIg: str = None) -> list:
        try: return requests.get(f'{self.get_url()}/sajat/BejelentettSzamonkeresek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/BejelentettSzamonkeresek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
    
    def getClassAverage(self, oktatasiNevelesiFeladatUid: str, tantargyUid: str = None):
        try:
            return requests.get(f'{self.get_url()}/sajat/Ertekelesek/Atlagok/OsztalyAtlagok', params={
                'oktatasiNevelesiFeladatUid': oktatasiNevelesiFeladatUid,
                'tantargyUid': tantargyUid
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/Ertekelesek/Atlagok/OsztalyAtlagok', params={
                'oktatasiNevelesiFeladatUid': oktatasiNevelesiFeladatUid,
                'tantargyUid': tantargyUid
            }, headers=self.headers).json()
    
    def getClassMaster(self, Uids: str):
        try:
            return requests.get(f'{self.get_url()}/felhasznalok/Alkalmazottak/Tanarok/Osztalyfonokok', params={
                'Uids': Uids
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/felhasznalok/Alkalmazottak/Tanarok/Osztalyfonokok', params={
                'Uids': Uids
            }, headers=self.headers).json()
    
    def getConsultingHour(self, uid: str):
        try:
            return requests.get(f'{self.get_url()}/sajat/Fogadoorak/{uid}', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/Fogadoorak/{uid}', headers=self.headers).json()
    
    def getConsultingHours(self, datumTol: str = None, datumIg: str = None) -> list:
        try:
            return requests.get(f'{self.get_url()}/sajat/Fogadoorak', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/Fogadoorak', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
    
    def getDeviceGivenState(self) -> bool | None:
        try:
            return bool(requests.get(f'{self.get_url()}/TargyiEszkoz/IsEszkozKiosztva', headers=self.headers).text)
        except:
            self.refresh()
            return bool(requests.get(f'{self.get_url()}/TargyiEszkoz/IsEszkozKiosztva', headers=self.headers).text)
    
    def getEvaluations(self) -> list:
        try:
            return requests.get(f'{self.get_url()}/sajat/Ertekelesek', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/Ertekelesek', headers=self.headers).json()
    
    def getGroups(self) -> list:
        try:
            return requests.get(f'{self.get_url()}/sajat/OsztalyCsoportok', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/OsztalyCsoportok', headers=self.headers).json()
    
    def getGuardian4T(self):
        try:
            return requests.get(f'{self.get_url()}/sajat/GondviseloAdatlap', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/GondviseloAdatlap', headers=self.headers).json()
    
    def getHomework(self, id: str):
        try:
            return requests.get(f'{self.get_url()}/sajat/HaziFeladatok/{id}', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/HaziFeladatok/{id}', headers=self.headers).json()
    
    def getHomeworks(self, datumTol: str = None, datumIg: str = None):
        try:
            return requests.get(f'{self.get_url()}/sajat/HaziFeladatok', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/HaziFeladatok', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
    
    def getLEPEvents(self):
        try:
            return requests.get(f'{self.get_url()}/Lep/Eloadasok', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/Lep/Eloadasok', headers=self.headers).json()
    
    def getLesson(self, orarendElemUid: str = None):
        try:
            return requests.get(f'{self.get_url()}/sajat/OrarendElem', params={
                'orarendElemUid': orarendElemUid
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/OrarendElem', params={
                'orarendElemUid': orarendElemUid
            }, headers=self.headers).json()
    
    def getLessons(self, datumTol: str = None, datumIg: str = None):
        try:
            return requests.get(f'{self.get_url()}/sajat/OrarendElemek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/OrarendElemek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
    
    def getNotes(self, datumTol: str = None, datumIg: str = None):
        try:
            return requests.get(f'{self.get_url()}/sajat/Feljegyzesek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/Feljegyzesek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
    
    def getNoticeBoardItems(self):
        try:
            return requests.get(f'{self.get_url()}/sajat/FaliujsagElemek', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/FaliujsagElemek', headers=self.headers).json()
    
    def getOmissions(self, datumTol: str = None, datumIg: str = None) -> list:
        try:
            return requests.get(f'{self.get_url()}/sajat/Mulasztasok', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/Mulasztasok', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
    
    def getRegistrationState(self) -> str:
        """probably a str bool i didnt test it yet"""
        try:
            return requests.get(f'{self.get_url()}/TargyiEszkoz/IsRegisztralt', headers=self.headers).text
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/TargyiEszkoz/IsRegisztralt', headers=self.headers).text
    
    def getSchoolYearCalendar(self):
        try:
            return requests.get(f'{self.get_url()}/sajat/Intezmenyek/TanevRendjeElemek', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/Intezmenyek/TanevRendjeElemek', headers=self.headers).json()
    
    def getStudent(self):
        try:
            return requests.get(f'{self.get_url()}/sajat/TanuloAdatlap', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/TanuloAdatlap', headers=self.headers).json()
            
    def getSubjectAverage(self, oktatasiNevelesiFeladatUid: str):
        try:
            return requests.get(f'{self.get_url()}/sajat/Ertekelesek/Atlagok/TantargyiAtlagok', params={
                'oktatasiNevelesiFeladatUid': oktatasiNevelesiFeladatUid
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/Ertekelesek/Atlagok/TantargyiAtlagok', params={
                'oktatasiNevelesiFeladatUid': oktatasiNevelesiFeladatUid
            }, headers=self.headers).json()
    
    def getTimeTableWeeks(self):
        try:
            return requests.get(f'{self.get_url()}/sajat/Intezmenyek/Hetirendek/Orarendi', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.get_url()}/sajat/Intezmenyek/Hetirendek/Orarendi', headers=self.headers).json()
    
    def postBankAccountNumber(self, 
        BankszamlaSzam: str, 
        BankszamlaTulajdonosNeve: str, 
        BankszamlaTulajdonosTipusId: str, 
        SzamlavezetoBank: str
        ):
        try:
            return requests.post(f'{self.get_url()}/sajat/Bankszamla', data=f'BankAccountNumberPostDto(bankAccountNumber={BankszamlaSzam}, bankAccountOwnerType={BankszamlaTulajdonosTipusId}, bankAccountOwnerName={BankszamlaTulajdonosNeve}, bankName={SzamlavezetoBank})', headers=self.headers).text
        except:
            self.refresh()
            return requests.post(f'{self.get_url()}/sajat/Bankszamla', data=f'BankAccountNumberPostDto(bankAccountNumber={BankszamlaSzam}, bankAccountOwnerType={BankszamlaTulajdonosTipusId}, bankAccountOwnerName={BankszamlaTulajdonosNeve}, bankName={SzamlavezetoBank})', headers=self.headers).text
    
    def postContact(self, email, telefonszam):
        try:
            return requests.post(f'{self.get_url()}/sajat/Elerhetoseg', data={
                'email': email,
                'telefonszam': telefonszam
            }, headers=self.headers).text
        except:
            self.refresh()
            return requests.post(f'{self.get_url()}/sajat/Elerhetoseg', data={
                'email': email,
                'telefonszam': telefonszam
            }, headers=self.headers).text
    
    def postCovidForm(self):
        try:
            return requests.post(f'{self.get_url()}/Bejelentes/Covid', headers=self.headers).text
        except:
            self.refresh()
            return requests.post(f'{self.get_url()}/Bejelentes/Covid', headers=self.headers).text
    
    def postReservation(self, uid: str):
        try:
            return requests.post(f'{self.get_url()}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
        except:
            self.refresh()
            return requests.post(f'{self.get_url()}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
    
    def updateLepEventPermission(self, EloadasId: str, Dontes: bool):
        try:
            return requests.post(f'{self.get_url()}/Lep/Eloadasok/GondviseloEngedelyezes', data=f'LepEventGuardianPermissionPostDto(eventId={EloadasId}, isPermitted={str(Dontes)})', headers=self.headers).text
        except:
            self.refresh()
            return requests.post(f'{self.get_url()}/Lep/Eloadasok/GondviseloEngedelyezes', data=f'LepEventGuardianPermissionPostDto(eventId={EloadasId}, isPermitted={str(Dontes)})', headers=self.headers).text

class KRETAEncoder:
    KeyProd = "baSsxOwlU1jM".encode("utf-8")

    @classmethod
    def encodeRefreshToken(cls, refreshToken: str) -> str:
        return cls.encodeKey(refreshToken)
    
    @classmethod
    def createLoginKey(cls, userName: str, klik: str, nonce: str) -> str:
        loginKeyPayload = klik.upper() + nonce + userName.upper()
        return cls.encodeKey(loginKeyPayload)

    @classmethod
    def encodeKey(cls, payload: str) -> str:
        return base64.b64encode(
            hmac.new(
                cls.KeyProd, payload.encode("utf-8"), digestmod=hashlib.sha512
            ).digest()
        ).decode("utf-8")

# Az E-Kréta API-hoz szükséges kommunikáció kezelő
class IdpApiV1:

    @staticmethod
    def extendToken(refresh_token: str, klik: str) -> dict: 
        refresh_token_data = {
            "refresh_token": refresh_token,
            "institute_code": klik,
            "grant_type": "refresh_token",
            "client_id": "kreta-ellenorzo-mobile-android",
            "refresh_user_data": False,
        }

        refreshTokenHeaders = HEADERS.copy()
        refreshTokenHeaders.update(
            {
                "X-AuthorizationPolicy-Key": KRETAEncoder.encodeRefreshToken(
                    refresh_token
                ),
                "X-AuthorizationPolicy-Version": "v2",
            }
        )

        return requests.post(
            "https://idp.e-kreta.hu/connect/token",
            data=refresh_token_data,
            headers=refreshTokenHeaders,
            proxies=proxies,
        ).json()

    @staticmethod
    def getNonce() -> str | None:
        return requests.get(
            "https://idp.e-kreta.hu/nonce", headers=HEADERS
        ).text

    @staticmethod
    def login(
        userName: str, password: str, klik: str, nonce: str
    ) -> dict:
    
        login_data = {
            "userName": userName,
            "password": password,
            "institute_code": klik,
            "grant_type": "password",
            "client_id": "kreta-ellenorzo-mobile-android",
        }

        loginHeaders = HEADERS.copy()
        loginHeaders.update(
            {
                "X-AuthorizationPolicy-Nonce": nonce,
                "X-AuthorizationPolicy-Key": KRETAEncoder.createLoginKey(
                    userName, klik, nonce
                ),
                "X-AuthorizationPolicy-Version": "v2",
            }
        )

        return requests.post(
            "https://idp.e-kreta.hu/connect/token",
            data=login_data,
            headers=loginHeaders,
            proxies=proxies,
        ).json()
    
    @staticmethod
    def revokeRefreshToken(refresh_token: str) -> str:

        revokeRefreshTokenData = {
            "token": refresh_token,
            "client_id": "kreta-ellenorzo-mobile-android",
            "token_type": "refresh token",
        }

        return requests.post(
            "https://idp.e-kreta.hu/connect/revocation",
            data=revokeRefreshTokenData,
            headers=HEADERS,
            proxies=proxies,
        ).text
