# Healthcare Backend API

A backend healthcare management system built using Django, Django REST Framework (DRF), and PostgreSQL.  
The project provides secure RESTful APIs for authentication, patient management, doctor management, and patient-doctor mappings using JWT authentication.

---

# Features

- User Registration and Login
- JWT Authentication using SimpleJWT
- Patient CRUD APIs
- Doctor CRUD APIs
- Patient-Doctor Mapping APIs
- PostgreSQL Database Integration
- Django ORM for Database Interaction
- Protected API Endpoints
- Input Validation and Error Handling
- Environment Variable Configuration

---

# Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- PostgreSQL
- SimpleJWT
- Postman
- Git & GitHub

---

# Project Structure

```bash
healthcare_backend/
│
├── accounts/
├── patients/
├── doctors/
├── mappings/
├── config/
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/Mukilmk007/healthcare-backend-django.git
```

## 2. Navigate to Project Directory

```bash
cd healthcare-backend-django
```

## 3. Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE healthcare_db;
```

---

# Configure Environment Variables

Create a `.env` file in the root directory.

Example:

```env
DB_NAME=healthcare_db
DB_USER=your_postgres_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

SECRET_KEY=your_secret_key
DEBUG=True
```

---

# Run Migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

---

# Run Development Server

```bash
python3 manage.py runserver
```

Server will start at:

```text
http://127.0.0.1:8000/
```

---

# Authentication

JWT Authentication is implemented using:

```text
djangorestframework-simplejwt
```

After login, use the access token in protected APIs.

Example:

```text
Authorization: Bearer <access_token>
```

---

# API Endpoints

# Authentication APIs

## Register User

```http
POST /api/auth/register/
```

### Request Body

```json
{
    "username": "mukil",
    "email": "mukil@gmail.com",
    "password": "123456"
}
```

---

## Login User

```http
POST /api/auth/login/
```

### Request Body

```json
{
    "username": "mukil",
    "password": "123456"
}
```

### Response

```json
{
    "refresh": "token",
    "access": "token"
}
```

---

# Patient APIs

## Create Patient

```http
POST /api/patients/
```

## Get All Patients

```http
GET /api/patients/
```

## Get Single Patient

```http
GET /api/patients/<id>/
```

## Update Patient

```http
PUT /api/patients/<id>/
```

## Delete Patient

```http
DELETE /api/patients/<id>/
```

---

# Doctor APIs

## Create Doctor

```http
POST /api/doctors/
```

## Get All Doctors

```http
GET /api/doctors/
```

## Get Single Doctor

```http
GET /api/doctors/<id>/
```

## Update Doctor

```http
PUT /api/doctors/<id>/
```

## Delete Doctor

```http
DELETE /api/doctors/<id>/
```

---

# Mapping APIs

## Assign Doctor to Patient

```http
POST /api/mappings/
```

### Request Body

```json
{
    "patient": 1,
    "doctor": 1
}
```

---

## Get All Mappings

```http
GET /api/mappings/
```

---

## Get Doctors Assigned to a Patient

```http
GET /api/mappings/patient/<patient_id>/
```

---

## Remove Doctor from Patient

```http
DELETE /api/mappings/<id>/
```

---

# Validation and Error Handling

- JWT-protected endpoints
- Input validation using DRF serializers
- Proper error responses for invalid requests
- Duplicate mapping prevention using `unique_together`

Example validation:

```python
def validate_age(self, value):
    if value < 0:
        raise serializers.ValidationError(
            "Age cannot be negative"
        )
    return value
```

---

# Database Design

The project uses Django ORM with PostgreSQL.

Relationships implemented using ForeignKey:

- One User → Many Patients
- One Patient → Many Doctor Mappings
- One Doctor → Many Patient Mappings

---

# Testing

All APIs were tested using Postman.

---


# Author

Mukil K
