import psycopg2
import os
from dotenv import load_dotenv

# Load POSTGRES_URL from backend/.env
load_dotenv(dotenv_path="../backend/.env")
DB_URL = os.getenv("POSTGRES_URL")

if not DB_URL:
    # If not in env, check the root as well
    load_dotenv(dotenv_path=".env")
    DB_URL = os.getenv("POSTGRES_URL")

# Fallback explicit for this specific user case if env loading fails
if not DB_URL:
    DB_URL = "postgresql://neondb_owner:npg_TBWgl4SM1Ejn@ep-morning-water-acsrbm4u-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

def generate_ddl():
    print(f"Connecting to database to generate DDL...")
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        
        # Get tables
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE' ORDER BY table_name")
        tables = [t[0] for t in cur.fetchall()]
        
        ddl = "-- MobCap DB Schema Dump\n-- Generated automatically\n\n"
        
        for table in tables:
            print(f"  Exporting table: {table}")
            ddl += f"-- Table: {table}\n"
            ddl += f"CREATE TABLE IF NOT EXISTS public.\"{table}\" (\n"
            
            # Get columns
            cur.execute(f"""
                SELECT column_name, data_type, character_maximum_length, is_nullable, column_default
                FROM information_schema.columns
                WHERE table_name = '{table}'
                ORDER BY ordinal_position
            """)
            
            columns = cur.fetchall()
            col_lines = []
            for col in columns:
                name, dtype, length, nullable, default = col
                line = f"    \"{name}\" {dtype}"
                if length:
                    line += f"({length})"
                if nullable == "NO":
                    line += " NOT NULL"
                if default:
                    line += f" DEFAULT {default}"
                col_lines.append(line)
            
            # Get Primary Key via information_schema
            cur.execute(f"""
                SELECT kcu.column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu ON tc.constraint_name = kcu.constraint_name
                WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_name = '{table}'
            """)
            pk_cols = [r[0] for r in cur.fetchall()]
            if pk_cols:
                col_lines.append(f"    CONSTRAINT \"{table}_pkey\" PRIMARY KEY (\"{'\", \"'.join(pk_cols)}\")")
                
            ddl += ",\n".join(col_lines)
            ddl += "\n);\n\n"
            
        # Get Foreign Keys via information_schema
        print("  Exporting Foreign Keys...")
        cur.execute("""
            SELECT
                tc.constraint_name, 
                tc.table_name, 
                kcu.column_name, 
                ccu.table_name AS foreign_table_name,
                ccu.column_name AS foreign_column_name 
            FROM 
                information_schema.table_constraints AS tc 
                JOIN information_schema.key_column_usage AS kcu
                  ON tc.constraint_name = kcu.constraint_name
                  AND tc.table_schema = kcu.table_schema
                JOIN information_schema.constraint_column_usage AS ccu
                  ON ccu.constraint_name = tc.constraint_name
                  AND ccu.table_schema = tc.table_schema
            WHERE tc.constraint_type = 'FOREIGN KEY';
        """)
        
        for fk in cur.fetchall():
            name, table, col, ftable, fcol = fk
            ddl += f"-- Foreign Key: {name}\n"
            ddl += f"ALTER TABLE public.\"{table}\" ADD CONSTRAINT \"{name}\" FOREIGN KEY (\"{col}\") REFERENCES public.\"{ftable}\"(\"{fcol}\");\n"
            
        with open("database_schema.sql", "w", encoding="utf-8") as f:
            f.write(ddl)
            
        print("\nSuccess! DDL script generated: database_schema.sql")
        conn.close()
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Error: {e}")

if __name__ == "__main__":
    generate_ddl()
