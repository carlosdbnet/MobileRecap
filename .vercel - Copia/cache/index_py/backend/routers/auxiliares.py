from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas

router = APIRouter(prefix="/auxiliares", tags=["Dados Auxiliares"])

@router.get("/setores", response_model=List[schemas.Setor])
def listar_setores(db: Session = Depends(get_db)):
    results = db.query(models.Setor).all()
    return [s for s in results if s.status and s.status.upper() == "ATIVO"]

@router.get("/operadores", response_model=List[schemas.Operador])
def listar_operadores(db: Session = Depends(get_db)):
    results = db.query(models.Operador).all()
    return [o for o in results if o.status and o.status.upper() == "ATIVO"]
