from typing import Optional

from pydantic import BaseModel, ConfigDict


class StatusResponseSchema(BaseModel):
    code: int
    message: str
    details: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
