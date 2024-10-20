from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class CreateOrganization(BaseModel):
    organization_name: str = Field(..., min_length=3)
    email: EmailStr
    type_of_organization: str = Field(..., min_length=3)
    organization_size: int = Field(..., ge=1)
    phone_number: str = Field(..., min_length=9, max_length=20)
    address: str = Field(..., min_length=5)
    website_url: Optional[str]
    password: str

class OrganizationResponse(BaseModel):
     organization_name: str
     email: str
     type_of_organization: str
     organization_size: int
     phone_number: str
     address: str
     website_url: Optional[str]