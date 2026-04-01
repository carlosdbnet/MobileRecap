import psycopg2

PG_URL = "postgresql://neondb_owner:npg_TBWgl4SM1Ejn@ep-morning-water-acsrbm4u-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

def rename_to_lowercase():
    try:
        conn = psycopg2.connect(PG_URL)
        cursor = conn.cursor()
        
        # Get tables
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        tables = [row[0] for row in cursor.fetchall()]
        
        for table in tables:
            # Rename table if it has uppercase
            if table != table.lower():
                print(f"Renaming table {table} to {table.lower()}...")
                cursor.execute(f'ALTER TABLE "{table}" RENAME TO "{table.lower()}"')
            
            # Get columns for this table
            cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table.lower()}'")
            columns = [row[0] for row in cursor.fetchall()]
            
            for column in columns:
                if column != column.lower():
                    print(f" - Renaming column {table.lower()}.{column} to {column.lower()}...")
                    cursor.execute(f'ALTER TABLE "{table.lower()}" RENAME COLUMN "{column}" TO "{column.lower()}"')
        
        conn.commit()
        print("✅ Success! All tables and columns renamed to lowercase.")
        conn.close()
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    rename_to_lowercase()
