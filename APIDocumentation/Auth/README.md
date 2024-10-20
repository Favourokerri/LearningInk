### API Endpoints Documentation


---

### 1. **Create Organization (Sign Up)**

**Endpoint:** `api/auth/organization/signUp`  
**Method:** `POST`  
**Description:** This endpoint allows a new organization to be registered. The organization's details, including email, name, and password, are provided in the request body.

**Request Body Example:**

```json
{
  "organization_name": "My Organization",
  "email": "example@organization.com",
  "type_of_organization": "Tech",
  "organization_size": 50,
  "phone_number": "+123456789",
  "address": "123 Main St, City, Country",
  "website_url": "https://example.com",
  "password": "securepassword123"
}
```

**Response Example (Status Code: 201 Created):**

```json
{
  "organization_name": "My Organization",
  "email": "example@organization.com",
  "type_of_organization": "Tech",
  "organization_size": 50,
  "phone_number": "+123456789",
  "address": "123 Main St, City, Country",
  "website_url": "https://example.com"
}
```

**Error Responses:**

- `409 Conflict`: If an organization with the provided email already exists.

---

### 2. **Login and Get Access Token**

**Endpoint:** `api/auth/organization/login`  
**Method:** `POST`  
**Description:** This endpoint allows an existing organization to log in using email and password. Upon successful authentication, a JWT access token is returned, which can be used for subsequent authenticated requests.

**Request Format:**  
The login request uses **form data**, not JSON. The credentials (username and password) must be sent as form data.

**Form Data:**

- `username`: The email address of the organization (used as the username).
- `password`: The password of the organization.

**Example Request (Form Data):**

```
username: example@organization.com
password: securepassword123
```

**Response Example (Status Code: 200 OK):**

```json
{
  "access_token": "jwt_token_here",
  "token_type": "bearer"
}
```

**Error Responses:**

- `404 Not Found`: If the username or password is incorrect.

---

### Authentication

After logging in and receiving the access token, the token must be sent in the `Authorization` header for protected routes in the following format:

```
Authorization: Bearer <access_token>
```

The token is a JWT that contains information such as the organization's username and user ID, which is used to authenticate future requests.

---
