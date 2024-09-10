from typing import List

from pydantic import BaseModel, EmailStr, ConfigDict

from schemas.address import AddressSchema


# Schema para criação/atualizacao de um novo cliente
class CustomerSaveSchema(BaseModel):
    name: str
    email: EmailStr
    phone: str
    age: int
    address: AddressSchema

    model_config = ConfigDict(from_attributes=True)


# Schema para exibir os dados de um cliente
class CustomerViewSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    age: int
    address: AddressSchema

    model_config = ConfigDict(from_attributes=True)


class ListCustomerViewSchema(BaseModel):
    """ Define como uma listagem de clientes será retornada.
    """
    per_page: int
    page: int
    total: int
    customers: List[CustomerViewSchema]
