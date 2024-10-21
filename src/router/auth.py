from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from db.session import get_db
from typing import Optional, Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from crud.auth import authenticate_user, create_access_token
from schema.auth import Token
from schema.organization import CreateOrganization, OrganizationResponse
from crud.auth import create_organization_in_db, verify_password

router = APIRouter()

#routes
@router.post('/organization/signUp', response_model=OrganizationResponse, status_code=status.HTTP_201_CREATED)
def organization_sign_up( organization_data: CreateOrganization,
                               db: Session=Depends(get_db)):
    verify_password(organization_data.password)
    organization = create_organization_in_db(db, organization_data)
    return organization

@router.post('/organization/login', response_model=Token, status_code=status.HTTP_200_OK)
def log_in_get_access_token(from_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                    db: Session = Depends(get_db)):
    user =  authenticate_user(from_data.username, from_data.password, db)
    token = create_access_token(user.username, user.id)

    return {'access_token': token, 'token_type': 'bearer'}