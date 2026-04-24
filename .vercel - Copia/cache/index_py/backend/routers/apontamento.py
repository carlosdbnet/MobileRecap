from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas

router = APIRouter(prefix="/apontamento", tags=["Apontamento de Serviço"])

@router.get("/", response_model=List[schemas.Producao])
def listar_apontamentos(db: Session = Depends(get_db)):
    return db.query(models.Producao).all()

@router.post("/", response_model=schemas.Producao)
def criar_apontamento(apontamento: schemas.ProducaoCreate, db: Session = Depends(get_db)):
    db_apontamento = models.Producao(**apontamento.model_dump())
    db.add(db_apontamento)
    db.commit()
    db.refresh(db_apontamento)
    return db_apontamento

@router.get("/{id}", response_model=schemas.Producao)
def ver_apontamento(id: int, db: Session = Depends(get_db)):
    db_apontamento = db.query(models.Producao).filter(models.Producao.id == id).first()
    if not db_apontamento:
        raise HTTPException(status_code=404, detail="Apontamento não encontrado")
    return db_apontamento
