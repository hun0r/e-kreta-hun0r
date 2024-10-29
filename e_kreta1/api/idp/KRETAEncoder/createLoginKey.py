from . import encodeKey

def createLoginKey(userName: str, klik: str, nonce: str) -> str:
    loginKeyPayload = klik.upper() + nonce + userName.upper()
    return encodeKey(loginKeyPayload)