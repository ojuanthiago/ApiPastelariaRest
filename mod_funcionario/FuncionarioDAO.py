from fastapi import APIRouter
from mod_funcionario.Funcionario import FuncionarioModel

import db
from mod_funcionario.FuncionarioModel import FuncionarioDB

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE
@router.get("/funcionario/", tags=["Funcionário"])
def get_funcionario():
    try:
        session = db.Session()
        # busca todos
        dados = session.query(FuncionarioDB).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/funcionario/{id}", tags=["Funcionário"])
def get_funcionario(id: int):
    try:
        session = db.Session()
        # busca um com filtro
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/funcionario/", tags=["Funcionário"])
def post_funcionario(corpo: FuncionarioModel):
    try:
        session = db.Session()
        dados = FuncionarioDB(None, corpo.nome, corpo.matricula,

        corpo.cpf, corpo.telefone, corpo.grupo, corpo.senha)

        session.add(dados)
        session.commit()
        return {"id": dados.id_funcionario}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/funcionario/{id}", tags=["Funcionário"])
def put_funcionario(id: int, corpo: FuncionarioModel):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(
        FuncionarioDB.id_funcionario == id).one()
        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        dados.senha = corpo.senha
        dados.matricula = corpo.matricula
        dados.grupo = corpo.grupo
        session.add(dados)
        session.commit()
        return {"id": dados.id_funcionario}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one()
        session.delete(dados)
        session.commit()
        return {"id": dados.id_funcionario}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()