import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoa'

    id = Column(Integer, primary_key=True)
    nome = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Endereco(Base):
    __tablename__ = 'endereco'

    id = Column(Integer, primary_key=True)
    rua = Column(String(250))
    numero = Column(String(250))
    cep = Column(String(250), nullable=False)
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship(Pessoa)


class Telefone(Base):
    __tablename__ = 'telefones'

    id = Column(Integer, primary_key=True)
    tipo_telefone = Column(String(250))
    numero = Column(Integer)
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship(Pessoa)

# Cria o engine apontando para o arquivo pessoa.db
engine = create_engine('sqlite:///agenda.db')
#engine = create_engine('mysql://versatek1:aluno123!!@xmysql1.versatek.com.br:3306/versatek1')

# Cria todas as tabelas. Isso e equivalente ao "Create Table" do SQL
Base.metadata.create_all(engine)
