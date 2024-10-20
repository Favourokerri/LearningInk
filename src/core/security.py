from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

# Password hashing context
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/organization/login")