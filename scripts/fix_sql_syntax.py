import re

sql_file = "database_schema_050426.sql"

with open(sql_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add missing commas to numeric definitions at the end of lines
# This matches numeric(X,Y) at the end of a line if the next line starts with a column name (indented)
content = re.sub(r'(numeric\(\d+,\d+\))(?=\n\s+\w)', r'\1,', content)

# 2. Add missing commas to character/integer/boolean definitions at the end of lines
# This is trickier as it might catch the last column. 
# We look for lines that don't end in , or ) and the next line is a column definition (starts with spaces and alphanumeric)
# But we must avoid matching the last column before a constraint or closing paren.
content = re.sub(r'(\s+\w+\s+(?:character|integer|boolean|numeric|timestamp|text|bytea)[^,\n]*)(?=\n\s+\w)', r'\1,', content)

# 3. Specific fixes for corrupted lines found
content = content.replace("FLAGCLIENTE DEFAULT TRUE,", "FLAGCLIENTE BOOLEAN DEFAULT TRUE,")
content = content.replace("FLAGCLIENTE ,", "FLAGCLIENTE BOOLEAN DEFAULT TRUE,")
content = content.replace("FLAGFORNECEDORBOOLEAN", "FLAGFORNECEDOR BOOLEAN")
content = content.replace("USERLANOOLEAN", "USERLAN BOOLEAN")
content = content.replace("VCOMBREALLEAN", "VCOMBREAL BOOLEAN") # Guessing based on pattern
content = content.replace("FLAGVENDEDOR BOOLEAN DEFAULT FALSE", "FLAGVENDEDOR BOOLEAN DEFAULT FALSE,") # Ensure comma if missing

# 4. Fix specific known missing commas that regex might miss
content = content.replace("VALOR numeric(15,2)\n    VTOTAL", "VALOR numeric(15,2),\n    VTOTAL")

# 5. Fix the 'ATIVO' lines that might be missing types if they were like 'FLAGCLIENTE'
content = re.sub(r'(\s+ATIVO\s+)(?=BOOLEAN DEFAULT)', r'\1', content) 

# Let's do a pass to add commas to any line that looks like a column definition followed by another column definition
# Padrão: (indent)(name)(type)(metadata) \n (indent)(name)
content = re.sub(r'^(\s+\w+\s+[\w\s\(\),]+)(?<!,)$(?=\n\s+\w)', r'\1,', content, flags=re.MULTILINE)

with open(sql_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Sucesso! {sql_file} corrigido com lógica mais robusta.")
