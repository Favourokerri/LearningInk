# test_organization_signup.py
from fastapi.testclient import TestClient
import pytest
from model.organization import OrganizationModel
from test.testSettings import db, engine, client, setup_database
from db.base import Base


organization_data = {
  "organization_name": "testOrganization",
  "email": "testEmail3@gmail.com",
  "type_of_organization": "Educational",
  "organization_size": 5,
  "phone_number": "09087466729",
  "address": "No 4 old american road",
  "website_url": "https://visit.com",
  "password": "testPassword"
}


# Test the signup route
def test_signup(db, setup_database):
    response = client.post('/api/auth/organization/signUp', json=organization_data)
    assert response.status_code == 201
    
    # Ensure you query the correct field
    organization = (db.query(OrganizationModel)
                    .filter(OrganizationModel.email == organization_data["email"])
                    .first()
                    )
    assert organization is not None

# Test the signup route
def test_signup_with_exisiting_user(db, setup_database):
    response = client.post('/api/auth/organization/signUp', json=organization_data)
    organization = (db.query(OrganizationModel)
                    .filter(OrganizationModel.email == organization_data["email"])
                    .first()
                    )
    assert organization is not None

     #create organization again
    response = client.post('/api/auth/organization/signUp', json=organization_data)
    assert response.status_code == 409
    error_response = response.json()
    
    assert error_response['detail'] == "User with this username already exist" 
