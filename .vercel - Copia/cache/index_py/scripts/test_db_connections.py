import fdb
import psycopg2
import sys

# Connection details
FB_PATH = r'c:\Sistema\mobcap\firebird_data\dbrecap.fdb'
FB_USER = 'SYSDBA'
FB_PASS = 'masterkey' # Generic default
FB_CHARSET = 'WIN1252'

PG_URL = "postgresql://neondb_owner:npg_TBWgl4SM1Ejn@ep-morning-water-acsrbm4u-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

def test_connections():
    print(f"--- Testing Firebird Connection: {FB_PATH} ---")
    try:
        fb_conn = fdb.connect(database=FB_PATH, user=FB_USER, password=FB_PASS, charset=FB_CHARSET)
        print("✅ Firebird connection successful!")
        fb_conn.close()
    except Exception as e:
        print(f"❌ Firebird connection failed: {e}")
    
    print("\n--- Testing Neon PostgreSQL Connection ---")
    try:
        pg_conn = psycopg2.connect(PG_URL)
        print("✅ PostgreSQL connection successful!")
        pg_conn.close()
    except Exception as e:
        print(f"❌ PostgreSQL connection failed: {e}")

if __name__ == "__main__":
    test_connections()
