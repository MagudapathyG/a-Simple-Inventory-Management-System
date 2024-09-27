# a-Simple-Inventory-Management-System API



## Overview
This project is a simple Inventory Management System built using Django Rest Framework. It allows users to manage inventory items with secure access through JWT authentication. The API supports CRUD operations and utilizes Redis for caching frequently accessed items.

## Requirements
- Python 3.x
- Django
- Django Rest Framework
- MySQL
- Redis
- Django Redis

## Installation Steps

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd inventory-management-system
```



### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up MySQL Database   Note: i am not used PostgreSQL
- Create a database in MySQL for the inventory management system. Use the following command in MySQL:
```sql
CREATE DATABASE inventory_db;
```
- Update the database settings in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inventory_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Set Up Redis
- Follow the instructions to install and run Redis on your machine.

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser
To access the Django admin panel, create a superuser:
```bash
python manage.py createsuperuser
```
- Follow the prompts to enter your username, email, and password.

### 7. Start the Server
```bash
python manage.py runserver
```

### 8. Access the API
You can access the API at `http://127.0.0.1:8000/api/items/`. Use tools like Postman or cURL to interact with the API.

### 9. Endpoints
- **Create Item:** `POST /api/items/`
- **Read Item:** `GET /api/items/{item_id}/`
- **Update Item:** `PUT /api/items/{item_id}/`
- **Delete Item:** `DELETE /api/items/{item_id}/`

### 10. Authentication
- Use JWT for securing the API endpoints. Obtain a token by sending a `POST` request to `/api/token/` with your credentials:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

### 11. Unit Tests
To run unit tests, execute:
```bash
python manage.py test
```

## 12. Logging
The application integrates logging to track API usage and errors.

## 13. Troubleshooting
- If you encounter connection errors with Redis, ensure that the Redis server is running and accessible at `127.0.0.1:6379`.

## 14. Conclusion
This inventory management API provides a simple way to manage items with a focus on performance and security. Feel free to expand on its features to meet your specific needs.
