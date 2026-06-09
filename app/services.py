from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories import ProdutoRepository
from app.schemas import ProdutoCreate
from app.models import ProdutoModel

class ProdutoService:
    def __init__(self, db: Session):
        self.repository = ProdutoRepository(db)

    def obter_produto(self, produto_id: int) -> ProdutoModel:
        produto = self.repository.buscar_por_id(produto_id)
        if not produto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado.")
        return produto
    
    def listar_todos(self) -> list[ProdutoModel]:
        return self.repository.listar_todos()
    
    def criar_produto(self, produto_dados: ProdutoCreate) -> ProdutoModel:
        return self.repository.criar(produto_dados)

    def deletar_produto(self, produto_id: int) -> None:
        produto = self.obter_produto(produto_id)
        self.repository.deletar(produto)