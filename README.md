# Budgetracker 

## Authentication
All endpoints require authentication. Include the JWT token in the Authorization header:
Authorization: Bearer your_jwt_token

## Rate Limiting
The API implements rate limiting to prevent abuse. The following limits are in place:

- Authenticated Users: 100 requests per day
- Anonymous Users: 10 requests per hour

When the rate limit is exceeded, the API will respond with:
{
  "detail": "Request was throttled. Expected available in 86399 seconds."
}
Status Code: 429 (Too Many Requests)

---

## User Authentication API

### Register
- Method: POST
- URL: /api/register/
- Body (form-data):
  username: johndoe
  email: john@example.com
  password: SecurePass123
  role: user
  profile_photo: [upload file]

- Response:
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "role": "user",
  "profile_photo": "http://localhost:8000/media/profile_photos/photo.jpg"
}

### Login (JWT Token)
- Method: POST
- URL: /api/token/
- Body (JSON):
{
  "username": "johndoe",
  "password": "SecurePass123"
}

- Response:
{
  "access": "jwt_access_token_here",
  "refresh": "jwt_refresh_token_here"
}

### Get Current User
- Method: GET
- URL: /api/me/
- Headers:
  Authorization: Bearer your_jwt_token

- Response:
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "role": "user",
  "profile_photo": "http://localhost:8000/media/profile_photos/photo.jpg"
}

---

## Transaction API

### List/Create Transactions
- Method: GET, POST
- URL: /api/transactions/
- Headers:
  Content-Type: application/json
  Authorization: Bearer your_jwt_token

- Sample POST Body:
{
  "title": "Allowance",
  "amount": 500,
  "date": "2025-06-03",
  "type": "income",
  "category": null,
  "note": "Weekly allowance"
}

- GET Response:
[
  {
    "id": 1,
    "user": 1,
    "title": "Allowance",
    "amount": "500.00",
    "date": "2025-06-03",
    "type": "income",
    "category": null,
    "note": "Weekly allowance"
  }
]

### Retrieve/Update/Delete Transaction
- Method: GET, PUT, DELETE
- URL: /api/transactions/<id>/
- Headers:
  Authorization: Bearer your_jwt_token

- Sample PUT Body:
{
  "title": "Updated Title",
  "amount": 600,
  "date": "2025-06-03",
  "type": "income",
  "category": null,
  "note": "Updated note"
}

---

## File Upload (Profile Photo)
- Accepted formats: .jpg, .jpeg, .png, .webp
- Max file size: 2MB
- Field name: profile_photo
- Used during registration: /api/register/

---

## Status Codes
200: OK
201: Created
400: Bad Request
401: Unauthorized
403: Forbidden
404: Not Found
429: Too Many Requests
500: Internal Server Error

---

## Error Responses
{
  "detail": "Error message here"
}

---

## Base URL for Local Testing
http://127.0.0.1:8000/
