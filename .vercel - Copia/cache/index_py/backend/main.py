from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import models
import schemas
from database import engine, get_db

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
    db_item = db.query(model).filter(model.ID == id).first()
    if not db_item:
        return None
    for var, value in schema_in.model_dump(exclude_unset=True).items():
        setattr(db_item, var, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_generic(model, id, db):
    db_item = db.query(model).filter(model.ID == id).first()
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item

# --- ENDPOINTS: EMPRESA ---
@app.get("/empresas", response_model=List[schemas.Empresa])
def list_empresas(db: Session = Depends(get_db)):
    return db.query(models.Empresa).all()

@app.put("/empresas/{id}", response_model=schemas.Empresa)
def update_empresa(id: int, empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    res = update_generic(models.Empresa, id, empresa, db)
    if not res: raise HTTPException(status_code=404, detail="Empresa not found")
    return res

# --- ENDPOINTS: SETOR ---
@app.get("/setores", response_model=List[schemas.Setor])
def list_setores(db: Session = Depends(get_db)):
    return db.query(models.Setor).order_by(models.Setor.SEQUENCIA).all()

@app.post("/setores", response_model=schemas.Setor)
def create_setor(setor: schemas.SetorCreate, db: Session = Depends(get_db)):
    return create_generic(models.Setor, setor, db)

# --- ENDPOINTS: OPERADOR ---
@app.get("/operadores", response_model=List[schemas.Operador])
def list_operadores(db: Session = Depends(get_db)):
    return db.query(models.Operador).all()

@app.post("/operadores", response_model=schemas.Operador)
def create_operador(operador: schemas.OperadorCreate, db: Session = Depends(get_db)):
    return create_generic(models.Operador, operador, db)

# --- ENDPOINTS: MEDIDA ---
@app.get("/medidas", response_model=List[schemas.Medida])
def list_medidas(db: Session = Depends(get_db)):
    return db.query(models.Medida).order_by(models.Medida.DESCRICAO).all()

@app.post("/medidas", response_model=schemas.Medida)
def create_medida(medida: schemas.MedidaCreate, db: Session = Depends(get_db)):
    return create_generic(models.Medida, medida, db)

# --- ENDPOINTS: DESENHO ---
@app.get("/desenhos", response_model=List[schemas.Desenho])
def list_desenhos(db: Session = Depends(get_db)):
    return db.query(models.Desenho).order_by(models.Desenho.DESCRICAO).all()

@app.post("/desenhos", response_model=schemas.Desenho)
def create_desenho(desenho: schemas.DesenhoCreate, db: Session = Depends(get_db)):
    return create_generic(models.Desenho, desenho, db)

# --- ENDPOINTS: SERVICO ---
@app.get("/servicos", response_model=List[schemas.Servico])
def list_servicos(db: Session = Depends(get_db)):
    return db.query(models.Servico).all()

@app.post("/servicos", response_model=schemas.Servico)
def create_servico(servico: schemas.ServicoCreate, db: Session = Depends(get_db)):
    return create_generic(models.Servico, servico, db)

# --- ENDPOINTS: PNEU ---
@app.get("/pneus", response_model=List[schemas.Pneu])
def list_pneus(q: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(models.Pneu)
    if q:
        query = query.filter(models.Pneu.CODBARRA.contains(q))
    return query.order_by(models.Pneu.ID.desc()).limit(100).all()

@app.post("/pneus", response_model=schemas.Pneu)
def create_pneu(pneu: schemas.PneuCreate, db: Session = Depends(get_db)):
    return create_generic(models.Pneu, pneu, db)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8082)
