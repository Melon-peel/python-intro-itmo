def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def say_something(something):
    return f"I said {something}"




# ---------------


class UppercaseDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)
        return result.upper()


@UppercaseDecorator
def say_something(something):
    return f"I said {something}"



# --------------------

def citizen_decorator(class_):
    def wrapper(id_, name, age):
        if not isinstance(name, str):
            raise TypeError

        if not isinstance(age, (float, int)):
            raise TypeError

        obj = class_(id_, name, age)

        return obj
    return wrapper

@citizen_decorator
class Citizen:
    def __init__(self, id_, name, age):
        self.id_ = id_
        self.name = name
        self.age = age
        self.location = 0

    def walk(self, how_far):
        self.location += how_far
