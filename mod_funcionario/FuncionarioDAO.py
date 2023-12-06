from fastapi import APIRouter, Depends
from mod_funcionario.Funcionario import FuncionarioModel

# import da segurança
import security

import db
from mod_funcionario.FuncionarioModel import FuncionarioDB

router = APIRouter( dependencies=[Depends(security.verify_token), Depends(security.verify_key)] )

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

@router.get("/funcionario/{cpf}", tags=["Funcionário"])
def get_funcionario(cpf: str):
    try:
        session = db.Session()
        # busca um com filtro
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.cpf == cpf).all()
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
        return {"cpf": dados.cpf}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/funcionario/{cpf}", tags=["Funcionário"])
def put_funcionario(cpf: str, corpo: FuncionarioModel):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(
        FuncionarioDB.cpf == cpf).one()
        dados.id_funcionario = corpo.id_funcionario
        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        dados.senha = corpo.senha
        dados.matricula = corpo.matricula
        dados.grupo = corpo.grupo
        session.add(dados)
        session.commit()
        return {"cpf": dados.cpf}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/funcionario/{cpf}", tags=["Funcionário"])
def delete_funcionario(cpf: str):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.cpf == cpf).one()
        session.delete(dados)
        session.commit()
        return {"cpf": dados.cpf}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()