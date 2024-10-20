from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db.base import Base
from core.security import oauth2_scheme
from db.session import engine
from router import auth

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/api/auth", tags=['OrganizationAuth'])

#test application health
@app.get('/health',)
def health(token: str = Depends(oauth2_scheme)):
    return {'status': 'application up and running'}