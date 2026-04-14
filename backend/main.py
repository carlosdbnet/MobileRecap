from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import models
import schemas
from database import engine, get_db
from routers import exames, apontamento, falhas #, auxiliares, consumo, dashboard, expedicao

# Nota: O banco já contém as tabelas migradas, então o SQLAlchemy refletirá elas.
# models.Base.metadata.create_all(bind=engine) 

app = FastAPI(title="MobCap API", description="API para Gerenciamento de Recapagem de Pneus")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "MobCap API is running"}

# Registrar Routers
app.include_router(exames.router)
app.include_router(apontamento.router)
app.include_router(falhas.router)
# app.include_router(auxiliares.router)
# app.include_router(consumo.router)
# app.include_router(dashboard.router)
# app.include_router(expedicao.router)

@app.get("/dashboard")
def get_dashboard_stats(db: Session = Depends(get_db)):
    """
    Retorna estatísticas para o dashboard inicial.
    Por enquanto com dados simulados até as tabelas de histórico estarem populadas.
    """
    return {
        "total_producao_dia": 0,
        "total_falhas_dia": 0,
        "pneus_pendentes": 0,
        "ultimas_falhas": []
    }

# --- Helper logic for CRUD ---
def get_generic_list(model, schema, db, skip=0, limit=100):
    items = db.query(model).offset(skip).limit(limit).all()
    return items

def create_generic(model, schema_in, db):
    db_item = model(**schema_in.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_generic(model, id, schema_in, db):
    db_item = db.query(model).filter(model.id == id).first()
    if not db_item:
        return None
    for var, value in schema_in.model_dump(exclude_unset=True).items():
        setattr(db_item, var, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_generic(model, id, db):
    db_item = db.query(model).filter(model.id == id).first()
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item

# --- ENDPOINTS: EMPRESA ---
@app.get("/empresas", response_model=List[schemas.Empresa])
def list_empresas(db: Session = Depends(get_db)):
    return db.query(models.Empresa).all()

@app.put("/empresas/{id}", response_model=schemas.Empresa, response_model_by_alias=False)
def update_empresa(id: int, empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    res = update_generic(models.Empresa, id, empresa, db)
    if not res: raise HTTPException(status_code=404, detail="Empresa not found")
    return res

# --- ENDPOINTS: SETOR ---
@app.get("/setores", response_model=List[schemas.Setor], response_model_by_alias=False)
def list_setores(db: Session = Depends(get_db)):
    return db.query(models.Setor).order_by(models.Setor.sequencia).all()

@app.post("/setores", response_model=schemas.Setor, response_model_by_alias=False)
def create_setor(setor: schemas.SetorCreate, db: Session = Depends(get_db)):
    return create_generic(models.Setor, setor, db)

# --- ENDPOINTS: OPERADOR ---
@app.get("/operadores", response_model=List[schemas.Operador], response_model_by_alias=False)
def list_operadores(db: Session = Depends(get_db)):
    return db.query(models.Operador).all()

@app.post("/operadores", response_model=schemas.Operador, response_model_by_alias=False)
def create_operador(operador: schemas.OperadorCreate, db: Session = Depends(get_db)):
    return create_generic(models.Operador, operador, db)

# --- ENDPOINTS: MEDIDA ---
@app.get("/medidas", response_model=List[schemas.Medida], response_model_by_alias=False)
def list_medidas(db: Session = Depends(get_db)):
    return db.query(models.Medida).order_by(models.Medida.descricao).all()

@app.post("/medidas", response_model=schemas.Medida, response_model_by_alias=False)
def create_medida(medida: schemas.MedidaCreate, db: Session = Depends(get_db)):
    return create_generic(models.Medida, medida, db)

# --- ENDPOINTS: DESENHO ---
@app.get("/desenhos", response_model=List[schemas.Desenho], response_model_by_alias=False)
def list_desenhos(db: Session = Depends(get_db)):
    return db.query(models.Desenho).order_by(models.Desenho.descricao).all()

@app.post("/desenhos", response_model=schemas.Desenho, response_model_by_alias=False)
def create_desenho(desenho: schemas.DesenhoCreate, db: Session = Depends(get_db)):
    return create_generic(models.Desenho, desenho, db)

# --- ENDPOINTS: TIPORECAP ---
@app.get("/tiporecap", response_model=List[schemas.TipoRecap], response_model_by_alias=False)
def list_tiporecap(db: Session = Depends(get_db)):
    return db.query(models.TipoRecap).all()

@app.post("/tiporecap", response_model=schemas.TipoRecap, response_model_by_alias=False)
def create_tiporecap(tipo: schemas.TipoRecapCreate, db: Session = Depends(get_db)):
    return create_generic(models.TipoRecap, tipo, db)

# --- ENDPOINTS: TIPONOTA ---
@app.get("/tiponotas", response_model=List[schemas.TipoNota], response_model_by_alias=False)
def list_tiponotas(db: Session = Depends(get_db)):
    return db.query(models.TipoNota).all()

@app.post("/tiponotas", response_model=schemas.TipoNota, response_model_by_alias=False)
def create_tiponota(tipo: schemas.TipoNotaCreate, db: Session = Depends(get_db)):
    return create_generic(models.TipoNota, tipo, db)

# --- ENDPOINTS: SERVICO ---
@app.get("/servicos", response_model=List[schemas.Servico], response_model_by_alias=False)
def list_servicos(db: Session = Depends(get_db)):
    return db.query(models.Servico).all()

@app.post("/servicos", response_model=schemas.Servico, response_model_by_alias=False)
def create_servico(servico: schemas.ServicoCreate, db: Session = Depends(get_db)):
    return create_generic(models.Servico, servico, db)

# --- ENDPOINTS: PNEU ---
@app.get("/pneus", response_model=List[schemas.Pneu])
def list_pneus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    results = db.query(models.Pneu, models.OrdemServico.numos, models.Contato.razaosocial).\
        outerjoin(models.OrdemServico, models.Pneu.id_ordem == models.OrdemServico.id).\
        outerjoin(models.Contato, models.Pneu.id_contato == models.Contato.id).\
        offset(skip).limit(limit).all()
    
    pneus = []
    for p, numos, razaosocial in results:
        # Create a dict from the model and add numos
        p_dict = {c.name: getattr(p, c.name) for c in p.__table__.columns}
        p_dict["numos"] = numos
        p_dict["nome_cliente"] = razaosocial
        pneus.append(p_dict)
    return pneus

@app.get("/pneus/buscar")
def buscar_pneu(codbarra: str, db: Session = Depends(get_db)):
    codbarra = codbarra.strip()
    result = db.query(models.Pneu, models.OrdemServico.numos, models.Contato.razaosocial).\
        outerjoin(models.OrdemServico, models.Pneu.id_ordem == models.OrdemServico.id).\
        outerjoin(models.Contato, models.Pneu.id_contato == models.Contato.id).\
        filter(models.Pneu.codbarra == codbarra).first()
    
    if not result:
        raise HTTPException(status_code=404, detail=f"Pneu '{codbarra}' não encontrado")
    
    p, numos, razaosocial = result
    p_dict = {c.name: getattr(p, c.name) for c in p.__table__.columns}
    p_dict["numos"] = numos
    p_dict["nome_cliente"] = razaosocial if razaosocial else "Sem nome cadastrado"

    # Buscar Histórico de Apontamentos (Produção)
    historico = db.query(models.Producao, models.Setor.descricao, models.Setor.sequencia).\
        join(models.Setor, models.Producao.id_setor == models.Setor.id).\
        filter(models.Producao.id_pneu == p.id).\
        order_by(models.Setor.sequencia).all()
    
    lista_hist = []
    for h, desc, seq in historico:
        h_dict = {c.name: getattr(h, c.name) for c in h.__table__.columns}
        h_dict["nome_setor"] = desc
        lista_hist.append(h_dict)
    
    p_dict["historico"] = lista_hist

    return p_dict

@app.post("/pneus", response_model=schemas.Pneu)
def create_pneu(pneu: schemas.PneuCreate, db: Session = Depends(get_db)):
    return create_generic(models.Pneu, pneu, db)

# --- ENDPOINTS: ORDEM SERVICO ---
@app.get("/ordens", response_model=List[schemas.OrdemServico])
def list_ordens(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.OrdemServico).offset(skip).limit(limit).all()

# --- ENDPOINTS: PNEU SERVICO ---
@app.get("/pneu-servicos", response_model=List[schemas.PneuServico])
def list_pneu_servicos(id_pneu: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(models.PneuServico)
    if id_pneu:
        query = query.filter(models.PneuServico.id_pneu == id_pneu)
    return query.all()

# --- ENDPOINTS: AVALIACAO ---
@app.get("/avaliacoes", response_model=List[schemas.Avaliacao])
def list_avaliacoes(db: Session = Depends(get_db)):
    return db.query(models.Avaliacao).all()

@app.post("/avaliacoes", response_model=schemas.Avaliacao)
def create_avaliacao(avaliacao: schemas.AvaliacaoCreate, db: Session = Depends(get_db)):
    return create_generic(models.Avaliacao, avaliacao, db)

@app.get("/devtools/tables")
def get_tables(db: Session = Depends(get_db)):
    from sqlalchemy import text
    result = db.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")).fetchall()
    return [{"table": r[0]} for r in result]

@app.get("/devtools/columns/{table}")
def get_columns(table: str, db: Session = Depends(get_db)):
    from sqlalchemy import text
    result = db.execute(text(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name='{table}'")).fetchall()
    return [{"column": r[0], "type": r[1]} for r in result]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8082)
