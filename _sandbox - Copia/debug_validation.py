import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from sqlalchemy.orm import Session
from database import SessionLocal
import models
import schemas
from pydantic import ValidationError

def debug_pneu_validation(codbarra):
    db = SessionLocal()
    try:
        print(f"Buscando pneu com codbarra: '{codbarra}'")
        pneu_db = db.query(models.Pneu).filter(models.Pneu.codbarra == codbarra).first()
        if pneu_db:
            print("✅ Pneu encontrado no banco!")
            # Convert to dict to inspect values
            pneu_dict = {c.name: getattr(pneu_db, c.name) for c in pneu_db.__table__.columns}
            print("\nValores no banco:")
            for k, v in pneu_dict.items():
                print(f"  {k}: {v} ({type(v)})")
            
            # Try to validate with Pydantic
            print("\nTentando validar com schemas.Pneu...")
            try:
                pneu_schema = schemas.Pneu.model_validate(pneu_db)
                print("✅ Validação Pydantic SUCESSO!")
            except ValidationError as e:
                print("❌ Erro de Validação Pydantic:")
                print(e.json(indent=2))
        else:
            print("❌ Pneu não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    debug_pneu_validation("00004")
