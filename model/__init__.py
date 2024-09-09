from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.customer import Base

# Configuração do banco SQLite
DATABASE_URL = "sqlite:///customer_crud.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)
