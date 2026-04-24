import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import models

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("POSTGRES_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def debug_pneu(codbarra):
    db = SessionLocal()
    try:
        print(f"Buscando pneu com codbarra: {codbarra}")
        pneu = db.query(models.Pneu).filter(models.Pneu.codbarra == codbarra).first()
        if pneu:
            print(f"Pneu encontrado: ID={pneu.id}, CodBarra={pneu.codbarra}")
            # Test schema validation manually or just print fields
            for column in models.Pneu.__table__.columns:
                print(f"  {column.name}: {getattr(pneu, column.name)}")
        else:
            print("Pneu não encontrado.")
    except Exception as e:
        print(f"\n--- ERRO NA BUSCA ---")
        print(str(e))
        import traceback
        traceback.print_exc()
        print("----------------------\n")
    finally:
        db.close()

if __name__ == "__main__":
    debug_pneu("00004")
