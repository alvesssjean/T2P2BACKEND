from fastapi import FastAPI, APIRouter
from app.routes import router
from app.database import engine, Base
from app.models import ProdutoModel

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "pagina inicial"}