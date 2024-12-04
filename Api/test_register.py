import pytest
import requests
import time

@pytest.fixture
def base_url():
    return "http://localhost:8080/api/v1/auth"

@pytest.fixture
def register_data():
    return {
        "email": "luz52ass12123dw1asadzzsdd@gmail.com",
        "username": "luas23a1sdaasdwqdasdsdzzsddz",
        "password":"123s12dasa2sdszqwezadasdd456",
        "fullName": "Lua23ss23sdasd3sdsdsaaaddzzzz katy"
    }

@pytest.fixture
def login_data():
    return {
        "username": "luz",
        "password": "asd"
    }

def test_successful_register(base_url,register_data):
    response = requests.post(f"{base_url}/register",json=register_data)
    assert response.status_code == 201
    data = response.json()
    print(data)
    assert "userId" in data
    assert data["email"] == register_data["email"]
    assert data["fullName"] == register_data["fullName"]

def test_successful_login(base_url,login_data):
    response = requests.post(f"{base_url}/login",json=login_data)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["username"] == login_data["username"]
    assert data["message"] == "User logged in successfully"
    assert data["success"] is True
    assert "token" in data



def test_invalid_login(base_url):
    invalid_data = {
        "username":"lusz",
        "password":"1223456"
    }
    response = requests.post(f"{base_url}/login",json=invalid_data)
    assert response.status_code == 401
