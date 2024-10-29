from requests import post
from ..config import HEADERS, proxies

def revokeRefreshToken(refresh_token: str) -> str:
    revokeRefreshTokenData = {
        "token": refresh_token,
        "client_id": "kreta-ellenorzo-mobile-android",
        "token_type": "refresh token",
    }

    return post(
        "https://idp.e-kreta.hu/connect/revocation",
        headers=HEADERS,
        data=revokeRefreshTokenData,
        proxies=proxies,
    ).text
