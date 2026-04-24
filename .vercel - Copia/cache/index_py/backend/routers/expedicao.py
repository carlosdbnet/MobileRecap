from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas

router = APIRouter(prefix="/expedicao", tags=["Expedição"])

@router.get("/", response_model=List[schemas.Expedicao])
def listar_expedicoes(db: Session = Depends(get_db)):
    return db.query(models.Expedicao).all()

@router.post("/", response_model=schemas.Expedicao)
def registrar_expedicao(expedicao: schemas.ExpedicaoCreate, db: Session = Depends(get_db)):
    db_expedicao = models.Expedicao(**expedicao.model_dump())
    db.add(db_expedicao)
    db.commit()
    db.refresh(db_expedicao)
    return db_expedicao
