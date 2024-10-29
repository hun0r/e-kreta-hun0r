import auth
import delete
import extra
import get
import post
from pydantic import Field

def alias(a: str):
    return Field(alias=a, frozen=True, default=None)


__all__ = [
    "auth",
    "delete",
    "extra",
    "get",
    "post",
]