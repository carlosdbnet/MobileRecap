import os

sql_file = r"c:\Sistema\mobcap\scripts\database_schema_050426.sql"

with open(sql_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Rename ID_TIPOSERV and TIPOSERV columns (order matters!)
# Replace ID_TIPOSERV first
content = content.replace("ID_TIPOSERV", "ID_RECAP")
# Replace TIPOSERV (the field) with CODRECAP
# Wait, let's be careful. If it's the table name "TIPOSERV", it's different.
# Most occurrences are column definitions: "TIPOSERV character varying(5)"
# I'll use regex for columns
import re
content = re.sub(r'\bTIPOSERV\b', 'CODRECAP', content)

# 2. But we need to make sure the TABLE name is TIPORECAP
# If the user already added TIPORECAP, the old TIPOSERV might still be there if it was a rename.
# The user's diff showed adding TIPORECAP. I should check if TIPOSERV table still exists and rename it if so.

with open(sql_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Sucesso! 'TIPOSERV' renomeado para 'CODRECAP' em {sql_file}.")
