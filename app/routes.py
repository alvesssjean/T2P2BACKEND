from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ProdutoCreate, ProdutoResponse
from app.services import ProdutoService

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.post("/", response_model=ProdutoResponse, status_code=status.HTTP_201_CREATED)
def criar(payload: ProdutoCreate, db: Session = Depends(get_db)):
    service = ProdutoService(db)
    return service.criar_produto(payload)


@router.get("/", response_model=list[ProdutoResponse])
def listar_todos(db: Session = Depends(get_db)):
    service = ProdutoService(db)
    return service.listar_todos()

@router.get("/{produto_id}", response_model=ProdutoResponse)
def obter(produto_id: int, db: Session = Depends(get_db)):
    service = ProdutoService(db)
    return service.obter_produto(produto_id)

@router.delete("/{produto_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar(produto_id: int, db: Session = Depends(get_db)):
    service = ProdutoService(db)
    return service.deletar_produto(produto_id)

