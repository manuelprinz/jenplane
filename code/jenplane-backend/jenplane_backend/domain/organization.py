from pydantic import BaseModel, Field


class Organization(BaseModel):
    id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
