from sqlalchemy import create_engine, Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Определение базового URL для API
BASE_URL = "https://x-clients-be.onrender.com"

DATABASE_URL = "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Employee(Base):
    tablename = 'employee'
    
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

Base.metadata.create_all(bind=engine)
