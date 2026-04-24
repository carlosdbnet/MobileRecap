import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("POSTGRES_URL", "postgresql://neondb_owner:npg_TBWgl4SM1Ejn@ep-morning-water-acsrbm4u-pooler.sa-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require")

print(f"--- Diagnóstico de Banco de Dados ---")
print(f"URL: {DB_URL.split('@')[1] if '@' in DB_URL else 'HIDDEN'}")

try:
    engine = create_engine(DB_URL)
    with engine.connect() as conn:
        print("✅ Conexão bem sucedida!")
        
        # Verificar tabelas existentes
        print("\n--- Tabelas no Schema Public ---")
        res = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'"))
        tables = [r[0] for r in res]
        for t in tables:
            # Contar registros
            count_res = conn.execute(text(f"SELECT COUNT(*) FROM \"{t}\""))
            count = count_res.scalar()
            print(f"Table: {t:20} | Records: {count}")
            
except Exception as e:
    print(f"❌ Erro: {e}")
