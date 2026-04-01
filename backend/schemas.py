from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional, List

class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

# Setor
class SetorBase(BaseSchema):
    descricao: str
    tempo_padrao: Optional[float] = 0.0
    sequencia: Optional[int] = 0
    status: Optional[str] = "ATIVO"

class SetorCreate(SetorBase):
    pass

class Setor(SetorBase):
    id: int

# Operador
class OperadorBase(BaseSchema):
    nome: str
    id_setor: int
    valor_hora: Optional[float] = 0.0
    status: Optional[str] = "ATIVO"

class OperadorCreate(OperadorBase):
    pass

class Operador(OperadorBase):
    id: int

# Pneu
class PneuBase(BaseSchema):
    codigo_barra: str
    id_cliente: Optional[int] = 0
    medida: Optional[str] = None
    desenho: Optional[str] = None
    marca: Optional[str] = None
    dot: Optional[str] = None
    numserie: Optional[str] = None
    numfogo: Optional[str] = None
    data_entrada: Optional[date] = None
    data_producao: Optional[date] = None
    data_faturamento: Optional[date] = None
    data_expedicao: Optional[date] = None
    status: Optional[str] = "PENDENTE"

class PneuCreate(PneuBase):
    pass

class Pneu(PneuBase):
    id: int

# Producao
class ProducaoBase(BaseSchema):
    codigo_barra: str
    id_pneu: int
    id_setor: int
    id_operdor: int # Mantendo nome do banco (id_operdor)
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None

class ProducaoCreate(ProducaoBase):
    pass

class Producao(ProducaoBase):
    id: int

# Falha
class FalhaBase(BaseSchema):
    descricao: str
    valor_custo: Optional[float] = 0.0
    status: Optional[str] = "ATIVO"

class FalhaCreate(FalhaBase):
    pass

class Falha(FalhaBase):
    id: int

# Registro Falha
class RegistroFalhaBase(BaseSchema):
    codigo_barra: str
    id_pneu: int
    id_setor: int
    id_operdor: int
    id_falha: int
    data: Optional[date] = None
    observacao: Optional[str] = ""

class RegistroFalhaCreate(RegistroFalhaBase):
    pass

class RegistroFalha(RegistroFalhaBase):
    id: int

# Consumo
class ConsumoBase(BaseSchema):
    id_produto: int
    quantidade: float
    data: Optional[date] = None

class ConsumoCreate(ConsumoBase):
    pass

class Consumo(ConsumoBase):
    id: int

# Expedicao
class ExpedicaoBase(BaseSchema):
    codigo_barra: str
    id_pneu: int
    data: Optional[date] = None
    observacao: Optional[str] = ""

class ExpedicaoCreate(ExpedicaoBase):
    pass

class Expedicao(ExpedicaoBase):
    id: int

# Dashboard / Stats
class DashboardStats(BaseSchema):
    total_producao_dia: int
    total_falhas_dia: int
    pneus_pendentes: int
    ultimas_falhas: List[RegistroFalha]
