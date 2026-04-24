from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas

router = APIRouter(prefix="/exames", tags=["Exames Iniciais e Finais"])

@router.get("/pneu/{codigo_barra}", response_model=schemas.Pneu)
def buscar_pneu(codigo_barra: str, db: Session = Depends(get_db)):
    db_pneu = db.query(models.Pneu).filter(models.Pneu.codigo_barra == codigo_barra).first()
    if not db_pneu:
        raise HTTPException(status_code=404, detail="Pneu não encontrado com este código de barras")
    return db_pneu

@router.put("/pneu/{codigo_barra}/status", response_model=schemas.Pneu)
def atualizar_status_pneu(codigo_barra: str, status: str, db: Session = Depends(get_db)):
    db_pneu = db.query(models.Pneu).filter(models.Pneu.codigo_barra == codigo_barra).first()
    if not db_pneu:
        raise HTTPException(status_code=404, detail="Pneu não encontrado")
    db_pneu.status = status
    db.commit()
    db.refresh(db_pneu)
    return db_pneu
