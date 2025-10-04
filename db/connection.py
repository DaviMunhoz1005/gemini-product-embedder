from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv

load_dotenv()

db_url = f"postgresql+psycopg://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:{os.getenv('DB_PORT')}/{os.getenv('POSTGRES_DB')}"
engine = create_engine(db_url)
metadata = MetaData()
