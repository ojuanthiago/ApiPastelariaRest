import db
from sqlalchemy import Column, VARCHAR, Integer

class LoginDB(db.Base):
  __tablename__ = 'tb_login'
  id_login = Column(Integer, primary_key=True, autoincrement=True, index=True)
  cpf = Column(VARCHAR(100), nullable=False)
  senha = Column(VARCHAR(200), nullable=False)
  grupo = Column(Integer, nullable=False)
  def __init__(self, id_login, cpf, senha, grupo):
    self.id_login = id_login
    self.cpf = cpf
    self.senha = senha
    self.grupo = grupo