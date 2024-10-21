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

#data in this format because Oauth expects form data
organization_login_data={
            'username': organization_data['email'],
            'password': organization_data['password']
        }


def test_signup(db, setup_database):
    response = client.post('/api/auth/organization/signUp', json=organization_data)
    assert response.status_code == 201
    
    organization = (db.query(OrganizationModel)
                    .filter(OrganizationModel.email == organization_data["email"])
                    .first()
                    )
    assert organization is not None

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
  
def test_signup_with_wrong_password_length(db, setup_database):
    organization_data['password'] = "1234"
    response = client.post('/api/auth/organization/signUp', json=organization_data)
    organization = (db.query(OrganizationModel)
                    .filter(OrganizationModel.email == organization_data["email"])
                    .first()
                    )
    assert response.status_code == 400
    assert organization is None
    error_response = response.json()
    
    assert error_response['detail'] == "Password must be greater than 7"

    #change modified filed to ensure other test run successfully 
    organization_data['password'] = "testPassword"

def test_login_with_correct_details(db, setup_database):
    client.post('/api/auth/organization/signUp', json=organization_data)
    response = client.post('/api/auth/organization/login', data=organization_login_data)
    
    organization = (db.query(OrganizationModel)
                    .filter(OrganizationModel.email == organization_data["email"])
                    .first()
                    )
    login_data = response.json()
    assert organization is not None
    assert response.status_code == 200
    assert 'access_token' in login_data
    assert login_data['token_type'] == 'bearer'

def test_login_with_unexisting_user(db, setup_database):
    response = client.post('/api/auth/organization/login', data=organization_login_data)
    
    organization = (db.query(OrganizationModel)
                    .filter(OrganizationModel.email == organization_data["email"])
                    .first()
                    )
    error_response = response.json()

    assert organization is  None
    assert response.status_code == 404
    assert error_response['detail'] == "Username or password incorrect"

#test login with incorrect password
def test_login_with_wrong_password(db, setup_database):
    organization_login_wrong_password={
            'username': organization_data['email'],
            'password': 'wrongpassword'
        }
    
    client.post('/api/auth/organization/signUp', json=organization_data)
    response = client.post('/api/auth/organization/login', data=organization_login_wrong_password)
    
    organization = (db.query(OrganizationModel)
                    .filter(OrganizationModel.email == organization_data["email"])
                    .first()
                    )
    error_response = response.json()

    assert organization is  not None
    assert response.status_code == 404
    assert error_response['detail'] == "Username or password incorrect"