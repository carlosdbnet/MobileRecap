import fdb
import psycopg2
import logging

# Configuration
FB_CONFIG = {
    'database': r'c:\Sistema\mobcap\firebird_data\dbrecap.fdb',
    'user': 'SYSDBA',
    'password': 'masterkey',
    'charset': 'WIN1252'
}

PG_URL = "postgresql://neondb_owner:npg_TBWgl4SM1Ejn@ep-morning-water-acsrbm4u-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def verify():
    try:
        fb_conn = fdb.connect(**FB_CONFIG)
        pg_conn = psycopg2.connect(PG_URL)
        
        fb_cursor = fb_conn.cursor()
        pg_cursor = pg_conn.cursor()
        
        # Get tables from Firebird
        fb_cursor.execute("""
            SELECT RDB$RELATION_NAME 
            FROM RDB$RELATIONS 
            WHERE RDB$SYSTEM_FLAG = 0 AND RDB$VIEW_BLR IS NULL
        """)
        tables = [row[0].strip() for row in fb_cursor.fetchall()]
        
        print(f"{'Table':<30} | {'Firebird Rows':<15} | {'Postgres Rows':<15} | {'Status':<7}")
        print("-" * 75)
        
        all_ok = True
        for table in tables:
            # Row count Firebird
            fb_cursor.execute(f'SELECT COUNT(*) FROM "{table}"')
            fb_rows = fb_cursor.fetchone()[0]
            
            # Row count Postgres
            try:
                pg_cursor.execute(f'SELECT COUNT(*) FROM "{table}"')
                pg_rows = pg_cursor.fetchone()[0]
            except:
                pg_rows = "N/A"
                pg_conn.rollback()
            
            status = "✅ OK" if fb_rows == pg_rows else "❌ ERR"
            if status == "❌ ERR": all_ok = False
            
            print(f"{table:<30} | {fb_rows:<15} | {pg_rows:<15} | {status:<7}")
            
        if all_ok:
            print("\n🎉 All tables migrated correctly!")
        else:
            print("\n⚠️ Some rows or tables were not migrated correctly.")
            
    except Exception as e:
        logger.error(f"Verification failed: {e}")
    finally:
        if fb_conn: fb_conn.close()
        if pg_conn: pg_conn.close()

if __name__ == "__main__":
    verify()
