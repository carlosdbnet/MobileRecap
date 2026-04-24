from database import engine
from sqlalchemy import text

def get_schema():
    tables = ['pneu_servico']
    with engine.connect() as conn:
        for table in tables:
            print(f"--- TABLE: {table} ---")
            query = text(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name='{table}'")
            res = conn.execute(query).fetchall()
            for r in res:
                print(f"{r[0]}: {r[1]}")

if __name__ == "__main__":
    get_schema()
