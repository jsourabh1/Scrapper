

# File Upload System

The File Upload Service is a RESTful API built with Django and Django Rest Framework. It provides token-based authentication for secure file uploads, storage, and retrieval.

## Features

- Token authentication for secure API access
- File upload functionality with various file types supported
- APIs for listing and downloading files
- Secure and private storage for uploaded files

Requirements:
Django==3.2.8
djangorestframework==3.12.4
django-cors-headers==3.8.0

## Installation

1. Extract the Zip file:

2. Run database migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
3: Create the superuser:
   ```
    python manage.py createsuperuser
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

7. Access the API at `http://localhost:8000/api/`

## API Documentation

The API provides the following endpoints:

- `POST /api/token/`: Obtain an authentication token by providing valid credentials.
- `POST /api/upload/`: Upload a file by providing the file data. Requires token authentication.
- `GET /api/files/`: List all files uploaded by the authenticated user. Requires token authentication.
- `GET /api/files/<file_id>/`: Download a specific file by file ID. Requires token authentication.

For detailed API documentation and examples, refer to the API documentation page at `http://localhost:8000/api/docs/` after starting the server.

## Configuration

The following configuration options are available:

- Token authentication: Token authentication is enabled for secure API access. Tokens can be obtained by authenticating with valid credentials using the `/api/token/` endpoint.
- File storage: By default, the files are stored locally in the `media/uploads/` directory. You can configure a different storage backend, such as Amazon S3, by modifying the project settings.

## Contact

For any inquiries or questions, please contact jsourabh861@gmail.com.
