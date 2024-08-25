import pytest
from sqlalchemy.orm import sessionmaker
from db_config import engine, SessionLocal, Employee
from sqlalchemy.exc import IntegrityError

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

@pytest.fixture
def create_employee(db_session):
    def _create_employee(**kwargs):
        employee = Employee(**kwargs)
        db_session.add(employee)
        db_session.commit()
        db_session.refresh(employee)
        return employee
    return _create_employee

@pytest.fixture
def delete_employee(db_session):
    def _delete_employee(employee_id):
        employee = db_session.query(Employee).filter(Employee.id == employee_id).first()
        if employee:
            db_session.delete(employee)
            db_session.commit()
    return _delete_employee
