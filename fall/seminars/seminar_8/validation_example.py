class Citizen:
    def __init__(self, id_, name, age):
        self.id_ = id_
        self.name = name
        self.age = age
        self.location = 0

    def walk(self, how_far):
        self.location += how_far