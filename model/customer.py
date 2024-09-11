from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model import Base


class Customer(Base):
    __tablename__ = 'customer'  # Nome da tabela ajustado

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String)
    gender = Column(String)
    age = Column(Integer)
    address = relationship("Address", uselist=False, back_populates="customer", cascade="all, delete-orphan")

    def __init__(self, name, email, phone, gender, age, address=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.gender = gender
        self.age = age
        self.address = address

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'gender': self.gender,
            'age': self.age,
            'address': self.address.to_dict() if self.address else None
        }
