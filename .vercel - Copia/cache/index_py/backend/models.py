from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, CHAR, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
    __tablename__ = "EMPRESA"
    ID = Column(Integer, primary_key=True, index=True)
    CODEMP = Column(CHAR(3))
    CNPJ = Column(String)
    NOMEFANTASIA = Column(String(50))
    RAZAOSOCIAL = Column(String(100))
    ENDERECO = Column(CHAR(60))
    NUMCASA = Column(CHAR(10))
    BAIRRO = Column(CHAR(30))
    CEP = Column(CHAR(9))
    CIDADE = Column(CHAR(60))
    UF = Column(CHAR(2))
    INSCRICAO = Column(CHAR(15))
    TELEFONE = Column(CHAR(17))
    EMAIL = Column(CHAR(80))
    TOKEN = Column(String(8000))
    ATIVO = Column(CHAR(1))

class Setor(Base):
    __tablename__ = "SETOR"
    ID = Column(Integer, primary_key=True, index=True)
    CODSET = Column(String(10))
    DESCRICAO = Column(String(50))
    SEQUENCIA = Column(Integer)
    ATIVO = Column(CHAR(1))
    TEMPOMEDIO = Column(Integer)
    QMETA = Column(Integer)

class Operador(Base):
    __tablename__ = "OPERADOR"
    ID = Column(Integer, primary_key=True, index=True)
    CODFUN = Column(CHAR(20))
    NOME = Column(String(80))
    CARGO = Column(String(10))
    ID_SETOR = Column(Integer, ForeignKey("SETOR.ID"))
    VALOR = Column(Numeric)
    ATIVO = Column(CHAR(1))
    
    setor = relationship("Setor")

class Medida(Base):
    __tablename__ = "MEDIDA"
    ID = Column(Integer, primary_key=True, index=True)
    CODIGO = Column(CHAR(15))
    DESCRICAO = Column(CHAR(50))
    TIPO = Column(CHAR(5))
    ATIVO = Column(CHAR(1))

class Desenho(Base):
    __tablename__ = "DESENHO"
    ID = Column(Integer, primary_key=True, index=True)
    CODIGO = Column(String(10))
    DESCRICAO = Column(String(50))
    TIPO = Column(CHAR(1))
    LARGURA = Column(String(3))
    ATIVO = Column(CHAR(1))

class Servico(Base):
    __tablename__ = "SERVICO"
    ID = Column(Integer, primary_key=True, index=True)
    CODSERVICO = Column(String(30))
    DESCRICAO = Column(String(100))
    MEDIDA = Column(String(20))
    DESENHO = Column(String(20))
    TIPOSERV = Column(String(5))
    ATIVO = Column(CHAR(1))

class Pneu(Base):
    __tablename__ = "PNEU"
    ID = Column(Integer, primary_key=True, index=True)
    CODBARRA = Column(String(15))
    NUMOS = Column(Integer)
    SEQOS = Column(Integer)
    CPFCNPJ = Column(CHAR(18))
    MEDIDA = Column(String(20))
    DESENHO = Column(String(20))
    TIPOSERV = Column(String(5))
    MARCA = Column(CHAR(10))
    NUMSERIE = Column(CHAR(20))
    NUMFOGO = Column(String(10))
    DOT = Column(String(15))
    PLACA = Column(String(10))
    VALOR = Column(Numeric)
    STATPRO = Column(CHAR(1))
    STATFAT = Column(CHAR(1))
    DATALAN = Column(TIMESTAMP)
    USERLAN = Column(CHAR(10))
