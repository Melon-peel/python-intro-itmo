class Citizen:
    def __init__(self, id_, name, age):
        self.id_ = id_
        self.name = self._validate_name(name)
        self.age = self._validate_age(age)
        self.location = 0

    def walk(self, how_far):
        self.location += self._validate_walk(how_far)

    # --------------------
    # validation block
    # --------------------

    @staticmethod
    def _validate_name(name):
        if isinstance(name, str):
            return name
        else:
            raise TypeError

    @staticmethod
    def _validate_age(age):
        if isinstance(age, int):
            return age
        else:
            raise TypeError


    @staticmethod
    def _validate_walk(how_far):
        if isinstance(how_far, (float, int)):
            return how_far
        else:
            raise TypeError

c = Citizen(100, "alice", 30)
c.name = 10
print(c.name)