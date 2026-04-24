import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from sqlalchemy.orm import Session
from database import SessionLocal
import models
import schemas
from fastapi.encoders import jsonable_encoder
import json

def debug_json_serialization(codbarra):
    db = SessionLocal()
    try:
        print(f"Buscando pneu com codbarra: '{codbarra}'")
        pneu_db = db.query(models.Pneu).filter(models.Pneu.codbarra == codbarra).first()
        if pneu_db:
            print("✅ Pneu encontrado no banco!")
            
            # Step 1: Pydantic validation
            print("\nStep 1: Pydantic validation...")
            pneu_schema = schemas.Pneu.model_validate(pneu_db)
            print("✅ Pydantic Success!")
            
            # Step 2: JSON serialization
            print("\nStep 2: JSON serialization...")
            data = jsonable_encoder(pneu_schema)
            json_str = json.dumps(data)
            print("✅ JSON Serialization Success!")
            print(f"JSON: {json_str[:100]}...")
            
        else:
            print("❌ Pneu não encontrado.")
    except Exception as e:
        print(f"--- ERROR AT STEP ---")
        print(str(e))
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    debug_json_serialization("00004")
