from typing import List

from pydantic import BaseModel, EmailStr, ConfigDict

from schemas.address import AddressSchema


# Schema para criação/atualizacao de um novo cliente
class CustomerSaveSchema(BaseModel):
    """
    Define os Dados do Cliente para Criação/Alteração
    """
    name: str
    email: EmailStr
    phone: str
    gender: str
    age: int
    address: AddressSchema

    model_config = ConfigDict(from_attributes=True)


# Schema para exibir os dados de um cliente
class CustomerViewSchema(BaseModel):
    """
    Define os Dados do Cliente para visualização
    """
    id: int
    name: str
    email: EmailStr
    phone: str
    gender: str
    age: int
    address: AddressSchema

    model_config = ConfigDict(from_attributes=True)


class ListCustomerViewSchema(BaseModel):
    """
    Define como uma listagem de clientes será retornada.
    """
    per_page: int
    page: int
    total: int
    customers: List[CustomerViewSchema]

    model_config = ConfigDict(from_attributes=True)


class IdCustomerPathSchema(BaseModel):
    """
    Define objeto de busca
    """
    id_customer: int

    model_config = ConfigDict(from_attributes=True)
