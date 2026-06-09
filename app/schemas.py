from pydantic import BaseModel
from typing import Optional

class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    descricao: Optional[str] = None

class ProdutoResponse(BaseModel):
    id: int
    nome: str
    preco: float
    descricao: Optional[str] = None

    class Config:
        from_attributes = True