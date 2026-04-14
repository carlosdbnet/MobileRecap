from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas

router = APIRouter(prefix="/falhas", tags=["Registro de Falhas"])

@router.get("", response_model=List[schemas.Falha])
def listar_falhas_catalogo(db: Session = Depends(get_db)):
    """Lista o catálogo de falhas possíveis (tabela física: falha)"""
    return db.query(models.Falha).filter(models.Falha.ativo == True).order_by(models.Falha.codigo).all()

@router.get("/registros", response_model=List[schemas.RegistroFalha])
def listar_falhas_registradas(db: Session = Depends(get_db)):
    """Lista todas as falhas registradas em pneus (PNEU_FALHA)"""
    return db.query(models.RegistroFalha).all()

@router.post("", response_model=schemas.RegistroFalha)
def registrar_falha(falha: schemas.RegistroFalhaCreate, db: Session = Depends(get_db)):
    """Grava o registro de falha na tabela pneu_falha"""
    db_falha = models.RegistroFalha(**falha.model_dump())
    db.add(db_falha)
    db.commit()
    db.refresh(db_falha)
    return db_falha
