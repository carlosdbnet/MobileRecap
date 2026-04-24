from sqlalchemy import create_engine, MetaData

DB_PATH = r"c:\Sistema\mobcap\firebird_data\dbrecap.FDB"
SQLALCHEMY_DATABASE_URL = f"firebird+fdb://SYSDBA:masterkey@localhost:3050/{DB_PATH}?charset=UTF8"

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    
    with open("schema_info.txt", "w", encoding="utf-8") as f:
        f.write("=== Tables reflected successfully ===\n")
        for table_name in metadata.tables.keys():
            f.write(f"\nTable: {table_name}\n")
            table = metadata.tables[table_name]
            for column in table.columns:
                f.write(f"  - {column.name} ({column.type})\n")
    print("Schema saved to schema_info.txt")
except Exception as e:
    print(f"Error reflecting tables: {e}")
