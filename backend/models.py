from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, CHAR, TIMESTAMP, Boolean, func, Text
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
    __tablename__ = "empresa"
    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String(18))
    nome = Column(String(50))
    razaosocial = Column(String(100))
    endereco = Column(String(60))
    numcasa = Column(String(10))
    bairro = Column(String(30))
    cep = Column(String(9))
    cidade = Column(String(60))
    uf = Column(String(2))
    telefone = Column(String(17))
    cxpostal = Column(String(6))
    email = Column(String(80))
    inscestadual = Column(String(15))
    inscmunicipio = Column(String(12))
    ativo = Column(Boolean)
    token = Column(String(8000))

class Contato(Base):
    __tablename__ = "contato"
    id = Column(Integer, primary_key=True, index=True)
    razaosocial = Column(String(100))
    nome = Column(String(100))
    cpfcnpj = Column(String(18))
    cidade = Column(String(60))
    uf = Column(String(2))
    email = Column(String(80))
    foneprincipal = Column(String(20))

class Setor(Base):
    __tablename__ = "setor"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(10), nullable=False)
    descricao = Column(String(50))
    sequencia = Column(Integer)
    tempomedio = Column(Integer)
    tempominimo = Column(Integer)
    qmeta = Column(Integer)
    ativo = Column(Boolean)
    avaliacao = Column(Boolean)
    falha = Column(Boolean)
    consumomp = Column(Boolean)
    faturamento = Column(Boolean)
    proxsetor = Column(String(10))

class Operador(Base):
    __tablename__ = "operador"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(CHAR(20), nullable=False)
    nome = Column(String(80))
    cargo = Column(String(10))
    id_setor = Column(Integer, ForeignKey("setor.id"))
    ativo = Column(Boolean)
    qmeta = Column(Integer)
    valor = Column(Numeric(15, 2))
    
    setor = relationship("Setor")

class Medida(Base):
    __tablename__ = "medida"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(15), nullable=False)
    descricao = Column(String(50))
    ativo = Column(Boolean)

class Desenho(Base):
    __tablename__ = "desenho"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(10))
    descricao = Column(String(50))
    ativo = Column(Boolean)

class TipoRecap(Base):
    __tablename__ = "tiporecap"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(5))
    descricao = Column(String(50))
    ativo = Column(Boolean)

class TipoNota(Base):
    __tablename__ = "tiponota"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(Integer)
    sinal = Column(String(1))
    descricao = Column(String(50))
    ativo = Column(Boolean)

class Servico(Base):
    __tablename__ = "servico"
    id = Column(Integer, primary_key=True, index=True)
    id_recap = Column(Integer)
    id_medida = Column(Integer)
    id_desenho = Column(Integer)
    codservico = Column(String(30))
    descricao = Column(String(100))
    medida = Column(String(20))
    desenho = Column(String(20))
    codrecap = Column(String(5))
    piso = Column(String(3))
    ativo = Column(Boolean)

class OrdemServico(Base):
    __tablename__ = "ordemservico"
    id = Column(Integer, primary_key=True, index=True)
    id_empresa = Column(Integer)
    id_contato = Column(Integer)
    id_vendedor = Column(Integer)
    id_banco = Column(Integer)
    id_planopag = Column(Integer)
    id_contrato = Column(Integer)
    id_borracheiro = Column(Integer)
    numos = Column(Integer)
    dataentrada = Column(TIMESTAMP)
    dataprevisao = Column(TIMESTAMP)
    vrservico = Column(Numeric(15, 2))
    vrtotal = Column(Numeric(15, 2))
    vrproduto = Column(Numeric(15, 2))
    vrcarcaca = Column(Numeric(15, 2))
    vrbonus = Column(Numeric(15, 2))
    vrmontagem = Column(Numeric(15, 2))
    pcomissao = Column(Numeric(15, 2))
    vrcomissao = Column(Numeric(15, 2))
    id_mobos = Column(Integer)
    datalan = Column(TIMESTAMP)
    serienotaent = Column(Integer)
    numnotaent = Column(Integer)
    emissaopropria = Column(Boolean)
    datalib = Column(TIMESTAMP)
    placa = Column(String(10))
    descricaoveiculo = Column(String(50))
    motivolib = Column(Text)
    obs_fatura = Column(Text)
    chavenotaent = Column(String(50))
    userlan = Column(CHAR(20))
    statuslib = Column(CHAR(1))
    status = Column(String(20))
    usuariolib = Column(CHAR(20))
    senhalib = Column(CHAR(20))

class Pneu(Base):
    __tablename__ = "pneu"
    id = Column(Integer, primary_key=True, index=True)
    id_ordem = Column(Integer)
    id_fatura = Column(Integer) # Antes id_nota
    id_empresa = Column(Integer)
    id_contato = Column(Integer)
    id_medida = Column(Integer)
    id_desenho = Column(Integer)
    codbarra = Column(String(15))
    numserie = Column(CHAR(20))
    numfogo = Column(String(10))
    dot = Column(String(15))
    placa = Column(String(9))
    desenhoriginal = Column(String(12))
    qreforma = Column(Integer)
    quant = Column(Integer)
    valor = Column(Numeric(15, 2))
    vrtotal = Column(Numeric(15, 2))
    statuspro = Column(Boolean)
    statusfat = Column(Boolean)
    obs = Column(String(80))
    valornfe = Column(Numeric(15, 2))
    id_laudo = Column(Integer)
    id_exped = Column(Integer)
    datalan = Column(TIMESTAMP)

class Producao(Base):
    __tablename__ = "apontamento"
    id = Column(Integer, primary_key=True, index=True)
    id_pneu = Column(Integer)
    id_setor = Column(Integer)
    id_operador = Column(Integer, nullable=False)
    id_retrabalho = Column(Integer, default=0)
    codbarra = Column(String(30))
    status = Column(String(1))
    inicio = Column(TIMESTAMP)
    termino = Column(TIMESTAMP)
    tempo = Column(Numeric(15, 2))
    obs = Column(String(100))
    datalan = Column(TIMESTAMP, server_default=func.now())

class Avaliacao(Base):
    __tablename__ = "pneu_avaliacao"
    id = Column(Integer, primary_key=True, index=True)
    id_pneu = Column(Integer, nullable=False)
    id_setor = Column(Integer, nullable=False)
    codbarra = Column(String(30), nullable=False)
    dataexa = Column(TIMESTAMP, server_default=func.now())
    tempo = Column(Numeric(15, 2))
    resultado = Column(String(1))
    obs = Column(String(100))

class Falha(Base):
    __tablename__ = "falha"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(Integer)
    descricao = Column(String(50))
    ativo = Column(Boolean, default=True)

class RegistroFalha(Base):
    __tablename__ = "pneu_falha"
    id = Column(Integer, primary_key=True, index=True)
    id_pneu = Column(Integer, nullable=False)
    id_falha = Column(Integer, nullable=False)
    id_setor = Column(Integer, nullable=False)
    id_operador = Column(Integer, nullable=False)
    codbarra = Column(String(30))
    motivo = Column(String(255))
    datareg = Column(TIMESTAMP)
    datalan = Column(TIMESTAMP, server_default=func.now())

class PneuServico(Base):
    __tablename__ = "pneu_servico"
    id = Column(Integer, primary_key=True, index=True)
    id_pneu = Column(Integer, ForeignKey("pneu.id"))
    id_servico = Column(Integer)
    id_empresa = Column(Integer)
    id_ordem = Column(Integer)
    id_fatura = Column(Integer)
    quant = Column(Integer)
    valor = Column(Numeric(15, 2))
    vrtotal = Column(Numeric(15, 2))
    datalan = Column(TIMESTAMP)
