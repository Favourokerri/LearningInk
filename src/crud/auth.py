from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.security import bcrypt_context
import jwt
from jose import JWTError
from datetime import datetime, timedelta
from core.config import settings
from schema.organization import CreateOrganization
from model.organization import OrganizationModel


def verify_password(password):
    if len(password) < 8:
         raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be greater than 7"
        )
    return password



def create_organization_in_db(db: Session, organization_data: CreateOrganization):
    try:
        organization_data.password = bcrypt_context.hash(organization_data.password)
        db_organization = OrganizationModel(username=organization_data.email,
                                            **organization_data.model_dump())
        db.add(db_organization)
        db.commit()
        db.refresh(db_organization)
        return db_organization
    
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this username already exist"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= f'{e}'
        )

def authenticate_user(username: str, password: str, db):
    user = db.query(OrganizationModel).filter(OrganizationModel.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Username or password incorrect"
        )
    
    if not bcrypt_context.verify(password, user.password):
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Username or password incorrect"
        )

    return user

def create_access_token(username: str, user_id: int):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode(encode, settings.SECRET_KEY, settings.ALGORITHM)

def get_current_user(db: Session, token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        
        user = db.query(OrganizationModel).filter(OrganizationModel.username == username).first()
        return user
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="could not validate credentials"
        )