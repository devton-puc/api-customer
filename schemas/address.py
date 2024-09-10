from pydantic import BaseModel, ConfigDict


class AddressSchema(BaseModel):
    zipcode: str
    address: str
    neighborhood: str
    city: str
    state: str
    number: str

    model_config = ConfigDict(from_attributes=True)

class AddressZipCodeSchema(BaseModel):
    zipcode: str
    address: str
    neighborhood: str
    city: str
    state: str

    model_config = ConfigDict(from_attributes=True)
