class Citizen:
    def __init__(self, person_name):
        self.__name = person_name  # Используем setter для валидации

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 3:
            raise ValueError("Name cannot exceed 3 characters.")
        self.__name = value

c = Citizen("aaaa")
c.name
