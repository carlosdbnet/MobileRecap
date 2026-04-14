import re
from collections import Counter

sql_file = r"c:\Sistema\mobcap\scripts\database_schema_050426.sql"

with open(sql_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

constraints = []
for i, line in enumerate(lines):
    match = re.search(r'CONSTRAINT\s+(\w+)', line)
    if match:
        constraints.append((match.group(1), i + 1))

names = [c[0] for c in constraints]
counts = Counter(names)

duplicates = [name for name, count in counts.items() if count > 1]

if not duplicates:
    print("Nenhuma constraint duplicada encontrada.")
else:
    print("Constraints duplicadas encontradas:")
    for name in duplicates:
        occurrences = [c[1] for c in constraints if c[0] == name]
        print(f"  - {name}: linhas {occurrences}")
