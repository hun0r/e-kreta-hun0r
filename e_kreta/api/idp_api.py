from ..utils import KRETAEncoder
from ..utils import RequestsHandler
from ..config import HEADERS, proxies

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
    def login(userName: str, password: str, klik: str, nonce: str) -> dict:
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
                "X-AuthorizationPolicy-Key": KRETAEncoder.createLoginKey(userName, klik, nonce),
                "X-AuthorizationPolicy-Version": "v2",
            }
        )

        return RequestsHandler.post(
            "https://idp.e-kreta.hu/connect/token",
            headers=loginHeaders,
            data=login_data,
            proxies=proxies,
        ).json()

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
