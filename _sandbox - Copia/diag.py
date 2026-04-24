import os
import json
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("POSTGRES_URL")

result = {
    "status": "iniciando",
    "tables": {},
    "error": None
}

try:
    engine = create_engine(DB_URL)
    with engine.connect() as conn:
        result["status"] = "conectado"
        res = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'"))
        tables = [r[0] for r in res]
        for t in tables:
            count = conn.execute(text(f"SELECT COUNT(*) FROM \"{t}\"")).scalar()
            result["tables"][t] = count
except Exception as e:
    result["status"] = "erro"
    result["error"] = str(e)

with open("diag_result.json", "w") as f:
    json.dump(result, f, indent=4)
print("Diagnóstico concluído. Verificando arquivo diag_result.json...")
