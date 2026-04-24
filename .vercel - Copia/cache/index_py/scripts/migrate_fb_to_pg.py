import fdb
import psycopg2
from psycopg2 import sql
import sys
import logging

# Configuration
FB_CONFIG = {
    'database': r'c:\Sistema\mobcap\firebird_data\dbrecap.fdb',
    'user': 'SYSDBA',
    'password': 'masterkey',
    'charset': 'WIN1252'
}

PG_URL = "postgresql://neondb_owner:npg_TBWgl4SM1Ejn@ep-morning-water-acsrbm4u-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

# Mapping Firebird types to PostgreSQL
TYPE_MAP = {
    7: 'SMALLINT',    # SMALLINT
    8: 'INTEGER',     # INTEGER
    10: 'FLOAT',      # FLOAT
    12: 'DATE',       # DATE
    13: 'TIME',       # TIME
    14: 'CHAR',       # CHAR
    16: 'BIGINT',     # INT64
    27: 'DOUBLE PRECISION', # DOUBLE PRECISION
    35: 'TIMESTAMP',  # TIMESTAMP
    37: 'VARCHAR',    # VARCHAR
    261: 'TEXT',      # BLOB (Subtype 1 is Text, default to TEXT for all for now)
}

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def get_fb_schema(fb_conn):
    cursor = fb_conn.cursor()
    
    # Query to get tables
    cursor.execute("""
        SELECT RDB$RELATION_NAME 
        FROM RDB$RELATIONS 
        WHERE RDB$SYSTEM_FLAG = 0 AND RDB$VIEW_BLR IS NULL
    """)
    tables = [row[0].strip() for row in cursor.fetchall()]
    
    schema = {}
    for table in tables:
        # Get columns
        cursor.execute(f"""
            SELECT 
                rf.RDB$FIELD_NAME, 
                f.RDB$FIELD_TYPE, 
                f.RDB$FIELD_LENGTH,
                f.RDB$FIELD_PRECISION,
                f.RDB$FIELD_SCALE,
                rf.RDB$NULL_FLAG,
                f.RDB$FIELD_SUB_TYPE
            FROM RDB$RELATION_FIELDS rf
            JOIN RDB$FIELDS f ON rf.RDB$FIELD_SOURCE = f.RDB$FIELD_NAME
            WHERE rf.RDB$RELATION_NAME = '{table}'
            ORDER BY rf.RDB$FIELD_POSITION
        """)
        columns = []
        for row in cursor.fetchall():
            name = row[0].strip()
            f_type = row[1]
            length = row[2]
            precision = row[3]
            scale = row[4]
            nullable = row[5] == 0 or row[5] is None
            sub_type = row[6]
            
            pg_type = TYPE_MAP.get(f_type, 'TEXT')
            if f_type == 14: # CHAR
                pg_type = f"CHAR({length})"
            elif f_type == 37: # VARCHAR
                pg_type = f"VARCHAR({length})"
            elif (f_type == 16 or f_type == 8 or f_type == 7) and scale < 0: # NUMERIC/DECIMAL
                # For NUMERIC(15,2) Firebird uses INT64 (16) with scale -2
                if precision == 0: precision = 15 # Default for INT64
                pg_type = f"NUMERIC({precision}, {-scale})"
            elif f_type == 261: # BLOB
                pg_type = 'TEXT' if sub_type == 1 else 'BYTEA'
            
            columns.append({
                'name': name,
                'pg_type': pg_type,
                'nullable': nullable
            })
        
        # Get Primary Key
        cursor.execute(f"""
            SELECT iseg.RDB$FIELD_NAME
            FROM RDB$RELATION_CONSTRAINTS rc
            JOIN RDB$INDEX_SEGMENTS iseg ON rc.RDB$INDEX_NAME = iseg.RDB$INDEX_NAME
            WHERE rc.RDB$CONSTRAINT_TYPE = 'PRIMARY KEY' AND rc.RDB$RELATION_NAME = '{table}'
            ORDER BY iseg.RDB$FIELD_POSITION
        """)
        pk = [row[0].strip() for row in cursor.fetchall()]
        
        schema[table] = {
            'columns': columns,
            'pk': pk
        }
    return schema

def migrate():
    fb_conn = None
    pg_conn = None
    try:
        fb_conn = fdb.connect(**FB_CONFIG)
        pg_conn = psycopg2.connect(PG_URL)
        pg_cursor = pg_conn.cursor()
        
        logger.info("Connected to both databases.")
        
        schema = get_fb_schema(fb_conn)
        logger.info(f"Found {len(schema)} tables to migrate.")
        
        for table, details in schema.items():
            columns = details['columns']
            pk = details['pk']
            logger.info(f"Migrating table: {table}")
            
            # 1. Drop table if exists
            pg_cursor.execute(sql.SQL('DROP TABLE IF EXISTS {} CASCADE').format(sql.Identifier(table)))
            
            # 2. Create table
            col_defs = []
            for col in columns:
                col_def = f'"{col["name"]}" {col["pg_type"]}'
                if not col['nullable']:
                    col_def += " NOT NULL"
                col_defs.append(col_def)
            
            # Add Primary Key constraint if exists
            if pk:
                pk_cols = ",".join([f'"{p}"' for p in pk])
                col_defs.append(f'PRIMARY KEY ({pk_cols})')
            
            create_query = f'CREATE TABLE "{table}" ({", ".join(col_defs)})'
            pg_cursor.execute(create_query)
            
            # 3. Migrate data
            fb_cursor = fb_conn.cursor()
            try:
                fb_cursor.execute(f'SELECT * FROM "{table}"')
                
                chunk_size = 500
                while True:
                    rows = fb_cursor.fetchmany(chunk_size)
                    if not rows:
                        break
                    
                    placeholders = ",".join(["%s"] * len(columns))
                    insert_query = f'INSERT INTO "{table}" VALUES ({placeholders})'
                    
                    # Manual type handling for efficiency
                    cleaned_rows = []
                    for row in rows:
                        cleaned_row = []
                        for i, val in enumerate(row):
                            col_info = columns[i]
                            if val is not None:
                                if col_info['pg_type'] == 'BYTEA' and isinstance(val, (fdb.BlobReader, bytes)):
                                    if hasattr(val, 'read'):
                                        val = val.read()
                                elif col_info['pg_type'] == 'TEXT' and hasattr(val, 'read'):
                                    val = val.read().decode('win1252', errors='ignore')
                                elif isinstance(val, str):
                                    val = val.strip()
                            cleaned_row.append(val)
                        cleaned_rows.append(tuple(cleaned_row))
                    
                    pg_cursor.executemany(insert_query, cleaned_rows)
                    logger.info(f"Migrated {len(cleaned_rows)} rows of {table}")
            except Exception as e:
                 logger.error(f"Error reading table {table}: {e}")
                 pg_conn.rollback()
                 continue
            
            pg_conn.commit()
            logger.info(f"Table {table} migrated successfully.")

        logger.info("Full migration completed!")
        
    except Exception as e:
        logger.error(f"Migration failed: {str(e)}")
        if pg_conn: pg_conn.rollback()
    finally:
        if fb_conn: fb_conn.close()
        if pg_conn: pg_conn.close()

if __name__ == "__main__":
    migrate()
