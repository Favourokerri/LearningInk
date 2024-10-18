from fastapi import FastAPI
from sqlalchemy.orm import Session
from db.base import Base
from db.session import engine

app = FastAPI()
#Base.metadata.create_all(bind=engine)

#test application health
@app.get('/health')
def health():
    return {'status': 'application up and running'}