# User Management API

A robust Django REST API for user management with JWT authentication and Swagger documentation.

## Overview

This project provides a RESTful API for managing users with features including:
- JWT-based authentication
- User CRUD operations
- Profile management
- Swagger/OpenAPI documentation
- Dockerized development environment
- PostgreSQL database

## API Documentation

Once the project is running, you can access the API documentation at:
- Swagger UI: `http://localhost:8000/api/docs/`
- ReDoc UI: `http://localhost:8000/api/redoc/`
- OpenAPI Schema: `http://localhost:8000/api/schema/`

## API Endpoints

- `POST /api/login/` - Obtain JWT token
- `POST /api/token/refresh/` - Refresh JWT token
- `GET /api/users/` - List all users
- `POST /api/users/` - Create new user
- `GET /api/users/{id}/` - Retrieve user details
- `PUT /api/users/{id}/` - Update user
- `DELETE /api/users/{id}/` - Delete user
- `GET /api/users/profile/` - Get current user's profile

## Technologies Used

### Core
- Python 3.11
- Django 5.0.2
- Django REST Framework 3.14.0
- PostgreSQL 13

### Authentication
- djangorestframework-simplejwt 5.3.1

### Documentation
- drf-spectacular 0.27.1

### Development & Deployment
- Docker
- docker-compose
- psycopg2-binary 2.9.9

### Additional Tools
- django-cors-headers 4.3.1
- python-dotenv 1.0.1

## Setup Instructions

### Prerequisites
- Docker
- Docker Compose

### Installation & Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd user-management-api
```

2. Build and start the containers:
```bash
docker-compose up --build
```

3. Create a superuser:
```bash
docker-compose exec web python src/manage.py createsuperuser
```

4. Apply migrations:
```bash
docker-compose exec web python src/manage.py migrate
```

The API will be available at `http://localhost:8000`

## Using the API

### Authentication

1. Obtain JWT Token:
```bash
curl -X POST http://localhost:8000/api/login/ \
    -H "Content-Type: application/json" \
    -d '{"username": "your_username", "password": "your_password"}'
```

Response:
```json
{
    "access": "your.jwt.token",
    "refresh": "your.refresh.token"
}
```

2. Use the token in subsequent requests:
```bash
curl -H "Authorization: Bearer your.jwt.token" \
    http://localhost:8000/api/users/profile/
```

### Example API Calls

1. Create a new user:
```bash
curl -X POST http://localhost:8000/api/users/ \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer your.jwt.token" \
    -d '{
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "securepassword",
        "first_name": "John",
        "last_name": "Doe"
    }'
```

2. Get user profile:
```bash
curl -X GET http://localhost:8000/api/users/profile/ \
    -H "Authorization: Bearer your.jwt.token"
```

## Development

### Running Tests
```bash
docker-compose exec web python src/manage.py test
```

### Database Management

Access PostgreSQL:
```bash
docker-compose exec db psql -U postgres -d user_management
```

Create new migrations:
```bash
docker-compose exec web python src/manage.py makemigrations
```

## Environment Variables

Create a `.env` file in the root directory with these variables:
```env
DEBUG=1
SECRET_KEY=your-secret-key-here
POSTGRES_DB=user_management
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

## Project Structure
```
user-management-api/
├── docker/                  # Docker configuration files
│   ├── Dockerfile
│   └── entrypoint.sh
├── src/                    # Source code
│   ├── manage.py
│   ├── core/              # Project core settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── users/             # Users app
│       ├── models.py      # User model definition
│       ├── serializers.py # API serializers
│       ├── urls.py        # URL routing
│       └── views.py       # API views
├── docker-compose.yml     # Docker compose configuration
└── requirements.txt       # Python dependencies
```

## Error Handling

The API uses standard HTTP status codes:
- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error
