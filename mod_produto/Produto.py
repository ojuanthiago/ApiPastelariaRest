from pydantic import BaseModel

class ProdutoModel(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str
    foto: bytes = None
    valor_unitario: float
    