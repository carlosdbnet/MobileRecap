import os
from sqlalchemy import create_engine, text, inspect
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("POSTGRES_URL")

if not url:
    print("❌ POSTGRES_URL NOT FOUND in .env")
    exit(1)

print(f"--- DATABASE DIAGNOSTIC ---")
print(f"Connecting to: {url.split('@')[1] if '@' in url else 'HIDDEN'}")

try:
    engine = create_engine(url)
    with engine.connect() as conn:
        print("✅ Connection established successfully!")
        
        # Test basic query
        print("-" * 30)
        res = conn.execute(text("SELECT current_database(), current_user;")).fetchone()
        print(f"DB Name: {res[0]}, Current User: {res[1]}")
        
        # List tables
        print("-" * 30)
        inspector = inspect(engine)
        tables = sorted(inspector.get_table_names())
        print(f"Tables found ({len(tables)}):")
        for t in tables:
            print(f"  - {t}")
        
        # Detail columns for key tables
        check_list = ["SETOR", "OPERADOR", "PNEU", "TIPONOTA", "OS", "os", "APONTAMENTO", "ORDEM", "CAB_OS", "TAB_OS"]
        for table in check_list:
            if table in tables:
                print(f"\n--- Columns in {table} ---")
                cols = inspector.get_columns(table)
                for col in cols:
                    print(f"- {col['name']} ({col['type']}) {'(PK)' if col.get('primary_key') else ''}")
                
                # Try to count records
                try:
                    count = conn.execute(text(f'SELECT count(*) FROM "{table}"')).scalar()
                    print(f"Record count in {table}: {count}")
                except Exception as e:
                    print(f"❌ Failed to count {table}: {e}")
            else:
                print(f"\n⚠️ Table '{table}' NOT FOUND in database!")

except Exception as e:
    print(f"\n❌ FINAL DB ERROR: {e}")
