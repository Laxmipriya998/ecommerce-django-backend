import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_create_product():
    user = User.objects.create_user(username="test", password="123456")

    client = APIClient()
    client.force_authenticate(user=user)

    data = {
        "name": "Laptop",
        "description": "Gaming laptop",
        "price": 75000,
        "stock": 5
    }

    response = client.post('/api/products/', data)

    assert response.status_code == 201


@pytest.mark.django_db
def test_get_products():
    user = User.objects.create_user(username="test", password="123456")

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get('/api/products/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_invalid_product():
    user = User.objects.create_user(username="test", password="123456")

    client = APIClient()
    client.force_authenticate(user=user)

    data = {
        "name": "",
        "price": -10,
        "stock": -1
    }

    response = client.post('/api/products/', data)

    assert response.status_code == 400