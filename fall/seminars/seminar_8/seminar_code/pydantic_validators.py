from typing import Union
from pydantic import BaseModel, Field, validate_call, field_validator, ConfigDict, model_validator


# ----------
# custom field validation

class FieldCitizen(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True, validate_assignment=True)
    id_: str
    name: str
    age: int
    location: Union[int, float] = 0  # или int | float начиная с Python.310

    def walk(self, how_far):
        self.location += how_far

    # @field_validator("age", mode="after")
    # @classmethod
    # def validate_age(cls, val):
    #     print(type(val))
    #     print(val)
    #     if val < 0:
    #         raise ValueError("Age can't be negative")
    #     return val

    # @model_validator(mode="after")  # if set to "before", then self is a dict
    # def model_validate_age(self):
    #     if self.age < 0:
    #         raise ValueError("Age can't be negative")
    #     return self



citizen = FieldCitizen(id_="100", name="Alice", age="30")

# jsonized = citizen.model_dump_json()
# print(jsonized)
# citizen = FieldCitizen.model_validate_json(jsonized)
# print(citizen)

# ------------------------
# ConfigDict to set some configurable params - here to allow float/int -> str coercion

class TransformationCitizen(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    id_: str
    name: str
    age: str
    location: Union[int, float] = 0  # или int | float начиная с Python.310

    def walk(self, how_far):
        self.location += how_far


# transformed_citizen = TransformationCitizen(id_=1, name="Alice", age="30")


# ----------

class Citizen(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True,
                              validate_assignment=True)

    id_: str
    name: str
    age: int
    location: Union[int, float] = 0  # или int | float начиная с Python.310

    def walk(self, how_far: Union[int, float]):
        return self.location + how_far


    @field_validator("location", mode="after")  # if set to "before", Citizen(...).location = "10" leads to an error
    @classmethod
    def validate_location(cls, location):
        print(f"location: {location}")
        print(f"location type: {type(location)}")
        if not isinstance(location, (int, float)):
            raise TypeError
        else:
            return location


# citizen = Citizen(id_=100, name="Alice", age=30)
# citizen.walk(20)
# print(citizen)
