from typing import Mapping, Any

from bson import ObjectId
from pydantic import BaseModel, Field
from pymongo.database import Database

from jenplane_backend.adapters.output.mongodb.mongo_db import PyObjectId
from jenplane_backend.domain.organization import Organization
from jenplane_backend.spi.organizations import OrganizationRepository


class MongoOrganization(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    organization_id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class MongoOrganizationRepository(OrganizationRepository):

    def __init__(self, database: Database[Mapping[str, Any] | Any]) -> None:
        self._collection = database["organizations"]

    def __call__(self, *args, **kwargs):
        pass

    def find_all(self):
        # return self._collection.find()
        return self._collection.count_documents({})

    def find_by_id(self, organization_id: str) -> Organization | None:
        # FIXME: correct search call
        return map_to_domain(self._collection.find_one())


def map_to_domain(mongo_entity: MongoOrganization) -> Organization:
    return Organization(
        id=mongo_entity.id,
        name=mongo_entity.name,
        description=mongo_entity.description,
    )
