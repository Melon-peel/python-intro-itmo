class Citizen:
    def __init__(self, id_, person_name, age):
        self.id_ = id_
        self.name = person_name
        self.age = age
        self.location = 0

    def __getattribute__(self, item):
        print("getattribute called")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return "f"

c = Citizen(1, 2, 3)
print(c.id_)