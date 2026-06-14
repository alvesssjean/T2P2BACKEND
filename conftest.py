import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import get_db, Base
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def client():

    Base.metadata.create_all(bind=engine)
    
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
            
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as test_client:
        yield test_client
        
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def produto_existente(client):
    payload = {
        "nome": "Monitor UltraWide",
        "preco": 1500.00,
        "descricao": "Tela de 29 polegadas IPS",
        "ativo": True
    }
    response = client.post("/produtos", json=payload)
    return response.json()