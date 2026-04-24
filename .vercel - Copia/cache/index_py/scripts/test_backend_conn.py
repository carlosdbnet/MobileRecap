import sys
import os

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from database import SessionLocal
import models

def test_backend_connection():
    db = SessionLocal()
    try:
        print("Testing connection to Neon PostgreSQL via SQLAlchemy...")
        setores = db.query(models.Setor).all()
        print(f"✅ Success! Found {len(setores)} sectors.")
        for s in setores:
            print(f" - Sector: {s.descricao} (Status: {s.status})")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_backend_connection()
