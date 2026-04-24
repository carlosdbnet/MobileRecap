import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("POSTGRES_URL")
print(f"Testing connection to: {url.split('@')[1] if url and '@' in url else 'URL missing'}")

try:
    engine = create_engine(url)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print(f"Success! Status: {result.fetchone()}")
except Exception as e:
    print(f"Connection Failed: {e}")
