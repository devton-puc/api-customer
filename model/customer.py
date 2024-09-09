from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id = Column("pk_customer", Integer, primary_key=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    age = Column(Integer)

    def __init__(self, name, email, phone, age):
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "age": self.age
        }