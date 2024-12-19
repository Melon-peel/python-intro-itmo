class Citizen:
    def __init__(self, id_, name, age):
        self.id_ = id_

        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError

        if isinstance(age, int):
            self.age = age
        else:
            raise TypeError

        self.location = 0

    def walk(self, how_far):
        if isinstance(how_far, (int, float)):
            self.location += how_far
        else:
            raise TypeError

