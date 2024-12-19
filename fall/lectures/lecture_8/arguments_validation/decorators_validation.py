def validate_name(setter):
    def wrapper(self, value):
        if not isinstance(value, str):
            raise TypeError
        setter(self, value)

    return wrapper


def validate_age(setter):
    def wrapper(self, value):
        if not isinstance(value, int):
            raise TypeError
        setter(self, value)

    return wrapper


def validate_location(setter):
    def wrapper(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        setter(self, value)

    return wrapper

# ---------------------

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
    @validate_name
    def name(self, value):
        self._name = value


    @property
    def age(self):
        return self._age

    @age.setter
    @validate_age
    def age(self, value):
        self._age = value


    @property
    def location(self):
        return self._location

    @location.setter
    @validate_location
    def location(self, value):
        self._location = value


