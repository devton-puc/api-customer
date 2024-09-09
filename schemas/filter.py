from typing import Optional

from pydantic import BaseModel, ConfigDict


class CustomerFilterSchema(BaseModel):
    per_page: int
    page: int
    name: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
