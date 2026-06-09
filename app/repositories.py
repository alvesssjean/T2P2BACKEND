from sqlalchemy.orm import Session
from app.models import ProdutoModel
from app.schemas import ProdutoCreate

class ProdutoRepository:
    def __init__(self, db: Session):
        self.db = db

    def buscar_por_id(self, produto_id: int) -> ProdutoModel:
        return self.db.query(ProdutoModel).filter(ProdutoModel.id ==produto_id).first()
    
    def listar_todos(self) -> list[ProdutoModel]:
        return self.db.query(ProdutoModel).all()
    
    def criar(self, produto_dados: ProdutoCreate) -> ProdutoModel:
        novo_produto = ProdutoModel(**produto_dados.model_dump())
        self.db.add(novo_produto)
        self.db.commit()
        self.db.refresh(novo_produto)
        return novo_produto
    
    def deletar(self, produto: ProdutoModel) -> None:
        self.db.delete(produto)
        self.db.commit()
