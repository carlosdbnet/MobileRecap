from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, CHAR, TIMESTAMP, Boolean, func
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
    __tablename__ = "empresa"
    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String(18))
    nome = Column(String(50)) # Anteriormente nomefantasia
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
    inscestadual = Column(String(15)) # Anteriormente inscricao
    inscmunicipio = Column(String(12))
    ativo = Column(Boolean) # Ajustado para Boolean conforme DB
    token = Column(String(8000))

class Contato(Base):
    __tablename__ = "contato"
    id = Column(Integer, primary_key=True, index=True)
    razaosocial = Column(String(100))

class Setor(Base):
    __tablename__ = "setor"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(10), nullable=False)
    descricao = Column(String(50))
    sequencia = Column(Integer)
    tempomedio = Column(Integer)
    tempominimo = Column(Integer)
    qmeta = Column(Integer)
    ativo = Column(Boolean) # Ajustado para Boolean

class Operador(Base):
    __tablename__ = "operador"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(CHAR(20), nullable=False) # Ajustado para CHAR
    nome = Column(String(80))
    cargo = Column(String(10))
    codset = Column(String(10))
    coddep = Column(String(10))
    qmeta = Column(Integer)
    valor = Column(Numeric(15, 2))
    ativo = Column(Boolean) # Ajustado para Boolean
    id_depto = Column(Integer)
    id_setor = Column(Integer, ForeignKey("setor.id"))
    
    setor = relationship("Setor")

class Medida(Base):
    __tablename__ = "medida"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(15), nullable=False)
    descricao = Column(String(50))
    tipo = Column(String(5))
    ativo = Column(Boolean) # Ajustado para Boolean

class Desenho(Base):
    __tablename__ = "desenho"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(10))
    descricao = Column(String(50))
    tipo = Column(String(1))
    ativo = Column(Boolean) # Ajustado para Boolean

class TipoRecap(Base):
    __tablename__ = "tiporecap"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(5))
    descricao = Column(String(50))
    ativo = Column(Boolean) # Ajustado para Boolean
    userlan = Column(String(20))
    datalan = Column(TIMESTAMP)

class TipoNota(Base):
    __tablename__ = "tiponota"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(Integer)
    sinal = Column(String(1))
    descricao = Column(String(50))
    ativo = Column(Boolean) # Ajustado para Boolean
    userlan = Column(String(20))
    datalan = Column(TIMESTAMP)

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
    ativo = Column(Boolean) # Ajustado para Boolean
class OrdemServico(Base):
    __tablename__ = "ordemservico"
    id = Column(Integer, primary_key=True, index=True)
    codemp = Column(String(3))
    numos = Column(Integer)
    tipofat = Column(Integer)
    numctr = Column(Integer)
    cpfcgc = Column(String(18))
    endent = Column(Integer)
    endcob = Column(Integer)
    diaspre = Column(Integer)
    dataos = Column(TIMESTAMP)
    datapre = Column(TIMESTAMP)
    datafat = Column(TIMESTAMP)
    dataent = Column(TIMESTAMP)
    notaent = Column(Integer)
    frete = Column(String(1))
    codtransp = Column(String(5))
    unipro = Column(String(3))
    codven = Column(String(5))
    codban = Column(String(4))
    numage = Column(String(4))
    codcfo = Column(String(5))
    codmsg = Column(Integer)
    codplano = Column(Integer)
    valprod = Column(Numeric(15, 2))
    valserv = Column(Numeric(15, 2))
    vallivr = Column(Numeric(15, 2))
    vbonus = Column(Numeric(15, 2))
    vcarca = Column(Numeric(15, 2))
    vconv = Column(Numeric(15, 2))
    vrequi = Column(Numeric(15, 2))
    valfrete = Column(Numeric(15, 2))
    totalfat = Column(Numeric(15, 2))
    vdescprod = Column(Numeric(15, 2))
    vdescserv = Column(Numeric(15, 2))
    qbonus = Column(Integer)
    pdescprod = Column(Numeric(15, 2))
    pdescserv = Column(Numeric(15, 2))
    pcomserv = Column(Numeric(15, 2))
    pcomprod = Column(Numeric(15, 2))
    placa = Column(String(9))
    carcaca = Column(String(1))
    cgcreq = Column(String(18))
    acabado = Column(String(1))
    msg_nf = Column(String)
    obs_fat = Column(String)
    userlan = Column(String(10))
    datalan = Column(TIMESTAMP)
    docorigem = Column(Integer)
    statlib = Column(String(1))
    datalib = Column(TIMESTAMP)
    userlib = Column(String(10))
    senhalib = Column(String(15))
    motivolib = Column(String)
    serient = Column(String(3))
    emitnfe = Column(String(1))
    statnfe = Column(String(1))
    nummob = Column(Integer)
    somentepar = Column(String(1))
    mudardesenho = Column(String(50))
    formapg = Column(String(10))
    unifat = Column(String(3))
    datadig = Column(TIMESTAMP)
    useretiq = Column(String(10))
    borracheiro = Column(String(100))
    vserv = Column(Numeric(15, 2))
    planta = Column(String(1))
    status = Column(String(1))

class Pneu(Base):
    __tablename__ = "pneu"
    id = Column(Integer, primary_key=True, index=True)
    id_ordem = Column(Integer)
    id_nota = Column(Integer)
    id_recap = Column(Integer)
    id_contato = Column(Integer)
    codbarra = Column(String(15))
    numnota = Column(Integer)
    numserie = Column(CHAR(20)) # Ajustado para CHAR
    numfogo = Column(String(10))
    dot = Column(String(15))
    placa = Column(String(9))
    desenhoriginal = Column(String(12))
    qreforma = Column(Integer)
    quant = Column(Integer)
    valor = Column(Numeric(15, 2))
    vrtotal = Column(Numeric(15, 2))
    vrtabela = Column(Numeric(15, 2))
    pdescto = Column(Numeric(15, 2))
    vrcarcaca = Column(Numeric(15, 2))
    vrcustomp = Column(Numeric(15, 2))
    vrcustodesp = Column(Numeric(15, 2))
    statuspro = Column(Boolean) # Ajustado para Boolean
    statusfat = Column(Boolean) # Ajustado para Boolean
    obs = Column(String(80))
    valornfe = Column(Numeric(15, 2))
    userlan = Column(String(10))
    datalan = Column(TIMESTAMP)
    id_laudo = Column(Integer) # Ajustado para Integer
    id_exped = Column(Integer)
    id_medida = Column(Integer)
    id_desenho = Column(Integer)
    id_marca = Column(Integer)

class PneuServico(Base):
    __tablename__ = "pneu_servico"
    id = Column(Integer, primary_key=True, index=True)
    id_pneu = Column(Integer)
    id_servico = Column(Integer)
    id_nota = Column(Integer)
    seqsrv = Column(Integer)
    codservico = Column(String(30))
    piso = Column(String(3))
    quant = Column(Integer)
    valor = Column(Numeric(15, 2))
    vrtotal = Column(Numeric(15, 2))
    vrtabela = Column(Numeric(15, 2))
    vdesc = Column(Numeric(15, 2))
    pcomiss = Column(Numeric(15, 2))
    vcomiss = Column(Numeric(15, 2))
    userlan = Column(String(10))
    datalan = Column(TIMESTAMP)

class Producao(Base):
    __tablename__ = "apontamento"
    id = Column(Integer, primary_key=True, index=True)
    id_pneu = Column(Integer)
    id_setor = Column(Integer)
    id_operador = Column(Integer, nullable=False)
    id_recap = Column(Integer)
    id_maquina = Column(Integer)
    id_proximo = Column(Integer)
    id_retrabalho = Column(Integer)
    codbarra = Column(String(30))
    status = Column(String(1))
    inicio = Column(TIMESTAMP) # Antigo DATAINI
    termino = Column(TIMESTAMP) # Antigo DATAFIM
    tempo = Column(Numeric(15, 2))
    obs = Column(String(100))
    userlan = Column(String(20))
    datalan = Column(TIMESTAMP, server_default=func.now())

class Avaliacao(Base):
    __tablename__ = "pneu_avaliacao"
    id = Column(Integer, primary_key=True, index=True)
    id_pneu = Column(Integer, nullable=False)
    id_setor = Column(Integer, nullable=False)
    codbarra = Column(String(30), nullable=False)
    id_empresa = Column(Integer)
    numos = Column(Integer)
    seqos = Column(Integer)
    dataexa = Column(TIMESTAMP, server_default=func.now())
    tempo = Column(Numeric(15, 2))
    resultado = Column(String(1))
    obs = Column(String(100))
    userlan = Column(String(20))
    datalan = Column(TIMESTAMP, server_default=func.now())

class Falha(Base):
    """Catálogo de tipos de falha (tabela física: falha)"""
    __tablename__ = "falha"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(Integer)
    descricao = Column(String(50))
    ativo = Column(Boolean, default=True)

class RegistroFalha(Base):
    """Registro de falhas em pneus (tabela PNEU_FALHA)"""
    __tablename__ = "pneu_falha"
    id = Column(Integer, primary_key=True, index=True)
    id_pneu = Column(Integer, nullable=False)
    id_falha = Column(Integer, nullable=False)
    id_setor = Column(Integer, nullable=False)
    id_operador = Column(Integer, nullable=False)
    codbarra = Column(String(30))
    motivo = Column(String(255))
    datareg = Column(TIMESTAMP)
    valor = Column(Numeric(15, 2))
    userlan = Column(String(20))
    datalan = Column(TIMESTAMP, server_default=func.now())
