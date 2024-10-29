from .KRETAEncoder import encodeKey
from requests import post
from ..config import HEADERS, proxies

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
            "X-AuthorizationPolicy-Key": encodeKey(refresh_token),
            "X-AuthorizationPolicy-Version": "v2",
        }
    )

    return post(
        "https://idp.e-kreta.hu/connect/token",
        headers=refreshTokenHeaders,
        data=refresh_token_data,
        proxies=proxies,
    ).json()