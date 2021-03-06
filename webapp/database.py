import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from psycopg2.extensions import register_adapter, AsIs
from pydantic.networks import IPv4Address

SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USERNAME')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

def get_db():
    db = Session(engine)
    try:
        return db
    finally:
        db.close()

def adapt_pydantic_ip_address(ip):
    return AsIs(repr(ip.exploded))

register_adapter(IPv4Address, adapt_pydantic_ip_address)
