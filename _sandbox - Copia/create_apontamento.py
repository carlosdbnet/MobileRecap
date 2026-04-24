from database import engine
from models import Base, Producao # Producao mapeia para APONTAMENTO
import argparse

if __name__ == "__main__":
    print("Criando tabela APONTAMENTO...")
    Producao.__table__.create(engine, checkfirst=True)
    print("Tabela APONTAMENTO verificada/criada com sucesso.")
