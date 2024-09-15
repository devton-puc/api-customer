from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuração do banco SQLite
DATABASE_URL = "sqlite:///customer_crud.db"

engine = create_engine(DATABASE_URL,pool_size=20, max_overflow=40)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def init_db():
    from model import address
    from model import customer
    Base.metadata.create_all(bind=engine)
