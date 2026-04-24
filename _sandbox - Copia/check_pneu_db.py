import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

SQL_URL = os.getenv("POSTGRES_URL")

def check_db_schema():
    print(f"Connecting to database...")
    engine = create_engine(SQL_URL)
    try:
        with engine.connect() as conn:
            print("\n--- PNEU TABLE COLUMNS ---")
            query = text("""
                SELECT column_name, data_type 
                FROM information_schema.columns 
                WHERE table_name = 'pneu';
            """)
            result = conn.execute(query)
            cols = result.fetchall()
            if not cols:
                print("Table 'pneu' (lowercase) not found. Checking 'PNEU' (uppercase)...")
                query = text("""
                    SELECT column_name, data_type 
                    FROM information_schema.columns 
                    WHERE table_name = 'PNEU';
                """)
                result = conn.execute(query)
                cols = result.fetchall()
            
            for col in cols:
                print(f"  - {col[0]} ({col[1]})")
                
            if not cols:
                print("❌ Table 'pneu' or 'PNEU' not found in database!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    check_db_schema()
