import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load local environment variables from .env file
load_dotenv()

# Database connection configuration
# Priority: Environment variable (Vercel/Production), Fallback: Neon PostgreSQL string
SQLALCHEMY_DATABASE_URL = os.getenv(
    "POSTGRES_URL", 
    "postgresql://neondb_owner:npg_TBWgl4SM1Ejn@ep-morning-water-acsrbm4u-pooler.sa-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require"
)

try:
    print(f"Connecting to database at: {SQLALCHEMY_DATABASE_URL.split('@')[1] if '@' in SQLALCHEMY_DATABASE_URL else 'HIDDEN'}")
    # Ajustando para PostgreSQL no Neon
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        pool_pre_ping=True,
        pool_recycle=3600
    )
    # Testar conexão imediatamente
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        print("[SUCCESS] Database connection established successfully!")
    
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
except Exception as e:
    import traceback
    print("[ERROR] Failed to connect to the database!")
    print(f"Error Type: {type(e).__name__}")
    print(f"Details: {str(e)}")
    # traceback.print_exc() # Descomente para log completo no console
    engine = None
    SessionLocal = None
    Base = declarative_base()

def get_db():
    if not SessionLocal:
        yield None
        return
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
