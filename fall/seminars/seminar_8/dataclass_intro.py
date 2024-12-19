from datetime import datetime
from dataclasses import dataclass, field



@dataclass
class User:
    id_: int
    age: int | float
    signup_ts: datetime = None # ~ field(default=None)
    events: list[str] = field(default_factory=list)
    name: str = 'John Doe'



class FaultyDataClass:
    def __init__(self, my_list=None):
        self.my_list = [] if my_list is None else my_list

# print(FaultyDataClass.__init__.__defaults__)
# first = FaultyDataClass()
# first.my_list.append("test first")
# print(first.my_list)
# print(FaultyDataClass.__init__.__defaults__)
# second = FaultyDataClass()
# second.my_list.append("test second")
# print(second.my_list)
#
# print(FaultyDataClass.__init__.__defaults__)
