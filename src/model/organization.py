from db.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class OrganizationModel(Base):
    __tablename__ = 'organizations'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(200), unique=True)
    organization_name = Column(String(200))
    email = Column(String(200), unique=True)
    type_of_organization = Column(String(200))
    organization_size = Column(Integer)
    phone_number = Column(String(20))
    address = Column(String(200))
    website_url = Column(String(200))
    password = Column(String(200))

