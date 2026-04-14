from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

# Helper for S/N conversion
def convert_to_sn(v):
    if v is True: return "S"
    if v is False: return "N"
    return v

# --- Empresa ---
class EmpresaBase(BaseModel):
    CNPJ: Optional[str] = Field(None, alias="cnpj")
    NOME: Optional[str] = Field(None, alias="nome")
    RAZAOSOCIAL: Optional[str] = Field(None, alias="razaosocial")
    ENDERECO: Optional[str] = Field(None, alias="endereco")
    NUMCASA: Optional[str] = Field(None, alias="numcasa")
    BAIRRO: Optional[str] = Field(None, alias="bairro")
    CEP: Optional[str] = Field(None, alias="cep")
    CIDADE: Optional[str] = Field(None, alias="cidade")
    UF: Optional[str] = Field(None, alias="uf")
    TELEFONE: Optional[str] = Field(None, alias="telefone")
    EMAIL: Optional[str] = Field(None, alias="email")
    INSCRIÇÃO: Optional[str] = Field(None, alias="inscestadual")
    TOKEN: Optional[str] = Field(None, alias="token")
    ATIVO: Optional[str] = Field(None, alias="ativo")
    
    @field_validator("ATIVO", mode="before")
    @classmethod
    def validate_ativo(cls, v):
        return convert_to_sn(v)
        
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    ID: int = Field(..., alias="id")

# --- Setor ---
class SetorBase(BaseModel):
    CODIGO: Optional[str] = Field(None, alias="codigo")
    DESCRICAO: Optional[str] = Field(None, alias="descricao")
    SEQUENCIA: Optional[int] = Field(None, alias="sequencia")
    ATIVO: Optional[str] = Field(None, alias="ativo")
    TEMPOMEDIO: Optional[int] = Field(None, alias="tempomedio")
    QMETA: Optional[int] = Field(None, alias="qmeta")
        
    @field_validator("ATIVO", mode="before")
    @classmethod
    def validate_ativo(cls, v):
        return convert_to_sn(v)
        
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

class SetorCreate(SetorBase):
    pass

class Setor(SetorBase):
    ID: int = Field(..., alias="id")

# --- Operador ---
class OperadorBase(BaseModel):
    CODIGO: Optional[str] = Field(None, alias="codigo")
    NOME: Optional[str] = Field(None, alias="nome")
    CARGO: Optional[str] = Field(None, alias="cargo")
    CODSET: Optional[str] = Field(None, alias="codset")
    VALOR: Optional[Decimal] = Field(None, alias="valor")
    ATIVO: Optional[str] = Field(None, alias="ativo")
        
    @field_validator("ATIVO", mode="before")
    @classmethod
    def validate_ativo(cls, v):
        return convert_to_sn(v)
        
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

class OperadorCreate(OperadorBase):
    pass

class Operador(OperadorBase):
    ID: int = Field(..., alias="id")
    setor: Optional[Setor] = None

# --- Medida ---
class MedidaBase(BaseModel):
    CODIGO: Optional[str] = Field(None, alias="codigo")
    DESCRICAO: Optional[str] = Field(None, alias="descricao")
    TIPO: Optional[str] = Field(None, alias="tipo")
    ATIVO: Optional[str] = Field(None, alias="ativo")
        
    @field_validator("ATIVO", mode="before")
    @classmethod
    def validate_ativo(cls, v):
        return convert_to_sn(v)
        
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

class MedidaCreate(MedidaBase):
    pass

class Medida(MedidaBase):
    ID: int = Field(..., alias="id")

# --- Desenho ---
class DesenhoBase(BaseModel):
    CODIGO: Optional[str] = Field(None, alias="codigo")
    DESCRICAO: Optional[str] = Field(None, alias="descricao")
    TIPO: Optional[str] = Field(None, alias="tipo")
    ATIVO: Optional[str] = Field(None, alias="ativo")
        
    @field_validator("ATIVO", mode="before")
    @classmethod
    def validate_ativo(cls, v):
        return convert_to_sn(v)
        
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

class DesenhoCreate(DesenhoBase):
    pass

class Desenho(DesenhoBase):
    ID: int = Field(..., alias="id")

# --- TipoRecap ---
class TipoRecapBase(BaseModel):
    CODIGO: Optional[str] = Field(None, alias="codigo")
    DESCRICAO: Optional[str] = Field(None, alias="descricao")
    ATIVO: Optional[str] = Field(None, alias="ativo")
        
    @field_validator("ATIVO", mode="before")
    @classmethod
    def validate_ativo(cls, v):
        return convert_to_sn(v)
        
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

class TipoRecapCreate(TipoRecapBase):
    pass

class TipoRecap(TipoRecapBase):
    ID: int = Field(..., alias="id")
    DATALAN: Optional[datetime] = Field(None, alias="datalan")

# --- TipoNota ---
class TipoNotaBase(BaseModel):
    CODIGO: Optional[int] = Field(None, alias="codigo")
    SINAL: Optional[str] = Field(None, alias="sinal")
    DESCRICAO: Optional[str] = Field(None, alias="descricao")
    ATIVO: Optional[str] = Field(None, alias="ativo")
        
    @field_validator("ATIVO", mode="before")
    @classmethod
    def validate_ativo(cls, v):
        return convert_to_sn(v)
        
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

class TipoNotaCreate(TipoNotaBase):
    pass

class TipoNota(TipoNotaBase):
    ID: int = Field(..., alias="id")
    DATALAN: Optional[datetime] = Field(None, alias="datalan")

# --- Servico ---
class ServicoBase(BaseModel):
    CODSERVICO: Optional[str] = Field(None, alias="codservico")
    DESCRICAO: Optional[str] = Field(None, alias="descricao")
    MEDIDA: Optional[str] = Field(None, alias="medida")
    DESENHO: Optional[str] = Field(None, alias="desenho")
    ID_RECAP: Optional[int] = Field(None, alias="id_recap")
    CODRECAP: Optional[str] = Field(None, alias="codrecap")
    PISO: Optional[str] = Field(None, alias="piso")
    ATIVO: Optional[str] = Field(None, alias="ativo")
        
    @field_validator("ATIVO", mode="before")
    @classmethod
    def validate_ativo(cls, v):
        return convert_to_sn(v)
        
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

class ServicoCreate(ServicoBase):
    pass

class Servico(ServicoBase):
    ID: int = Field(..., alias="id")

from datetime import datetime
from decimal import Decimal

# Schemas para Ordem de Serviço (OS)
class OrdemServicoBase(BaseModel):
    codemp: Optional[str] = None
    numos: Optional[int] = None
    tipofat: Optional[int] = None
    numctr: Optional[int] = None
    cpfcgc: Optional[str] = None
    endent: Optional[int] = None
    endcob: Optional[int] = None
    diaspre: Optional[int] = None
    dataos: Optional[datetime] = None
    datapre: Optional[datetime] = None
    datafat: Optional[datetime] = None
    dataent: Optional[datetime] = None
    notaent: Optional[int] = None
    frete: Optional[str] = None
    codtransp: Optional[str] = None
    unipro: Optional[str] = None
    codven: Optional[str] = None
    codban: Optional[str] = None
    numage: Optional[str] = None
    codcfo: Optional[str] = None
    codmsg: Optional[int] = None
    codplano: Optional[int] = None
    valprod: Optional[Decimal] = None
    valserv: Optional[Decimal] = None
    vallivr: Optional[Decimal] = None
    vbonus: Optional[Decimal] = None
    vcarca: Optional[Decimal] = None
    vconv: Optional[Decimal] = None
    vrequi: Optional[Decimal] = None
    valfrete: Optional[Decimal] = None
    totalfat: Optional[Decimal] = None
    vdescprod: Optional[Decimal] = None
    vdescserv: Optional[Decimal] = None
    qbonus: Optional[int] = None
    pdescprod: Optional[Decimal] = None
    pdescserv: Optional[Decimal] = None
    pcomserv: Optional[Decimal] = None
    pcomprod: Optional[Decimal] = None
    placa: Optional[str] = None
    carcaca: Optional[str] = None
    cgcreq: Optional[str] = None
    acabado: Optional[str] = None
    msg_nf: Optional[str] = None
    obs_fat: Optional[str] = None
    userlan: Optional[str] = None
    datalan: Optional[datetime] = None
    docorigem: Optional[int] = None
    statlib: Optional[str] = None
    datalib: Optional[datetime] = None
    userlib: Optional[str] = None
    senhalib: Optional[str] = None
    motivolib: Optional[str] = None
    serient: Optional[str] = None
    emitnfe: Optional[str] = None
    statnfe: Optional[str] = None
    nummob: Optional[int] = None
    somentepar: Optional[str] = None
    mudardesenho: Optional[str] = None
    formapg: Optional[str] = None
    unifat: Optional[str] = None
    datadig: Optional[datetime] = None
    useretiq: Optional[str] = None
    borracheiro: Optional[str] = None
    vserv: Optional[Decimal] = None
    planta: Optional[str] = None
    status: Optional[str] = None

class OrdemServicoCreate(OrdemServicoBase):
    pass

class OrdemServico(OrdemServicoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Schemas para Pneu
class PneuBase(BaseModel):
    id_ordem: Optional[int] = None
    id_nota: Optional[int] = None
    id_recap: Optional[int] = None
    id_contato: Optional[int] = None
    codbarra: Optional[str] = None
    numnota: Optional[int] = None
    numserie: Optional[str] = None
    numfogo: Optional[str] = None
    dot: Optional[str] = None
    placa: Optional[str] = None
    desenhoriginal: Optional[str] = None
    qreforma: Optional[int] = None
    quant: Optional[int] = None
    valor: Optional[Decimal] = None
    vrtotal: Optional[Decimal] = None
    vrtabela: Optional[Decimal] = None
    pdescto: Optional[Decimal] = None
    vrcarcaca: Optional[Decimal] = None
    vrcustomp: Optional[Decimal] = None
    vrcustodesp: Optional[Decimal] = None
    statuspro: Optional[str] = None
    statusfat: Optional[str] = None
    obs: Optional[str] = None
    valornfe: Optional[Decimal] = None
    userlan: Optional[str] = None
    datalan: Optional[datetime] = None
    id_laudo: Optional[str] = None
    id_exped: Optional[int] = None
    id_medida: Optional[int] = None
    id_desenho: Optional[int] = None
    id_marca: Optional[int] = None

    @field_validator("statuspro", "statusfat", "id_laudo", mode="before")
    @classmethod
    def validate_booleans(cls, v):
        return convert_to_sn(v)
        
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

class PneuCreate(PneuBase):
    pass

class Pneu(PneuBase):
    id: int
    numos: Optional[int] = None
    nome_cliente: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

# Schemas para Pneu_Servico
class PneuServicoBase(BaseModel):
    id_pneu: Optional[int] = None
    id_servico: Optional[int] = None
    id_nota: Optional[int] = None
    seqsrv: Optional[int] = None
    codservico: Optional[str] = None
    piso: Optional[str] = None
    quant: Optional[int] = None
    valor: Optional[Decimal] = None
    vrtotal: Optional[Decimal] = None
    vrtabela: Optional[Decimal] = None
    vdesc: Optional[Decimal] = None
    pcomiss: Optional[Decimal] = None
    vcomiss: Optional[Decimal] = None
    userlan: Optional[str] = None
    datalan: Optional[datetime] = None

class PneuServicoCreate(PneuServicoBase):
    pass

class PneuServico(PneuServicoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Schemas para Producao
class ProducaoBase(BaseModel):
    id_pneu: Optional[int] = None
    id_setor: Optional[int] = None
    id_operador: int
    id_recap: Optional[int] = None
    id_maquina: Optional[int] = None
    id_proximo: Optional[int] = None
    id_retrabalho: Optional[int] = None
    codbarra: Optional[str] = Field(None, alias="codigo_barra")
    status: Optional[str] = None
    inicio: Optional[datetime] = Field(None, alias="data_inicio")
    termino: Optional[datetime] = None
    tempo: Optional[Decimal] = None
    obs: Optional[str] = None
    userlan: Optional[str] = None
    datalan: Optional[datetime] = None

    @field_validator("inicio", "termino", mode="before")
    @classmethod
    def validate_datetime(cls, v):
        if isinstance(v, str) and len(v) == 10:
            return f"{v}T00:00:00"
        return v

    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

class ProducaoCreate(ProducaoBase):
    pass

class Producao(ProducaoBase):
    id: int

# Schemas para Avaliação
class AvaliacaoBase(BaseModel):
    id_pneu: int
    id_setor: int
    codbarra: str
    id_empresa: Optional[int] = None
    numos: Optional[int] = None
    seqos: Optional[int] = None
    dataexa: Optional[datetime] = None
    tempo: Optional[Decimal] = None
    resultado: Optional[str] = None
    obs: Optional[str] = None
    userlan: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

class AvaliacaoCreate(AvaliacaoBase):
    pass

class Avaliacao(AvaliacaoBase):
    id: int


# --- Falha (Catálogo - TABGERAL) ---
class FalhaBase(BaseModel):
    codigo: Optional[int] = None
    descricao: Optional[str] = None
    ativo: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

class Falha(FalhaBase):
    id: int

# --- RegistroFalha (PNEU_FALHA) ---
class RegistroFalhaCreate(BaseModel):
    id_pneu: int
    id_falha: int
    id_setor: int
    id_operador: int
    codbarra: Optional[str] = None
    motivo: Optional[str] = None
    datareg: Optional[datetime] = None
    valor: Optional[Decimal] = None
    userlan: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class RegistroFalha(RegistroFalhaCreate):
    id: int
    datalan: Optional[datetime] = None

