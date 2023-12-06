from fastapi import APIRouter, Depends, Form, HTTPException
import security
from mod_login.Login import Login

import db
from mod_login.LoginModel import LoginDB

router = APIRouter(dependencies=[Depends(security.verify_token), Depends(security.verify_key)])

@router.get("/login/", tags=["Login"])
def get_login():
    try:
        session = db.Session()
        dados = session.query(LoginDB).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/login", tags=["Login"])
def post_login(corpo: Login):
    try:
        session = db.Session()
        dados = LoginDB(None, corpo.cpf, corpo.senha, corpo.grupo)
        session.add(dados)
        session.commit()
        return {"id": dados.id_login}, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/login/{id}", tags=["Login"])
def get_login(id: int):
    try:
        session = db.Session()
        dados = session.query(LoginDB).filter(LoginDB.id_login == id).one()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()


@router.put("/login/{id}", tags=["Login"])
def put_login(id: int, corpo: Login):
    try:
        session = db.Session()
        dados = session.query(LoginDB).filter(LoginDB.id_login == id).one()
        dados.cpf = corpo.cpf
        dados.senha = corpo.senha
        dados.grupo = corpo.grupo
        session.add(dados)
        session.commit()
        return {"id": dados.id_login}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/login/{id}", tags=["Login"])
def delete_login(id: int):
    try:
        session = db.Session()
        dados = session.query(LoginDB).filter(LoginDB.id_login == id).one()
        session.delete(dados)
        session.commit()
        return {"status": "deletado"}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/login/autenticar", tags=["Login"])
def autenticar(cpf: str = Form(...), senha: str = Form(...)):
    if not cpf or not senha:
        raise HTTPException(status_code=422,
                            detail="Os parâmetros 'cpf' e 'senha' são obrigatórios.")
    user = LoginDB(cpf=cpf, senha=senha, grupo=0, id_login=0)
    if not user:
        raise HTTPException(status_code=403,
                            detail="CPF e/ou nome de usuário incorreto(s).")
    return user