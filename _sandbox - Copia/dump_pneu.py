import os
import json
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("POSTGRES_URL")

try:
    engine = create_engine(DB_URL)
    with engine.connect() as conn:
        res = conn.execute(text("SELECT id, codbarra, numserie, numfogo FROM pneu"))
        pneus = [dict(zip(res.keys(), r)) for r in res]
        
        with open("pneu_info.json", "w") as f:
            json.dump(pneus, f, indent=4)
        print(f"Sucesso! Dados de {len(pneus)} pneus salvos em pneu_info.json")
except Exception as e:
    print(f"Erro ao buscar pneu: {e}")
