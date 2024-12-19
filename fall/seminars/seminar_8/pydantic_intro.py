from typing import Union
from pydantic.dataclasses import dataclass
from pydantic import ConfigDict
from pydantic import BaseModel, validate_call, field_validator, Field


# ----------

class OldCitizen:
    def __init__(self, id_, name, age):
        self.id_ = id_
        self.name = name
        self.age = age
        self.location = 0

    def walk(self, how_far):
        self.location += how_far


# ------------


@dataclass(config=ConfigDict(validate_assignment=True,
                             coerce_numbers_to_str=True))
class Citizen:
    id_: str
    age: str
    name: str
    location: int | float = 0
    # location: Union[int, float] = 0  # или int | float начиная с Python.310


    def walk(self, how_far):
        self.location += how_far


# citizen = Citizen(id_="fff", name="Alice", age=30)



# --------------------

class BaseCitizen(BaseModel):

    model_config = ConfigDict(validate_assignment=True,
                             coerce_numbers_to_str=True)

    id_: str
    name: str
    age: str
    location: int | float = 0
    # location: Union[int, float] = 0  # или int | float начиная с Python.310

    def walk(self, how_far):
        self.location += how_far


citizen = BaseCitizen(id_="100", name="Alice", age=30)

c = BaseCitizen.model_validate({"id_": "100", "name": "Alice", "age": 30})


