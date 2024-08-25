import pytest
import requests

BASE_URL = "https://x-clients-be.onrender.com"

# Данные для авторизации
AUTH_DATA = {
    "login": "raphael",
    "password": "cool-but-crude"
}


@pytest.fixture(scope="session")
def auth_token():
    response = requests.post(f"{BASE_URL}/auth/login", json=AUTH_DATA)
    assert response.status_code == 200, "Не удалось получить токен авторизации"
    token = response.json().get('userToken')
    return token


@pytest.fixture
def headers(auth_token):
    return {
        "Authorization": f"Bearer {auth_token}"
    }


def test_get_employees(headers):
    response = requests.get(f"{BASE_URL}/employee", headers=headers)
    assert response.status_code == 200, "Ошибка при получении списка сотрудников"
    assert isinstance(response.json(), list), "Ответ должен быть списком"


@pytest.fixture
def test_create_employee(headers):
    payload = {
        "name": "Test Employee",
        "phone": "+1234567890",
        "email": "testemployee@example.com",
        "position": "QA Engineer"
    }
    response = requests.post(f"{BASE_URL}/employee", headers=headers, json=payload)
    assert response.status_code == 201, "Ошибка при создании сотрудника"
    employee_id = response.json().get('id')
    return employee_id


def test_get_employee_by_id(headers, test_create_employee):
    employee_id = test_create_employee
    response = requests.get(f"{BASE_URL}/employee/{employee_id}", headers=headers)
    assert response.status_code == 200, "Ошибка при получении сотрудника по ID"
    data = response.json()
    assert data.get('id') == employee_id, "Неверный ID сотрудника"


def test_patch_employee(headers, test_create_employee):
    employee_id = test_create_employee
    payload = {
        "position": "Senior QA Engineer"
    }
    response = requests.patch(
        f"{BASE_URL}/employee/{employee_id}", headers=headers, json=payload
    )
    assert response.status_code == 200, "Ошибка при обновлении сотрудника"
    assert response.json().get('position') == "Senior QA Engineer", (
        "Позиция сотрудника не обновлена"
    )


def test_create_employee_missing_name(headers):
    payload = {
        "phone": "+1234567890",
        "email": "testemployee@example.com",
        "position": "QA Engineer"
    }
    response = requests.post(f"{BASE_URL}/employee", headers=headers, json=payload)
    assert response.status_code == 422, "Должна быть ошибка при отсутствии имени"


def test_create_employee_missing_phone(headers):
    payload = {
        "name": "Test Employee",
        "email": "testemployee@example.com",
        "position": "QA Engineer"
    }
    response = requests.post(f"{BASE_URL}/employee", headers=headers, json=payload)
    assert response.status_code == 422, "Должна быть ошибка при отсутствии телефона"
    