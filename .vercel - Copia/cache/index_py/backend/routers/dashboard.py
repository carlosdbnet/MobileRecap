from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from database import get_db
import models, schemas

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/", response_model=schemas.DashboardStats)
def get_dashboard_stats(db: Session = Depends(get_db)):
    today = date.today()
    
    # Devido a limitações de compatibilidade do driver Firebird com SQLAlchemy .filter(),
    # estamos realizando a contagem e filtragem no lado do Python (servidor).
    
    producoes = db.query(models.Producao).all()
    total_producao = len([p for p in producoes if p.data_inicio == today])
    
    falhas_registradas = db.query(models.RegistroFalha).all()
    total_falhas = len([f for f in falhas_registradas if f.data == today])
    
    pneus = db.query(models.Pneu).all()
    pneus_pendentes = len([p for p in pneus if p.status and p.status.upper() == "PENDENTE"])
    
    # Ordenação e limite manual
    falhas_sorted = sorted(falhas_registradas, key=lambda x: x.id, reverse=True)
    ultimas_falhas = falhas_sorted[:5]
    
    return {
        "total_producao_dia": total_producao,
        "total_falhas_dia": total_falhas,
        "pneus_pendentes": pneus_pendentes,
        "ultimas_falhas": ultimas_falhas
    }
