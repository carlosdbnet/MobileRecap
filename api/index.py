import sys
import os

# Determina o diretório base para incluir o 'backend' no sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
backend_dir = os.path.join(parent_dir, 'backend')

if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

# Importa o app do backend
try:
    from main import app as backend_app
except ImportError:
    from backend.main import app as backend_app

# O Vercel espera que o arquivo api/index.py exporte 'app'
# Estamos renomeando para deixar 100% explícito.
app = backend_app
