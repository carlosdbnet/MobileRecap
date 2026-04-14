import os

sql_file = r"c:\Sistema\mobcap\scripts\database_schema_050426.sql"

with open(sql_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

count = 0
for i, line in enumerate(lines):
    if "CONSTRAINT PRODUCAO_pkey PRIMARY KEY (ID)" in line:
        count += 1
        if count == 1:
            # A primeira ocorrência está na tabela PNEU_AVALIACAO
            lines[i] = "    CONSTRAINT PNEU_AVALIACAO_pkey PRIMARY KEY (ID)\n"
            print(f"Renomeado PRODUCAO_pkey na linha {i+1}")

if count > 1:
    with open(sql_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Correção final aplicada.")
else:
    print("Ocorrência não encontrada ou já renomeada.")
