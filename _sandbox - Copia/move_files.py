import os
import shutil

root = r"c:\Sistema\Mobcap"
sandbox = os.path.join(root, "_sandbox")

root_files = [
    "debug_full.py",
    "debug_validation.py",
    "vercel_dev_full.log",
    "schema_subset.txt",
    "Comando para startar Backend e Front End.txt",
    "Configs feito pelo antigravity para habilitar rede.txt",
    "Dicas para rodar prostgree local.txt",
    "Link banco postgree Neon.txt",
    "Vincular nova conta no Eas CLI.txt"
]

backend_files = [
    "check_pneu_db.py",
    "create_apontamento.py",
    "db_check.py",
    "db_diagnostic.py",
    "debug_pneu.py",
    "diag.py",
    "diag_result.json",
    "dump_pneu.py",
    "get_ip.py",
    "inspect_db.py",
    "pneu_info.json",
    "reflect_db.py",
    "results.txt",
    "schema_info.txt",
    "schema_output.txt",
    "schema_reflection.txt",
    "simple_test.py",
    "startup_log.txt",
    "test_db.py",
    "test_db_debug.py",
    "test_pure_sql.py"
]

for f in root_files:
    src = os.path.join(root, f)
    if os.path.exists(src):
        print("Moving", f)
        shutil.move(src, os.path.join(sandbox, f))

for f in backend_files:
    src = os.path.join(root, "backend", f)
    if os.path.exists(src):
        print("Moving", f)
        shutil.move(src, os.path.join(sandbox, f))
