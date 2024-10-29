from json import dumps

from requests import Response

class Error:
    def __init__(self, json: dict) -> None:
        self.json = json
    @property
    def PropertyName(self) -> str|None:
        if self.json is None: 
            return None
        return self.json["PropertyName"]
    @property
    def Message(self) -> str|None:
        if self.json is None: 
            return None
        return self.json["Message"]
    @property
    def ExceptionType(self) -> str|None:
        if self.json is None: 
            return None
        return self.json["ExceptionType"]

class error_base1(Exception):
    def __init__(self, json: dict|None = None, status_code: int = 0) -> None:
        super().__init__()
        self.message = str(status_code) + ": " + dumps(json, indent=4)
        self.status_code = status_code
        self.json = json

    @property
    def ExceptionId(self) -> str|None:
        if self.json is None: 
            return None
        return self.json["ExceptionId"]
    @property
    def ExceptionType(self) -> str|None:
        if self.json is None: 
            return None
        return self.json["ExceptionType"]
    @property
    def Message(self) -> str|None:
        if self.json is None: 
            return None
        return self.json["Message"]
    @property
    def ErrorList(self) -> list[Error]|None:
        if self.json is None: 
            return None
        return [Error(error) for error in self.json["ErrorList"]]
    
class error_base2(Exception):
    def __init__(self, message: str = "unknown error", status_code: int = 0) -> None:
        super().__init__()
        self.message = f"{status_code}: {message}"
        self.status_code = status_code

def raise_error(response: Response) -> Exception:
    if "}" in response.text:
        raise error_base2(response.text)
    raise error_base1(response.json())