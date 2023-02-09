# 🛒 E-Commerce Backend (Django REST)

## 📌 Overview

A production-ready e-commerce backend built using Django REST Framework. This project demonstrates a modular architecture with secure JWT authentication, API documentation, and automated testing.

---

## 🚀 Features

* 🔐 User Registration & JWT Authentication
* 📦 Product Management (Create, Read, Update, Delete)
* 🛒 Cart Management System
* 📄 Order Creation & Management
* 💳 Payment Simulation (Order Status Update)
* 🔒 Protected APIs (Authenticated Access)
* 📄 Swagger API Documentation
* 🧪 Automated API Testing using pytest
* 🔍 Product Search & Pagination

---

## 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* JWT Authentication
* pytest
* Swagger (drf-yasg)

---

## 📂 Project Structure

```
ecommerce_project/
│
├── core/        # Main project settings
├── user/        # Custom user & authentication
├── product/     # Product management
├── cart/        # Cart functionality
├── order/       # Order & payment simulation
└── manage.py
```

---

## ⚙️ Setup Instructions

```bash
git clone <your-repository-link>
cd ecommerce_project

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
```

---

## API Documentation

Access Swagger UI:

```
http://127.0.0.1:8000/swagger/
```

---

##  Authentication Flow

1. Register user
2. Generate JWT token via `/api/token/`
3. Click **Authorize** in Swagger
4. Enter:

```
Bearer <access_token>
```

---

## Run Tests

```bash
pytest
```

---

## Key Highlights

* Modular architecture with separate apps
* Secure JWT-based authentication
* Clean API design using APIView
* Integrated Swagger documentation
* Scalable and maintainable code structure

---

## Author

**Laxmipriya Sahoo**
B.Tech CSE | Python & Django Developer

---
