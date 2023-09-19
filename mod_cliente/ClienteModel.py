import db
from sqlalchemy import BLOB, Column, VARCHAR, CHAR, Integer, FLOAT
# ORM

class ClienteDB(db.Base):
    __tablename__ = 'tb_cliente'

    id_cliente = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    cpf = Column(CHAR(100), nullable=False)
    telefone = Column(CHAR(100), nullable=False)
    compra_fiado = Column(CHAR(100), nullable=False)
    dia_fiado = Column(Integer, nullable=False)
    senha = Column(CHAR(100), nullable=False)
    
    def __init__(self, id_cliente, nome, cpf, telefone, compra_fiado, dia_fiado, senha):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.compra_fiado = compra_fiado
        self.dia_fiado = dia_fiado
        self.senha = senha
