import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Garantir que o diretório 'backend' esteja no path para que os imports internos funcionem no Vercel
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import engine
from routers import dashboard, apontamento, exames, falhas, consumo, expedicao, auxiliares

app = FastAPI(title="MobCap Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluindo os roteadores das funcionalidades centrais
app.include_router(dashboard.router)
app.include_router(apontamento.router)
app.include_router(exames.router)
app.include_router(falhas.router)
app.include_router(consumo.router)
app.include_router(expedicao.router)
app.include_router(auxiliares.router)

@app.get("/")
def read_root():
    return {"message": "MobCap API is running."}
