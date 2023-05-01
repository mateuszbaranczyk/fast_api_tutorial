from enum import Enum
from pydantic import BaseModel, Field, HttpUrl


class VegetablesModel(str, Enum):
    onion = "onion"
    garlic = "garlic"
    potato = "potato"


class Image(BaseModel):
    url: HttpUrl
    title: str


# models can by nested for example Image in Item model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float
    image: Image


# validation provided by pydantic can be used in model directly instead of endpoint parameters
class User(BaseModel):
    username: str
    full_name: str | None = Field(default=None, title="Full name", max_length=64)
