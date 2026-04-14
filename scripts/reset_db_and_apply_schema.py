import psycopg2
import os
import sys
from dotenv import load_dotenv

# Caminho absoluto para o arquivo .env no backend
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend', '.env'))
load_dotenv(dotenv_path=env_path)

DB_URL = os.getenv("POSTGRES_URL")
SCHEMA_SQL_PATH = "database_schema_050426.sql" # Relativo a scripts/

if not DB_URL:
    print("ERRO: POSTGRES_URL não encontrada no arquivo .env.")
    sys.exit(1)

def reset_and_apply_schema():
    print("🚀 Iniciando reset do banco de dados...")
    
    try:
        # Conectar ao banco
        conn = psycopg2.connect(DB_URL)
        conn.autocommit = True
        cur = conn.cursor()
        
        # 1. Limpar o esquema public
        print("🚮 Removendo esquema 'public' existente...")
        cur.execute("DROP SCHEMA IF EXISTS public CASCADE;")
        
        print("🏗️ Recriando esquema 'public'...")
        cur.execute("CREATE SCHEMA public;")
        
        # 2. Ler o script SQL
        print(f"📖 Lendo script SQL: {SCHEMA_SQL_PATH}...")
        script_abs_path = os.path.join(os.path.dirname(__file__), SCHEMA_SQL_PATH)
        with open(script_abs_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()
            
        # 3. Executar o script SQL
        print("🔨 Aplicando esquema DDL...")
        cur.execute(sql_script)
        
        print("✅ Esquema aplicado com sucesso!")
        
        # 4. Verificar tabelas
        print("\n📋 Tabelas criadas:")
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name;")
        tables = cur.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        print(f"\n✨ Total de tabelas criadas: {len(tables)}")
        
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ ERRO durante a execução: {e}")
        # Mostrar o contexto do erro se possível
        sys.exit(1)

if __name__ == "__main__":
    reset_and_apply_schema()
