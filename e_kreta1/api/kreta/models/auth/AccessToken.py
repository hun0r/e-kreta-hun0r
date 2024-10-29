from __future__ import annotations
from datetime import datetime, timedelta
import jwt
from . import Header

class AccessToken:
    def __init__(self, access_token: str, token_type: str, expires_in: int|None = None, scope: str|None = None) -> None:
        self.access_token = access_token
        self.header = Header(jwt.get_unverified_header(access_token))
        self.json = jwt.decode(access_token, algorithms=[self.header.alg], verify=False)
        self.token_type = token_type

    def __str__(self) -> str:
        """
        Returns a string representation of the access token in the format
        "token_type access_token", for example "Bearer myaccesstoken"
        """        
        return f"{self.token_type} {self.access_token}"
    
    def __repr__(self) -> str:        
        """
        Returns a string representation of the access token.

        Returns
        -------
        str
            A string representation of the access token in the format
            "token_type access_token", for example "Bearer myaccesstoken"
        """
        return self.__str__()

    @property
    def isExpired(self) -> bool:
        """Whether the access token has expired."""
        return datetime.now() > self.exp
    
    @property
    def expiresIn(self) -> timedelta:
        """The number of seconds until the access token expires."""
        return self.exp - datetime.now()
    
    @property
    def iss(self) -> str:
        """The issuer of the access token."""
        return self.json["iss"]
    
    @property
    def nbf(self) -> datetime:
        """The time at which the access token becomes valid."""
        return datetime.fromtimestamp(self.json["nbf"])
    
    @property
    def iat(self) -> datetime:
        """The time at which the access token was issued."""
        return datetime.fromtimestamp(self.json["iat"])
    
    @property
    def exp(self) -> datetime:
        """The time at which the access token expires."""
        return datetime.fromtimestamp(self.json["exp"])
    
    @property
    def aud(self) -> list[str]:
        """The audience of the access token."""
        return self.json["sub"]
    
    @property
    def scope(self) -> list[str]:
        """The scope of the access token."""
        return self.json["scope"]
    
    @property
    def amr(self) -> list[str]:
        """Authentication Methods."""
        return self.json["amr"]
    
    @property
    def client_id(self) -> str:
        """The client_id of the access token."""
        return self.json["client_id"]
    
    @property
    def sub(self) -> str:
        """The subject of the access token. This is the unique identifier of the user."""
        return self.json["sub"]
    
    @property
    def auth_time(self) -> datetime:
        """The time at which the user last authenticated. This is the time when the
        authentication took place, not when the access token was issued."""
        return datetime.fromtimestamp(self.json["auth_time"])
    
    @property
    def idp(self) -> str:
        """The Identity Provider of the user."""
        return self.json["idp"]
    
    @property
    def kreta_institute_user_idp_unique_id(self) -> str:
        """The unique identifier of the user at the Identity Provider of the user."""
        return self.json["kreta:institute_user_idp_unique_id"]

    @property
    def kreta_institute_code(self) -> str:
        """The code of the institution of the user."""
        return self.json["kreta:institute_code"]
    
    @property
    def kreta_institute_user_id(self) -> str:
        """The unique identifier of the user in the institution."""
        return self.json["kreta:institute_user_id"]
    
    @property
    def kreta_institute_user_unique_id(self) -> str:
        """The unique identifier of the user in the institution. This is the identifier that
        is unique accross all institutions and identity providers."""
        return self.json["kreta:institute_user_unique_id"]
    
    @property
    def kreta_school_year_id(self) -> str:
        """The identifier of the school year in the institution."""
        return self.json["kreta:school_year_id"]
    
    @property
    def kreta_school_year_unique_id(self) -> str:
        """
        The unique identifier of the school year in the institution. This is the identifier that
        is unique accross all institutions and identity providers.
        """
        return self.json["kreta:school_year_unique_id"]
    
    @property
    def kreta_institute_unique_id(self) -> str:
        """The unique identifier of the institution. This is the identifier that
        is unique accross all institutions and identity providers."""

        return self.json["kreta:institute_unique_id"]
    
    @property
    def name(self) -> str:
        """The full name of the user."""
        return self.json["name"]
    
    @property
    def kreta_user_name(self) -> str:
        """The username of the user in the institution."""
        return self.json["kreta:user_name"]
    
    @property
    def role(self) -> str:
        """The role of the user in the institution. The possible values are:
        - Tanulo (no more are known)
        """
        return self.json["kreta:role"]

    @property
    def kreta_user_type(self) -> str:
        """The type of the user. The possible values are:
        - Tanulo (no more are known)
        """
        return self.json["kreta:user_type"]
    
    @property
    def sid(self) -> str:
        """The session id of the user. This is the identifier of the user
        in the session. This is unique accross all institutions and identity providers.
        """
        return self.json["sid"]
    
    @property
    def jti(self) -> str:
        """The JWT Token Identifier. This is the identifier of the JWT token.
        This is unique accross all institutions and identity providers.
        """
        return self.json["jti"]
    