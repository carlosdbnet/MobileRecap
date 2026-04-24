from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

# --- Empresa ---
class EmpresaBase(BaseModel):
    CODEMP: Optional[str] = None
    CNPJ: Optional[str] = None
    NOMEFANTASIA: Optional[str] = None
    RAZAOSOCIAL: Optional[str] = None
    ENDERECO: Optional[str] = None
    NUMCASA: Optional[str] = None
    BAIRRO: Optional[str] = None
    CEP: Optional[str] = None
    CIDADE: Optional[str] = None
    UF: Optional[str] = None
    TELEFONE: Optional[str] = None
    EMAIL: Optional[str] = None
    TOKEN: Optional[str] = None
    ATIVO: Optional[str] = "S"

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    ID: int
    model_config = ConfigDict(from_attributes=True)

# --- Setor ---
class SetorBase(BaseModel):
    CODSET: Optional[str] = None
    DESCRICAO: Optional[str] = None
    SEQUENCIA: Optional[int] = None
    ATIVO: Optional[str] = "S"
    TEMPOMEDIO: Optional[int] = None
    QMETA: Optional[int] = None

class SetorCreate(SetorBase):
    pass

class Setor(SetorBase):
    ID: int
    model_config = ConfigDict(from_attributes=True)

# --- Operador ---
class OperadorBase(BaseModel):
    CODFUN: Optional[str] = None
    NOME: Optional[str] = None
    CARGO: Optional[str] = None
    ID_SETOR: Optional[int] = None
    VALOR: Optional[Decimal] = None
    ATIVO: Optional[str] = "S"

class OperadorCreate(OperadorBase):
    pass

class Operador(OperadorBase):
    ID: int
    setor: Optional[Setor] = None
    model_config = ConfigDict(from_attributes=True)

# --- Medida ---
class MedidaBase(BaseModel):
    CODIGO: Optional[str] = None
    DESCRICAO: Optional[str] = None
    TIPO: Optional[str] = None
    ATIVO: Optional[str] = "S"

class MedidaCreate(MedidaBase):
    pass

class Medida(MedidaBase):
    ID: int
    model_config = ConfigDict(from_attributes=True)

# --- Desenho ---
class DesenhoBase(BaseModel):
    CODIGO: Optional[str] = None
    DESCRICAO: Optional[str] = None
    TIPO: Optional[str] = None
    LARGURA: Optional[str] = None
    ATIVO: Optional[str] = "S"

class DesenhoCreate(DesenhoBase):
    pass

class Desenho(DesenhoBase):
    ID: int
    model_config = ConfigDict(from_attributes=True)

# --- Servico ---
class ServicoBase(BaseModel):
    CODSERVICO: Optional[str] = None
    DESCRICAO: Optional[str] = None
    MEDIDA: Optional[str] = None
    DESENHO: Optional[str] = None
    TIPOSERV: Optional[str] = None
    ATIVO: Optional[str] = "S"

class ServicoCreate(ServicoBase):
    pass

class Servico(ServicoBase):
    ID: int
    model_config = ConfigDict(from_attributes=True)

# --- Pneu ---
class PneuBase(BaseModel):
    CODBARRA: Optional[str] = None
    NUMOS: Optional[int] = None
    SEQOS: Optional[int] = None
    CPFCNPJ: Optional[str] = None
    MEDIDA: Optional[str] = None
    DESENHO: Optional[str] = None
    TIPOSERV: Optional[str] = None
    MARCA: Optional[str] = None
    NUMSERIE: Optional[str] = None
    NUMFOGO: Optional[str] = None
    DOT: Optional[str] = None
    PLACA: Optional[str] = None
    VALOR: Optional[Decimal] = None
    STATPRO: Optional[str] = None
    STATFAT: Optional[str] = None
    USERLAN: Optional[str] = None

class PneuCreate(PneuBase):
    pass

class Pneu(PneuBase):
    ID: int
    DATALAN: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)
