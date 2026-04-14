import re
import os

models_path = r"C:\Sistema\mobcap\backend\models.py"

with open(models_path, "r", encoding="utf-8") as f:
    text = f.read()

# Substitui __tablename__ = "QUALQUER_COISA" por minúsculo
def to_lower(match):
    # Se for OS, manteremos 'os'. Se for APONTAMENTO, manteremos 'apontamento'
    return f'__tablename__ = "{match.group(1).lower()}"'

text = re.sub(r'__tablename__\s*=\s*"([^"]+)"', to_lower, text)

# Corrige também as ForeignKeys
text = text.replace('ForeignKey("SETOR.id")', 'ForeignKey("setor.id")')

with open(models_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Convertido com sucesso os nomes de tabelas para minúsculas!")
