import pytest
import requests
from sqlalchemy import create_engine, Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

# Подключение к базе данных
DATABASE_URL = "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Определение модели Employee для работы с базой данных
class Employee(Base):
    tablename = 'employee'  # Указание имени таблицы

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    is_active = Column(Boolean, default=True)
    create_timestamp = Column(TIMESTAMP, default=datetime.utcnow)
    change_timestamp = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    middle_name = Column(String(20))
    phone = Column(String(15), nullable=False)
    email = Column(String(256), nullable=False)
    avatar_url = Column(String(1024))
    company_id = Column(Integer, nullable=False)

@pytest.fixture(scope="session")
def db_session():
    # Создание сессии базы данных
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="session")
def auth_token():
    # Получение токена авторизации
    AUTH_DATA = {
        "login": "raphael",
        "password": "cool-but-crude"
    }
    response = requests.post("https://x-clients-be.onrender.com/auth/login", json=AUTH_DATA)
    assert response.status_code == 200, "Не удалось получить токен авторизации"
    token = response.json().get('userToken')
    return token

@pytest.fixture
def headers(auth_token):
    # Заголовки с авторизационным токеном
    return {
        "Authorization": f"Bearer {auth_token}"
    }

@pytest.fixture
def employee_data():
    # Данные сотрудника для тестов
    return {
        "first_name": "Test",
        "last_name": "Employee",
        "phone": "+1234567890",
        "email": "testemployee@example.com",
        "company_id": 1
    }

@pytest.fixture
def create_employee_in_db(db_session, employee_data):
    # Создание сотрудника напрямую в базе данных
    new_employee = Employee(**employee_data)
    db_session.add(new_employee)
    db_session.commit()
    db_session.refresh(new_employee)
    yield new_employee
    # Удаление сотрудника после теста
    db_session.delete(new_employee)
    db_session.commit()

def test_create_and_verify_employee_via_api(db_session, headers, employee_data, create_employee_in_db):
    # Шаг 1: Создание сотрудника через API
    response = requests.post("https://x-clients-be.onrender.com/employee", headers=headers, json=employee_data)
    assert response.status_code == 201, "Ошибка при создании сотрудника через API"
    api_employee_id = response.json().get('id')

    # Шаг 2: Проверка наличия сотрудника в базе данных
    db_employee = db_session.query(Employee).filter(Employee.id == api_employee_id).first()
    assert db_employee is not None, "Сотрудник не найден в базе данных"
    assert db_employee.first_name == employee_data['first_name'], "Имя сотрудника не совпадает"
    assert db_employee.last_name == employee_data['last_name'], "Фамилия сотрудника не совпадает"
    assert db_employee.phone == employee_data['phone'], "Телефон сотрудника не совпадает"
    assert db_employee.email == employee_data['email'], "Email сотрудника не совпадает"
    assert db_employee.company_id == employee_data['company_id'], "ID компании сотрудника не совпадает"

    # Шаг 3: Получение сотрудника через API и проверка данных
    response = requests.get(f"https://x-clients-be.onrender.com/employee/{api_employee_id}", headers=headers)
    assert response.status_code == 200, "Ошибка при получении сотрудника через API"
    api_employee = response.json()

    assert api_employee['first_name'] == employee_data['first_name'], "Имя сотрудника через API не совпадает"
    assert api_employee['last_name'] == employee_data['last_name'], "Фамилия сотрудника через API не совпадает"
    assert api_employee['phone'] == employee_data['phone'], "Телефон сотрудника через API не совпадает"
    assert api_employee['email'] == employee_data['email'], "Email сотрудника через API не совпадает"
    assert api_employee['company_id'] == employee_data['company_id'], "ID компании сотрудника через API не совпадает"

    # Удаление сотрудника, созданного через API
    db_session.query(Employee).filter(Employee.id == api_employee_id).delete()
    db_session.commit()

def test_soft_delete_employee_via_api(headers, create_employee_in_db):
    # Шаг 1: Удаление сотрудника через API
    employee_id = create_employee_in_db.id
    response = requests.patch(f"https://x-clients-be.onrender.com/employee/{employee_id}", headers=headers, json={"is_active": False})
    assert response.status_code == 200, "Ошибка при мягком удалении сотрудника через API"

    # Шаг 2: Проверка, что сотрудник деактивирован в базе данных
    db_employee = create_employee_in_db
    assert db_employee.is_active is False, "Сотрудник не деактивирован в базе данных"

    # Шаг 3: Проверка, что сотрудник не возвращается через API
    response = requests.get(f"https://x-clients-be.onrender.com/employee/{employee_id}", headers=headers)
    assert response.status_code == 404, "Сотрудник не должен возвращаться через API после мягкого удаления"
    