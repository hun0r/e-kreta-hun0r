from ..utils import KRETAEncoder
from ..utils import RequestsHandler
from ..config import HEADERS, proxies
from requests import Session

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
                "X-AuthorizationPolicy-Key": KRETAEncoder.encodeRefreshToken(refresh_token),
                "X-AuthorizationPolicy-Version": "v2",
            }
        )

        return RequestsHandler.post(
            "https://idp.e-kreta.hu/connect/token",
            headers=refreshTokenHeaders,
            data=refresh_token_data,
            proxies=proxies,
        ).json()

    @staticmethod
    def getNonce() -> str | None:
        return RequestsHandler.get("https://idp.e-kreta.hu/nonce", headers=HEADERS).text

    @staticmethod
    def login(UserName: str, Password: str, klik: str) -> dict:
        session = Session()

        # main html
        url = "https://idp.e-kreta.hu/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fprompt%3Dlogin%26nonce%3DwylCrqT4oN6PPgQn2yQB0euKei9nJeZ6_ffJ-VpSKZU%26response_type%3Dcode%26code_challenge_method%3DS256%26scope%3Dopenid%2520email%2520offline_access%2520kreta-ellenorzo-webapi.public%2520kreta-eugyintezes-webapi.public%2520kreta-fileservice-webapi.public%2520kreta-mobile-global-webapi.public%2520kreta-dkt-webapi.public%2520kreta-ier-webapi.public%26code_challenge%3DHByZRRnPGb-Ko_wTI7ibIba1HQ6lor0ws4bcgReuYSQ%26redirect_uri%3Dhttps%253A%252F%252Fmobil.e-kreta.hu%252Fellenorzo-student%252Fprod%252Foauthredirect%26client_id%3Dkreta-ellenorzo-student-mobile-ios%26state%3Drefilc_student_mobile%26suppressed_prompt%3Dlogin"
        request0 = session.get(url)

        # login form
        __RequestVerificationToken = request0.text.partition('<input name="__RequestVerificationToken" type="hidden" value="')[2].partition('" /></form>')[0]

        url = "https://idp.e-kreta.hu/account/login"

        payload = f'ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fprompt%3Dlogin%26nonce%3DwylCrqT4oN6PPgQn2yQB0euKei9nJeZ6_ffJ-VpSKZU%26response_type%3Dcode%26code_challenge_method%3DS256%26scope%3Dopenid%2520email%2520offline_access%2520kreta-ellenorzo-webapi.public%2520kreta-eugyintezes-webapi.public%2520kreta-fileservice-webapi.public%2520kreta-mobile-global-webapi.public%2520kreta-dkt-webapi.public%2520kreta-ier-webapi.public%26code_challenge%3DHByZRRnPGb-Ko_wTI7ibIba1HQ6lor0ws4bcgReuYSQ%26redirect_uri%3Dhttps%253A%252F%252Fmobil.e-kreta.hu%252Fellenorzo-student%252Fprod%252Foauthredirect%26client_id%3Dkreta-ellenorzo-student-mobile-ios%26state%3Drefilc_student_mobile%26suppressed_prompt%3Dlogin&\
        IsTemporaryLogin=False&\
        UserName={UserName}&\
        Password={Password}&\
        InstituteCode={klik}&\
        loginType=InstituteLogin&\
        __RequestVerificationToken={__RequestVerificationToken}'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        }
        url = "https://idp.e-kreta.hu/account/login"
        session.post(url, data=payload, headers=headers)

        # cookies -> code
        url = "https://idp.e-kreta.hu/connect/authorize/callback?prompt=login&nonce=wylCrqT4oN6PPgQn2yQB0euKei9nJeZ6_ffJ-VpSKZU&response_type=code&code_challenge_method=S256&scope=openid%20email%20offline_access%20kreta-ellenorzo-webapi.public%20kreta-eugyintezes-webapi.public%20kreta-fileservice-webapi.public%20kreta-mobile-global-webapi.public%20kreta-dkt-webapi.public%20kreta-ier-webapi.public&code_challenge=HByZRRnPGb-Ko_wTI7ibIba1HQ6lor0ws4bcgReuYSQ&redirect_uri=https%3A%2F%2Fmobil.e-kreta.hu%2Fellenorzo-student%2Fprod%2Foauthredirect&client_id=kreta-ellenorzo-student-mobile-ios&state=refilc_student_mobile&suppressed_prompt=login"
        response1 = session.get(url, allow_redirects=False)


        code = response1.headers["location"]\
            .removeprefix("https://mobil.e-kreta.hu/ellenorzo-student/prod/oauthredirect?code=")\
            .partition("&scope=openid%20email%20offline_access%20kreta-ellenorzo-webapi.public%20kreta-eugyintezes-webapi.public%20kreta-fileservice-webapi.public%20kreta-mobile-global-webapi.public%20kreta-dkt-webapi.public%20kreta-ier-webapi.public&state=refilc_student_mobile&session_state=")\
            [0]

        data = {
            "code": code,
            "code_verifier": "DSpuqj_HhDX4wzQIbtn8lr8NLE5wEi1iVLMtMK0jY6c",
            "redirect_uri": "https://mobil.e-kreta.hu/ellenorzo-student/prod/oauthredirect",
            "client_id": "kreta-ellenorzo-student-mobile-ios",
            "grant_type": "authorization_code"
        }

        # code -> jwt
        response3 = session.post(
            "https://idp.e-kreta.hu"+"/connect/token",
            data=data
        )
        return response3

    @staticmethod
    def revokeRefreshToken(refresh_token: str) -> str:
        revokeRefreshTokenData = {
            "token": refresh_token,
            "client_id": "kreta-ellenorzo-mobile-android",
            "token_type": "refresh token",
        }

        return RequestsHandler.post(
            "https://idp.e-kreta.hu/connect/revocation",
            headers=HEADERS,
            data=revokeRefreshTokenData,
            proxies=proxies,
        ).text
