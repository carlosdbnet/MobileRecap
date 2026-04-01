import fdb

def list_tables():
    dsns = [
        r"c:\Sistema\mobcap\firebird_data\dbrecap.FDB",  # Direct local path
        r"localhost:c:\Sistema\mobcap\firebird_data\dbrecap.FDB", # Localhost with port 
        r"127.0.0.1:c:\Sistema\mobcap\firebird_data\dbrecap.FDB"
    ]
    
    conn = None
    for dsn in dsns:
        try:
            conn = fdb.connect(
                dsn=dsn,
                user='SYSDBA',
                password='masterkey',
                charset='UTF8'
            )
            break
        except Exception:
            continue
    
    if not conn:
        print("Could not connect to the database.")
        return

    try:
        cur = conn.cursor()
        cur.execute("SELECT rdb$relation_name FROM rdb$relations WHERE rdb$view_context IS NULL AND rdb$system_flag = 0")
        tables = [t[0].strip() for t in cur.fetchall()]
        
        with open("schema_info.txt", "w", encoding="utf-8") as f:
            f.write("=== Tables in dbrecap.FDB ===\n")
            for table in tables:
                f.write(f"\nTable: {table}\n")
                cur.execute(f"""
                    SELECT 
                        f.rdb$field_name AS field_name,
                        t.rdb$type_name AS field_type,
                        f.rdb$field_length AS field_length
                    FROM rdb$relation_fields f
                    JOIN rdb$fields b ON f.rdb$field_source = b.rdb$field_name
                    JOIN rdb$types t ON b.rdb$field_type = t.rdb$type AND t.rdb$field_name = 'RDB$FIELD_TYPE'
                    WHERE f.rdb$relation_name = '{table}'
                    ORDER BY f.rdb$field_position
                """)
                columns = cur.fetchall()
                for col in columns:
                    name = col[0].strip()
                    type_ = col[1].strip()
                    length = col[2]
                    f.write(f"  - {name} ({type_}, {length})\n")
        
        conn.close()
        print("Schema saved to schema_info.txt")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_tables()
