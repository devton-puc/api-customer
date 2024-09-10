from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model import Base


class Address(Base):
    __tablename__ = 'address'  # Nome da tabela ajustado

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    zipcode = Column(String(20), nullable=False)
    address = Column(String(200), nullable=False)
    neighborhood = Column(String(200), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    number = Column(String(10), nullable=False)

    # Relacionamento 1-para-1 com a tabela de cliente
    customer = relationship("Customer", back_populates="address")

    def __init__(self, zipcode, address, neighborhood, city, state, number):
        self.zipcode = zipcode
        self.address = address
        self.neighborhood = neighborhood
        self.city = city
        self.state = state
        self.number = number

    def to_dict(self):
        return {
            'zipcode': self.zipcode,
            'address': self.address,
            'neighborhood': self.neighborhood,
            'city': self.city,
            'state': self.state,
            'number': self.number
        }
