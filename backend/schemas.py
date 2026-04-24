from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

class EmpresaBase(BaseModel):
    cnpj: Optional[str] = None
    nome: Optional[str] = None
    razaosocial: Optional[str] = None
    email: Optional[str] = None
    ativo: Optional[bool] = True

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class ContatoBase(BaseModel):
    razaosocial: Optional[str] = None
    nome: Optional[str] = None
    cpfcnpj: Optional[str] = None

class Contato(ContatoBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class SetorBase(BaseModel):
    codigo: str
    descricao: Optional[str] = None
    sequencia: Optional[int] = None
    ativo: Optional[bool] = True
    avaliacao: Optional[bool] = False
    falha: Optional[bool] = False
    consumomp: Optional[bool] = False
    faturamento: Optional[bool] = False
    expedicao: Optional[bool] = False
    supervisao: Optional[bool] = False
    sopassagem: Optional[bool] = False
    userlan: Optional[str] = None

class SetorCreate(SetorBase):
    pass

class Setor(SetorBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class OperadorBase(BaseModel):
    codigo: str
    nome: Optional[str] = None
    id_setor: Optional[int] = None
    id_depto: Optional[int] = None
    codset: Optional[str] = None
    coddep: Optional[str] = None
    ativo: Optional[bool] = True
    userlan: Optional[str] = None

class OperadorCreate(OperadorBase):
    pass

class Operador(OperadorBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class MedidaBase(BaseModel):
    codigo: str
    descricao: Optional[str] = None

class MedidaCreate(MedidaBase):
    pass

class Medida(MedidaBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class DesenhoBase(BaseModel):
    codigo: Optional[str] = None
    descricao: Optional[str] = None

class DesenhoCreate(DesenhoBase):
    pass

class Desenho(DesenhoBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class TipoRecapBase(BaseModel):
    codigo: Optional[str] = None
    descricao: Optional[str] = None
    ativo: Optional[bool] = True

class TipoRecapCreate(TipoRecapBase):
    pass

class TipoRecap(TipoRecapBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class TipoNotaBase(BaseModel):
    codigo: Optional[int] = None
    descricao: Optional[str] = None
    ativo: Optional[bool] = True

class TipoNotaCreate(TipoNotaBase):
    pass

class TipoNota(TipoNotaBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class ServicoBase(BaseModel):
    codigo: Optional[str] = None
    descricao: Optional[str] = None
    id_recap: Optional[int] = None
    id_medida: Optional[int] = None
    id_desenho: Optional[int] = None
    id_produto: Optional[int] = None
    grupo: Optional[str] = None
    valor: Optional[Decimal] = 0
    ativo: Optional[bool] = True
    userlan: Optional[str] = None

class ServicoCreate(ServicoBase):
    pass

class Servico(ServicoBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class PneuServicoBase(BaseModel):
    id_pneu: int
    id_servico: int
    quant: Optional[int] = 1
    valor: Optional[Decimal] = 0
    vrtotal: Optional[Decimal] = 0

class PneuServico(PneuServicoBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class OrdemServicoBase(BaseModel):
    id_empresa: Optional[int] = None
    id_contato: Optional[int] = None
    id_vendedor: Optional[int] = None
    id_banco: Optional[int] = None
    id_planopag: Optional[int] = None
    numos: Optional[int] = None
    dataentrada: Optional[datetime] = None
    dataprevisao: Optional[datetime] = None
    vrservico: Optional[Decimal] = 0
    vrtotal: Optional[Decimal] = 0
    placa: Optional[str] = None
    status: Optional[str] = None
    obs_fatura: Optional[str] = None

class OrdemServico(OrdemServicoBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class PneuBase(BaseModel):
    id_ordem: Optional[int] = None
    id_fatura: Optional[int] = None
    id_empresa: Optional[int] = None
    id_contato: Optional[int] = None
    id_medida: Optional[int] = None
    id_desenho: Optional[int] = None
    id_recap: Optional[int] = None
    id_servico: Optional[int] = None
    id_produto: Optional[int] = None
    id_vendedor: Optional[int] = None
    codbarra: Optional[str] = None
    numserie: Optional[str] = None
    numfogo: Optional[str] = None
    statuspro: Optional[bool] = True
    statusfat: Optional[bool] = False
    placa: Optional[str] = None
    userlan: Optional[str] = None

class PneuCreate(PneuBase):
    pass

class Pneu(PneuBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    numos: Optional[int] = None
    nome_cliente: Optional[str] = None
    historico: Optional[List] = []

class ProducaoBase(BaseModel):
    id_pneu: int
    id_setor: int
    id_operador: int
    id_retrabalho: Optional[int] = 0
    id_recap: Optional[int] = None
    id_maquina: Optional[int] = None
    id_proximo: Optional[int] = None
    codbarra: Optional[str] = None
    status: Optional[str] = "I"
    inicio: Optional[datetime] = None
    termino: Optional[datetime] = None
    tempo: Optional[Decimal] = 0
    obs: Optional[str] = None
    userlan: Optional[str] = None

class ProducaoCreate(ProducaoBase):
    pass

class Producao(ProducaoBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class AvaliacaoBase(BaseModel):
    id_pneu: int
    id_setor: int
    codbarra: str
    resultado: Optional[str] = None
    obs: Optional[str] = None

class AvaliacaoCreate(AvaliacaoBase):
    pass

class Avaliacao(AvaliacaoBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class FalhaBase(BaseModel):
    codigo: int
    descricao: str

class Falha(FalhaBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class RegistroFalhaBase(BaseModel):
    id_pneu: int
    id_falha: int
    id_setor: int
    id_operador: int
    codbarra: Optional[str] = None
    motivo: Optional[str] = None

class RegistroFalhaCreate(RegistroFalhaBase):
    pass

class RegistroFalha(RegistroFalhaBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    datareg: Optional[datetime] = None
