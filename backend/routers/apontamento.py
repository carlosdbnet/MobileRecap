from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
import models, schemas

router = APIRouter(prefix="/apontamento", tags=["Apontamento de Serviço"])

@router.get("/", response_model=List[schemas.Producao])
def listar_apontamentos(db: Session = Depends(get_db)):
    return db.query(models.Producao).all()

@router.get("/buscar", response_model=Optional[schemas.Producao])
def buscar_apontamento_existente(id_pneu: int, id_setor: int, db: Session = Depends(get_db)):
    return db.query(models.Producao).filter(
        models.Producao.id_pneu == id_pneu,
        models.Producao.id_setor == id_setor,
        models.Producao.termino == None
    ).order_by(models.Producao.inicio.desc()).first()

@router.post("/", response_model=schemas.Producao)
def criar_apontamento(apontamento: schemas.ProducaoCreate, db: Session = Depends(get_db)):
    db_apontamento = models.Producao(**apontamento.model_dump(by_alias=False))
    db.add(db_apontamento)
    db.commit()
    db.refresh(db_apontamento)
    return db_apontamento

@router.put("/{id}", response_model=schemas.Producao)
def atualizar_apontamento(id: int, apontamento: schemas.ProducaoCreate, db: Session = Depends(get_db)):
    db_apontamento = db.query(models.Producao).filter(models.Producao.id == id).first()
    if not db_apontamento:
        raise HTTPException(status_code=404, detail="Apontamento não encontrado")
    
    # Update fields
    for key, value in apontamento.model_dump(by_alias=False, exclude_unset=True).items():
        setattr(db_apontamento, key, value)
    
    db.commit()
    db.refresh(db_apontamento)
    return db_apontamento

@router.get("/{id}", response_model=schemas.Producao)
def ver_apontamento(id: int, db: Session = Depends(get_db)):
    db_apontamento = db.query(models.Producao).filter(models.Producao.id == id).first()
    if not db_apontamento:
        raise HTTPException(status_code=404, detail="Apontamento não encontrado")
    return db_apontamento

@router.delete("/{id}")
def excluir_apontamento(id: int, db: Session = Depends(get_db)):
    db_apontamento = db.query(models.Producao).filter(models.Producao.id == id).first()
    if not db_apontamento:
        raise HTTPException(status_code=404, detail="Apontamento não encontrado")
    db.delete(db_apontamento)
    db.commit()
    return {"message": "Apontamento removido"}
