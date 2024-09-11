from typing import Optional

from pydantic import BaseModel, ConfigDict


class CustomerFilterSchema(BaseModel):
    """
    Define os Dados para filtrar a consulta do cliente
    """
    per_page: int
    page: int
    name: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
