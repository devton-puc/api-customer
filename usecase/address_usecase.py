import requests

from schemas.address import AddressZipCodeSchema
from schemas.status import StatusResponseSchema


class AddressUseCase:

    def find_address_by_zipcode(self, zipcode) -> AddressZipCodeSchema | StatusResponseSchema:
        try:
            response = requests.get(f'https://viacep.com.br/ws/{zipcode}/json/')
            if response.status_code == 400:
                return StatusResponseSchema(code=response.status_code, message="Cep enviado no formato inválido.")
            elif response.status_code != 200:
                return StatusResponseSchema(code=response.status_code, message="A consulta dos correios retornou um erro não especificado.")

            address_data = response.json()

            if "erro" in address_data:
                return StatusResponseSchema(code=404, message="Cep não encontrado.")

            return AddressZipCodeSchema(
                zipcode=address_data.get("cep"),
                address=address_data.get("logradouro"),
                neighborhood=address_data.get("bairro"),
                city=address_data.get("localidade"),
                state=address_data.get("uf"),
                number=address_data.get("numero"),
                complement=address_data.get("complemento")
            )

        except Exception as error:
            return StatusResponseSchema(code=500, message="Erro ao obter o cep", details=f"{error}")
