from database import SessionLocal
import models
import schemas
from typing import List

db = SessionLocal()
try:
    print("Testing query on Setor...")
    items = db.query(models.Setor).order_by(models.Setor.sequencia).all()
    print(f"Success! Found {len(items)} items.")
    for item in items[:2]:
        print(f"ID: {item.id}, CODSET: {item.codset}, DESCRICAO: {item.descricao}")
except Exception as e:
    print("--- ERROR ---")
    print(e)
finally:
    db.close()
