import base64
import hashlib
import hmac

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
