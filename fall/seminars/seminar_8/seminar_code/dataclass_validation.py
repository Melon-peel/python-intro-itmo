from dataclasses import dataclass
from typing import Union


class OldCitizen:
    def __init__(self, id_, name, age):
        self.id_ = id_
        self.name = name
        self.age = age
        self.location = 0

    def walk(self, how_far):
        self.location += how_far



@dataclass
class Citizen:
    id_: str
    name: str
    age: int
    location: int | float = 0

    def walk(self, how_far):
        self.location = "fff"

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError
        if not isinstance(self.age, int):
            raise TypeError
        if not isinstance(self.location, (int, float)):
            raise TypeError

citizen = Citizen("1234", "Alice", 30)
print(citizen)
