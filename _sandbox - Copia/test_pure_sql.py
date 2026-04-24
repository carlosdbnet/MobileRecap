import os
import psycopg2
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Link do banco
url = os.getenv("POSTGRES_URL")

try:
    print(f"Tentando conectar ao banco na Neon...")
    conn = psycopg2.connect(url)
    cur = conn.cursor()
    
    print("Conexão estabelecida. Testando busca na tabela SETOR...")
    # Testamos com aspas duplas, que é como a migração criou.
    cur.execute('SELECT * FROM "SETOR" LIMIT 1')
    r = cur.fetchone()
    print(f"SUCESSO NO SQL PURO: {r}")
    
    cur.close()
    conn.close()
    print("Teste concluído com sucesso.")

except Exception as e:
    print("\n--- ERRO NO SQL PURO ---")
    print(str(e))
    print("------------------------\n")
