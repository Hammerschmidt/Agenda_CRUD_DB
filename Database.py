from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session

from DBClasses import Endereco, Base, Pessoa, engine, Telefone

DBSession = sessionmaker(bind=engine, expire_on_commit=False)


def insertPessoa(nome_, email_):
    session = DBSession()
    p = Pessoa(nome=nome_, email=email_)
    session.add(p)
    session.commit()
    session.close()
    return p


def insertEndereco(rua_, numero_, cep_, pessoa_):
    session = DBSession()
    e = Endereco(rua=rua_, numero=numero_, cep=cep_, pessoa=pessoa_)
    session.add(e)
    session.commit()
    session.close()
    return e


def insertTelefone(telefone_, tipo_, pessoa_):
    session = DBSession()
    f = Telefone(tipo_telefone=tipo_, numero=telefone_, pessoa=pessoa_)
    session.add(f)
    session.commit()
    session.close()


def updatePessoa(pessoa_):
    session = DBSession()
    session.add(pessoa_)
    session.commit()
    session.close()
    return pessoa_


def updateEndereco(endereco_):
    session = DBSession()
    session.add(endereco_)
    session.commit()
    session.close()
    return endereco_


def updateTelefone(telefone_):
    session = DBSession()
    session.add(telefone_)
    session.commit()
    session.close()
    return telefone_


def getPessoa(nome_):
    session = DBSession()
    pessoa = session.query(Pessoa).filter_by(nome=nome_).first()
    session.close()
    return pessoa


def getPessoas():
    session = DBSession()
    pessoas = session.query(Pessoa).all()
    session.close()
    return pessoas


def getEnderecos():
    session = DBSession()
    enderecos = session.query(Endereco).all()
    session.close()
    return enderecos


def getEnderecos(pessoa):
    session = DBSession()
    enderecos = session.query(Endereco).filter_by(pessoa_id=pessoa.id).all()
    session.close()
    return enderecos


def getTelefones():
    session = DBSession()
    telefones = session.query(Endereco).all()
    session.close()
    return telefones


def getTelefones(pessoa):
    session = DBSession()
    telefones = session.query(Telefone).filter_by(pessoa_id=pessoa.id).all()
    session.close()
    return telefones


def deletarPessoa(nome_):
    session = DBSession()
    p = getPessoa(nome_)
    if p != None:
        telefones = session.query(Telefone).filter_by(pessoa_id=p.id)
        for x in telefones:
            session.delete(x)
        enderecos = session.query(Endereco).filter_by(pessoa_id=p.id)
        for x in enderecos:
            session.delete(x)
            session.delete(p)
            session.commit()
    else:
        print("Contato não encontrado.\n")

    session.close()
