import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_create_product():
    client = APIClient()

    data = {
        "name": "Laptop",
        "description": "Gaming laptop",
        "price": 75000,
        "stock": 5
    }

    response = client.post('/api/products/', data)

    assert response.status_code == 201
    assert response.data['name'] == "Laptop"


@pytest.mark.django_db
def test_get_products():
    client = APIClient()

    response = client.get('/api/products/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_invalid_product():
    client = APIClient()

    data = {
        "name": "",
        "price": -10,
        "stock": -1
    }

    response = client.post('/api/products/', data)

    assert response.status_code == 400