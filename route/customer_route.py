from flask import request, jsonify
from pydantic import ValidationError
from route import customer_tag, zipcode_tag
from schemas import CustomerSaveSchema, CustomerViewSchema
from schemas.address import AddressSchema, AddressZipCodeSchema
from schemas.customer import ListCustomerViewSchema
from schemas.filter import CustomerFilterSchema
from schemas.status import StatusResponseSchema
from usecase.address_usecase import AddressUseCase
from usecase.customer_usecase import CustomerUseCase


class CustomerRoute:

    def __init__(self):
        self.usecase = CustomerUseCase()
        self.address_usecase = AddressUseCase()

    def init_routes(self, app):
        @app.post('/customer/create', tags=[customer_tag],
                  responses={"201": {"description": "Cliente criado com sucesso.",
                                     "content": {
                                         "application/json": {"schema": StatusResponseSchema.model_json_schema()}}},
                             "400": {"description": "Dados inválidos.",
                                     "content": {
                                         "application/json": {"schema": StatusResponseSchema.model_json_schema()}}},
                             "500": {"description": "Erro generico", "details": "ERRO INFORMADO",
                                     "content": {
                                         "application/json":
                                             {"schema": StatusResponseSchema.model_json_schema()}}}})
        def create_customer_route():
            """Cria um novo cliente."""
            try:
                customer_data = CustomerSaveSchema.parse_obj(request.json)
            except ValidationError as e:
                return jsonify(StatusResponseSchema(
                    message="Cliente ao validar os dados do cliente",
                    details=e.errors()).dict()), 400

            response = self.usecase.create_customer(customer_data)
            return jsonify(response.dict()), response.code

        @app.post('/customer/list', tags=[customer_tag],
                  responses={
                      "200": {"description": "Lista de Clientes.",
                              "content": {
                                  "application/json":
                                      {"schema": {"type": "array", "items": CustomerViewSchema.model_json_schema()}}}},
                      "204": {"description": "Não há resultado para consulta.",
                              "content": {
                                  "application/json":
                                      {"schema": StatusResponseSchema.model_json_schema()}}},
                      "500": {"description": "Erro generico", "details": "ERRO INFORMADO",
                              "content": {
                                  "application/json":
                                      {"schema": StatusResponseSchema.model_json_schema()}}}})
        def list_customers_route():
            """Lista os clientes cadastrados filtrando pelo nome."""
            try:
                filter_data = CustomerFilterSchema.parse_obj(request.json)
            except ValidationError as e:
                return jsonify(StatusResponseSchema(
                    message="Cliente ao validar os dados do cliente",
                    details=e.errors()).dict()), 400

            response = self.usecase.list_customers(filter_data)
            print(f"response: {response}")
            if isinstance(response, ListCustomerViewSchema):
                return jsonify(response.dict()), 200
            else:
                return jsonify(response.dict()), response.code

        @app.get('/customer/<int:id_customer>', tags=[customer_tag],
                 responses={"200": {"description": "Cliente encontrado.",
                                    "content":
                                        {"application/json":
                                             {"schema": CustomerViewSchema.model_json_schema()}}},
                            "404": {"description": "Não há registro para o id informado.",
                                    "content": {
                                        "application/json":
                                            {"schema": StatusResponseSchema.model_json_schema()}}},
                            "500": {"description": "Erro generico", "details": "ERRO INFORMADO",
                                    "content": {
                                        "application/json":
                                            {"schema": StatusResponseSchema.model_json_schema()}}}})
        def get_customer_route():
            id_customer = request.view_args.get('id_customer')
            """Busca um cliente pelo ID."""
            response = self.usecase.get_customer(id_customer)
            if isinstance(response, CustomerViewSchema):
                return jsonify(response.dict()), 200
            else:
                return jsonify(response.dict()), response.code

        @app.put('/customer/<int:id_customer>', tags=[customer_tag],
                 responses={"200": {"description": "Cliente alterado com sucesso",
                                    "content": {
                                        "application/json": {"schema": StatusResponseSchema.model_json_schema()}}},
                            "400": {"description": "Os dados informado são inválidos.",
                                    "content": {
                                        "application/json": {"schema": StatusResponseSchema.model_json_schema()}}},
                            "404": {"description": "Não há registro para o id informado.",
                                    "content": {
                                        "application/json":
                                            {"schema": StatusResponseSchema.model_json_schema()}}},
                            "500": {"description": "Erro generico", "details": "ERRO INFORMADO",
                                    "content": {
                                        "application/json":
                                            {"schema": StatusResponseSchema.model_json_schema()}}}})
        def update_customer_route():
            """Atualiza um cliente existente."""
            try:
                id_customer = request.view_args.get('id_customer')
                customer_data = CustomerSaveSchema.parse_obj(request.json)
            except ValidationError as e:
                return jsonify(StatusResponseSchema(
                    message="Cliente ao validar os dados do cliente",
                    details=e.errors()).dict()), 400

            response = self.usecase.update_customer(id_customer, customer_data)
            return jsonify(response.dict()), response.code

        @app.delete('/customer/<int:id_customer>', tags=[customer_tag],
                    responses={"200": {"description": "Cliente excluído com sucesso.",
                                       "content": {
                                           "application/json": {"schema": StatusResponseSchema.model_json_schema()}}},
                               "404": {"description": "Não há registro para o id informado.",
                                       "content": {
                                           "application/json":
                                               {"schema": StatusResponseSchema.model_json_schema()}}},
                               "500": {"description": "Erro generico", "details": "ERRO INFORMADO",
                                       "content": {
                                           "application/json":
                                               {"schema": StatusResponseSchema.model_json_schema()}}}})
        def delete_customer_route():
            """Exclui um cliente."""
            id_customer = request.view_args.get('id_customer')
            response = self.usecase.delete_customer(id_customer)
            return jsonify(response.dict()), response.code

        @app.get('/customer/zipcode/<int:zipcode>', tags=[zipcode_tag],
                    responses={"200": {"description": "Cep encontrado.",
                                       "content": {
                                           "application/json": {"schema": AddressZipCodeSchema.model_json_schema()}}},
                               "404": {"description": "Não há registro para o cep informado.",
                                       "content": {
                                           "application/json":
                                               {"schema": StatusResponseSchema.model_json_schema()}}},
                               "500": {"description": "Erro generico", "details": "ERRO INFORMADO",
                                       "content": {
                                           "application/json":
                                               {"schema": StatusResponseSchema.model_json_schema()}}}})
        def find_address_by_zipcode():
            zipcode = request.view_args.get('zipcode')
            response = self.address_usecase.find_address_by_zipcode(zipcode)
            if isinstance(response, AddressZipCodeSchema):
                return jsonify(response.dict()), 200
            else:
                return jsonify(response.dict()), response.code
