import jwt

from argon2 import PasswordHasher
from argon2._utils import Type
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from starlette.requests import Request
from typing import Optional, Dict


SECRET_KEY = "1v9wY[N9FBwTtTRTR"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15


class OAuth2PasswordBearerWithCookie(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        authorization: str = request.cookies.get(
            "access_token"
        )  # changed to accept access token from httpOnly Cookie

        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")
oauth2_cookie_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/api/token")


def get_password_hash(password: str) -> str:
    """
        This needs to mantain compatibility with django webook app hash settings
        Details how django stores password: https://docs.djangoproject.com/en/4.0/topics/auth/passwords/
    """
    algorithm = 'argon2'
    ph = PasswordHasher(time_cost=2, memory_cost=512, parallelism=2, salt_len=12, hash_len=16, type=Type.I)
    data = ph.hash(password)
    return algorithm + data


def verify_password(plain_password: str, django_encoded_password: str) -> bool:
    """
        Details how django stores password: https://docs.djangoproject.com/en/4.0/topics/auth/passwords/
        Details how argon works: https://argon2-cffi.readthedocs.io/en/stable/api.html
    """
    try:
        ph = PasswordHasher()
        algorithm, hashed = django_encoded_password.split('$', 1)
        hashed = '$'+hashed
        ph.verify(hashed, plain_password)
        return True
    except:
        return False


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
