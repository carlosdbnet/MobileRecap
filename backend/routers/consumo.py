from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas

router = APIRouter(prefix="/consumo", tags=["Consumo de Matéria-Prima"])

@router.get("/", response_model=List[schemas.Consumo])
def listar_consumos(db: Session = Depends(get_db)):
    return db.query(models.Consumo).all()

@router.post("/", response_model=schemas.Consumo)
def registrar_consumo(consumo: schemas.ConsumoCreate, db: Session = Depends(get_db)):
    db_consumo = models.Consumo(**consumo.model_dump())
    db.add(db_consumo)
    db.commit()
    db.refresh(db_consumo)
    return db_consumo
