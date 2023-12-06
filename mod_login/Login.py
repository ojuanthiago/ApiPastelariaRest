from pydantic import BaseModel

class Login(BaseModel):
    id_login: int = None
    cpf: str
    senha: str = None
    grupo: int
    