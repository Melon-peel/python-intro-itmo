class NameDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get('name')

    def __set__(self, instance, value):
        if isinstance(value, str):
            instance.__dict__['name'] = value
        else:
            raise TypeError

class AgeDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get('age')

    def __set__(self, instance, value):
        if isinstance(value, int):
            instance.__dict__['age'] = value
        else:
            raise TypeError

class LocationDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get('location', 0)

    def __set__(self, instance, value):
        if isinstance(value, (float, int)):
            instance.__dict__['location'] = value
        else:
            raise TypeError

class Citizen:
    name = NameDescriptor()
    age = AgeDescriptor()
    location = LocationDescriptor()

    def __init__(self, id_, name, age):
        self.id_ = id_
        self.name = name  # Вызов NameDescriptor.__set__
        self.age = age    # Вызов AgeDescriptor.__set__
        self.location = 0  # Устанавливается значение по умолчанию

    def walk(self, how_far):
        self.location = how_far  # Вызов WalkDescriptor.__set__


c = Citizen(1, "f", 30)
print(c.name)