import json

with open("full_pg_schema.json", "r") as f:
    schema = json.load(f)

tables = ["SETOR", "PNEU", "SERVICO", "MEDIDA", "DESENHO", "OPERADOR", "EMPRESA"]
with open("schema_subset.txt", "w") as f:
    for t in tables:
        f.write(f"--- {t} ---\n")
        cols = schema.get(t, [])
        for c in cols:
            f.write(f"{c['name']}: {c['type']}({c['length']})\n")
        f.write("\n")
