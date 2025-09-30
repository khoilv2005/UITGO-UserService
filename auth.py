import os
from datetime import datetime, timedelta, timezone
from typing import Union
from jose import JWTError, jwt
from passlib.context import CryptContext
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES_STR = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

# Validate that required environment variables are set
if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable is not set")
if not ALGORITHM:
    raise ValueError("ALGORITHM environment variable is not set")
if not ACCESS_TOKEN_EXPIRE_MINUTES_STR:
    raise ValueError("ACCESS_TOKEN_EXPIRE_MINUTES environment variable is not set")

ACCESS_TOKEN_EXPIRE_MINUTES = int(ACCESS_TOKEN_EXPIRE_MINUTES_STR)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    # Truncate password to 72 bytes if needed (bcrypt limitation)
    if len(plain_password.encode('utf-8')) > 72:
        plain_password = plain_password.encode('utf-8')[:72].decode('utf-8')
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    # Truncate password to 72 bytes if needed (bcrypt limitation)
    if len(password.encode('utf-8')) > 72:
        password = password.encode('utf-8')[:72].decode('utf-8')
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
