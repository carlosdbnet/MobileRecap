import psycopg2
import json

URL = "postgresql://neondb_owner:npg_TBWgl4SM1Ejn@ep-morning-water-acsrbm4u-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

def dump_schema():
    conn = psycopg2.connect(URL)
    cur = conn.cursor()
    
    # Get tables
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = [t[0] for t in cur.fetchall()]
    
    schema = {}
    for table in tables:
        # Get columns
        cur.execute(f"""
            SELECT column_name, data_type, character_maximum_length, is_nullable
            FROM information_schema.columns
            WHERE table_name = '{table}'
            ORDER BY ordinal_position
        """)
        columns = []
        for col in cur.fetchall():
            columns.append({
                "name": col[0],
                "type": col[1],
                "length": col[2],
                "nullable": col[3] == "YES"
            })
        schema[table] = columns
        
    with open("full_pg_schema.json", "w") as f:
        json.dump(schema, f, indent=2)
    
    conn.close()
    print("Full schema dumped to full_pg_schema.json")

if __name__ == "__main__":
    dump_schema()
