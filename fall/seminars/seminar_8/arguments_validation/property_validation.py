class Citizen:
    def __init__(self, id_, name, age):
        self.id_ = id_
        self._name = name
        self._age = age
        self._location = 0

    def walk(self, how_far):
        self.location = how_far

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("Name must be a string.")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self._age = value
        else:
            raise TypeError

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if isinstance(value, (float, int)):
            self._location = value
        else:
            raise TypeError

