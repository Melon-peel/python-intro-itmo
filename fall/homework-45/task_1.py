class BaseTeaException(Exception):
    pass

class Sugar:
    def __init__(self):
        ...

    # make it static
    def validate_kind(kind):
        # this method should set `kind` attribute of the object or raise ValueError if `kind` argument isn't valid
        ...

class Tea:
    def __init__(self):
        ...

    # make it static
    def validate_kind(kind):
        # this method should set `kind` attribute of the object or raise ValueError if `kind` argument isn't valid
        ...


class TeaCup:
    def __init__(self):
        self.sweetness = 0
        self.fullness = 0

    def pour_water(self, amount=None):
        ...

    def drink(self, amount=None):
        ...

    def is_full(self):
        ...

    def __add__(self, other):
        ...

    def __sub__(self, other):
        ...
