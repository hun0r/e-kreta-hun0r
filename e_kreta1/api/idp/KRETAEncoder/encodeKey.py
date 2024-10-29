import base64
import hashlib
import hmac

def encodeKey(cls, payload: str) -> str:
    return base64.b64encode(
        hmac.new(
            cls.KeyProd, payload.encode("utf-8"), digestmod=hashlib.sha512
        ).digest()
    ).decode("utf-8")