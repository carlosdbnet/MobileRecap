import os
import sys
# Adiciona o diretório atual ao path para importar models e database
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import models
    from database import SessionLocal
    print("Módulos carregados com sucesso.")
    
    db = SessionLocal()
    print("Sessão do banco iniciada.")
    
    # Tenta buscar os setores
    setores = db.query(models.Setor).all()
    print(f"SUCESSO: {len(setores)} setores encontrados!")
    for s in setores[:3]:
        print(f" - ID: {s.ID}, Desc: {s.DESCRICAO}")

except Exception as e:
    print("\n--- ERRO LOCALIZADO ---")
    print(str(e))
    print("------------------------\n")
finally:
    if 'db' in locals():
        db.close()
