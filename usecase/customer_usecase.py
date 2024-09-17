from sqlalchemy.exc import IntegrityError
from model import SessionLocal
from model.address import Address
from model.customer import Customer
from schemas.customer import CustomerSaveSchema, ListCustomerViewSchema, CustomerViewSchema
from schemas.filter import CustomerFilterSchema
from schemas.status import StatusResponseSchema
from schemas.address import AddressSchema


class CustomerUseCase:

    def list_customers(self, filter_customer: CustomerFilterSchema) -> ListCustomerViewSchema | StatusResponseSchema:
        try:
            session = SessionLocal()
            query = session.query(Customer)

            if filter_customer.name:
                query = query.filter(Customer.name.like(f'%{filter_customer.name}%'))

            total = query.count()
            customers = query.offset((filter_customer.page - 1) * filter_customer.per_page).limit(
                filter_customer.per_page).all()

            if not customers:
                return StatusResponseSchema(code=204, message="Cliente não encontrado.")

            return ListCustomerViewSchema(total=total, page=filter_customer.page, per_page=filter_customer.per_page,
                                          customers=[customer.to_dict() for customer in customers])

        except Exception as error:
            return StatusResponseSchema(code=500, message="Erro ao listar os clientes", details=f"{error}")


    def create_customer(self, customer_data: CustomerSaveSchema) -> StatusResponseSchema:

        try:
            session = SessionLocal()

            new_customer = Customer(
                name=customer_data.name,
                email=customer_data.email,
                phone=customer_data.phone,
                gender=customer_data.gender,
                age=customer_data.age
            )

            if customer_data.address:
                new_customer.address=Address(
                    zipcode=customer_data.address.zipcode,
                    address=customer_data.address.address,
                    neighborhood=customer_data.address.neighborhood,
                    city=customer_data.address.city,
                    state=customer_data.address.state,
                    number=customer_data.address.number
                )


            session.add(new_customer)
            session.commit()

            return StatusResponseSchema(code=201, message="Cliente criado com sucesso.")

        except IntegrityError as error:
            return StatusResponseSchema(code=500, message="Erro ao Criar o cliente",
                                        details="Dados informados já existem")

        except Exception as error:
            return StatusResponseSchema(code=500, message="Erro ao Criar o cliente", details=f"{error}")

    def update_customer(self, id: int, customer_data: CustomerSaveSchema) -> StatusResponseSchema:

        try:

            session = SessionLocal()
            customer = session.query(Customer).get(id)
            if not customer:
                return StatusResponseSchema(code=404, message="Cliente não encontrado.")

            if customer_data.name:
                customer.name = customer_data.name
            if customer_data.email:
                customer.email = customer_data.email
            if customer_data.phone:
                customer.phone = customer_data.phone
            if customer_data.gender:
                customer.gender = customer_data.gender
            if customer_data.age:
                customer.age = customer_data.age

            if customer_data.address:
                customer.address.zipcode = customer_data.address.zipcode
                customer.address.address = customer_data.address.address
                customer.address.neighborhood = customer_data.address.neighborhood
                customer.address.city = customer_data.address.city
                customer.address.state = customer_data.address.state
                customer.address.number = customer_data.address.number

            session.commit()
            return StatusResponseSchema(code=200, message="Cliente alterado com sucesso.")

        except IntegrityError as error:
            return StatusResponseSchema(code=500, message="Os dados informados já existem",
                                        details="")

        except Exception as error:
            return StatusResponseSchema(code=500, message="Erro ao Alterar o cliente", details=f"{error}")

    def delete_customer(self, id: int) -> StatusResponseSchema:
        try:

            session = SessionLocal()
            customer = session.query(Customer).get(id)
            if not customer:
                return StatusResponseSchema(code=404, message="Cliente não encontrado.")

            session.delete(customer)
            session.commit()
            return StatusResponseSchema(code=200, message="Cliente excluído com sucesso.")

        except Exception as error:
            return StatusResponseSchema(code=500, message="Erro ao excluir o cliente", details=f"{error}")

    def get_customer(self, id: int) -> CustomerViewSchema | StatusResponseSchema:

        try:

            session = SessionLocal()
            customer = session.get(Customer, id)
            if not customer:
                return StatusResponseSchema(code=404, message="Cliente não encontrado.")
            return CustomerViewSchema(**customer.to_dict())

        except Exception as error:
            return StatusResponseSchema(code=500, message="Erro ao obter o cliente", details=f"{error}")


