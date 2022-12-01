"""Beanie database models"""

from beanie import Document, PydanticObjectId, Link
from pydantic import Field, BaseModel


class Customer(Document):
    customer_name: str
    vat_number: str
    country: str


class Project(Document):
    project_id: str
    project_description: str
