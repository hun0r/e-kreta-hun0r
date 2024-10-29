from .main import Session
from . import KRETAEncoder
from .login import login
from .extendToken import extendToken
from .revokeRefreshToken import revokeRefreshToken
client_id = "kreta-ellenorzo-student-mobile-ios"
URL = "https://idp.e-kreta.hu"

__all__ = ["Session", "KRETAEncoder", "login", "extendToken", "revokeRefreshToken"]
