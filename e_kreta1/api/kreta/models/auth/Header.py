class Header:
    def __init__(self, json: dict) -> None:
        self.json = json
    
    @property
    def alg(self) -> str:
        """The algorithm used to sign the token"""
        return self.json["alg"]

    @property
    def kid(self) -> str:
        """The key ID used to sign the token"""
        return self.json["kid"]
    
    @property
    def x5t(self) -> str:
        """The X.509 certificate thumbprint used to sign the token"""
        return self.json["x5t"]

    @property
    def typ(self) -> str:
        """The type of the token, such as "JWT" or "Bearer"."""
        return self.json["typ"]