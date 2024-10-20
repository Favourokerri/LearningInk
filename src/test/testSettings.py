# testSettings.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from db.session import get_db
from db.base import Base

# Set up a SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test3.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#overide get_db for testing
@pytest.fixture(scope="module")
def db():
    """ provide database session for test"""
    db = TestSessionLocal()
    yield db
    db.close()

#we use this to over ride since we cannot call fitures directly
def overide_get_db():
    try:
        db = TestSessionLocal()
        yield db
    finally:
        db.close()

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    #create all tables on test run
    Base.metadata.create_all(bind=engine)
    yield
    #drop all tables when test is finished
    Base.metadata.drop_all(bind=engine)

app.dependency_overrides[get_db] = overide_get_db

client = TestClient(app)