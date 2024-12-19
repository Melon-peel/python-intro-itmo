class Citizen:
    def __init__(self, id_, name, age):
        self.id_ = id_
        self.name = name
        self.age = age
        self.location = 0

    def walk(self, how_far):
        self.location += how_far

    # если у класса есть метод __eq__, метод __hash__ должен быть реализован юзером
    # для поддержки хеширования (чтобы объекты можно было использовать, например, как ключи в словарях или в списках)
    def __eq__(self, other):
        return self.id_ == other.id_

    def __hash__(self):
        return hash(self.id_)


# citizen_1 = Citizen(1, 2, 3)
# citizen_2 = Citizen(1, 2, 3)


from datetime import datetime
from dataclasses import dataclass, field


@dataclass(unsafe_hash=True)
class User:
    id_: int
    name: str = 'John Doe'
    signup_ts: datetime = None

    def __post_init__(self):
        pass


user_1 = User(id_=1)
user_2 = User(id_=1)

print({user_1, user_2})