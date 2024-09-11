from flask import request, jsonify
from route import customer_tag, zipcode_tag
from schemas import CustomerSaveSchema, CustomerViewSchema
from schemas.address import AddressZipCodeSchema, ZipCodePathSchema
from schemas.customer import ListCustomerViewSchema, IdCustomerPathSchema
from schemas.filter import CustomerFilterSchema
from schemas.status import StatusResponseSchema
from usecase.address_usecase import AddressUseCase
from usecase.customer_usecase import CustomerUseCase


class CustomerRoute:

    def __init__(self):
        self.usecase = CustomerUseCase()
        self.address_usecase = AddressUseCase()

    def init_routes(self, app):
        @app.post('/customer/list', tags=[customer_tag],
                  responses={
                      200: ListCustomerViewSchema,
                      204: None,
                      500: StatusResponseSchema
                  })
        def list_customers_route(body: CustomerFilterSchema):
            """Lista os clientes cadastrados filtrando pelo nome."""
            response = self.usecase.list_customers(body)
            print(f"response: {response}")
            if isinstance(response, ListCustomerViewSchema):
                return jsonify(response.dict()), 200
            else:
                return jsonify(response.dict()), response.code

        @app.get('/customer/<int:id_customer>', tags=[customer_tag],
                 responses={
                     200: CustomerViewSchema,
                     404: StatusResponseSchema,
                     500: StatusResponseSchema
                 })
        def get_customer_route(path: IdCustomerPathSchema):

            """Busca um cliente pelo ID."""

            response = self.usecase.get_customer(path.id_customer)
            if isinstance(response, CustomerViewSchema):
                return jsonify(response.dict()), 200
            else:
                return jsonify(response.dict()), response.code

        @app.post('/customer/create', tags=[customer_tag],
                  responses={
                      200: StatusResponseSchema,
                      400: StatusResponseSchema,
                      404: StatusResponseSchema,
                      500: StatusResponseSchema
                  })
        def create_customer_route(body: CustomerSaveSchema):
            """Cria um novo cliente."""
            response = self.usecase.create_customer(body)
            return jsonify(response.dict()), response.code

        @app.put('/customer/<int:id_customer>', tags=[customer_tag],
                 responses={
                     200: StatusResponseSchema,
                     400: StatusResponseSchema,
                     404: StatusResponseSchema,
                     500: StatusResponseSchema
                 })
        def update_customer_route(path: IdCustomerPathSchema, body: CustomerSaveSchema):
            """Atualiza um cliente existente."""

            response = self.usecase.update_customer(path.id_customer, body)
            return jsonify(response.dict()), response.code

        @app.delete('/customer/<int:id_customer>', tags=[customer_tag],
                    responses={
                        200: StatusResponseSchema,
                        404: StatusResponseSchema,
                        500: StatusResponseSchema
                    })
        def delete_customer_route(path: IdCustomerPathSchema):
            """Exclui um cliente."""
            response = self.usecase.delete_customer(path.id_customer)
            return jsonify(response.dict()), response.code

        @app.get('/customer/zipcode/<int:zipcode>', tags=[zipcode_tag],
                 responses={
                     200: AddressZipCodeSchema,
                     400: StatusResponseSchema,
                     500: StatusResponseSchema
                 })
        def find_address_by_zipcode(path: ZipCodePathSchema):
            response = self.address_usecase.find_address_by_zipcode(path.zipcode)
            if isinstance(response, AddressZipCodeSchema):
                return jsonify(response.dict()), 200
            else:
                return jsonify(response.dict()), response.code
