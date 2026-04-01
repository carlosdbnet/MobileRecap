from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, BLOB
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
    __tablename__ = "empresa"
    id = Column(Integer, primary_key=True, index=True)
    razaosocial = Column(String(200))
    nomefantasia = Column(String(200))
    endereco = Column(String(255))
    bairro = Column(String(100))
    cep = Column(String(30))
    cidade = Column(String(100))
    uf = Column(String(2))
    Cnpj = Column(String(20))
    inscricao = Column(String(100))
    telefone = Column(String(50))
    email = Column(String(150))
    incricaomunicipal = Column(String(50))
    aliquotaiss = Column(Float)
    regimetributacao = Column(String(100))
    clientid = Column(String(255))
    secretid = Column(String(255))
    codigoaut2 = Column(String(255))
    token = Column(String(8000))
    logo = Column(BLOB)

class Setor(Base):
    __tablename__ = "setor"
    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(200))
    tempo_padrao = Column(Float)
    sequencia = Column(Integer)
    status = Column(String(20))

class Operador(Base):
    __tablename__ = "operador"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(200))
    id_setor = Column(Integer, ForeignKey("setor.id"))
    valor_hora = Column(Float)
    status = Column(String(20))
    
    setor = relationship("Setor")

class Pneu(Base):
    __tablename__ = "pneu"
    id = Column(Integer, primary_key=True, index=True)
    codigo_barra = Column(String(100))
    id_cliente = Column(Integer)
    medida = Column(String(20))
    desenho = Column(String(20))
    marca = Column(String(20))
    dot = Column(String(20))
    numserie = Column(String(20))
    numfogo = Column(String(20))
    data_entrada = Column(Date)
    data_producao = Column(Date)
    data_faturamento = Column(Date)
    data_expedicao = Column(Date)
    status = Column(String(20))

class Producao(Base):
    __tablename__ = "producao"
    id = Column(Integer, primary_key=True, index=True)
    codigo_barra = Column(String(100))
    id_pneu = Column(Integer, ForeignKey("pneu.id"))
    id_setor = Column(Integer, ForeignKey("setor.id"))
    id_operdor = Column(Integer) # Mantendo nome do banco (id_operdor)
    data_inicio = Column(Date)
    data_fim = Column(Date)
    
    pneu = relationship("Pneu")
    setor = relationship("Setor")

class Falha(Base):
    __tablename__ = "falha"
    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(255))
    valor_custo = Column(Float)
    status = Column(String(20))

class RegistroFalha(Base):
    __tablename__ = "regitrofalha" # Mantendo nome do banco (regitrofalha)
    id = Column(Integer, primary_key=True, index=True)
    codigo_barra = Column(String(100))
    id_pneu = Column(Integer, ForeignKey("pneu.id"))
    id_setor = Column(Integer, ForeignKey("setor.id"))
    id_operdor = Column(Integer)
    id_falha = Column(Integer, ForeignKey("falha.id"))
    data = Column(Date)
    observacao = Column(String(200))

    pneu = relationship("Pneu")
    setor = relationship("Setor")
    falha = relationship("Falha")

class Consumo(Base):
    __tablename__ = "consumo"
    id = Column(Integer, primary_key=True, index=True)
    id_produto = Column(Integer)
    quantidade = Column(Float)
    data = Column(Date)

class Expedicao(Base):
    __tablename__ = "expedicao"
    id = Column(Integer, primary_key=True, index=True)
    codigo_barra = Column(String(100))
    id_pneu = Column(Integer, ForeignKey("pneu.id"))
    data = Column(Date)
    observacao = Column(String(200))
    
    pneu = relationship("Pneu")
