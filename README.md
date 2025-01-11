# 📚 CinemaApp

A lightweight Django application to demonstrate the basic functionality of the Django framework, including models, views, templates, and URL routing.
It is small cinema application

## 🌟 Features

1. User authentication (registration, login, logout)

2. Basic CRUD operations

3. Responsive UI using Django templates

4. Admin panel for managing models

## 🧑‍💻 Installation

### 1. Clone Repository

```bash
    git clone https://github.com/Gor903/CinemaApp.git
    cd CinemaApp
```

### 2. Create a Virtual Environment
```bash
    python -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate
```
```bash
    pip install --upgrade pip
    pip install -r requirements.txt
```

### 3. Create .env file
```bash
    SECRET_KEY="Your secret key"
```

### 4. Apply migrations and run
```bash
    cd Cinema
    python manage.py migrate
    python manage.py runserver
```

### 5. Create superuser to have access to admin panel
```bash
    python manage.py createsuperuser
```

## 🔗 Links

1. Auth:
   1. Login: http://localhost:8000/auth/login
   2. Register: http://localhost:8000/auth/register
2. Booking:
   1. Rooms: http://localhost:8000/booking/rooms 

