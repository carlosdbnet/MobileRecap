import os
from sqlalchemy import create_engine
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
    # Ajustando para PostgreSQL no Neon
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        pool_pre_ping=True,
        pool_recycle=3600
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
except Exception as e:
    print(f"Failed to connect to the database: {e}")
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
