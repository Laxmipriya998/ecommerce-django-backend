import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_user_registration():
    client = APIClient()

    data = {
        "username": "testuser",
        "email": "test@gmail.com",
        "password": "123456"
    }

    response = client.post('/api/user/register/', data)

    assert response.status_code == 200

@pytest.mark.django_db
def test_login_fail():
    client = APIClient()

    response = client.post('/api/token/', {
        "username": "wrong",
        "password": "wrong"
    })

    assert response.status_code == 401