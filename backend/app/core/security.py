import jwt
from fastapi.security import OAuth2PasswordBearer
from argon2 import PasswordHasher
from argon2._utils import Type
from datetime import datetime, timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")


SECRET_KEY = "1v9wY[N9FBw"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


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
    ph = PasswordHasher()
    algorithm, hashed = django_encoded_password.split('$', 1)
    hashed = '$'+hashed
    return ph.verify(hashed, plain_password)


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
